# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

<small>[Compare with 0.1.0](https://github.com/nsidnev/edgeql-queries/compare/0.1.0...HEAD)</small>

### Changed

- Pin `edgedb` 0.17.0 as minimal required version.
- Use new `.query_single` methods instead of `.query_one`.

### Misc

- Bump dependencies.
- Update `EdgeQL` lexer from latest master commit.
- Run CI using latest `EdgeDB Beta 3` version.
- Move `EdgeQL` queries files used in tests into `dbschema` directory created by `edgedb project`.
- Update tests to get rid of `EdgeDB`'s DNS.

## [0.1.0] - 2021-05-17

<small>[Compare with 0.0.5](https://github.com/nsidnev/edgeql-queries/compare/0.0.5...0.1.0)</small>

### Added

- Support transactions as arguments in queries.

### Misc

- Bump dependencies.
- Add cache for dependencies in CI.
- Add `Python 3.9` in CI's matrix when running tests.
- Run CI using latest `EdgeDB Beta 2` version.
- Update CI using latest stable actions.
- Migrate to GitHub-native Dependantbot.
- Replace `docker-compose` with `edgedb projects`.
- Move `pytest`, `coverage`, `mypy` and `isort` configuration into `pyproject.toml`.
- Run `flake8` on tests with `flake8-pytest-style` and fix issues.

## [0.0.5] - 2020-09-02

<small>[Compare with 0.0.4](https://github.com/nsidnev/edgeql-queries/compare/0.0.4...0.0.5)</small>

### Changed

- Pin `edgedb-python` version on `>= 0.9.0`.

### Misc

- Run CI on `EdgeDB Alpha 5`.

## [0.0.4] - 2020-08-22

<small>[Compare with 0.0.3](https://github.com/nsidnev/edgeql-queries/compare/0.0.3...0.0.4)</small>

### Changed

- Change queries parsing allowing arbitrary comments in queries.

## [0.0.3] - 2020-08-14

<small>[Compare with 0.0.2](https://github.com/nsidnev/edgeql-queries/compare/0.0.2...0.0.3)</small>

### Added

- Support `aiosql` via custom adapter.

### Changed

- Change the license from `MIT` to `FreeBSD` as in the parent projects([`aiosql`](https://github.com/nackjicholson/aiosql) and [`anosql`](https://github.com/honza/anosql)).

### Misc

- Update `netlify-action` to update existing message with docs deployment instead of spaming with new one.

## [0.0.2] - 2020-08-11

<small>[Compare with 0.0.1](https://github.com/nsidnev/edgeql-queries/compare/0.0.1...0.0.2)</small>

### Added

- Support positional arguments in queries.
- Include `py.typed` file for providing types information for type checkers.
- Support running queries through pools.

### Changed

- Pin `edgedb-python` on `^0.9.0`.

### Fixed

- Fix typos and examples in docs.

### Misc

- Move to `nox` from scripts.
- Run CI on `EdgeDB alpha 4`.

## [0.0.1] - 2020-04-09

<small>[Compare with first commit](https://github.com/nsidnev/edgeql-queries/compare/8ccbf7955a1e158f58a978b18e662c9bf137f5a5...0.0.1)</small>

### Added

- First release.
