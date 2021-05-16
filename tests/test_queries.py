from edgeql_queries.models import EdgeQLOperationType, Query
from edgeql_queries.queries import Queries


def test_queries_repr() -> None:
    queries = Queries()
    assert repr(queries) == "Queries(queries: [], groups: {})"  # noqa: P103


def test_getattr_for_queries(async_queries: Queries) -> None:
    assert callable(async_queries.movies.create_new_movie)


def test_available_queries_are_sorted_by_name() -> None:
    manual_queries = [
        Query(f"query{i}", EdgeQLOperationType.set_return, "SELECT 1 + 1")
        for i in range(10)
    ]
    queries = Queries()
    for query in manual_queries:
        queries.add_query(query.name, query)

    assert queries.available_queries == manual_queries
