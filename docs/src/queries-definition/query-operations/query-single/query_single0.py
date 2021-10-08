import edgedb

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")

user = conn.query_single(
    """
        SELECT Person {
            username
        }
        FILTER .ip = <str>$user_ip
        LIMIT 1
    """,
    user_ip="127.0.0.1",
)

if user is None:
    print("oops, no user was found")
else:
    print("user:", user.username)
