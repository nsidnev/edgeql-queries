# name: create-test-users*
FOR x IN {
    (name := 'Alice', theme := 'fire'),
    (name := 'Bob', theme := 'rain'),
    (name := 'Carol', theme := 'clouds'),
    (name := 'Dave', theme := 'forest')
}
UNION (
    INSERT
        User {
            name := x.name,
            theme := x.theme,
        }
);