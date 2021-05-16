import pytest

from edgeql_queries.queries import Queries
from tests.typing import EdgeDBAsyncFetcher

pytestmark = pytest.mark.asyncio


async def test_selecting_single_object(
    async_fetcher: EdgeDBAsyncFetcher,
    async_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    print(async_fetcher)
    movie = await async_queries.movies.select_movie_by_title(
        async_fetcher,
        title=title_regex,
    )
    assert movie.title == "Blade Runner 2049"


async def test_selecting_multiple_objects(
    async_fetcher: EdgeDBAsyncFetcher,
    async_queries: Queries,
) -> None:
    year = 2017
    movies = await async_queries.movies.select_movies_by_year(async_fetcher, year=year)
    assert movies
    for movie in movies:
        assert movie.year == year


async def test_executing_statemnt(
    async_fetcher: EdgeDBAsyncFetcher,
    async_queries: Queries,
) -> None:
    keanu_first_name = "Keanu"
    await async_queries.persons.create_keanu_reeves(async_fetcher)

    person = await async_queries.persons.get_person_by_first_name(
        async_fetcher,
        first_name=keanu_first_name,
    )
    assert person.first_name == keanu_first_name
    assert person.last_name == "Reeves"


async def test_selecting_using_positional_arguments(
    async_fetcher: EdgeDBAsyncFetcher,
    async_queries: Queries,
) -> None:
    first_arg = "Harry Potter and the Philosopher's Stone"
    second_arg = "Harry Potter%"
    check_result = await async_queries.check_string_matches_regex(
        async_fetcher,
        first_arg,
        second_arg,
    )
    assert check_result
