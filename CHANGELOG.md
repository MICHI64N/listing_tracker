# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Created `commands.py` to streamline command actions
- Implemented the `view` command
- Created the `classes.md` and `database/table_class.md` (originally `database/tables.md`) files within the `/docs/` directory

### Changed
- File changes:
  - File `classes.py` is now `table_class.py`
  - Files `listings.py` and `websites.py` moved under the new `listing_tracker/database/tables/` directory
- Documentation changes:
  - Added depth to existing documentation
  - File `database/tables.md` now has documentation regarding the tables in the database.

## [0.1.0] - 2025-09-21

### Added
- Started this changelog (`CHANGELOG.md`)
- Created the `/docs/` directory containing `commands.md` and documentation (`toplevel.md`, `database.md`, `database/listings.md`, `database/tables.md`) for the tracker's files
- Created GitHub Actions workflows under `./github/workflows` to publish this package to PyPI

### Changed
- Upgraded Python requirements from >=3.9 to >=3.10
- Rewrote `README.md` to a "usage" syntax
- Listing command changes:
  - Modified and clarified existing command syntax
  - Listings are now added to the database by adding urls in the command statement
  - More than one listing can be added to the database at a time by adding multiple urls to the command statement

### Fixed
- A print statement from [`listing_tracker/database/listings.py`](/listing_tracker/database/listings.py) now notifies users about successful database insertions

## [0.1.0-planning] - 2025-08-03

### Added
- The first repository commit and initial publish

[Unreleased]: https://github.com/MICHI64N/listing_tracker/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/MICHI64N/listing_tracker/compare/v0.1.0-planning...v0.1.0
[0.1.0-planning]: https://github.com/MICHI64N/listing_tracker/releases/tag/v0.1.0-planning