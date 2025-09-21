# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- A print statement from [`listing_tracker/database/listings.py`](/listing_tracker/database/listings.py) notifies users about successful database insertions
- Inserted the GitHub repository link in the `pyproject.toml` file
- Started this changelog (`CHANGELOG.md`)
- Created the `/docs/` directory containing `commands.md` and documentation for the tracker's files
- Created GitHub Actions workflows under `./github/workflows` to publish this package to PyPI

### Changed
- Rewrote `README.md` to a "usage" syntax 
- Upgraded the `pyproject.toml` requires-python project attribute from >=3.9 to >=3.10
- Modified and clarified existing command syntax across various files
- Corrected general grammatical and mechanical errors
- Listings are added to the database by adding urls in the command statement
- More than one listing can be added to the database at a time by adding multiple urls to the command statement
- Changed inserted_webpages to listings

### Removed
- Unnecessary class method

## [0.1.0-planning] - 2025-08-03

### Added
- The first repository commit and initial publish

[Unreleased]: https://github.com/MICHI64N/listing_tracker/compare/v0.1.0-planning...HEAD
[0.1.0-planning]: https://github.com/MICHI64N/listing_tracker/releases/tag/v0.1.0-planning