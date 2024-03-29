"""Definition for main collection for queries."""

from __future__ import annotations

from typing import Callable, Dict, List, Set, Union

from edgeql_queries.executors.async_executor import AsyncExecutor
from edgeql_queries.executors.sync_executor import SyncExecutor
from edgeql_queries.models import Query
from edgeql_queries.typing import QueriesTree

Executor = Union[AsyncExecutor, SyncExecutor]
QueryHandler = Union[Executor, "Queries"]


def load_from_list(queries_collection: Queries, queries: List[Query]) -> Queries:
    """Add queries from list.

    Arguments:
        queries_collection: already registered queries.
        queries: list of queries to be added.

    Returns:
        Collection of queries to which method was applied.
    """
    for query in queries:
        queries_collection.add_query(query.name, query)

    return queries_collection


def load_from_tree(queries_collection: Queries, query_tree: QueriesTree) -> Queries:
    """Add queries from tree.

    Arguments:
        queries_collection: already registered queries.
        query_tree: tree of queries that should be added.

    Returns:
        Collection of queries to which method was applied.
    """
    for group_name, queries in query_tree.items():
        if isinstance(queries, dict):
            queries_collection.add_query(
                group_name,
                load_from_tree(Queries(queries_collection.is_async), queries),
            )
        else:
            queries_collection.add_query(queries.name, queries)

    return queries_collection


class Queries:
    """Collection and executor for queries."""

    def __init__(self, is_async: bool = True) -> None:
        """Initialize collection and executor for queries.

        Arguments:
            is_async: use async driver for creating queries.
        """
        self._query_handlers: Dict[str, QueryHandler] = {}
        self._available_queries: Set[Query] = set()
        self._available_queries_groups: Dict[str, Queries] = {}
        self._is_async = is_async
        self._json = False

    @property
    def available_queries(self) -> List[Query]:
        """Sorted list of queries available on this collection.

        Returns:
            List of queries.
        """
        return sorted(self._available_queries, key=lambda query: query.name)

    @property
    def is_async(self) -> bool:
        """Will be query handlers generated for async execution.

        Returns:
            Will be query handlers generated for async execution.
        """
        return self._is_async

    @property
    def json(self) -> "Queries":
        """Return copy of queries that will use JSON as output format.

        Returns:
            Copied queries.
        """
        handlers = {}
        for name, query_handler in self._query_handlers.items():
            if isinstance(query_handler, Queries):
                query_handler = query_handler.json
            else:
                query_handler = query_handler.as_json()

            handlers[name] = query_handler

        queries = self.__class__()
        queries._query_handlers = handlers
        queries._json = True
        queries._available_queries = self._available_queries
        queries._available_queries_groups = self._available_queries_groups
        queries._is_async = self._is_async
        return queries

    def add_query(self, name: str, query_handler: Union[Queries, Query]) -> None:
        """Add a single query to collection.

        Arguments:
            name: name of query or sub-queries to be added.
            query_handler: a single [query][edgeql_queries.models.Query] that
                will be transformed to executor or
                [collection of queries][edgeql_queries.queries.Queries]
                that will be registered as sub-queries.
        """
        handler_for_query: Union[Callable, Queries]

        if isinstance(query_handler, Query):
            self._available_queries.add(query_handler)

            if self._is_async:
                handler_for_query = AsyncExecutor(query_handler)
            else:
                handler_for_query = SyncExecutor(query_handler)
        else:
            handler_for_query = query_handler
            self._available_queries_groups[name] = handler_for_query

        self._query_handlers[name] = handler_for_query

    def get_executor(self, query_name: str) -> Union[Callable, "Queries"]:
        """Return executor for query by name.

        Arguments:
            query_name: name of query for which executor should be returned.

        Returns:
            Executor for query.
        """
        return self._query_handlers[query_name]

    def __getattr__(self, query_name: str) -> Union[Callable, "Queries"]:
        """Get executor for query by name.

        Arguments:
            query_name: name of query or group.

        Returns:
            Executor for query.
        """
        return self.get_executor(query_name)

    def __repr__(self) -> str:
        """Return special string representation of collection.

        Returns:
            Raw string for queries collection.
        """
        return "Queries(queries: {0}, groups: {1})".format(
            self.available_queries,
            self._available_queries_groups,
        )
