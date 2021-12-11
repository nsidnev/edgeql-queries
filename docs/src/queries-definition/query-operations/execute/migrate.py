import edgedb
from edgeql_queries import from_path

queries = from_path("./edgeql", async_driver=False)

conn = edgedb.connect()

for migration_query in queries.migrations.available_queries:
    print(f"migrate: {migration_query.name}")
    for tx in conn.transaction():
        with tx:
            queries.migrations.get_executor(migration_query.name)(tx)
