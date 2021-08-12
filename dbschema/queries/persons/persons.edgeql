# name: create-new-person!
# Create new person with passing first and lst names.
INSERT Person {
    first_name := <str>$first_name,
    last_name := <str>$last_name,
}

# name: create-keanu-reeves*
# Create Keanu Reeves.
INSERT Person {
    first_name := 'Keanu',
    last_name := 'Reeves',
}

# name: get-person-by-first-name!
# Get a single user by first name.
SELECT Person {
    first_name,
    last_name,
}
FILTER .first_name = <str>$first_name
LIMIT 1
