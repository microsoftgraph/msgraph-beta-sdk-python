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
    from ....models.inbound_shared_user_profile import InboundSharedUserProfile
    from ....models.o_data_errors.o_data_error import ODataError
    from .export_personal_data.export_personal_data_request_builder import ExportPersonalDataRequestBuilder
    from .remove_personal_data.remove_personal_data_request_builder import RemovePersonalDataRequestBuilder

class InboundSharedUserProfileUserItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the inboundSharedUserProfiles property of the microsoft.graph.directory entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new InboundSharedUserProfileUserItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/inboundSharedUserProfiles/{inboundSharedUserProfile%2DuserId}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property inboundSharedUserProfiles for directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InboundSharedUserProfileUserItemRequestBuilderGetQueryParameters]] = None) -> Optional[InboundSharedUserProfile]:
        """
        Read the properties of an inboundSharedUserProfile.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InboundSharedUserProfile]
        Find more info here: https://learn.microsoft.com/graph/api/inboundshareduserprofile-get?view=graph-rest-beta
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
        from ....models.inbound_shared_user_profile import InboundSharedUserProfile

        return await self.request_adapter.send_async(request_info, InboundSharedUserProfile, error_mapping)
    
    async def patch(self,body: InboundSharedUserProfile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[InboundSharedUserProfile]:
        """
        Update the navigation property inboundSharedUserProfiles in directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InboundSharedUserProfile]
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
        from ....models.inbound_shared_user_profile import InboundSharedUserProfile

        return await self.request_adapter.send_async(request_info, InboundSharedUserProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property inboundSharedUserProfiles for directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InboundSharedUserProfileUserItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties of an inboundSharedUserProfile.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: InboundSharedUserProfile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property inboundSharedUserProfiles in directory
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
    
    def with_url(self,raw_url: str) -> InboundSharedUserProfileUserItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InboundSharedUserProfileUserItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InboundSharedUserProfileUserItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def export_personal_data(self) -> ExportPersonalDataRequestBuilder:
        """
        Provides operations to call the exportPersonalData method.
        """
        from .export_personal_data.export_personal_data_request_builder import ExportPersonalDataRequestBuilder

        return ExportPersonalDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_personal_data(self) -> RemovePersonalDataRequestBuilder:
        """
        Provides operations to call the removePersonalData method.
        """
        from .remove_personal_data.remove_personal_data_request_builder import RemovePersonalDataRequestBuilder

        return RemovePersonalDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class InboundSharedUserProfileUserItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InboundSharedUserProfileUserItemRequestBuilderGetQueryParameters():
        """
        Read the properties of an inboundSharedUserProfile.
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
    class InboundSharedUserProfileUserItemRequestBuilderGetRequestConfiguration(RequestConfiguration[InboundSharedUserProfileUserItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InboundSharedUserProfileUserItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

