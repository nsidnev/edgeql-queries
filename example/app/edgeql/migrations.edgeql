# name: create-movies*
# Migrate movies schema inside transaction.
START TRANSACTION;

CREATE MIGRATION movies TO {
    module default {
        type Movie {
            required property title -> str;
            # the year of release
            property year -> int64;
            required link director -> Person;
            multi link actors -> Person;
        }
        type Person {
            required property first_name -> str;
            required property last_name -> str;
        }
    }
};

COMMIT MIGRATION movies;

COMMIT;
