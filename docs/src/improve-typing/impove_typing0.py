from typing import Protocol, Set, Union, cast
from uuid import UUID

import edgedb
import edgeql_queries


class Person(Protocol):
    id: UUID
    first_name: str
    last_name: str


class Queries:
    async def select_users_by_last_name(
        self,
        executor: edgedb.AsyncIOExecutor,
        last_name: str,
    ) -> Set[Person]:
        ...

    async def select_user_by_id(
        self,
        executor: edgedb.AsyncIOExecutor,
        user_id: UUID,
    ) -> Person:
        ...

    async def create_keanu_reeves(self, executor: edgedb.AsyncIOExecutor) -> None:
        ...


queries = cast(Queries, edgeql_queries.from_path("./queries.edgeql"))
