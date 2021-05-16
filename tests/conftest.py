import os
import pathlib

import edgedb
import pytest

import edgeql_queries
from edgeql_queries.queries import Queries
from tests.typing import EdgeDBAsyncFetcher


async def _async_transaction_creator(dsn: str) -> edgedb.transaction.AsyncIOTransaction:
    conn = await edgedb.async_connect(dsn)
    tx_iter = await conn.retrying_transaction().__anext__()
    tx = await tx_iter.__aenter__()

    async def _fake_async_close():
        await tx.__aexit__(None, None, None)
        await conn.aclose()

    tx.aclose = _fake_async_close

    return tx


def _sync_transaction_creator(dsn: str) -> edgedb.transaction.Transaction:
    conn = edgedb.connect(dsn)
    tx_iter = conn.retrying_transaction().__next__()
    tx = tx_iter.__enter__()

    def _fake_sync_close():
        tx.__exit__(None, None, None)
        conn.close()

    tx.close = _fake_sync_close

    return tx


@pytest.fixture()
def edgedb_dsn() -> str:
    return os.getenv("EDGEDB_DSN")


@pytest.fixture()
def queries_path() -> pathlib.Path:
    return pathlib.Path(__file__).parent / "queries"


@pytest.fixture()
def async_queries(queries_path: pathlib.Path) -> Queries:
    return edgeql_queries.from_path(queries_path)


@pytest.fixture()
def sync_queries(queries_path: pathlib.Path) -> Queries:
    return edgeql_queries.from_path(queries_path, async_driver=False)


@pytest.fixture(
    params=[edgedb.create_async_pool, edgedb.async_connect, _async_transaction_creator],
)
async def async_fetcher(request, edgedb_dsn: str) -> EdgeDBAsyncFetcher:
    fetcher_creator = request.param
    fetcher = await fetcher_creator(edgedb_dsn)
    yield fetcher
    await fetcher.aclose()


@pytest.fixture(params=[edgedb.connect, _sync_transaction_creator])
def sync_fetcher(request, edgedb_dsn: str) -> edgedb.BlockingIOConnection:
    fetcher_creator = request.param
    fetcher = fetcher_creator(edgedb_dsn)
    yield fetcher
    fetcher.close()


@pytest.fixture(autouse=True)
def _setup_database(edgedb_dsn: str, sync_queries: Queries) -> None:
    connection = edgedb.connect(edgedb_dsn)
    sync_queries.migrations.create_movies(connection)
    connection.execute(
        """
        INSERT Movie {
            title := 'Blade Runner 2049',
            year := 2017,
            director := (
                INSERT Person {
                    first_name := 'Denis',
                    last_name := 'Villeneuve',
                }
            ),
            actors := {
                (INSERT Person {
                    first_name := 'Harrison',
                    last_name := 'Ford',
                }),
                (INSERT Person {
                    first_name := 'Ryan',
                    last_name := 'Gosling',
                }),
                (INSERT Person {
                    first_name := 'Ana',
                    last_name := 'de Armas',
                }),
            }
        };
        """,
    )
    yield
    connection.execute(
        """
        DELETE Movie;
        DELETE Person;
        """,
    )
    connection.close()
