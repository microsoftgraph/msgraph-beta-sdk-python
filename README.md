# Microsoft Graph Beta SDK for Python

[![PyPI version](https://badge.fury.io/py/msgraph-beta-sdk.svg)](https://badge.fury.io/py/msgraph-beta-sdk)
[![Downloads](https://pepy.tech/badge/msgraph-beta-sdk)](https://pepy.tech/project/msgraph-beta-sdk)
[![Supported Versions](https://img.shields.io/pypi/pyversions/msgraph-beta-sdk.svg)](https://pypi.org/project/msgraph-beta-sdk)
[![Contributors](https://img.shields.io/github/contributors/microsoftgraph/msgraph-beta-sdk-python.svg)](https://github.com/microsoftgraph/msgraph-beta-sdk-python/graphs/contributors)

Get started with the Microsoft Graph Beta SDK for Python by integrating the [Microsoft Graph API](https://docs.microsoft.com/graph/overview) into your Python application.

> **Note:**
>
> * This SDK allows you to build applications using the latest [beta](https://docs.microsoft.com/graph/use-the-api#version) version of Microsoft Graph. If you want to try the v1.0 Microsoft Graph API, use the [v1.0](https://github.com/microsoftgraph/msgraph-sdk-python) SDK.

## 1. Installation

```py
pip install msgraph-beta-sdk
```

> **Note:**
>
> * The Microsoft Graph Beta SDK for Python is a fairly large package. It may take a few minutes for the initial installation to complete.
> * Enable long paths in your environment if you receive a `Could not install packages due to an OSError`. For details, see [Enable Long Paths in Windows 10, Version 1607, and Later](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later).

## 2. Getting started with Microsoft Graph

### 2.1 Register your application

Register your application by following the steps at [Register your app with the Microsoft Identity Platform](https://docs.microsoft.com/graph/auth-register-app-v2).

### 2.3 Get a GraphServiceClient object

You must get a **GraphServiceClient** object to make requests against the service.

An instance of the **GraphServiceClient** class handles building client. To create a new instance of this class, you need to provide an instance of **Credential**, which can authenticate requests to Microsoft Graph.

> **Note**: For authentication we support both `sync` and `async` credential classes from `azure.identity`. Please see the azure identity [docs](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity?view=azure-python) for more information.

```py
# Example using async credentials.
from azure.identity.aio import EnvironmentCredential
from msgraph_beta import GraphServiceClient

scopes = ['User.Read', 'Mail.Read']
credential = EnvironmentCredential()
client = GraphServiceClient(credential, scopes=scopes)
```

> **Note**: Refer to the [following documentation page](https://learn.microsoft.com/graph/sdks/customize-client?tabs=python#configuring-the-http-proxy-for-the-client) if you need to configure an HTTP proxy.

## 3. Make requests against the service

After you have a **GraphServiceClient** that is authenticated, you can begin making calls against the service. The requests against the service look like our [REST API](https://docs.microsoft.com/graph/api/overview?view=graph-rest-1.0).

> **Note**: This SDK offers an asynchronous API by default. Async is a concurrency model that is far more efficient than multi-threading, and can provide significant performance benefits and enable the use of long-lived network connections such as WebSockets. We support popular python async envronments such as `asyncio`, `anyio` or `trio`.

The following is a complete example that shows how to fetch a user from Microsoft Graph.

```py
import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph_beta import GraphServiceClient

credential = ClientSecretCredential(
    'tenant_id',
    'client_id',
    'client_secret'
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credential, scopes=scopes)

async def get_user():
    user = await client.users.by_user_id('userPrincipalName').get()
    if user:
      print(user.display_name)
asyncio.run(get_user())
```

Note that to calling `me` requires a signed-in user and therefore delegated permissions. See [Authenticating Users](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#authenticate-users)) for more:

```py
import asyncio
from azure.identity import InteractiveBrowserCredential
from msgraph_beta import GraphServiceClient

credential = InteractiveBrowserCredential()
scopes=['User.Read']
client = GraphServiceClient(credential, scopes=scopes)

async def me():
    me = await client.me.get()
    if me:
        print(me.display_name)
asyncio.run(me())
```

### 3.1 Error Handling

Failed requests raise `APIError` exceptions. You can handle these exceptions using `try` `catch` statements.

```py
from kiota_abstractions.api_error import APIError
async def get_user():
    try:
        user = await client.users.by_user_id('userID').get()
        print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())
```

## Documentation and resources

* [Overview](https://docs.microsoft.com/graph/overview)

* [Microsoft Graph website](https://aka.ms/graph)

* [Samples](docs)

## Upgrading

For detailed information on breaking changes, bug fixes and new functionality introduced during major upgrades, check out our [Upgrade Guide](UPGRADING.md)

## Issues

View or log issues on the [Issues](https://github.com/microsoftgraph/msgraph-beta-sdk-python/issues) tab in the repo.

## Contribute

Please read our [Contributing](CONTRIBUTING.md) guidelines carefully for advice on how to contribute to this repo.

## Copyright and license

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the MIT [license](LICENSE).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Third Party Notices

[Third-party notices](THIRD%20PARTY%20NOTICES)
