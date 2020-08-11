An EdgeQL query that can be parsed using `edgeql-queries` has some limitations:

1. Query must be named.
2. The query's name must not contain characters that cannot be used in Python
    identifiers (**except for the `-` character, since it will be converted to `_`**).
3. They can have special characters after their names, which will change the way
    these queries are executed:
    * `*`: query will be executed as a script using the `.execute` method from the driver.
    * `!`: query will always return a single object, and therefore such query will be
        executed using the `.query_one` method from the driver.
    * empty: a regular query that returns a set of objects and will be executed by the
        `.query` method from the driver.


## Names

The query name must be a valid Python identifier, but it can contain a `-` character,
which will be converted to `_`. An example of valid query names:

* Example 1:
```edgeql
{!./src/queries-definition/right-names/right_name0.edgeql!}
```

* Example 2:
```edgeql
{!./src/queries-definition/right-names/right_name1.edgeql!}
```

* Example 3:
```edgeql
{!./src/queries-definition/right-names/right_name2.edgeql!}
```
