from typing import List, Protocol, cast
from uuid import UUID

from edgedb import AsyncIOConnection
from edgeql_queries import from_path

from app.models import Movie


class EdgeDBObject(Protocol):
    id: UUID


class Queries(Protocol):
    async def create_movies(self, conn: AsyncIOConnection) -> None:
        ...

    async def create_new_person(
        self,
        conn: AsyncIOConnection,
        first_name: str,
        last_name: str,
    ) -> EdgeDBObject:
        ...

    async def create_new_movie(
        self,
        conn: AsyncIOConnection,
        title: str,
        year: int,
        director_id: UUID,
        person_ids: List[UUID],
    ) -> EdgeDBObject:
        ...

    async def select_movie_by_id(self, conn: AsyncIOConnection, id: UUID) -> Movie:
        ...


queries: Queries = cast(Queries, from_path("./app/edgeql"))
