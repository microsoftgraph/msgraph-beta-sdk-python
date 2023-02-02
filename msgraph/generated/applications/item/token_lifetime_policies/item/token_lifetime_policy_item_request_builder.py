from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ref_request_builder = lazy_import('msgraph.generated.applications.item.token_lifetime_policies.item.ref.ref_request_builder')

class TokenLifetimePolicyItemRequestBuilder():
    """
    Builds and executes requests for operations under /applications/{application-id}/tokenLifetimePolicies/{tokenLifetimePolicy-id}
    """
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        """
        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, token_lifetime_policy_id: Optional[str] = None) -> None:
        """
        Instantiates a new TokenLifetimePolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
            tokenLifetimePolicyId: key: id of tokenLifetimePolicy
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/applications/{application%2Did}/tokenLifetimePolicies/{tokenLifetimePolicy%2Did}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["tokenLifetimePolicy%2Did"] = tokenLifetimePolicyId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    

