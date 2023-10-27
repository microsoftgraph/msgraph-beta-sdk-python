# Create the API Client

```py
import asyncio

from azure.identity import EnvironmentCredential
from msgraph_beta import GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Create authentication provider object. Used to authenticate request
credential=EnvironmentCredential()

# Get a service client.
client = GraphServiceClient(credentials=credential)
```

## 1. LIST ALL APPLICATIONS IN THE TENANT (GET /applications)

```py
async def get_applications():
    apps = await client.applications.get()
    if apps and apps.value:
        for app in apps.value:
            print(app.id)
asyncio.run(get_applications())
```