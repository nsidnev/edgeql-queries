import json

import edgedb
import pytest

from edgeql_queries.queries import Queries


def test_selecting_required_single_object(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    movie = sync_queries.movies.select_movie_by_title_required(
        sync_client,
        title=title_regex,
    )
    assert movie.title == "Blade Runner 2049"

    title_regex = "this does not exist"
    with pytest.raises(edgedb.errors.NoDataError):
        sync_queries.movies.select_movie_by_title_required(
            sync_client,
            title=title_regex,
        )


def test_selecting_single_object(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    movie = sync_queries.movies.select_movie_by_title(sync_client, title=title_regex)
    assert movie.title == "Blade Runner 2049"

    title_regex = "this does not exist"
    movie = sync_queries.movies.select_movie_by_title(
        sync_client,
        title=title_regex,
    )
    assert movie is None


def test_selecting_multiple_objects(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    year = 2017
    movies = sync_queries.movies.select_movies_by_year(sync_client, year=year)
    assert movies
    for movie in movies:
        assert movie.year == year


def test_executing_statemnt(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    keanu_first_name = "Keanu"
    sync_queries.persons.create_keanu_reeves(sync_client)

    person = sync_queries.persons.get_person_by_first_name(
        sync_client,
        first_name=keanu_first_name,
    )
    assert person.first_name == keanu_first_name
    assert person.last_name == "Reeves"


def test_selecting_using_positional_arguments(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    first_arg = "Harry Potter and the Philosopher's Stone"
    second_arg = "Harry Potter%"
    check_result = sync_queries.check_string_matches_regex(
        sync_client,
        first_arg,
        second_arg,
    )
    assert check_result


def test_selecting_single_object_in_json(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    title_regex = "blade runner%"
    movie_raw = sync_queries.json.movies.select_movie_by_title(
        sync_client,
        title=title_regex,
    )
    movie = json.loads(movie_raw)
    assert movie["title"] == "Blade Runner 2049"


def test_selecting_multiple_objects_in_json(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    year = 2017
    movies_raw = sync_queries.json.movies.select_movies_by_year(sync_client, year=year)
    movies = json.loads(movies_raw)
    assert movies
    for movie in movies:
        assert movie["year"] == year


def test_executing_statemnt_in_json(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    keanu_first_name = "Keanu"
    sync_queries.json.persons.create_keanu_reeves(sync_client)

    person_raw = sync_queries.json.persons.get_person_by_first_name(
        sync_client,
        first_name=keanu_first_name,
    )
    person = json.loads(person_raw)
    assert person["first_name"] == keanu_first_name
    assert person["last_name"] == "Reeves"


def test_selecting_using_positional_arguments_in_json(
    sync_client: edgedb.Executor,
    sync_queries: Queries,
) -> None:
    first_arg = "Harry Potter and the Philosopher's Stone"
    second_arg = "Harry Potter%"
    check_result_raw = sync_queries.json.check_string_matches_regex(
        sync_client,
        first_arg,
        second_arg,
    )
    check_result = json.loads(check_result_raw)
    assert check_result
