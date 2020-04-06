# name: select-users-by-last-name
# Select all users that have same last name.
SELECT Person {
    first_name,
}
FILTER .last_name = <str>$last_name

# name: select-user-by-id!
# Select single user's last name by it's id.
SELECT Person {
    last_name
}
FILTER .id = <uuid>$user_id

# name: create-keanu-reeves*
# Create new user.
INSERT Person {
    first_name := "Keanu",
    last_name := "Reeves",
}