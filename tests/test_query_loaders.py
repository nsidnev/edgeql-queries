import pathlib

import pytest

from edgeql_queries.query_loaders import load_query_data_from_dir_path


def test_error_if_call_load_from_dir_when_path_is_not_dir(
    queries_path: pathlib.Path,
) -> None:
    with pytest.raises(ValueError):
        load_query_data_from_dir_path(queries_path / "movies" / "movies.esdl")
