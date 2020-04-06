# name: migration_0001_add_movies*
CREATE MIGRATION migration_0001_add_movies TO {
    module default {
        type Person {
            required property first_name -> str;
            required property last_name -> str;
        }
        type Movie {
                required property title -> str;
                # the year of release
                property year -> int64;
                required link director -> Person;
                multi link actors -> Person;
        }
    }
};
COMMIT MIGRATION migration_0001_add_movies;
