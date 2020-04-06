from dataclasses import dataclass
from typing import Set, cast
from uuid import UUID

import edgedb
from edgeql_queries import from_path


@dataclass
class EdgeDBObject:
    id: UUID


@dataclass
class Person(EdgeDBObject):
    first_name: str
    last_name: str


class Queries:
    async def select_users_by_last_name(
        self, conn: edgedb.AsyncIOConnection, last_name: str
    ) -> Set[Person]:
        ...

    async def select_user_by_id(
        self, conn: edgedb.AsyncIOConnection, user_id: UUID
    ) -> Person:
        ...

    async def create_keanu_reeves(self, conn: edgedb.AsyncIOConnection) -> None:
        ...


queries = cast(Queries, from_path("./queries.edgeql"))
