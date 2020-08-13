<h1 align="center">edgeql-queries</h1>
<p align="center">
    <em>Simple EdgeQL in Python.</em>
</p>
<p align="center">
    <a href=https://github.com/nsidnev/edgeql-queries>
        <img src=https://github.com/nsidnev/edgeql-queries/workflows/Tests/badge.svg alt="Tests" />
    </a>
    <a href=https://github.com/nsidnev/edgeql-queries>
        <img src=https://github.com/nsidnev/edgeql-queries/workflows/Styles/badge.svg alt="Styles" />
    </a>
    <a href="https://codecov.io/gh/nsidnev/edgeql-queries">
        <img src="https://codecov.io/gh/nsidnev/edgeql-queries/branch/master/graph/badge.svg" alt="Coverage" />
    </a>
    <a href="https://github.com/ambv/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style" />
    </a>
    <a href="https://github.com/wemake-services/wemake-python-styleguide">
        <img src="https://img.shields.io/badge/style-wemake-000000.svg" alt="WPS Linter"/>
    </a>
    <a href="https://github.com/nsidnev/edgeql-queries/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/License-FreeBSD-blue" alt="License" />
    </a>
    <a href="https://pypi.org/project/edgeql-queries/">
        <img src="https://badge.fury.io/py/edgeql-queries.svg" alt="Package version" />
    </a>
</p>

---

# Introduction


`edgeql-queries` is a library that allows you to store your
[EdgeQL](https://edgedb.com/docs/edgeql/overview/) queries in separate files and then
execute them like normal Python functions. This way you can control versions of the
queries code, as with any other languages, but use it in Python applications.

!!! information
    This library may become less useful after the release of the
    [query builder](https://edgedb.com/roadmap#client_language_bindings) for EdgeDB,
    but who knows  `¯\_(ツ)_/¯`.

## Requirements

`edgeql-queries` require only the [EdgeDB driver for Python](https://github.com/edgedb/edgedb-python).

## Installation

You can install `edgeql-queries` using `pip`:
```bash
{!./src/index/install_using_pip.sh!}
```

Or if you are using `poetry`:
```bash
{!./src/index/install_using_poetry.sh!}
```

## Example


There is a more complex example based on the EdgeDB [tutorial](https://edgedb.com/docs/tutorial/index)
in the [example](https://github.com/nsidnev/edgeql-queries/blob/master/example) folder in the repository.
You can look there to see more features.

Here is a simplified version:

1. Let's assume that we have the following schema in our already configured database:
```edgeql
{!./src/index/schema.edgeql!}
```

2. We'll write our queries in the `queries.edgeql`:
```edgeql
{!./src/index/queries.edgeql!}
```

3. Finally, we'll write our Python code:
```python3
{!./src/index/main.py!}
```

## Credits

This project is inspired by [aiosql](https://github.com/nackjicholson/aiosql)
project and is based on it's source code.

## License

This project is licensed under the terms of the FreeBSD license.
