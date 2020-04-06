# name: get-persons-by-age
SELECT Person {
    first_name
}
FILTER .age = <int64>$age
