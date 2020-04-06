from edgeql_queries.models import EdgeQLOperationType, Query


def test_query_repr() -> None:
    query = Query("query", EdgeQLOperationType.execute, "SELECT 1 + 1")
    expected = "Query(name: 'query', operation_type: execute, edgeql: 'SELECT 1 + 1')"
    assert repr(query) == expected


def test_queries_str() -> None:
    query = Query("query", EdgeQLOperationType.execute, "SELECT 1 + 1")
    assert str(query) == query.name
