"""Definition for aliases for complex types from typing."""

from typing import Dict, Union

from edgeql_queries.models import Query

# mypy has limitation on understanding cyclic types
# https://github.com/python/mypy/issues/7069
QueriesTree = Dict[str, Union[Query, "QueriesTree"]]  # type: ignore
