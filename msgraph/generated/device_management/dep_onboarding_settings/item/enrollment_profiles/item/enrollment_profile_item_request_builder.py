from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

export_mobile_config_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.enrollment_profiles.item.export_mobile_config.export_mobile_config_request_builder')
set_default_profile_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.enrollment_profiles.item.set_default_profile.set_default_profile_request_builder')
update_device_profile_assignment_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.enrollment_profiles.item.update_device_profile_assignment.update_device_profile_assignment_request_builder')
enrollment_profile = lazy_import('msgraph.generated.models.enrollment_profile')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class EnrollmentProfileItemRequestBuilder():
    """
    Provides operations to manage the enrollmentProfiles property of the microsoft.graph.depOnboardingSetting entity.
    """
    @property
    def set_default_profile(self) -> set_default_profile_request_builder.SetDefaultProfileRequestBuilder:
        """
        Provides operations to call the setDefaultProfile method.
        """
        return set_default_profile_request_builder.SetDefaultProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_device_profile_assignment(self) -> update_device_profile_assignment_request_builder.UpdateDeviceProfileAssignmentRequestBuilder:
        """
        Provides operations to call the updateDeviceProfileAssignment method.
        """
        return update_device_profile_assignment_request_builder.UpdateDeviceProfileAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EnrollmentProfileItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}/enrollmentProfiles/{enrollmentProfile%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property enrollmentProfiles for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def create_get_request_information(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The enrollment profiles.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[enrollment_profile.EnrollmentProfile] = None, request_configuration: Optional[EnrollmentProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property enrollmentProfiles in deviceManagement
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property enrollmentProfiles for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def export_mobile_config(self,) -> export_mobile_config_request_builder.ExportMobileConfigRequestBuilder:
        """
        Provides operations to call the exportMobileConfig method.
        Returns: export_mobile_config_request_builder.ExportMobileConfigRequestBuilder
        """
        return export_mobile_config_request_builder.ExportMobileConfigRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def get(self,request_configuration: Optional[EnrollmentProfileItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[enrollment_profile.EnrollmentProfile]:
        """
        The enrollment profiles.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[enrollment_profile.EnrollmentProfile]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, enrollment_profile.EnrollmentProfile, response_handler, error_mapping)
    
    async def patch(self,body: Optional[enrollment_profile.EnrollmentProfile] = None, request_configuration: Optional[EnrollmentProfileItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[enrollment_profile.EnrollmentProfile]:
        """
        Update the navigation property enrollmentProfiles in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[enrollment_profile.EnrollmentProfile]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, enrollment_profile.EnrollmentProfile, response_handler, error_mapping)
    
    @dataclass
    class EnrollmentProfileItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EnrollmentProfileItemRequestBuilderGetQueryParameters():
        """
        The enrollment profiles.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class EnrollmentProfileItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EnrollmentProfileItemRequestBuilder.EnrollmentProfileItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EnrollmentProfileItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

