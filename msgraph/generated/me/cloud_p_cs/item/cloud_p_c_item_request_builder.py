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

microsoft_graph_change_user_account_type_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_change_user_account_type.microsoft_graph_change_user_account_type_request_builder')
microsoft_graph_end_grace_period_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_end_grace_period.microsoft_graph_end_grace_period_request_builder')
microsoft_graph_get_cloud_pc_connectivity_history_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_get_cloud_pc_connectivity_history.microsoft_graph_get_cloud_pc_connectivity_history_request_builder')
microsoft_graph_get_cloud_pc_launch_info_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_get_cloud_pc_launch_info.microsoft_graph_get_cloud_pc_launch_info_request_builder')
microsoft_graph_get_shift_work_cloud_pc_access_state_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_get_shift_work_cloud_pc_access_state.microsoft_graph_get_shift_work_cloud_pc_access_state_request_builder')
microsoft_graph_get_supported_cloud_pc_remote_actions_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_get_supported_cloud_pc_remote_actions.microsoft_graph_get_supported_cloud_pc_remote_actions_request_builder')
microsoft_graph_reboot_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_reboot.microsoft_graph_reboot_request_builder')
microsoft_graph_rename_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_rename.microsoft_graph_rename_request_builder')
microsoft_graph_reprovision_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_reprovision.microsoft_graph_reprovision_request_builder')
microsoft_graph_restore_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_restore.microsoft_graph_restore_request_builder')
microsoft_graph_retry_partner_agent_installation_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_retry_partner_agent_installation.microsoft_graph_retry_partner_agent_installation_request_builder')
microsoft_graph_troubleshoot_request_builder = lazy_import('msgraph.generated.me.cloud_p_cs.item.microsoft_graph_troubleshoot.microsoft_graph_troubleshoot_request_builder')
cloud_p_c = lazy_import('msgraph.generated.models.cloud_p_c')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CloudPCItemRequestBuilder():
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
    """
    @property
    def microsoft_graph_change_user_account_type(self) -> microsoft_graph_change_user_account_type_request_builder.MicrosoftGraphChangeUserAccountTypeRequestBuilder:
        """
        Provides operations to call the changeUserAccountType method.
        """
        return microsoft_graph_change_user_account_type_request_builder.MicrosoftGraphChangeUserAccountTypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_end_grace_period(self) -> microsoft_graph_end_grace_period_request_builder.MicrosoftGraphEndGracePeriodRequestBuilder:
        """
        Provides operations to call the endGracePeriod method.
        """
        return microsoft_graph_end_grace_period_request_builder.MicrosoftGraphEndGracePeriodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_cloud_pc_connectivity_history(self) -> microsoft_graph_get_cloud_pc_connectivity_history_request_builder.MicrosoftGraphGetCloudPcConnectivityHistoryRequestBuilder:
        """
        Provides operations to call the getCloudPcConnectivityHistory method.
        """
        return microsoft_graph_get_cloud_pc_connectivity_history_request_builder.MicrosoftGraphGetCloudPcConnectivityHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_cloud_pc_launch_info(self) -> microsoft_graph_get_cloud_pc_launch_info_request_builder.MicrosoftGraphGetCloudPcLaunchInfoRequestBuilder:
        """
        Provides operations to call the getCloudPcLaunchInfo method.
        """
        return microsoft_graph_get_cloud_pc_launch_info_request_builder.MicrosoftGraphGetCloudPcLaunchInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_shift_work_cloud_pc_access_state(self) -> microsoft_graph_get_shift_work_cloud_pc_access_state_request_builder.MicrosoftGraphGetShiftWorkCloudPcAccessStateRequestBuilder:
        """
        Provides operations to call the getShiftWorkCloudPcAccessState method.
        """
        return microsoft_graph_get_shift_work_cloud_pc_access_state_request_builder.MicrosoftGraphGetShiftWorkCloudPcAccessStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_supported_cloud_pc_remote_actions(self) -> microsoft_graph_get_supported_cloud_pc_remote_actions_request_builder.MicrosoftGraphGetSupportedCloudPcRemoteActionsRequestBuilder:
        """
        Provides operations to call the getSupportedCloudPcRemoteActions method.
        """
        return microsoft_graph_get_supported_cloud_pc_remote_actions_request_builder.MicrosoftGraphGetSupportedCloudPcRemoteActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reboot(self) -> microsoft_graph_reboot_request_builder.MicrosoftGraphRebootRequestBuilder:
        """
        Provides operations to call the reboot method.
        """
        return microsoft_graph_reboot_request_builder.MicrosoftGraphRebootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_rename(self) -> microsoft_graph_rename_request_builder.MicrosoftGraphRenameRequestBuilder:
        """
        Provides operations to call the rename method.
        """
        return microsoft_graph_rename_request_builder.MicrosoftGraphRenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reprovision(self) -> microsoft_graph_reprovision_request_builder.MicrosoftGraphReprovisionRequestBuilder:
        """
        Provides operations to call the reprovision method.
        """
        return microsoft_graph_reprovision_request_builder.MicrosoftGraphReprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_restore(self) -> microsoft_graph_restore_request_builder.MicrosoftGraphRestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return microsoft_graph_restore_request_builder.MicrosoftGraphRestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_retry_partner_agent_installation(self) -> microsoft_graph_retry_partner_agent_installation_request_builder.MicrosoftGraphRetryPartnerAgentInstallationRequestBuilder:
        """
        Provides operations to call the retryPartnerAgentInstallation method.
        """
        return microsoft_graph_retry_partner_agent_installation_request_builder.MicrosoftGraphRetryPartnerAgentInstallationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_troubleshoot(self) -> microsoft_graph_troubleshoot_request_builder.MicrosoftGraphTroubleshootRequestBuilder:
        """
        Provides operations to call the troubleshoot method.
        """
        return microsoft_graph_troubleshoot_request_builder.MicrosoftGraphTroubleshootRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    async def delete(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property cloudPCs for me
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
    
    async def get(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> Optional[cloud_p_c.CloudPC]:
        """
        Get cloudPCs from me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_p_c.CloudPC]
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
        return await self.request_adapter.send_async(request_info, cloud_p_c.CloudPC, error_mapping)
    
    async def patch(self,body: Optional[cloud_p_c.CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[cloud_p_c.CloudPC]:
        """
        Update the navigation property cloudPCs in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_p_c.CloudPC]
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
        return await self.request_adapter.send_async(request_info, cloud_p_c.CloudPC, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_get_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
    
    def to_patch_request_information(self,body: Optional[cloud_p_c.CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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

    

