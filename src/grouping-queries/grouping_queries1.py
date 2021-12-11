import edgedb
import edgeql_queries

queries = edgeql_queries.from_path("./edgeql", async_driver=False)

conn = edgedb.connect()

movies = queries.movies.select_movies_by_year(conn, year=2020)

print(movies)
