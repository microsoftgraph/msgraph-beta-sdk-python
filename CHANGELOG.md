# Changelog

All notable changes to this project will be documented in this file.

## [1.9.0](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.8.0...v1.9.0) (2024-10-04)


### Features

* **generation:** update request builders and models ([5e70b3f](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/5e70b3f0068b15d5b12ecfc814e876b002c546dc))

## [1.8.0](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.7.0...v1.8.0) (2024-09-26)


### Features

* **generation:** update request builders and models ([9d28eaf](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/9d28eaf3846ff18884b374175374d25f7d8fefdc))

## [1.7.0](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.6.0...v1.7.0) (2024-09-12)


### Features

* **generation:** update request builders and models ([1900608](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/1900608fda6ca721da3ca578e400cde2c5bdd0e0))

## [1.6.0](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.5.3...v1.6.0) (2024-09-06)


### Features

* readme formatting to trigger release please ([e351f0a](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/e351f0accd9009fcde9e385b25b0d25ba239fcd0))


### Bug Fixes

* release please type configuration ([5c3f611](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/5c3f6119a2b7015ddd97c1aaa54a0147353da767))

## [1.5.3](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.5.2...v1.5.3) (2024-08-02)


### Bug Fixes

* requires a higher version of the JSON dependency ([6e8cd64](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/6e8cd6493c44432d7f72d6bf3357dd019d7e68a1))

## [1.5.2](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.5.1...v1.5.2) (2024-07-17)


### Bug Fixes

* bump abstractions requirements to avoid missing multipart ([be1fd47](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/be1fd47754e73523063411bd5f18e4c1db695022))

## [1.5.1](https://github.com/microsoftgraph/msgraph-beta-sdk-python/compare/v1.5.0...v1.5.1) (2024-07-10)


### Bug Fixes

* do not use default mutable parameters ([1ba984e](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/1ba984e9549d02f0206ed191732858a32bbc81a4))
* fixes module name for release ([567b176](https://github.com/microsoftgraph/msgraph-beta-sdk-python/commit/567b176954e587183f620f68b84c600b34ff8035))

## [1.5.0] - 2024-05-23

### Changed

- Weekly generation with Kiota 21st May 2024

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
