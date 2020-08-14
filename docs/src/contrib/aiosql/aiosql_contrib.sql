-- name: get-username-by-id^
-- Get username by user's ID.
SELECT username
FROM users
WHERE id = :id;
