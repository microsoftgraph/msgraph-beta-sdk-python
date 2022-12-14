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

assign_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.assignments.assignments_request_builder')
windows_defender_application_control_supplemental_policy_assignment_item_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.assignments.item.windows_defender_application_control_supplemental_policy_assignment_item_request_builder')
deploy_summary_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.deploy_summary.deploy_summary_request_builder')
device_statuses_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.device_statuses.device_statuses_request_builder')
windows_defender_application_control_supplemental_policy_deployment_status_item_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.device_statuses.item.windows_defender_application_control_supplemental_policy_deployment_status_item_request_builder')
windows_defender_application_control_supplemental_policy = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilder():
    """
    Provides operations to manage the wdacSupplementalPolicies property of the microsoft.graph.deviceAppManagement entity.
    """
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deploy_summary(self) -> deploy_summary_request_builder.DeploySummaryRequestBuilder:
        """
        Provides operations to manage the deploySummary property of the microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy entity.
        """
        return deploy_summary_request_builder.DeploySummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> device_statuses_request_builder.DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy entity.
        """
        return device_statuses_request_builder.DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> windows_defender_application_control_supplemental_policy_assignment_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_defender_application_control_supplemental_policy_assignment_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDefenderApplicationControlSupplementalPolicyAssignment%2Did"] = id
        return windows_defender_application_control_supplemental_policy_assignment_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/wdacSupplementalPolicies/{windowsDefenderApplicationControlSupplementalPolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property wdacSupplementalPolicies for deviceAppManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The collection of Windows Defender Application Control Supplemental Policies.
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
    
    def create_patch_request_information(self,body: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy] = None, request_configuration: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property wdacSupplementalPolicies in deviceAppManagement
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
    
    async def delete(self,request_configuration: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property wdacSupplementalPolicies for deviceAppManagement
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
    
    def device_statuses_by_id(self,id: str) -> windows_defender_application_control_supplemental_policy_deployment_status_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatusItemRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_defender_application_control_supplemental_policy_deployment_status_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDefenderApplicationControlSupplementalPolicyDeploymentStatus%2Did"] = id
        return windows_defender_application_control_supplemental_policy_deployment_status_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]:
        """
        The collection of Windows Defender Application Control Supplemental Policies.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]
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
        return await self.request_adapter.send_async(request_info, windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy, response_handler, error_mapping)
    
    async def patch(self,body: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy] = None, request_configuration: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]:
        """
        Update the navigation property wdacSupplementalPolicies in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]
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
        return await self.request_adapter.send_async(request_info, windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy, response_handler, error_mapping)
    
    @dataclass
    class WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderGetQueryParameters():
        """
        The collection of Windows Defender Application Control Supplemental Policies.
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
    class WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilder.WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

