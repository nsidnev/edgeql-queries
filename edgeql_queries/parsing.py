"""Definition for parsing functions for queries.

Queries that are acceptable by this library should follow some rules:

1. They should be named.
2. Their names should not contain symbols that could not
    be used in Python identifier(**except for `-` symbol since
    it would be converted into `_`**)
3. They can have special symbols after their names that will change how
    this queries will be executed:
    * `*`: query will be executed as script with using `.execute` method from driver.
    * `!`: query will always return a single object and executed with `.fetchone`
        method from driver.
    * empty: common query that will return a set of objects and will be executed with
        `.fetchall` method from driver.

An example query that can be successfuly parsed:
```edgeql
    # name: select-user-by-username!
    # Find user by username and return it.
    SELECT User {
        username,
        bio,
        is_active
    }
    FILTER .username = <str>$username
    LIMIT 1
```
"""

import re
from types import MappingProxyType
from typing import List, Mapping, Tuple

from edgeql_queries.exceptions import EdgeQLParsingError
from edgeql_queries.models import EdgeQLOperationType, Query

NAME_DELIMITER = "# name: "
QUERY_DEFINITION_PATTERN = re.compile(r"#\s*name\s*:\s*")

QUERY_NAME_DEFINITION_PATTERN = re.compile(r"#\s*name\s*:\s*(.+)\s*")

EMPTY_PATTERN = re.compile(r"^\s*$")

VALID_QUERY_NAME_PATTERN = re.compile(r"^\w+$")

DOC_COMMENT_PATTERN = re.compile(r"\s*\#\s*(.*)$")

_OPERATION_SUFFFIXES_TO_TYPES: Mapping[str, EdgeQLOperationType] = MappingProxyType(
    {
        "*": EdgeQLOperationType.execute,
        "!": EdgeQLOperationType.single_return,
        "": EdgeQLOperationType.set_return,
    },
)


def get_query_name_and_operation(header_line: str) -> Tuple[str, EdgeQLOperationType]:
    """Return query name and operation from query headers.

    Arguments:
        header_line: start line from query definition
            from which name and operation should be parsed.

    Returns:
        Query name and [operation type][edgeql_queries.models.EdgeQLOperationType]

    Raises:
        EdgeQLParsingError: if header is in wrong format or name could not be
            converted into Python identificator.
    """
    name_match = QUERY_NAME_DEFINITION_PATTERN.match(header_line)

    if not name_match:
        raise EdgeQLParsingError("query definition should start with name definition")

    name = name_match.group(1).replace("-", "_")

    operation_suffix = ""
    for suffix in _OPERATION_SUFFFIXES_TO_TYPES:  # pragma: no branch
        if name.endswith(suffix):
            operation_suffix = suffix
            break

    if operation_suffix:
        query_name = name[: -len(operation_suffix)]
    else:
        query_name = name

    if not VALID_QUERY_NAME_PATTERN.match(query_name):
        raise EdgeQLParsingError(
            'name must be convertable to valid python variable, got "{0}"'.format(
                query_name,
            ),
        )

    return (
        query_name,
        _OPERATION_SUFFFIXES_TO_TYPES[operation_suffix],
    )


def get_edgeql_query(lines: List[str]) -> str:
    """Parse EdgeQL query.

    Arguments:
        lines: lines from which EdgeQL query should be created.

    Returns:
        Created EdgeQL query.
    """
    return "\n".join(lines)


def parse_query_from_string(query: str) -> Query:
    """Parse EdgeQL query string into [edgeql_queries.models.Query].

    Arguments:
        query: EdgeQL query that should be parsed.

    Returns:
        [edgeql_queries.models.Query] that will be later added for creating executors.
    """
    lines = query.strip().splitlines()

    query_name, operation_type = get_query_name_and_operation(lines[0])

    return Query(query_name, operation_type, get_edgeql_query(lines[1:]))
