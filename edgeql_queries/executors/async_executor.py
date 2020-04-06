"""Definition for creator of async executors."""

from functools import partial
from types import MappingProxyType
from typing import Any, Callable, Mapping

from edgedb import AsyncIOConnection
from edgedb.datatypes import datatypes

from edgeql_queries.models import EdgeQLOperationType, Query


async def _execute(conn: AsyncIOConnection, *, query: Query) -> None:
    return await conn.execute(query.edgeql)


async def _set_return(
    conn: AsyncIOConnection, *, query: Query, **query_args: Any,
) -> datatypes.Set:
    return await conn.fetchall(query.edgeql, **query_args)


async def _single_return(
    conn: AsyncIOConnection, *, query: Query, **query_args: Any,
) -> Any:
    return await conn.fetchone(query.edgeql, **query_args)


_OPERATION_TO_EXECUTOR: Mapping[EdgeQLOperationType, Callable] = MappingProxyType(
    {
        EdgeQLOperationType.single_return: _single_return,
        EdgeQLOperationType.set_return: _set_return,
        EdgeQLOperationType.execute: _execute,
    },
)


def create_async_executor(query: Query) -> Callable:
    """Create async executor for query.

    Arguments:
        query: query for which executor should be created.

    Returns:
        Created async executor.
    """
    executor = _OPERATION_TO_EXECUTOR[query.operation_type]
    return partial(executor, query=query)
