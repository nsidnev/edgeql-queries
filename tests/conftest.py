import os
import pathlib

import edgedb
import pytest

from edgeql_queries import from_path
from edgeql_queries.queries import Queries


@pytest.fixture
def queries_path() -> pathlib.Path:
    return pathlib.Path(__file__).parent / "queries"


@pytest.fixture
def async_queries(queries_path: pathlib.Path) -> Queries:
    return from_path(queries_path)


@pytest.fixture
def sync_queries(queries_path: pathlib.Path) -> Queries:
    return from_path(queries_path, async_driver=False)


@pytest.fixture
def edgedb_dsn() -> str:
    return os.getenv("EDGEDB_DSN")


@pytest.fixture
async def async_connection(edgedb_dsn: str) -> edgedb.AsyncIOConnection:
    conn = await edgedb.async_connect(edgedb_dsn)
    yield conn
    await conn.aclose()


@pytest.fixture
def sync_connection(edgedb_dsn: str) -> edgedb.BlockingIOConnection:
    conn = edgedb.connect(edgedb_dsn)
    yield conn
    conn.close()


@pytest.fixture(autouse=True)
async def setup_database(
    async_connection: edgedb.AsyncIOConnection, async_queries: Queries
) -> None:
    await async_queries.migrations.create_movies(async_connection)
    await async_connection.execute(
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
        """
    )
    yield
    await async_connection.execute(
        """
        DELETE Movie;
        DELETE Person;
        """
    )
