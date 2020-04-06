import asyncio

import edgedb

from app.models import Person
from app.queries import queries


async def main() -> None:
    conn = await edgedb.async_connect("edgedb://edgedb@localhost/edgedb")

    await queries.create_movies(conn)

    direcror_id = (
        await queries.create_new_person(
            conn, first_name="Denis", last_name="Villeneuve"
        )
    ).id

    persons = [
        Person("Harrison", "Ford"),
        Person("Ryan", "Gosling"),
        Person("Ana", "de Armas"),
    ]
    person_ids = []
    for person in persons:
        created_person = await queries.create_new_person(
            conn, first_name=person.first_name, last_name=person.last_name
        )
        person_ids.append(created_person.id)

    created_movie = await queries.create_new_movie(
        conn,
        year=2017,
        title="Blade Runner 2049",
        director_id=direcror_id,
        person_ids=person_ids,
    )

    movie = await queries.select_movie_by_id(conn, id=created_movie.id)

    print("Movie: ", movie)
    print("Director name: ", movie.director.first_name, movie.director.last_name)

    await conn.aclose()


if __name__ == "__main__":
    asyncio.run(main())
