`edgeql-queries` provides an adapter for [aiosql](https://github.com/nackjicholson/aiosql). Using it is quite simple and with its help, you can use `aiosql` and `edgeql-queries` together, while still being able to replace it with another adapter.
You can use, for example, PostgreSQL with EdgeDB, since EdgeDB is based on PostgreSQL and it is possible that in the future, access to the PostgreSQL server that is used by EdgeDB will be open.

`queries.edgeql`:
```edgeql
{!./src/contrib/aiosql/aiosql_contrib.edgeql!}
```

`queries.sql`:
```sql
{!./src/contrib/aiosql/aiosql_contrib.sql!}
```

And python code:
```python3
{!./src/contrib/aiosql/aiosql_contrib.py!}
```
