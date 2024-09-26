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
    from ......models.enrollment_profile import EnrollmentProfile
    from ......models.o_data_errors.o_data_error import ODataError
    from .export_mobile_config.export_mobile_config_request_builder import ExportMobileConfigRequestBuilder
    from .set_default_profile.set_default_profile_request_builder import SetDefaultProfileRequestBuilder
    from .update_device_profile_assignment.update_device_profile_assignment_request_builder import UpdateDeviceProfileAssignmentRequestBuilder

class EnrollmentProfileItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the enrollmentProfiles property of the microsoft.graph.depOnboardingSetting entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EnrollmentProfileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}/enrollmentProfiles/{enrollmentProfile%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property enrollmentProfiles for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EnrollmentProfileItemRequestBuilderGetQueryParameters]] = None) -> Optional[EnrollmentProfile]:
        """
        The enrollment profiles.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EnrollmentProfile]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.enrollment_profile import EnrollmentProfile

        return await self.request_adapter.send_async(request_info, EnrollmentProfile, error_mapping)
    
    async def patch(self,body: EnrollmentProfile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EnrollmentProfile]:
        """
        Update the navigation property enrollmentProfiles in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EnrollmentProfile]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.enrollment_profile import EnrollmentProfile

        return await self.request_adapter.send_async(request_info, EnrollmentProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property enrollmentProfiles for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EnrollmentProfileItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The enrollment profiles.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: EnrollmentProfile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property enrollmentProfiles in deviceManagement
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
    
    def with_url(self,raw_url: str) -> EnrollmentProfileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EnrollmentProfileItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EnrollmentProfileItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def export_mobile_config(self) -> ExportMobileConfigRequestBuilder:
        """
        Provides operations to call the exportMobileConfig method.
        """
        from .export_mobile_config.export_mobile_config_request_builder import ExportMobileConfigRequestBuilder

        return ExportMobileConfigRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_default_profile(self) -> SetDefaultProfileRequestBuilder:
        """
        Provides operations to call the setDefaultProfile method.
        """
        from .set_default_profile.set_default_profile_request_builder import SetDefaultProfileRequestBuilder

        return SetDefaultProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_device_profile_assignment(self) -> UpdateDeviceProfileAssignmentRequestBuilder:
        """
        Provides operations to call the updateDeviceProfileAssignment method.
        """
        from .update_device_profile_assignment.update_device_profile_assignment_request_builder import UpdateDeviceProfileAssignmentRequestBuilder

        return UpdateDeviceProfileAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EnrollmentProfileItemRequestBuilderGetQueryParameters():
        """
        The enrollment profiles.
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
    class EnrollmentProfileItemRequestBuilderGetRequestConfiguration(RequestConfiguration[EnrollmentProfileItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EnrollmentProfileItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

