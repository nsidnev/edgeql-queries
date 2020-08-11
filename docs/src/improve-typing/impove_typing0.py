from typing import Protocol, Set, Union, cast
from uuid import UUID

import edgedb
import edgeql_queries

EdgeDBFetcher = Union[edgedb.AsyncIOPool, edgedb.AsyncIOConnection]


class Person(Protocol):
    id: UUID
    first_name: str
    last_name: str


class Queries:
    async def select_users_by_last_name(
        self, fetcher: EdgeDBFetcher, last_name: str,
    ) -> Set[Person]:
        ...

    async def select_user_by_id(self, fetcher: EdgeDBFetcher, user_id: UUID,) -> Person:
        ...

    async def create_keanu_reeves(self, fetcher: EdgeDBFetcher) -> None:
        ...


queries = cast(Queries, edgeql_queries.from_path("./queries.edgeql"))
