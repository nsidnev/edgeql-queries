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
