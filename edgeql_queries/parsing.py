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
from typing import Mapping, Tuple

from edgeql_queries.exceptions import EdgeQLParsingError
from edgeql_queries.models import EdgeQLOperationType, Query

QUERY_DEFINITION_PATTERN = re.compile(r"^\s*#\s*name:\s*(.*)\s*", re.MULTILINE)
VALID_QUERY_NAME_PATTERN = re.compile(r"^\w+$")

_OPERATION_SUFFFIXES_TO_TYPES: Mapping[str, EdgeQLOperationType] = MappingProxyType(
    {
        "*": EdgeQLOperationType.execute,
        "!": EdgeQLOperationType.single_return,
        "": EdgeQLOperationType.set_return,
    },
)


def get_query_name_and_operation(name: str) -> Tuple[str, EdgeQLOperationType]:
    """Return query name and operation from query headers.

    Arguments:
        name: raw query name with operator from which
            final name and operation should be extracted.

    Returns:
        Query name and [operation type][edgeql_queries.models.EdgeQLOperationType]

    Raises:
        EdgeQLParsingError: if header is in wrong format or name could not be
            converted into Python identificator.
    """
    name = name.replace("-", "_")

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


def parse_query_from_string(raw_name: str, query_body: str) -> Query:
    """Parse EdgeQL query string into [edgeql_queries.models.Query].

    Arguments:
        raw_name: query name with operation.
        query_body: EdgeQL query.

    Returns:
        [edgeql_queries.models.Query] that will be later added for creating executors.
    """
    query_name, operation_type = get_query_name_and_operation(raw_name)

    return Query(query_name, operation_type, query_body)
