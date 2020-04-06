import edgedb
from edgeql_queries import from_path

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")
queries = from_path("./queries", async_driver=False)

user = queries.select_person_by_ip(conn, user_ip="37.204.79.75")
