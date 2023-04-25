# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0a8] - 2023-04-25

### Added

### Changed

- Changed the request builders api to include indexers as part of the path. [#2528](https://github.com/microsoft/kiota/issues/2528)

## [1.0.0a7] - 2023-04-12

### Added

### Changed

- Fixed a bug where UUIDs were being passed as u_u_i_d to desrialization methods.

## [1.0.0a6] - 2023-03-29

### Added

### Changed

- Refactored the import mechanism to use conditional and deferred imports.
- Fixed a bug where discriminator methods were missing some valid types.
- Fixed a bug where the date and guid types were improperly mapped.
- Re-ordered method hierarchy to match python conventions
- Added support for custom httpx client.