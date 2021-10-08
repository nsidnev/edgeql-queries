## Just Execute Query With `*`:


If you are not using the result of the query, you can mark it `*`. This will tell
`edgeql-queries` to use the `.execute` driver method. This may be useful for migration, for example.

!!! information
    This is only an example, because full migration support is directly in the EdgeDB CLI.

For example, there are the following migrations for our scheme:

`edgeql/migrations/migrtaion_0000_default.edgeql`:
```edgeql
{!./src/queries-definition/query-operations/execute/edgeql/migrations/migration_0000_default.edgeql!}
```

`edgeql/migrations/migration_0001_add_movies.edgeql`:
```edgeql
{!./src/queries-definition/query-operations/execute/edgeql/migrations/migration_0001_add_movies.edgeql!}
```

`edgeql/migrations/migration_0002_add_min_year_contraint.edgeql`:
```edgeql
{!./src/queries-definition/query-operations/execute/edgeql/migrations/migration_0002_add_min_year_contraint.edgeql!}
```

We can migrate it using the following code:

```migrate.py```:
```python3
{!./src/queries-definition/query-operations/execute/migrate.py!}
```
