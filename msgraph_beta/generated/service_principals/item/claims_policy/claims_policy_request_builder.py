from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.custom_claims_policy import CustomClaimsPolicy
    from ....models.o_data_errors.o_data_error import ODataError

class ClaimsPolicyRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the claimsPolicy property of the microsoft.graph.servicePrincipal entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ClaimsPolicyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/claimsPolicy{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ClaimsPolicyRequestBuilderGetQueryParameters]] = None) -> Optional[CustomClaimsPolicy]:
        """
        Get the properties and relationships of a customClaimsPolicy object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomClaimsPolicy]
        Find more info here: https://learn.microsoft.com/graph/api/customclaimspolicy-get?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.custom_claims_policy import CustomClaimsPolicy

        return await self.request_adapter.send_async(request_info, CustomClaimsPolicy, error_mapping)
    
    async def patch(self,body: CustomClaimsPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomClaimsPolicy]:
        """
        Update a customClaimsPolicy object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomClaimsPolicy]
        Find more info here: https://learn.microsoft.com/graph/api/customclaimspolicy-update?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.custom_claims_policy import CustomClaimsPolicy

        return await self.request_adapter.send_async(request_info, CustomClaimsPolicy, error_mapping)
    
    async def put(self,body: CustomClaimsPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomClaimsPolicy]:
        """
        Update a customClaimsPolicy object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomClaimsPolicy]
        Find more info here: https://learn.microsoft.com/graph/api/customclaimspolicy-update?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.custom_claims_policy import CustomClaimsPolicy

        return await self.request_adapter.send_async(request_info, CustomClaimsPolicy, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ClaimsPolicyRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the properties and relationships of a customClaimsPolicy object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CustomClaimsPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update a customClaimsPolicy object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_put_request_information(self,body: CustomClaimsPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update a customClaimsPolicy object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ClaimsPolicyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ClaimsPolicyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ClaimsPolicyRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ClaimsPolicyRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a customClaimsPolicy object.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
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
    class ClaimsPolicyRequestBuilderGetRequestConfiguration(RequestConfiguration[ClaimsPolicyRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ClaimsPolicyRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ClaimsPolicyRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

