# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-09-21

### Added
- A print statement from [`listing_tracker/database/listings.py`](/listing_tracker/database/listings.py) notifies users about successful database insertions
- Inserted the GitHub repository link in the `pyproject.toml` file
- Started this changelog (`CHANGELOG.md`)
- Created the `/docs/` directory containing `commands.md` and documentation for the tracker's files
- Created GitHub Actions workflows under `./github/workflows` to publish this package to PyPI

### Changed
- Upgraded Python requirements from >=3.9 to >=3.10
- Revised database listing references from the term "inserted_webpages" or "webpages" to "listings"
- Rewrote `README.md` to a "usage" syntax 
- Modified and clarified existing command syntax across various files
- Corrected general grammatical and mechanical errors
- Listings are added to the database by adding urls in the command statement
- More than one listing can be added to the database at a time by adding multiple urls to the command statement

### Removed
- Unnecessary class method

## [0.1.0-planning] - 2025-08-03

### Added
- The first repository commit and initial publish

[0.1.0]: https://github.com/MICHI64N/listing_tracker/compare/v0.1.0-planning...v0.1.0
[0.1.0-planning]: https://github.com/MICHI64N/listing_tracker/releases/tag/v0.1.0-planning