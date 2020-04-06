import edgedb
import pytest

from edgeql_queries.queries import Queries

pytestmark = pytest.mark.asyncio


async def test_selecting_single_object(
    async_connection: edgedb.AsyncIOConnection, async_queries: Queries
) -> None:
    title_regex = "blade runner%"
    movie = await async_queries.movies.select_movie_by_title(
        async_connection, title=title_regex
    )
    assert movie.title == "Blade Runner 2049"


async def test_selecting_multiple_objects(
    async_connection: edgedb.AsyncIOConnection, async_queries: Queries
) -> None:
    year = 2017
    movies = await async_queries.movies.select_movies_by_year(
        async_connection, year=year
    )
    assert movies
    for movie in movies:
        assert movie.year == year


async def test_executing_statemnt(
    async_connection: edgedb.AsyncIOConnection, async_queries: Queries
) -> None:
    keanu_first_name = "Keanu"
    await async_queries.persons.create_keanu_reeves(async_connection)

    person = await async_queries.persons.get_person_by_first_name(
        async_connection, first_name=keanu_first_name
    )
    assert person.first_name == keanu_first_name
    assert person.last_name == "Reeves"
