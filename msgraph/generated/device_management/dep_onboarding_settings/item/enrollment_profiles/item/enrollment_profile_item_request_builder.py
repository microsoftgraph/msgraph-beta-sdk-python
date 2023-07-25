from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EnrollmentProfileItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}/enrollmentProfiles/{enrollmentProfile%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property enrollmentProfiles for deviceManagement
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[EnrollmentProfile]:
        """
        The enrollment profiles.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EnrollmentProfile]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.enrollment_profile import EnrollmentProfile

        return await self.request_adapter.send_async(request_info, EnrollmentProfile, error_mapping)
    
    async def patch(self,body: Optional[EnrollmentProfile] = None, request_configuration: Optional[EnrollmentProfileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[EnrollmentProfile]:
        """
        Update the navigation property enrollmentProfiles in deviceManagement
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EnrollmentProfile]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.enrollment_profile import EnrollmentProfile

        return await self.request_adapter.send_async(request_info, EnrollmentProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property enrollmentProfiles for deviceManagement
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The enrollment profiles.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[EnrollmentProfile] = None, request_configuration: Optional[EnrollmentProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property enrollmentProfiles in deviceManagement
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class EnrollmentProfileItemRequestBuilderGetQueryParameters():
        """
        The enrollment profiles.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EnrollmentProfileItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EnrollmentProfileItemRequestBuilder.EnrollmentProfileItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EnrollmentProfileItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

