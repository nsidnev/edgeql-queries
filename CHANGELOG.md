# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

<small>[Compare with 0.0.5](https://github.com/nsidnev/edgeql-queries/compare/0.0.5...HEAD)</small>

### Changed

* Run CI on EdgeDB Alpha 6.
* Run EdgeDB in docker-compose using EdgeDB Alpha 6.
* Bump dependencies.

## [0.0.5] - 2020-09-02

<small>[Compare with 0.0.4](https://github.com/nsidnev/edgeql-queries/compare/0.0.4...0.0.5)</small>

### Changed

* Pin `edgedb-python` version on `>= 0.9.0`.
* Run CI on EdgeDB Alpha 5.

## [0.0.4] - 2020-08-22

<small>[Compare with 0.0.3](https://github.com/nsidnev/edgeql-queries/compare/0.0.3...0.0.4)</small>

### Changed

* Change queries parsing allowing arbitrary comments in queries.

## [0.0.3] - 2020-08-14

<small>[Compare with 0.0.2](https://github.com/nsidnev/edgeql-queries/compare/0.0.2...0.0.3)</small>

### Added

* Add support for `aiosql` via custom adapter.

### Changed

* Update `netlify-action` to update existing message with docs deployment instead of spaming with new one.
* Change the license from `MIT` to `FreeBSD` as in the parent projects([`aiosql`](https://github.com/nackjicholson/aiosql) and [`anosql`](https://github.com/honza/anosql)).

## [0.0.2] - 2020-08-11

<small>[Compare with 0.0.1](https://github.com/nsidnev/edgeql-queries/compare/0.0.1...0.0.2)</small>

### Added

* Add support for positional arguments.
* Add `py.typed` file for providing types information for type checkers.
* Add support for pools.

### Changed

* Move to `nox` from scripts.
* Run CI on EdgeDB alpha 4.
* Pin `edgedb-python` on `^0.9.0`.

### Fixed

* Fix typos and examples in docs.

## [0.0.1] - 2020-04-09

<small>[Compare with first commit](https://github.com/nsidnev/edgeql-queries/compare/8ccbf7955a1e158f58a978b18e662c9bf137f5a5...0.0.1)</small>

### Added

* First release.
