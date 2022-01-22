"""Definition for creator of async executors."""

from functools import partial
from types import MappingProxyType
from typing import Any, Callable, Mapping

from edgedb import AsyncIOExecutor
from edgedb.datatypes import datatypes

from edgeql_queries.models import EdgeQLOperationType, Query


async def _execute(__edgeql_query__: Query, conn: AsyncIOExecutor) -> None:
    return await conn.execute(__edgeql_query__.edgeql)


async def _set_return(
    __edgeql_query__: Query,
    conn: AsyncIOExecutor,
    *query_args: Any,
    **query_kwargs: Any,
) -> datatypes.Set:
    return await conn.query(__edgeql_query__.edgeql, *query_args, **query_kwargs)


async def _single_return(
    __edgeql_query__: Query,
    conn: AsyncIOExecutor,
    *query_args: Any,
    **query_kwargs: Any,
) -> Any:
    return await conn.query_single(__edgeql_query__.edgeql, *query_args, **query_kwargs)


async def _required_single_return(
    __edgeql_query__: Query,
    conn: AsyncIOExecutor,
    *query_args: Any,
    **query_kwargs: Any,
) -> Any:
    return await conn.query_required_single(
        __edgeql_query__.edgeql,
        *query_args,
        **query_kwargs,
    )


_OPERATION_TO_EXECUTOR: Mapping[EdgeQLOperationType, Callable] = MappingProxyType(
    {
        EdgeQLOperationType.required_single_return: _required_single_return,
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
    return partial(executor, query)
