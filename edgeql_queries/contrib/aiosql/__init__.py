"""Definition of classes for usage with aiosql."""

from edgeql_queries.contrib.aiosql.adapters import EdgeQLAsyncAdapter, EdgeQLSyncAdapter
from edgeql_queries.contrib.aiosql.queries import EdgeQLQueries
from edgeql_queries.contrib.aiosql.query_loaders import EdgeQLQueryLoader

__all__ = (
    "EdgeQLAsyncAdapter",
    "EdgeQLSyncAdapter",
    "EdgeQLQueries",
    "EdgeQLQueryLoader",
)
