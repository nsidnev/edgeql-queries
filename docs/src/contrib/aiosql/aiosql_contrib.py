import asyncio
from uuid import UUID

import aiosql
import asyncpg
import edgedb
from edgeql_queries.contrib import aiosql as eq_aiosql

MOVIE_ID = UUID("6000323c-cc31-474d-828b-dadaa6404674")

pg_queries = aiosql.from_path("./aiosql_contrib.sql", "asyncpg")
edb_queries = aiosql.from_path(
    "./aiosql_contrib.edgeql",
    driver_adapter=eq_aiosql.EdgeQLAsyncAdapter,
    loader_cls=eq_aiosql.EdgeQLQueryLoader,
    queries_cls=eq_aiosql.EdgeQLQueries,
)


async def main():
    edb_conn = await edgedb.async_connect()
    pg_conn = await asyncpg.connect("postgres://postgres@localhost/postgres")

    movie = await edb_queries.select_movie_by_id(edb_conn, MOVIE_ID)
    user_record = await pg_queries.get_username_by_id(
        pg_conn,
        id=movie.director.user_id,
    )
    print(f"Director's name: {user_record[0]}")


asyncio.run(main())
