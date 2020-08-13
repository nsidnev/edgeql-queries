"""Definition for aiosql compatible adapters.

Adapters here aren't "real" adapters, that can execute queries
but just dummy classes with compatible interface.
"""


# this drivers won't and shouldn't be used as real drivers.
# they are required only for queries building.


class EdgeQLAsyncAdapter:
    """Dummy adapter for async driver."""

    is_aio_driver = True


class EdgeQLSyncAdapter:
    """Dummy adapter for sync driver."""

    is_aio_driver = False
