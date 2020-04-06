"""Definition for main data models used in this library."""

from dataclasses import dataclass
from enum import IntEnum, auto


class EdgeQLOperationType(IntEnum):
    """Enumeration for operation types for queries."""

    single_return = auto()
    """type for operation that returns a single object."""

    set_return = auto()
    """type for operation that returns a common set of object."""

    execute = auto()
    """type for operation that returns nothing."""


@dataclass
class Query:
    """Parsed query."""

    name: str
    """name of parsed query."""

    operation_type: EdgeQLOperationType
    """query operation type."""

    edgeql: str
    """EdgeQL query that should be executed."""

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
            self.name, self.operation_type.name, self.edgeql,
        )
