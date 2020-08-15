import pathlib

import pytest

from edgeql_queries.query_loaders import (
    load_query_data_from_dir_path,
    load_query_data_from_edgeql,
)


def test_error_if_call_load_from_dir_when_path_is_not_dir(
    queries_path: pathlib.Path,
) -> None:
    with pytest.raises(ValueError):
        load_query_data_from_dir_path(queries_path / "movies" / "movies.esdl")


def test_comments_dont_affect_loading_queries() -> None:
    queries = load_query_data_from_edgeql(
        """

    # comment 1 before query1

    # name: query1
    # comment 2

    SELECT 1 + 1;

    # comment 2 after query1 and before query1
    #name:   query2!

    # command 3: query with single_return operator
    SELECT 1 + 1
    LIMIT 1;

    # comment 4 after query2 and before query1
    #
    #
    # comment 5 before complex query


    """,
    )
    assert len(queries) == 2
