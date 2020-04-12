# name: create-new-person!
# Create new person with passing first and lst names.
INSERT Person {
    first_name := <str>$first_name,
    last_name := <str>$last_name,
}

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
