"""Definition for base executor."""

import abc
from typing import TypeVar

ExecutorT = TypeVar("ExecutorT", bound="BaseExecutor")


class BaseExecutor(abc.ABC):
    """Base executor for queries."""

    @abc.abstractmethod
    def as_json(self: ExecutorT) -> ExecutorT:  # pragma: no cover
        """Create an executor copy that will use JSON as output format.

        Returns:
            Copied executor.
        """
