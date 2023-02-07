from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

microsoft_graph_endpoint_request_builder = lazy_import('msgraph.generated.me.devices.item.registered_owners.item.microsoft_graph_endpoint.microsoft_graph_endpoint_request_builder')
microsoft_graph_service_principal_request_builder = lazy_import('msgraph.generated.me.devices.item.registered_owners.item.microsoft_graph_service_principal.microsoft_graph_service_principal_request_builder')
microsoft_graph_user_request_builder = lazy_import('msgraph.generated.me.devices.item.registered_owners.item.microsoft_graph_user.microsoft_graph_user_request_builder')
ref_request_builder = lazy_import('msgraph.generated.me.devices.item.registered_owners.item.ref.ref_request_builder')

class DirectoryObjectItemRequestBuilder():
    """
    Builds and executes requests for operations under /me/devices/{device-id}/registeredOwners/{directoryObject-id}
    """
    @property
    def microsoft_graph_endpoint(self) -> microsoft_graph_endpoint_request_builder.MicrosoftGraphEndpointRequestBuilder:
        """
        Casts the previous resource to endpoint.
        """
        return microsoft_graph_endpoint_request_builder.MicrosoftGraphEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_service_principal(self) -> microsoft_graph_service_principal_request_builder.MicrosoftGraphServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        return microsoft_graph_service_principal_request_builder.MicrosoftGraphServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_user(self) -> microsoft_graph_user_request_builder.MicrosoftGraphUserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        return microsoft_graph_user_request_builder.MicrosoftGraphUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        """
        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/devices/{device%2Did}/registeredOwners/{directoryObject%2Did}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    

