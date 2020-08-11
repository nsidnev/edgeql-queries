import edgedb
import edgeql_queries

# or edgeql_queries.from_path('./edgeql', async_driver=False) for directory
queries = edgeql_queries.from_path("./queries.edgeql", async_driver=False)

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")

queries.create_new_person(conn, first_name="Keanu", last_name="Reeves")
