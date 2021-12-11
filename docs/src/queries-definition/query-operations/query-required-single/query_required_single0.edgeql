# name: select-person-by-ip!
# Query user by IP.
SELECT Person {
    username
}
FILTER .ip = <str>$user_ip
LIMIT 1
