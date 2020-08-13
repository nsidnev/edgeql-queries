import os
import pathlib

import edgedb
import pytest

import edgeql_queries
from edgeql_queries.queries import Queries
from tests.typing import EdgeDBAsyncFetcher


@pytest.fixture()
def queries_path() -> pathlib.Path:
    return pathlib.Path(__file__).parent / "queries"


@pytest.fixture()
def async_queries(queries_path: pathlib.Path) -> Queries:
    return edgeql_queries.from_path(queries_path)


@pytest.fixture()
def sync_queries(queries_path: pathlib.Path) -> Queries:
    return edgeql_queries.from_path(queries_path, async_driver=False)


@pytest.fixture()
def edgedb_dsn() -> str:
    return os.getenv("EDGEDB_DSN")


@pytest.fixture(params=[edgedb.create_async_pool, edgedb.async_connect])
async def async_fetcher(request, edgedb_dsn: str) -> EdgeDBAsyncFetcher:
    fetcher_creator = request.param
    fetcher = await fetcher_creator(edgedb_dsn)
    yield fetcher
    await fetcher.aclose()


@pytest.fixture()
def sync_fetcher(edgedb_dsn: str) -> edgedb.BlockingIOConnection:
    conn = edgedb.connect(edgedb_dsn)
    yield conn
    conn.close()


@pytest.fixture(autouse=True)
def setup_database(
    sync_fetcher: edgedb.BlockingIOConnection, sync_queries: Queries,
) -> None:
    sync_queries.migrations.create_movies(sync_fetcher)
    sync_fetcher.execute(
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
    sync_fetcher.execute(
        """
        DELETE Movie;
        DELETE Person;
        """,
    )
