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

assign_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.assignments.assignments_request_builder')
device_management_configuration_policy_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.assignments.item.device_management_configuration_policy_assignment_item_request_builder')
create_copy_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.create_copy.create_copy_request_builder')
reorder_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.reorder.reorder_request_builder')
settings_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.settings.settings_request_builder')
device_management_configuration_setting_item_request_builder = lazy_import('msgraph.generated.device_management.reusable_policy_settings.item.referencing_configuration_policies.item.settings.item.device_management_configuration_setting_item_request_builder')
device_management_configuration_policy = lazy_import('msgraph.generated.models.device_management_configuration_policy')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceManagementConfigurationPolicyItemRequestBuilder():
    """
    Provides operations to manage the referencingConfigurationPolicies property of the microsoft.graph.deviceManagementReusablePolicySetting entity.
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
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementConfigurationPolicy entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_copy(self) -> create_copy_request_builder.CreateCopyRequestBuilder:
        """
        Provides operations to call the createCopy method.
        """
        return create_copy_request_builder.CreateCopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reorder(self) -> reorder_request_builder.ReorderRequestBuilder:
        """
        Provides operations to call the reorder method.
        """
        return reorder_request_builder.ReorderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementConfigurationPolicy entity.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> device_management_configuration_policy_assignment_item_request_builder.DeviceManagementConfigurationPolicyAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementConfigurationPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_policy_assignment_item_request_builder.DeviceManagementConfigurationPolicyAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationPolicyAssignment%2Did"] = id
        return device_management_configuration_policy_assignment_item_request_builder.DeviceManagementConfigurationPolicyAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementConfigurationPolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/reusablePolicySettings/{deviceManagementReusablePolicySetting%2Did}/referencingConfigurationPolicies/{deviceManagementConfigurationPolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DeviceManagementConfigurationPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property referencingConfigurationPolicies for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DeviceManagementConfigurationPolicyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management_configuration_policy.DeviceManagementConfigurationPolicy]:
        """
        configuration policies referencing the current reusable setting. This property is read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_configuration_policy.DeviceManagementConfigurationPolicy]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management_configuration_policy.DeviceManagementConfigurationPolicy, error_mapping)
    
    async def patch(self,body: Optional[device_management_configuration_policy.DeviceManagementConfigurationPolicy] = None, request_configuration: Optional[DeviceManagementConfigurationPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management_configuration_policy.DeviceManagementConfigurationPolicy]:
        """
        Update the navigation property referencingConfigurationPolicies in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_configuration_policy.DeviceManagementConfigurationPolicy]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management_configuration_policy.DeviceManagementConfigurationPolicy, error_mapping)
    
    def settings_by_id(self,id: str) -> device_management_configuration_setting_item_request_builder.DeviceManagementConfigurationSettingItemRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementConfigurationPolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_configuration_setting_item_request_builder.DeviceManagementConfigurationSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementConfigurationSetting%2Did"] = id
        return device_management_configuration_setting_item_request_builder.DeviceManagementConfigurationSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceManagementConfigurationPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property referencingConfigurationPolicies for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementConfigurationPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        configuration policies referencing the current reusable setting. This property is read-only.
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
    
    def to_patch_request_information(self,body: Optional[device_management_configuration_policy.DeviceManagementConfigurationPolicy] = None, request_configuration: Optional[DeviceManagementConfigurationPolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property referencingConfigurationPolicies in deviceManagement
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
    
    @dataclass
    class DeviceManagementConfigurationPolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceManagementConfigurationPolicyItemRequestBuilderGetQueryParameters():
        """
        configuration policies referencing the current reusable setting. This property is read-only.
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
    class DeviceManagementConfigurationPolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementConfigurationPolicyItemRequestBuilder.DeviceManagementConfigurationPolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementConfigurationPolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

