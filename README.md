# Microsoft Graph Beta SDK for Python

Get started with the Microsoft Graph SDK for Python by integrating the [Microsoft Graph API](https://docs.microsoft.com/graph/overview) into your Python application.

> **Note:** 
> * This SDK allows you to build applications using the latest [beta](https://docs.microsoft.com/graph/use-the-api#version) version of Microsoft Graph. If you want to try the v1.0 Microsoft Graph API, use the [v1.0](https://github.com/microsoftgraph/msgraph-sdk-python) SDK.
> * The Microsoft Graph Beta Python SDK is currently in public preview. Don't use this SDK in production environments. For details see [SDKs in preview or GA status](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview#sdks-in-preview-or-ga-status).

## 1. Installation

```py
pip install msgraph-beta-sdk
```

## 2. Getting started with Microsoft Graph

### 2.1 Register your application

Register your application by following the steps at [Register your app with the Microsoft Identity Platform](https://docs.microsoft.com/graph/auth-register-app-v2).

### 2.2 Create an AuthenticationProvider object

An instance of the **GraphServiceClient** class handles building client. To create a new instance of this class, you need to provide an instance of **AuthenticationProvider**, which can authenticate requests to Microsoft Graph.

> **Note**: For authentication we support both `sync` and `async` credential classes from `azure.identity`. Please see the azure identity [docs](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity?view=azure-python) for more information.

```py
# Example using async credentials.
from azure.identity.aio import EnvironmentCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider

scopes = ['User.Read', 'Mail.Read']
credential=EnvironmentCredential()
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)
```

### 2.3 Initialise a GraphRequestAdapter object

The SDK uses an adapter object that handles the HTTP concerns. This HTTP adapter object is used to build the Graph client for making requests.

To initialise one using the authentication provider created in the previous step:

```py
from msgraph import GraphRequestAdapter

adapter = GraphRequestAdapter(auth_provider)
```

We currently use [HTTPX](https://www.python-httpx.org/) as our HTTP client. You can pass your custom configured `httpx.AsyncClient` using:

```py
from msgraph import GraphRequestAdapter
from msgraph_core import GraphClientFactory

http_Client = GraphClientFactory.create_with_default_middleware(client=httpx.AsyncClient())
request_adapter = GraphRequestAdapter(auth_Provider, http_client)
```

### 2.3 Get a GraphServiceClient object

You must get a **GraphServiceClient** object to make requests against the service.

```py
from msgraph import GraphServiceClient

client = GraphServiceClient(request_adapter)
```

## 3. Make requests against the service

After you have a **GraphServiceClient** that is authenticated, you can begin making calls against the service. The requests against the service look like our [REST API](https://docs.microsoft.com/graph/api/overview?view=graph-rest-1.0).

> **Note**: This SDK offers an asynchronous API by default. Async is a concurrency model that is far more efficient than multi-threading, and can provide significant performance benefits and enable the use of long-lived network connections such as WebSockets. We support popular python async envronments such as `asyncio`, `anyio` or `trio`.

The following is a complete example that shows how to fetch a user from Microsoft Graph.

```py
import asyncio
from azure.identity.aio import ClientSecretCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

credential = ClientSecretCredential(
    'tenant_id',
    'client_id',
    'client_secret'
)
scopes = ['User.Read']
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)

async def get_user():
    user = await client.users_by_id('userPrincipalName').get())
    print(user.display_name)

asyncio.run(get_user())
```

Note that to calling `me` requires a signed-in user and therefore delegated permissions (obtained using the `authorization_code` flow):

```py
import asyncio
from azure.identity.aio import AuthorizationCodeCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

credential = AuthorizationCodeCredential(
    'tenant_id',
    'client_id',
    'authorization_code',
    'redirect_uri',
)
scopes=['User.Read']
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)

async def me():
    me = await client.me.get()
    print(me.display_name)

asyncio.run(me())
```

### 3.1 Error Handling

Failed requests raise `APIError` exceptions. You can handle these exceptions using `try` `catch` statements.
```py
async def get_user():
    try:
        user = await client.users_by_id('userID').get()
        print(user.user_principal_name, user.display_name, user.id)
    except Exception as e:
        print(f'Error: {e.error.message}')

asyncio.run(get_user())
```


## Documentation and resources

* [Overview](https://docs.microsoft.com/graph/overview)

* [Microsoft Graph website](https://aka.ms/graph)

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
