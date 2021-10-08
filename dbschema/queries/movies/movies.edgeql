# name: create-new-movie!
# Create new movie with year, title, director id and actors ids.
INSERT Movie {
    title := <str>$title,
    year := <int64>$year,
    director := (SELECT Person FILTER .id = <uuid>$director_id LIMIT 1),
    actors := (SELECT Person FILTER contains(<array<uuid>>$person_ids, .id))
};

# name: select-movie-by-title+
# Get a single movie by it's title
SELECT Movie {
    title,
    year,
    director: {
        last_name,
    },
    actors: {
        first_name,
        last_name,
    }
}
FILTER .title ILIKE <str>$title
LIMIT 1

# name: select-movies-by-year
# Get movies by release year.
SELECT Movie {
    title,
    year,
    director: {
        last_name,
    },
    actors: {
        first_name,
        last_name,
    }
}
FILTER .year = <int64>$year
