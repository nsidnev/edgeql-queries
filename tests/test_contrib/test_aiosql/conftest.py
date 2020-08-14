import pathlib

import aiosql
import pytest

from edgeql_queries.contrib.aiosql import (
    EdgeQLAsyncAdapter,
    EdgeQLQueries,
    EdgeQLQueryLoader,
    EdgeQLSyncAdapter,
)


@pytest.fixture()
def aiosql_async_queries(queries_path: pathlib.Path) -> EdgeQLQueries:
    return aiosql.from_path(
        queries_path,
        driver_adapter=EdgeQLAsyncAdapter,
        loader_cls=EdgeQLQueryLoader,
        queries_cls=EdgeQLQueries,
    )


@pytest.fixture()
def aiosql_sync_queries(queries_path: pathlib.Path) -> EdgeQLQueries:
    return aiosql.from_path(
        queries_path,
        driver_adapter=EdgeQLSyncAdapter,
        loader_cls=EdgeQLQueryLoader,
        queries_cls=EdgeQLQueries,
    )
