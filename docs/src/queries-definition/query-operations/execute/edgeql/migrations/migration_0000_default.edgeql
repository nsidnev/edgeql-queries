# name: migration_0000_default*
CREATE MIGRATION migration_0000_default TO {
    module default {
        type Person {
            required property first_name -> str;
            required property last_name -> str;
        }
    }
};
COMMIT MIGRATION migration_0000_default;
