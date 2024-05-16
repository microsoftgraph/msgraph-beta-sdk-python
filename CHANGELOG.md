# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.4.0] - 2024-05-16

### Changed

- Weekly generation with Kiota 14th May 2024
- Updated Request Configuration classes to use base Request Configuration
-Added Reuest builder custom configuratons for backward compatibility.


## [1.3.0] - 2024-04-16

### Changed

- Weekly generation with Kiota.

## [1.2.0] - 2024-03-19

### Added
- Added support for multipart and form serialization.

### Changed
- Latest metadata updates from 19th March 2024.

## [1.1.0] - 2024-01-24

### Added

### Changed
- Latest metadata updates from 23rd January 2024.

## [1.0.0] - 2023-10-31

### Added

### Changed
- GA release.

## [1.0.0rc0] - 2023-10-27

### Added
- Added request translation method to native request object
- Added opentelemetry to support observability.
- Added support for continous access evaluation.
- Added backing store support and enabled backing store by default.


### Changed
- Refactored request headers from dictionary to HeaderCollection class.
- Fix issue with using raw url in request builder due to incorrect parameter order.
- Switched from uritemplate to std-uritemplate for URI templating.
- Simplified the creation of a graph client.


## [1.0.0a8] - 2023-04-25

### Added

### Changed

- Changed the request builders api to include indexers as part of the path. [#2528](https://github.com/microsoft/kiota/issues/2528)

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