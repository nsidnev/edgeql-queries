"""Definition for creator of async executors."""

from copy import copy
from types import MappingProxyType
from typing import Any, Awaitable, Callable, Mapping

from edgedb import AsyncIOExecutor
from edgedb.datatypes import datatypes

from edgeql_queries.executors.base_executor import BaseExecutor
from edgeql_queries.models import EdgeQLOperationType, Query


class AsyncExecutor(BaseExecutor):
    """Async executor for queries."""

    def __init__(self, query: Query) -> None:
        """Initialize an executor for query.

        Arguments:
            query: query for execution.
        """
        super().__init__()

        self._query = query
        self._executor = _OPERATION_TO_EXECUTOR[query.operation_type]

    def __call__(self, conn: AsyncIOExecutor, *args: Any, **kwargs: Any) -> Awaitable:
        """Execute query.

        Arguments:
            conn: asynchronous EdgeDB executor.
            args: positional arguments.
            kwargs: keyword arguments.

        Returns:
            Result of query execution.
        """
        return self._executor(self._query, conn, *args, **kwargs)

    def as_json(self) -> "AsyncExecutor":
        """Create an executor copy that will use JSON as output format.

        Returns:
            Copied executor.
        """
        executor = copy(self)
        executor._executor = _OPERATION_TO_JSON_EXECUTOR[self._query.operation_type]
        return executor


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


async def _json_set_return(
    __edgeql_query__: Query,
    conn: AsyncIOExecutor,
    *query_args: Any,
    **query_kwargs: Any,
) -> str:
    return await conn.query_json(__edgeql_query__.edgeql, *query_args, **query_kwargs)


async def _json_single_return(
    __edgeql_query__: Query,
    conn: AsyncIOExecutor,
    *query_args: Any,
    **query_kwargs: Any,
) -> str:
    return await conn.query_single_json(
        __edgeql_query__.edgeql,
        *query_args,
        **query_kwargs,
    )


async def _json_required_single_return(
    __edgeql_query__: Query,
    conn: AsyncIOExecutor,
    *query_args: Any,
    **query_kwargs: Any,
) -> str:
    return await conn.query_required_single_json(
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

_OPERATION_TO_JSON_EXECUTOR: Mapping[EdgeQLOperationType, Callable] = MappingProxyType(
    {
        EdgeQLOperationType.required_single_return: _json_required_single_return,
        EdgeQLOperationType.single_return: _json_single_return,
        EdgeQLOperationType.set_return: _json_set_return,
        EdgeQLOperationType.execute: _execute,
    },
)
