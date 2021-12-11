import edgedb
import pytest

from edgeql_queries.queries import Queries

pytestmark = pytest.mark.asyncio


async def test_selecting_single_object(
    async_client: edgedb.AsyncIOExecutor,
    aiosql_async_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    movie = await aiosql_async_queries.movies.select_movie_by_title(
        async_client,
        title=title_regex,
    )
    assert movie.title == "Blade Runner 2049"


async def test_selecting_multiple_objects(
    async_client: edgedb.AsyncIOExecutor,
    aiosql_async_queries: Queries,
) -> None:
    year = 2017
    movies = await aiosql_async_queries.movies.select_movies_by_year(
        async_client,
        year=year,
    )
    assert movies
    for movie in movies:
        assert movie.year == year


async def test_executing_statemnt(
    async_client: edgedb.AsyncIOExecutor,
    aiosql_async_queries: Queries,
) -> None:
    keanu_first_name = "Keanu"
    await aiosql_async_queries.persons.create_keanu_reeves(async_client)

    person = await aiosql_async_queries.persons.get_person_by_first_name(
        async_client,
        first_name=keanu_first_name,
    )
    assert person.first_name == keanu_first_name
    assert person.last_name == "Reeves"


async def test_selecting_using_positional_arguments(
    async_client: edgedb.AsyncIOExecutor,
    aiosql_async_queries: Queries,
) -> None:
    first_arg = "Harry Potter and the Philosopher's Stone"
    second_arg = "Harry Potter%"
    check_result = await aiosql_async_queries.check_string_matches_regex(
        async_client,
        first_arg,
        second_arg,
    )
    assert check_result
