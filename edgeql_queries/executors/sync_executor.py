"""Definition for creator of sync executors."""

from functools import partial
from types import MappingProxyType
from typing import Any, Callable, Mapping

from edgedb import Executor
from edgedb.datatypes import datatypes

from edgeql_queries.models import EdgeQLOperationType, Query


def _execute(__edgeql_query__: Query, executor: Executor) -> None:
    return executor.execute(__edgeql_query__.edgeql)


def _set_return(
    __edgeql_query__: Query,
    conn: Executor,
    *query_args: Any,
    **query_kwargs: Any,
) -> datatypes.Set:
    return conn.query(__edgeql_query__.edgeql, *query_args, **query_kwargs)


def _single_return(
    __edgeql_query__: Query,
    conn: Executor,
    *query_args: Any,
    **query_kwargs: Any,
) -> Any:
    return conn.query_single(__edgeql_query__.edgeql, *query_args, **query_kwargs)


def _required_single_return(
    __edgeql_query__: Query,
    conn: Executor,
    *query_args: Any,
    **query_kwargs: Any,
) -> Any:
    return conn.query_required_single(
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


def create_sync_executor(query: Query) -> Callable:
    """Create sync executor for query.

    Arguments:
        query: query for which executor should be created.

    Returns:
        Created sync executor.
    """
    executor = _OPERATION_TO_EXECUTOR[query.operation_type]
    return partial(executor, query)
