import pathlib

import pytest

from edgeql_queries import from_path
from edgeql_queries.exceptions import EdgeQLLoadError


def test_loader_raises_error_when_path_does_not_exist() -> None:
    with pytest.raises(EdgeQLLoadError):
        from_path("wrong_path")


def test_loader_raises_error_when_path_is_not_file_or_dir() -> None:
    with pytest.raises(EdgeQLLoadError):
        from_path("/dev/null")


def test_loading_queries_from_single_file(queries_path: pathlib.Path) -> None:
    queries = from_path(queries_path / "movies" / "movies.edgeql")
    assert queries.create_new_movie
