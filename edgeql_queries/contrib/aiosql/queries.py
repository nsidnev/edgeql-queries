"""Definition for aiosql compatible queries."""

from typing import List, Union

from edgeql_queries import queries as eq_queries
from edgeql_queries.contrib.aiosql.adapters import EdgeQLAsyncAdapter, EdgeQLSyncAdapter
from edgeql_queries.models import Query
from edgeql_queries.typing import QueriesTree


class EdgeQLQueries:
    """Queries that are compatible with aiosql."""

    def __init__(self, adapter: Union[EdgeQLSyncAdapter, EdgeQLAsyncAdapter]) -> None:
        """Init queries.

        Arguments:
            adapter: adapter for aiosql with `is_aio_driver` field.
        """
        self._use_async = adapter.is_aio_driver

    def load_from_list(self, queries: List[Query]) -> eq_queries.Queries:
        """Load list of queries.

        Arguments:
            queries: list of queries that should be used for creating
                executors for them.

        Returns:
            Built collection of queries with binded executors.
        """
        return eq_queries.load_from_list(eq_queries.Queries(self._use_async), queries)

    def load_from_tree(self, queries_tree: QueriesTree) -> eq_queries.Queries:
        """Load queries tree.

        Arguments:
            queries_tree: tree of queries that should be used for creating
                executors for them.

        Returns:
            Built collection of queries with binded executors.
        """
        return eq_queries.load_from_tree(
            eq_queries.Queries(self._use_async),
            queries_tree,
        )
