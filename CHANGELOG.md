# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## ["1.0.0a6] - 2023-03-29

### Added

### Changed

- Refactored the import mechanism to use conditional and deferred imports.
- Fixed a bug where discriminator methods were missing some valid types.
- Fixed a bug where the date and guid types were improperly mapped.
- Re-ordered method hierarchy to match python conventions
- Added support for custom httpx client.