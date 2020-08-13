"""Definition for aiosql compatible query loader."""

from pathlib import Path
from typing import Any, List

from edgeql_queries import query_loaders
from edgeql_queries.models import Query
from edgeql_queries.typing import QueriesTree


class EdgeQLQueryLoader:
    """Query loader that is compatible with aiosql."""

    def __init__(self, *args: Any) -> None:
        """Do nothing but be compatible with aiosql query loader.

        Arguments:
            args: any args that will be used for initializaton by aiosql.
        """

    def load_query_data_from_sql(self, edgeql: str) -> List[Query]:
        """Load queries from EdgeQL string.

        Arguments:
            edgeql: EdgeQL string to create a new collection of queries.

        Returns:
            Parsed queries.
        """
        return query_loaders.load_query_data_from_edgeql(edgeql)

    def load_query_data_from_file(self, file_path: Path) -> List[Query]:
        """Load queries from single file.

        Arguments:
            file_path: path to EdgeQL file to create a new collection of
                queries.

        Returns:
            Parsed queries.
        """
        return query_loaders.load_query_data_from_file(file_path)

    def load_query_data_from_dir_path(self, dir_path: Path) -> QueriesTree:
        """Load queries from directory.

        Arguments:
            dir_path: path to dir with EdgeQL files to create a new collection
                of queries.

        Returns:
            Parsed queries.
        """
        return query_loaders.load_query_data_from_dir_path(dir_path)
