from typing import Union

import edgedb

EdgeDBAsyncFetcher = Union[edgedb.AsyncIOPool, edgedb.AsyncIOConnection]
