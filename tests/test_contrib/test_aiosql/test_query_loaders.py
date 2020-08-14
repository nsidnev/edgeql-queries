import pathlib

import aiosql

from edgeql_queries.contrib.aiosql import (
    EdgeQLQueries,
    EdgeQLQueryLoader,
    EdgeQLSyncAdapter,
)


def test_loading_queries_from_single_file(queries_path: pathlib.Path) -> None:
    queries = aiosql.from_path(
        queries_path / "movies" / "movies.edgeql",
        driver_adapter=EdgeQLSyncAdapter,
        loader_cls=EdgeQLQueryLoader,
        queries_cls=EdgeQLQueries,
    )
    assert queries.create_new_movie


def test_loading_queries_from_string(queries_path: pathlib.Path) -> None:
    with open(queries_path / "movies" / "movies.edgeql") as query_file:
        queries = aiosql.from_str(
            query_file.read(),
            driver_adapter=EdgeQLSyncAdapter,
            loader_cls=EdgeQLQueryLoader,
            queries_cls=EdgeQLQueries,
        )
    assert queries.create_new_movie
