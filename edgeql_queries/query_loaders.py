"""Definition of loader for queries from files and directories."""

from pathlib import Path
from typing import Iterator, List, Match, Optional, Tuple

from edgeql_queries.models import Query
from edgeql_queries.parsing import QUERY_DEFINITION_PATTERN, parse_query_from_string
from edgeql_queries.typing import QueriesTree

MatchPair = Tuple[Match, Optional[Match]]


def _iter_pairs(matches: Iterator[Match]) -> Iterator[MatchPair]:
    start_match = next(matches)

    try:
        end_match = next(matches)
    except StopIteration:
        yield (start_match, None)
        return

    yield (start_match, end_match)

    for next_match in matches:
        start_match, end_match = end_match, next_match
        yield (start_match, end_match)

    yield (end_match, None)


def load_query_data_from_edgeql(edgeql: str) -> List[Query]:
    """Load queries from string.

    Arguments:
        edgeql: edgeql string that contains queries to be parsed.

    Returns:
        List of [queries][edgeql_queries.models.Query] that will be used
            later by [container][edgeql_queries.queries.Queries] for them.
    """
    query_data = []
    matches_iter = _iter_pairs(QUERY_DEFINITION_PATTERN.finditer(edgeql))
    for (start_match, end_match) in matches_iter:
        if end_match is not None:
            end_position = end_match.start()
        else:
            end_position = len(edgeql)
        query_data.append(
            parse_query_from_string(
                start_match.groups()[0],
                edgeql[start_match.end() : end_position],
            ),
        )
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
        raise ValueError("path {0} must be a directory".format(dir_path))

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
