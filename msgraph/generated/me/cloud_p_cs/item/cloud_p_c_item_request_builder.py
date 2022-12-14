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

change_user_account_type_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.change_user_account_type.change_user_account_type_request_builder')
end_grace_period_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.end_grace_period.end_grace_period_request_builder')
get_cloud_pc_connectivity_history_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.get_cloud_pc_connectivity_history.get_cloud_pc_connectivity_history_request_builder')
get_cloud_pc_launch_info_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.get_cloud_pc_launch_info.get_cloud_pc_launch_info_request_builder')
get_shift_work_cloud_pc_access_state_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.get_shift_work_cloud_pc_access_state.get_shift_work_cloud_pc_access_state_request_builder')
get_supported_cloud_pc_remote_actions_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.get_supported_cloud_pc_remote_actions.get_supported_cloud_pc_remote_actions_request_builder')
reboot_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.reboot.reboot_request_builder')
rename_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.rename.rename_request_builder')
reprovision_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.reprovision.reprovision_request_builder')
restore_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.restore.restore_request_builder')
retry_partner_agent_installation_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.retry_partner_agent_installation.retry_partner_agent_installation_request_builder')
troubleshoot_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.troubleshoot.troubleshoot_request_builder')
cloud_p_c = lazy_import('msgraph.generated.models.cloud_p_c')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CloudPCItemRequestBuilder():
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
    """
    @property
    def change_user_account_type(self) -> change_user_account_type_request_builder.ChangeUserAccountTypeRequestBuilder:
        """
        Provides operations to call the changeUserAccountType method.
        """
        return change_user_account_type_request_builder.ChangeUserAccountTypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end_grace_period(self) -> end_grace_period_request_builder.EndGracePeriodRequestBuilder:
        """
        Provides operations to call the endGracePeriod method.
        """
        return end_grace_period_request_builder.EndGracePeriodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot(self) -> reboot_request_builder.RebootRequestBuilder:
        """
        Provides operations to call the reboot method.
        """
        return reboot_request_builder.RebootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rename(self) -> rename_request_builder.RenameRequestBuilder:
        """
        Provides operations to call the rename method.
        """
        return rename_request_builder.RenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision(self) -> reprovision_request_builder.ReprovisionRequestBuilder:
        """
        Provides operations to call the reprovision method.
        """
        return reprovision_request_builder.ReprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retry_partner_agent_installation(self) -> retry_partner_agent_installation_request_builder.RetryPartnerAgentInstallationRequestBuilder:
        """
        Provides operations to call the retryPartnerAgentInstallation method.
        """
        return retry_partner_agent_installation_request_builder.RetryPartnerAgentInstallationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshoot(self) -> troubleshoot_request_builder.TroubleshootRequestBuilder:
        """
        Provides operations to call the troubleshoot method.
        """
        return troubleshoot_request_builder.TroubleshootRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CloudPCItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/cloudPCs/{cloudPC%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property cloudPCs for me
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
    
    def create_get_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get cloudPCs from me
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
    
    def create_patch_request_information(self,body: Optional[cloud_p_c.CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property cloudPCs in me
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
    
    async def delete(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property cloudPCs for me
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
    
    async def get(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[cloud_p_c.CloudPC]:
        """
        Get cloudPCs from me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[cloud_p_c.CloudPC]
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
        return await self.request_adapter.send_async(request_info, cloud_p_c.CloudPC, response_handler, error_mapping)
    
    def get_cloud_pc_connectivity_history(self,) -> get_cloud_pc_connectivity_history_request_builder.GetCloudPcConnectivityHistoryRequestBuilder:
        """
        Provides operations to call the getCloudPcConnectivityHistory method.
        Returns: get_cloud_pc_connectivity_history_request_builder.GetCloudPcConnectivityHistoryRequestBuilder
        """
        return get_cloud_pc_connectivity_history_request_builder.GetCloudPcConnectivityHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_cloud_pc_launch_info(self,) -> get_cloud_pc_launch_info_request_builder.GetCloudPcLaunchInfoRequestBuilder:
        """
        Provides operations to call the getCloudPcLaunchInfo method.
        Returns: get_cloud_pc_launch_info_request_builder.GetCloudPcLaunchInfoRequestBuilder
        """
        return get_cloud_pc_launch_info_request_builder.GetCloudPcLaunchInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_shift_work_cloud_pc_access_state(self,) -> get_shift_work_cloud_pc_access_state_request_builder.GetShiftWorkCloudPcAccessStateRequestBuilder:
        """
        Provides operations to call the getShiftWorkCloudPcAccessState method.
        Returns: get_shift_work_cloud_pc_access_state_request_builder.GetShiftWorkCloudPcAccessStateRequestBuilder
        """
        return get_shift_work_cloud_pc_access_state_request_builder.GetShiftWorkCloudPcAccessStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_supported_cloud_pc_remote_actions(self,) -> get_supported_cloud_pc_remote_actions_request_builder.GetSupportedCloudPcRemoteActionsRequestBuilder:
        """
        Provides operations to call the getSupportedCloudPcRemoteActions method.
        Returns: get_supported_cloud_pc_remote_actions_request_builder.GetSupportedCloudPcRemoteActionsRequestBuilder
        """
        return get_supported_cloud_pc_remote_actions_request_builder.GetSupportedCloudPcRemoteActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def patch(self,body: Optional[cloud_p_c.CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[cloud_p_c.CloudPC]:
        """
        Update the navigation property cloudPCs in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[cloud_p_c.CloudPC]
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
        return await self.request_adapter.send_async(request_info, cloud_p_c.CloudPC, response_handler, error_mapping)
    
    @dataclass
    class CloudPCItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CloudPCItemRequestBuilderGetQueryParameters():
        """
        Get cloudPCs from me
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
    class CloudPCItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CloudPCItemRequestBuilder.CloudPCItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CloudPCItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

