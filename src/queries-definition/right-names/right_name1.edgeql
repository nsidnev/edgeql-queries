# name: get-person-by-full-name!
SELECT Person {
    first_name,
    last_name,
    age
}
FILTER .first_name = <str>$first_name AND .last_name = <str>$last_name
