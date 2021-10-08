An EdgeQL query that can be parsed using `edgeql-queries` has some limitations:

1. Query must be named.
2. The query's name must not contain characters that cannot be used in Python
    identifiers (**except for the `-` character, since it will be converted to `_`**).
3. They can have special symbols after their names that will change how
    this queries will be executed:
    * `*`: query will be executed as script with using `.execute` method from driver.
    * `+`: query will return a single object or `None` and executed with
        `.query_single` method from driver.
    * `!`: query will always return a single object and executed with
        `.query_required_single` method from driver.
    * empty: common query that will return a set of objects and will be executed with
        `.query` method from driver.


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
