## Query Single Object With `+`:


If you know that your query can return either a single object or `None`, you can put `+` at the end of
its name and then `edgeql-queries` will use the `.query_single` method from driver for this query.

For example, here is the code that directly uses the python driver:
```python3
{!./src/queries-definition/query-operations/query-single/query_single0.py!}
```

And this is the code that uses `edgeql-queries`:

`queries.edgeql`:
```edgeql
{!./src/queries-definition/query-operations/query-single/query_single0.edgeql!}
```

And python code:
```python3
{!./src/queries-definition/query-operations/query-single/query_single1.py!}
```
