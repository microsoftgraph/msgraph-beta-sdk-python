from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import trust_framework
    from ..models.o_data_errors import o_data_error
    from .key_sets import key_sets_request_builder
    from .key_sets.item import trust_framework_key_set_item_request_builder
    from .policies import policies_request_builder
    from .policies.item import trust_framework_policy_item_request_builder

class TrustFrameworkRequestBuilder():
    """
    Provides operations to manage the trustFramework singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TrustFrameworkRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/trustFramework{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[TrustFrameworkRequestBuilderGetRequestConfiguration] = None) -> Optional[trust_framework.TrustFramework]:
        """
        Get trustFramework
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[trust_framework.TrustFramework]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import trust_framework

        return await self.request_adapter.send_async(request_info, trust_framework.TrustFramework, error_mapping)
    
    def key_sets_by_id(self,id: str) -> trust_framework_key_set_item_request_builder.TrustFrameworkKeySetItemRequestBuilder:
        """
        Provides operations to manage the keySets property of the microsoft.graph.trustFramework entity.
        Args:
            id: Unique identifier of the item
        Returns: trust_framework_key_set_item_request_builder.TrustFrameworkKeySetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .key_sets.item import trust_framework_key_set_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["trustFrameworkKeySet%2Did"] = id
        return trust_framework_key_set_item_request_builder.TrustFrameworkKeySetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[trust_framework.TrustFramework] = None, request_configuration: Optional[TrustFrameworkRequestBuilderPatchRequestConfiguration] = None) -> Optional[trust_framework.TrustFramework]:
        """
        Update trustFramework
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[trust_framework.TrustFramework]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import trust_framework

        return await self.request_adapter.send_async(request_info, trust_framework.TrustFramework, error_mapping)
    
    def policies_by_id(self,id: str) -> trust_framework_policy_item_request_builder.TrustFrameworkPolicyItemRequestBuilder:
        """
        Provides operations to manage the policies property of the microsoft.graph.trustFramework entity.
        Args:
            id: Unique identifier of the item
        Returns: trust_framework_policy_item_request_builder.TrustFrameworkPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .policies.item import trust_framework_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["trustFrameworkPolicy%2Did"] = id
        return trust_framework_policy_item_request_builder.TrustFrameworkPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[TrustFrameworkRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get trustFramework
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[trust_framework.TrustFramework] = None, request_configuration: Optional[TrustFrameworkRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update trustFramework
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def key_sets(self) -> key_sets_request_builder.KeySetsRequestBuilder:
        """
        Provides operations to manage the keySets property of the microsoft.graph.trustFramework entity.
        """
        from .key_sets import key_sets_request_builder

        return key_sets_request_builder.KeySetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> policies_request_builder.PoliciesRequestBuilder:
        """
        Provides operations to manage the policies property of the microsoft.graph.trustFramework entity.
        """
        from .policies import policies_request_builder

        return policies_request_builder.PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TrustFrameworkRequestBuilderGetQueryParameters():
        """
        Get trustFramework
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class TrustFrameworkRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TrustFrameworkRequestBuilder.TrustFrameworkRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TrustFrameworkRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

