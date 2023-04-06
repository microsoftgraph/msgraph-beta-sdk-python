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
    from .....models import cloud_p_c
    from .....models.o_data_errors import o_data_error
    from .change_user_account_type import change_user_account_type_request_builder
    from .end_grace_period import end_grace_period_request_builder
    from .get_cloud_pc_connectivity_history import get_cloud_pc_connectivity_history_request_builder
    from .get_cloud_pc_launch_info import get_cloud_pc_launch_info_request_builder
    from .get_shift_work_cloud_pc_access_state import get_shift_work_cloud_pc_access_state_request_builder
    from .get_supported_cloud_pc_remote_actions import get_supported_cloud_pc_remote_actions_request_builder
    from .power_off import power_off_request_builder
    from .power_on import power_on_request_builder
    from .reboot import reboot_request_builder
    from .rename import rename_request_builder
    from .reprovision import reprovision_request_builder
    from .restore import restore_request_builder
    from .retry_partner_agent_installation import retry_partner_agent_installation_request_builder
    from .start import start_request_builder
    from .stop import stop_request_builder
    from .troubleshoot import troubleshoot_request_builder

class CloudPCItemRequestBuilder():
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.virtualEndpoint entity.
    """
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
        self.url_template: str = "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property cloudPCs for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> Optional[cloud_p_c.CloudPC]:
        """
        Cloud managed virtual desktops.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cloud_p_c.CloudPC]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import cloud_p_c

        return await self.request_adapter.send_async(request_info, cloud_p_c.CloudPC, error_mapping)
    
    async def patch(self,body: Optional[cloud_p_c.CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[cloud_p_c.CloudPC]:
        """
        Update the navigation property cloudPCs in deviceManagement
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
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import cloud_p_c

        return await self.request_adapter.send_async(request_info, cloud_p_c.CloudPC, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property cloudPCs for deviceManagement
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
        Cloud managed virtual desktops.
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
    
    def to_patch_request_information(self,body: Optional[cloud_p_c.CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property cloudPCs in deviceManagement
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
    def change_user_account_type(self) -> change_user_account_type_request_builder.ChangeUserAccountTypeRequestBuilder:
        """
        Provides operations to call the changeUserAccountType method.
        """
        from .change_user_account_type import change_user_account_type_request_builder

        return change_user_account_type_request_builder.ChangeUserAccountTypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end_grace_period(self) -> end_grace_period_request_builder.EndGracePeriodRequestBuilder:
        """
        Provides operations to call the endGracePeriod method.
        """
        from .end_grace_period import end_grace_period_request_builder

        return end_grace_period_request_builder.EndGracePeriodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_connectivity_history(self) -> get_cloud_pc_connectivity_history_request_builder.GetCloudPcConnectivityHistoryRequestBuilder:
        """
        Provides operations to call the getCloudPcConnectivityHistory method.
        """
        from .get_cloud_pc_connectivity_history import get_cloud_pc_connectivity_history_request_builder

        return get_cloud_pc_connectivity_history_request_builder.GetCloudPcConnectivityHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_launch_info(self) -> get_cloud_pc_launch_info_request_builder.GetCloudPcLaunchInfoRequestBuilder:
        """
        Provides operations to call the getCloudPcLaunchInfo method.
        """
        from .get_cloud_pc_launch_info import get_cloud_pc_launch_info_request_builder

        return get_cloud_pc_launch_info_request_builder.GetCloudPcLaunchInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_shift_work_cloud_pc_access_state(self) -> get_shift_work_cloud_pc_access_state_request_builder.GetShiftWorkCloudPcAccessStateRequestBuilder:
        """
        Provides operations to call the getShiftWorkCloudPcAccessState method.
        """
        from .get_shift_work_cloud_pc_access_state import get_shift_work_cloud_pc_access_state_request_builder

        return get_shift_work_cloud_pc_access_state_request_builder.GetShiftWorkCloudPcAccessStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_supported_cloud_pc_remote_actions(self) -> get_supported_cloud_pc_remote_actions_request_builder.GetSupportedCloudPcRemoteActionsRequestBuilder:
        """
        Provides operations to call the getSupportedCloudPcRemoteActions method.
        """
        from .get_supported_cloud_pc_remote_actions import get_supported_cloud_pc_remote_actions_request_builder

        return get_supported_cloud_pc_remote_actions_request_builder.GetSupportedCloudPcRemoteActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power_off(self) -> power_off_request_builder.PowerOffRequestBuilder:
        """
        Provides operations to call the powerOff method.
        """
        from .power_off import power_off_request_builder

        return power_off_request_builder.PowerOffRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power_on(self) -> power_on_request_builder.PowerOnRequestBuilder:
        """
        Provides operations to call the powerOn method.
        """
        from .power_on import power_on_request_builder

        return power_on_request_builder.PowerOnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot(self) -> reboot_request_builder.RebootRequestBuilder:
        """
        Provides operations to call the reboot method.
        """
        from .reboot import reboot_request_builder

        return reboot_request_builder.RebootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rename(self) -> rename_request_builder.RenameRequestBuilder:
        """
        Provides operations to call the rename method.
        """
        from .rename import rename_request_builder

        return rename_request_builder.RenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision(self) -> reprovision_request_builder.ReprovisionRequestBuilder:
        """
        Provides operations to call the reprovision method.
        """
        from .reprovision import reprovision_request_builder

        return reprovision_request_builder.ReprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore import restore_request_builder

        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retry_partner_agent_installation(self) -> retry_partner_agent_installation_request_builder.RetryPartnerAgentInstallationRequestBuilder:
        """
        Provides operations to call the retryPartnerAgentInstallation method.
        """
        from .retry_partner_agent_installation import retry_partner_agent_installation_request_builder

        return retry_partner_agent_installation_request_builder.RetryPartnerAgentInstallationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> start_request_builder.StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start import start_request_builder

        return start_request_builder.StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> stop_request_builder.StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        from .stop import stop_request_builder

        return stop_request_builder.StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshoot(self) -> troubleshoot_request_builder.TroubleshootRequestBuilder:
        """
        Provides operations to call the troubleshoot method.
        """
        from .troubleshoot import troubleshoot_request_builder

        return troubleshoot_request_builder.TroubleshootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CloudPCItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CloudPCItemRequestBuilderGetQueryParameters():
        """
        Cloud managed virtual desktops.
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
    class CloudPCItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

