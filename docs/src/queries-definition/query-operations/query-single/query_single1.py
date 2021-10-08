import edgedb
from edgeql_queries import from_path

conn = edgedb.connect()
queries = from_path("./queries.edgeql", async_driver=False)

user = queries.select_person_by_ip(conn, user_ip="127.0.0.1")
if user is None:
    print("oops, no user was found")
else:
    print("user:", user.username)
