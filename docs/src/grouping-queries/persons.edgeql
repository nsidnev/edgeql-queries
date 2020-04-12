# name: create-new-person!
# Create new person with passing first and lst names.
INSERT Person {
    first_name := <str>$first_name,
    last_name := <str>$last_name,
}
