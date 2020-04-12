If you pass a single file or directory without nesting in the 
[from_path][edgeql_queries.loaders.from_path] function, then your EdgeQL queries will be placed 
directly in the returned [queries][edgeql_queries.queries.Queries] as attributes.

For example, if there is a single file with queries named `queries.edgeql`:
```edgeql
{!./src/grouping-queries/queries.edgeql!}
```

or a directory named `edgeql` with 2 `edgeql/persons.edgeql` and `edgeql/movies.edgeql` files:

`edgeql/persons.edgeql`:
```edgeql
{!./src/grouping-queries/persons.edgeql!}
```

`edgeql/movies.edgeql`
```edgeql
{!./src/grouping-queries/movies.edgeql!}
```

Then working python code will look like this:

```python
{!./src/grouping-queries/grouping_queries0.py!}
```


But if you pass a directory with subdirectories that contain `.edgeql` files, then these 
queries will be placed as subqueries in the returned queries.

For example, if there is the following directory tree:

```text
{!./src/grouping-queries/queries-tree.txt!}
```

Then `edgeql-queries` will generate 2 subgroups for the returned queries, and the 
working code will look like this:

```python
{!./src/grouping-queries/grouping_queries1.py!}
```