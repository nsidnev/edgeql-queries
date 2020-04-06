import edgedb
from edgeql_queries import from_path

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")
queries = from_path("./queries", async_driver=False)

users = queries.select_all_users(conn)
