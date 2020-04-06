from edgeql_queries.queries import Queries


def test_queries_repr() -> None:
    queries = Queries()
    assert repr(queries) == "Queries(queries: [], groups: {})"


def test_getattr_for_queries(async_queries: Queries) -> None:
    assert callable(async_queries.movies.create_new_movie)
