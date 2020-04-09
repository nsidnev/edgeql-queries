# name: migration_0002_add_min_year_constraint*
CREATE MIGRATION migration_0002_add_min_year_constraint TO {
    module default {
        type Person {
            required property first_name -> str;
            required property last_name -> str;
        }
        type Movie {
                required property title -> str;
                # the year of release
                property year -> int64 {
                    constraint min_value(1888);
                };
                required link director -> Person;
                multi link actors -> Person;
        }
    }
};
COMMIT MIGRATION migration_0002_add_min_year_constraint;
