"""Definition of loaders for queries."""

from pathlib import Path
from typing import Union

from edgeql_queries.exceptions import EdgeQLLoadError
from edgeql_queries.queries import Queries, load_from_list, load_from_tree
from edgeql_queries.query_loaders import (
    load_query_data_from_dir_path,
    load_query_data_from_file,
)


def from_path(edgeql_path: Union[str, Path], async_driver: bool = True) -> Queries:
    """Load queries by path to `.edgeql` file or directory with them.

    Arguments:
        edgeql_path: path to `.edgeql` file with queries or directory
            with queries.
        async_driver: create async executors for using with async driver.

    Returns:
        Loaded and parsed queries.

    Raises:
        EdgeQLLoadError: if path to queries does not exist.
    """
    path = Path(edgeql_path)

    if not path.exists():
        raise EdgeQLLoadError("{0} does not exist".format(path))

    queries = Queries(async_driver)

    if path.is_file():
        query_data = load_query_data_from_file(path)
        return load_from_list(queries, query_data)
    elif path.is_dir():
        query_data_tree = load_query_data_from_dir_path(path)
        return load_from_tree(queries, query_data_tree)

    raise EdgeQLLoadError(
        "edgeql_path must be a directory or file, got {0}".format(edgeql_path),
    )
