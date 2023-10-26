from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.cloud_p_c import CloudPC
    from .....models.o_data_errors.o_data_error import ODataError
    from .change_user_account_type.change_user_account_type_request_builder import ChangeUserAccountTypeRequestBuilder
    from .create_snapshot.create_snapshot_request_builder import CreateSnapshotRequestBuilder
    from .end_grace_period.end_grace_period_request_builder import EndGracePeriodRequestBuilder
    from .get_cloud_pc_connectivity_history.get_cloud_pc_connectivity_history_request_builder import GetCloudPcConnectivityHistoryRequestBuilder
    from .get_cloud_pc_launch_info.get_cloud_pc_launch_info_request_builder import GetCloudPcLaunchInfoRequestBuilder
    from .get_frontline_cloud_pc_access_state.get_frontline_cloud_pc_access_state_request_builder import GetFrontlineCloudPcAccessStateRequestBuilder
    from .get_shift_work_cloud_pc_access_state.get_shift_work_cloud_pc_access_state_request_builder import GetShiftWorkCloudPcAccessStateRequestBuilder
    from .get_supported_cloud_pc_remote_actions.get_supported_cloud_pc_remote_actions_request_builder import GetSupportedCloudPcRemoteActionsRequestBuilder
    from .power_off.power_off_request_builder import PowerOffRequestBuilder
    from .power_on.power_on_request_builder import PowerOnRequestBuilder
    from .reboot.reboot_request_builder import RebootRequestBuilder
    from .rename.rename_request_builder import RenameRequestBuilder
    from .reprovision.reprovision_request_builder import ReprovisionRequestBuilder
    from .resize.resize_request_builder import ResizeRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .retry_partner_agent_installation.retry_partner_agent_installation_request_builder import RetryPartnerAgentInstallationRequestBuilder
    from .start.start_request_builder import StartRequestBuilder
    from .stop.stop_request_builder import StopRequestBuilder
    from .troubleshoot.troubleshoot_request_builder import TroubleshootRequestBuilder

class CloudPCItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CloudPCItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/cloudPCs/{cloudPC%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property cloudPCs for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> Optional[CloudPC]:
        """
        Read the properties and relationships of a specific cloudPC object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpc-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    async def patch(self,body: Optional[CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[CloudPC]:
        """
        Update the navigation property cloudPCs in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property cloudPCs for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a specific cloudPC object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property cloudPCs in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CloudPCItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudPCItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CloudPCItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def change_user_account_type(self) -> ChangeUserAccountTypeRequestBuilder:
        """
        Provides operations to call the changeUserAccountType method.
        """
        from .change_user_account_type.change_user_account_type_request_builder import ChangeUserAccountTypeRequestBuilder

        return ChangeUserAccountTypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_snapshot(self) -> CreateSnapshotRequestBuilder:
        """
        Provides operations to call the createSnapshot method.
        """
        from .create_snapshot.create_snapshot_request_builder import CreateSnapshotRequestBuilder

        return CreateSnapshotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end_grace_period(self) -> EndGracePeriodRequestBuilder:
        """
        Provides operations to call the endGracePeriod method.
        """
        from .end_grace_period.end_grace_period_request_builder import EndGracePeriodRequestBuilder

        return EndGracePeriodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_connectivity_history(self) -> GetCloudPcConnectivityHistoryRequestBuilder:
        """
        Provides operations to call the getCloudPcConnectivityHistory method.
        """
        from .get_cloud_pc_connectivity_history.get_cloud_pc_connectivity_history_request_builder import GetCloudPcConnectivityHistoryRequestBuilder

        return GetCloudPcConnectivityHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cloud_pc_launch_info(self) -> GetCloudPcLaunchInfoRequestBuilder:
        """
        Provides operations to call the getCloudPcLaunchInfo method.
        """
        from .get_cloud_pc_launch_info.get_cloud_pc_launch_info_request_builder import GetCloudPcLaunchInfoRequestBuilder

        return GetCloudPcLaunchInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_frontline_cloud_pc_access_state(self) -> GetFrontlineCloudPcAccessStateRequestBuilder:
        """
        Provides operations to call the getFrontlineCloudPcAccessState method.
        """
        from .get_frontline_cloud_pc_access_state.get_frontline_cloud_pc_access_state_request_builder import GetFrontlineCloudPcAccessStateRequestBuilder

        return GetFrontlineCloudPcAccessStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_shift_work_cloud_pc_access_state(self) -> GetShiftWorkCloudPcAccessStateRequestBuilder:
        """
        Provides operations to call the getShiftWorkCloudPcAccessState method.
        """
        from .get_shift_work_cloud_pc_access_state.get_shift_work_cloud_pc_access_state_request_builder import GetShiftWorkCloudPcAccessStateRequestBuilder

        return GetShiftWorkCloudPcAccessStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_supported_cloud_pc_remote_actions(self) -> GetSupportedCloudPcRemoteActionsRequestBuilder:
        """
        Provides operations to call the getSupportedCloudPcRemoteActions method.
        """
        from .get_supported_cloud_pc_remote_actions.get_supported_cloud_pc_remote_actions_request_builder import GetSupportedCloudPcRemoteActionsRequestBuilder

        return GetSupportedCloudPcRemoteActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power_off(self) -> PowerOffRequestBuilder:
        """
        Provides operations to call the powerOff method.
        """
        from .power_off.power_off_request_builder import PowerOffRequestBuilder

        return PowerOffRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power_on(self) -> PowerOnRequestBuilder:
        """
        Provides operations to call the powerOn method.
        """
        from .power_on.power_on_request_builder import PowerOnRequestBuilder

        return PowerOnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot(self) -> RebootRequestBuilder:
        """
        Provides operations to call the reboot method.
        """
        from .reboot.reboot_request_builder import RebootRequestBuilder

        return RebootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rename(self) -> RenameRequestBuilder:
        """
        Provides operations to call the rename method.
        """
        from .rename.rename_request_builder import RenameRequestBuilder

        return RenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision(self) -> ReprovisionRequestBuilder:
        """
        Provides operations to call the reprovision method.
        """
        from .reprovision.reprovision_request_builder import ReprovisionRequestBuilder

        return ReprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resize(self) -> ResizeRequestBuilder:
        """
        Provides operations to call the resize method.
        """
        from .resize.resize_request_builder import ResizeRequestBuilder

        return ResizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retry_partner_agent_installation(self) -> RetryPartnerAgentInstallationRequestBuilder:
        """
        Provides operations to call the retryPartnerAgentInstallation method.
        """
        from .retry_partner_agent_installation.retry_partner_agent_installation_request_builder import RetryPartnerAgentInstallationRequestBuilder

        return RetryPartnerAgentInstallationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start.start_request_builder import StartRequestBuilder

        return StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        from .stop.stop_request_builder import StopRequestBuilder

        return StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshoot(self) -> TroubleshootRequestBuilder:
        """
        Provides operations to call the troubleshoot method.
        """
        from .troubleshoot.troubleshoot_request_builder import TroubleshootRequestBuilder

        return TroubleshootRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CloudPCItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a specific cloudPC object. This API is available in the following national cloud deployments.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
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
    class CloudPCItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CloudPCItemRequestBuilder.CloudPCItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

