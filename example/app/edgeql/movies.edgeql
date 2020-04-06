# name: create-new-movie!
# Create new movie with year, title, director id and actors ids.
INSERT Movie {
    title := <str>$title,
    year := <int64>$year,
    director := (SELECT Person FILTER .id = <uuid>$director_id LIMIT 1),
    actors := (SELECT Person FILTER contains(<array<uuid>>$person_ids, .id))
};

# name: select-movie-by-id!
# Get a single movie by it's id
SELECT Movie {
    title,
    year,
    director: {
        first_name,
        last_name,
    },
    actors: {
        first_name,
        last_name,
    }
}
FILTER .id = <uuid>$id
