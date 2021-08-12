# name: create-test-data*
# Setup objects for using in tests.

INSERT Movie {
    title := 'Blade Runner 2049',
    year := 2017,
    director := (
        INSERT Person {
            first_name := 'Denis',
            last_name := 'Villeneuve',
        }
    ),
    actors := {
        (INSERT Person {
            first_name := 'Harrison',
            last_name := 'Ford',
        }),
        (INSERT Person {
            first_name := 'Ryan',
            last_name := 'Gosling',
        }),
        (INSERT Person {
            first_name := 'Ana',
            last_name := 'de Armas',
        }),
    }
};

# name: drop-test-data*
# Delete objects used in tests.
DELETE Movie;
DELETE Person;
