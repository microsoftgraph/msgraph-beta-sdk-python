from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ref_request_builder = lazy_import('msgraph.generated.identity.b2x_user_flows.item.user_flow_identity_providers.item.ref.ref_request_builder')

class IdentityProviderBaseItemRequestBuilder():
    """
    Builds and executes requests for operations under /identity/b2xUserFlows/{b2xIdentityUserFlow-id}/userFlowIdentityProviders/{identityProviderBase-id}
    """
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of identityContainer entities.
        """
        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, identity_provider_base_id: Optional[str] = None) -> None:
        """
        Instantiates a new IdentityProviderBaseItemRequestBuilder and sets the default values.
        Args:
            identityProviderBaseId: key: id of identityProviderBase
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/userFlowIdentityProviders/{identityProviderBase%2Did}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["identityProviderBase%2Did"] = identityProviderBaseId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    

