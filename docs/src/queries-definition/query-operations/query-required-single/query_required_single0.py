import edgedb

conn = edgedb.connect()

user = conn.query_required_single(
    """
        SELECT Person {
            username
        }
        FILTER .ip = <str>$user_ip
        LIMIT 1
    """,
    user_ip="127.0.0.1",
)

print("user:", user.username)
