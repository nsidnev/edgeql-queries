# name: select-movie-by-id!
# Get movie by id.
SELECT Movie {
    title,
    year,
    director: {
        user_id,
    },
}
FILTER .id = <uuid>$0
LIMIT 1;
