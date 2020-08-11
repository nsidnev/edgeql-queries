import pytest

from edgeql_queries.exceptions import EdgeQLParsingError
from edgeql_queries.parsing import parse_query_from_string


def test_error_if_query_is_in_wrong_format() -> None:
    with pytest.raises(EdgeQLParsingError):
        parse_query_from_string(
            """
            SELECT Person {
                id,
                first_name,
                last_name
            }
            """,
        )


def test_error_if_query_name_is_in_wrong_format() -> None:
    with pytest.raises(EdgeQLParsingError):
        parse_query_from_string(
            """
            # name: error-+query
            SELECT Person {
                id,
                first_name,
                last_name
            }
            """,
        )
