import edgedb

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")

user = conn.fetchone(
    """
        SELECT Person {
            username
        }
        FILTER .ip = <str>$user_ip
        LIMIT 1
    """,
    user_ip="37.204.79.75",
)
