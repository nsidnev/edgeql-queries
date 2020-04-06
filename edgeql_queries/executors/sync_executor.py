"""Definition for creator of sync executors."""

from functools import partial
from types import MappingProxyType
from typing import Any, Callable, Mapping

from edgedb import BlockingIOConnection
from edgedb.datatypes import datatypes

from edgeql_queries.models import EdgeQLOperationType, Query


def _execute(conn: BlockingIOConnection, *, query: Query) -> None:
    return conn.execute(query.edgeql)


def _set_return(
    conn: BlockingIOConnection, *, query: Query, **query_args: Any,
) -> datatypes.Set:
    return conn.fetchall(query.edgeql, **query_args)


def _single_return(
    conn: BlockingIOConnection, *, query: Query, **query_args: Any,
) -> Any:
    return conn.fetchone(query.edgeql, **query_args)


_OPERATION_TO_EXECUTOR: Mapping[EdgeQLOperationType, Callable] = MappingProxyType(
    {
        EdgeQLOperationType.single_return: _single_return,
        EdgeQLOperationType.set_return: _set_return,
        EdgeQLOperationType.execute: _execute,
    },
)


def create_sync_executor(query: Query) -> Callable:
    """Create sync executor for query.

    Arguments:
        query: query for which executor should be created.

    Returns:
        Created sync executor.
    """
    executor = _OPERATION_TO_EXECUTOR[query.operation_type]
    return partial(executor, query=query)
