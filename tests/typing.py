from typing import Union

import edgedb

EdgeDBAsyncFetcher = Union[
    edgedb.AsyncIOPool,
    edgedb.AsyncIOConnection,
    edgedb.AsyncIOTransaction,
]
EdgeDBSyncFetcher = Union[edgedb.BlockingIOConnection, edgedb.Transaction]
