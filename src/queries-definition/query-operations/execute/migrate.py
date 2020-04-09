import edgedb
from edgeql_queries import from_path

queries = from_path("./edgeql", async_driver=False)

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")

for migration_query in queries.migrations.available_queries:
    print(f"migrate: {migration_query}")
    with conn.transaction():
        queries.migrations.get_executor(migration_query)(conn)
