"""Definition for main data models used in this library."""

from dataclasses import dataclass
from enum import IntEnum, auto


class EdgeQLOperationType(IntEnum):
    """Enumeration for operation types for queries."""

    #: type for operation that returns a single object.
    single_return = auto()

    #: type for operation that returns a common set of object.
    set_return = auto()

    #: type for operation that returns nothing.
    execute = auto()


@dataclass
class Query:
    """Parsed query."""

    #: name of parsed query.
    name: str

    #: query operation type.
    operation_type: EdgeQLOperationType

    #: EdgeQL query that should be executed.
    edgeql: str

    def __hash__(self) -> int:
        """Hash query.

        Hashing is done by query's name.

        Returns:
            Query's hash.
        """
        return hash(self.name)

    def __str__(self) -> str:
        """Return string representation of query.

        Returns:
            String representation of query that is its name.
        """
        return self.name

    def __repr__(self) -> str:
        """Return raw string representation of query.

        Returns:
            Raw string representation of query that contains all fields.
        """
        return "Query(name: {0!r}, operation_type: {1}, edgeql: {2!r})".format(
            self.name,
            self.operation_type.name,
            self.edgeql,
        )
