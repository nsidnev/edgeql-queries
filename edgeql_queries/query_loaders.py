"""Definition of loader for queries from files and directories."""

from pathlib import Path
from typing import List

from edgeql_queries.models import Query
from edgeql_queries.parsing import (
    EMPTY_PATTERN,
    NAME_DELIMITER,
    QUERY_DEFINITION_PATTERN,
    parse_query_from_string,
)
from edgeql_queries.typing import QueriesTree


def load_query_data_from_edgeql(edgeql: str) -> List[Query]:
    """Load queries from string.

    Arguments:
        edgeql: edgeql string that contains queries to be parsed.

    Returns:
        List of [queries][edgeql_queries.models.Query] that will be used
            later by [container][edgeql_queries.queries.Queries] for them.
    """
    query_data = []
    for query_edgeql_str in QUERY_DEFINITION_PATTERN.split(edgeql):
        if not EMPTY_PATTERN.match(query_edgeql_str):
            query_edgeql_str = NAME_DELIMITER + query_edgeql_str
            query_data.append(parse_query_from_string(query_edgeql_str))
    return query_data


def load_query_data_from_file(file_path: Path) -> List[Query]:
    """Load queries from esdl file.

    Arguments:
        file_path: path to file with queries to be parsed.

    Returns:
        List of [queries][edgeql_queries.models.Query] that will be used
            later by [container][edgeql_queries.queries.Queries] for them.

    Raises:
        FileNotFoundError: if failed to open file.  # noqa: DAR402
    """
    with open(file_path) as edgeql_file:
        return load_query_data_from_edgeql(edgeql_file.read())


def load_query_data_from_dir_path(dir_path: Path) -> QueriesTree:
    """Load queries from esdl file.

    Arguments:
        dir_path: path to file with queriesto be parsed.

    Returns:
        List of [queries][edgeql_queries.models.Query] that will be used
            later by [container][edgeql_queries.queries.Queries] for them.

    Raises:
        ValueError: if dir_path is not directory.
    """
    if not dir_path.is_dir():
        raise ValueError(f"path {dir_path} must be a directory")

    return _load_query_data_tree(dir_path, dir_path)


def _load_query_data_tree(root_path: Path, path: Path) -> QueriesTree:
    query_data_tree: QueriesTree = {}
    for sub_path in path.iterdir():
        if sub_path.is_file() and sub_path.suffix == ".edgeql":
            for query in load_query_data_from_file(sub_path):
                query_data_tree[query.name] = query
        elif sub_path.is_dir():
            group_name = sub_path.relative_to(root_path).name
            query_data_tree[group_name] = _load_query_data_tree(root_path, sub_path)
    return query_data_tree
