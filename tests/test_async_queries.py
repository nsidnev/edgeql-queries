import json

import edgedb

from edgeql_queries.queries import Queries


async def test_selecting_single_object(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    movie = await async_queries.movies.select_movie_by_title(
        async_client,
        title=title_regex,
    )
    assert movie.title == "Blade Runner 2049"


async def test_selecting_multiple_objects(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    year = 2017
    movies = await async_queries.movies.select_movies_by_year(async_client, year=year)
    assert movies
    for movie in movies:
        assert movie.year == year


async def test_executing_statemnt(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    keanu_first_name = "Keanu"
    await async_queries.persons.create_keanu_reeves(async_client)

    person = await async_queries.persons.get_person_by_first_name(
        async_client,
        first_name=keanu_first_name,
    )
    assert person.first_name == keanu_first_name
    assert person.last_name == "Reeves"


async def test_selecting_using_positional_arguments(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    first_arg = "Harry Potter and the Philosopher's Stone"
    second_arg = "Harry Potter%"
    check_result = await async_queries.check_string_matches_regex(
        async_client,
        first_arg,
        second_arg,
    )
    assert check_result


async def test_selecting_single_object_in_json(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    movie_raw = await async_queries.json.movies.select_movie_by_title(
        async_client,
        title=title_regex,
    )
    movie = json.loads(movie_raw)
    assert movie["title"] == "Blade Runner 2049"


async def test_selecting_multiple_objects_in_json(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    year = 2017
    movies_raw = await async_queries.json.movies.select_movies_by_year(
        async_client,
        year=year,
    )
    movies = json.loads(movies_raw)
    assert movies
    for movie in movies:
        assert movie["year"] == year


async def test_executing_statemnt_in_json(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    keanu_first_name = "Keanu"
    await async_queries.json.persons.create_keanu_reeves(async_client)

    person_raw = await async_queries.json.persons.get_person_by_first_name(
        async_client,
        first_name=keanu_first_name,
    )
    person = json.loads(person_raw)
    assert person["first_name"] == keanu_first_name
    assert person["last_name"] == "Reeves"


async def test_selecting_using_positional_arguments_in_json(
    async_client: edgedb.AsyncIOExecutor,
    async_queries: Queries,
) -> None:
    first_arg = "Harry Potter and the Philosopher's Stone"
    second_arg = "Harry Potter%"
    check_result_raw = await async_queries.json.check_string_matches_regex(
        async_client,
        first_arg,
        second_arg,
    )
    check_result = json.loads(check_result_raw)
    assert check_result
