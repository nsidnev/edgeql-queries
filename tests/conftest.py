import pathlib

import edgedb
import pytest

import edgeql_queries
from edgeql_queries.queries import Queries


@pytest.fixture()
def queries_path() -> pathlib.Path:
    return pathlib.Path(__file__).parents[1] / "dbschema" / "queries"


@pytest.fixture()
def async_queries(queries_path: pathlib.Path) -> Queries:
    return edgeql_queries.from_path(queries_path)


@pytest.fixture()
def sync_queries(queries_path: pathlib.Path) -> Queries:
    return edgeql_queries.from_path(queries_path, async_driver=False)


@pytest.fixture()
async def async_client() -> edgedb.AsyncIOExecutor:
    client = edgedb.create_async_client()
    yield client
    await client.aclose()


@pytest.fixture()
def sync_client() -> edgedb.Executor:
    client = edgedb.connect()
    yield client
    client.close()


@pytest.fixture(autouse=True)
def _setup_database(sync_queries: Queries) -> None:
    connection = edgedb.connect()
    sync_queries.seeds.create_test_data(connection)
    yield
    sync_queries.seeds.drop_test_data(connection)
    connection.close()
