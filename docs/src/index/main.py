import edgedb
import edgeql_queries

queries = edgeql_queries.from_path("./queries.edgeql", async_driver=False)

conn = edgedb.connect("edgedb://edgedb@localhost/edgedb")

# create Keanu
queries.create_keanu_reeves(conn)

# query all Keanu from database
keanu_set = queries.select_users_by_last_name(conn, last_name="Reeves")

for keanu in keanu_set:
    keanu_from_db = queries.select_user_by_id(conn, user_id=keanu.id)
    print(f"{keanu.first_name} {keanu_from_db.last_name}: {keanu_from_db.id}")
