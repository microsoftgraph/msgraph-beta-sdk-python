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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.virtual_endpoint import VirtualEndpoint
    from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder
    from .bulk_actions.bulk_actions_request_builder import BulkActionsRequestBuilder
    from .cloud_p_cs.cloud_p_cs_request_builder import CloudPCsRequestBuilder
    from .cross_cloud_government_organization_mapping.cross_cloud_government_organization_mapping_request_builder import CrossCloudGovernmentOrganizationMappingRequestBuilder
    from .device_images.device_images_request_builder import DeviceImagesRequestBuilder
    from .external_partner_settings.external_partner_settings_request_builder import ExternalPartnerSettingsRequestBuilder
    from .front_line_service_plans.front_line_service_plans_request_builder import FrontLineServicePlansRequestBuilder
    from .gallery_images.gallery_images_request_builder import GalleryImagesRequestBuilder
    from .get_effective_permissions.get_effective_permissions_request_builder import GetEffectivePermissionsRequestBuilder
    from .on_premises_connections.on_premises_connections_request_builder import OnPremisesConnectionsRequestBuilder
    from .organization_settings.organization_settings_request_builder import OrganizationSettingsRequestBuilder
    from .provisioning_policies.provisioning_policies_request_builder import ProvisioningPoliciesRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .service_plans.service_plans_request_builder import ServicePlansRequestBuilder
    from .shared_use_service_plans.shared_use_service_plans_request_builder import SharedUseServicePlansRequestBuilder
    from .snapshots.snapshots_request_builder import SnapshotsRequestBuilder
    from .supported_regions.supported_regions_request_builder import SupportedRegionsRequestBuilder
    from .user_settings.user_settings_request_builder import UserSettingsRequestBuilder

class VirtualEndpointRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the virtualEndpoint property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new VirtualEndpointRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[VirtualEndpointRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property virtualEndpoint for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[VirtualEndpointRequestBuilderGetRequestConfiguration] = None) -> Optional[VirtualEndpoint]:
        """
        Get virtualEndpoint from deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VirtualEndpoint]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.virtual_endpoint import VirtualEndpoint

        return await self.request_adapter.send_async(request_info, VirtualEndpoint, error_mapping)
    
    async def patch(self,body: Optional[VirtualEndpoint] = None, request_configuration: Optional[VirtualEndpointRequestBuilderPatchRequestConfiguration] = None) -> Optional[VirtualEndpoint]:
        """
        Update the navigation property virtualEndpoint in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VirtualEndpoint]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.virtual_endpoint import VirtualEndpoint

        return await self.request_adapter.send_async(request_info, VirtualEndpoint, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[VirtualEndpointRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property virtualEndpoint for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[VirtualEndpointRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get virtualEndpoint from deviceManagement
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
    
    def to_patch_request_information(self,body: Optional[VirtualEndpoint] = None, request_configuration: Optional[VirtualEndpointRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property virtualEndpoint in deviceManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> VirtualEndpointRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VirtualEndpointRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return VirtualEndpointRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def audit_events(self) -> AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.virtualEndpoint entity.
        """
        from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder

        return AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bulk_actions(self) -> BulkActionsRequestBuilder:
        """
        Provides operations to manage the bulkActions property of the microsoft.graph.virtualEndpoint entity.
        """
        from .bulk_actions.bulk_actions_request_builder import BulkActionsRequestBuilder

        return BulkActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_p_cs(self) -> CloudPCsRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.virtualEndpoint entity.
        """
        from .cloud_p_cs.cloud_p_cs_request_builder import CloudPCsRequestBuilder

        return CloudPCsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cross_cloud_government_organization_mapping(self) -> CrossCloudGovernmentOrganizationMappingRequestBuilder:
        """
        Provides operations to manage the crossCloudGovernmentOrganizationMapping property of the microsoft.graph.virtualEndpoint entity.
        """
        from .cross_cloud_government_organization_mapping.cross_cloud_government_organization_mapping_request_builder import CrossCloudGovernmentOrganizationMappingRequestBuilder

        return CrossCloudGovernmentOrganizationMappingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_images(self) -> DeviceImagesRequestBuilder:
        """
        Provides operations to manage the deviceImages property of the microsoft.graph.virtualEndpoint entity.
        """
        from .device_images.device_images_request_builder import DeviceImagesRequestBuilder

        return DeviceImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_partner_settings(self) -> ExternalPartnerSettingsRequestBuilder:
        """
        Provides operations to manage the externalPartnerSettings property of the microsoft.graph.virtualEndpoint entity.
        """
        from .external_partner_settings.external_partner_settings_request_builder import ExternalPartnerSettingsRequestBuilder

        return ExternalPartnerSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def front_line_service_plans(self) -> FrontLineServicePlansRequestBuilder:
        """
        Provides operations to manage the frontLineServicePlans property of the microsoft.graph.virtualEndpoint entity.
        """
        from .front_line_service_plans.front_line_service_plans_request_builder import FrontLineServicePlansRequestBuilder

        return FrontLineServicePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gallery_images(self) -> GalleryImagesRequestBuilder:
        """
        Provides operations to manage the galleryImages property of the microsoft.graph.virtualEndpoint entity.
        """
        from .gallery_images.gallery_images_request_builder import GalleryImagesRequestBuilder

        return GalleryImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_effective_permissions(self) -> GetEffectivePermissionsRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        """
        from .get_effective_permissions.get_effective_permissions_request_builder import GetEffectivePermissionsRequestBuilder

        return GetEffectivePermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_connections(self) -> OnPremisesConnectionsRequestBuilder:
        """
        Provides operations to manage the onPremisesConnections property of the microsoft.graph.virtualEndpoint entity.
        """
        from .on_premises_connections.on_premises_connections_request_builder import OnPremisesConnectionsRequestBuilder

        return OnPremisesConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def organization_settings(self) -> OrganizationSettingsRequestBuilder:
        """
        Provides operations to manage the organizationSettings property of the microsoft.graph.virtualEndpoint entity.
        """
        from .organization_settings.organization_settings_request_builder import OrganizationSettingsRequestBuilder

        return OrganizationSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provisioning_policies(self) -> ProvisioningPoliciesRequestBuilder:
        """
        Provides operations to manage the provisioningPolicies property of the microsoft.graph.virtualEndpoint entity.
        """
        from .provisioning_policies.provisioning_policies_request_builder import ProvisioningPoliciesRequestBuilder

        return ProvisioningPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.virtualEndpoint entity.
        """
        from .reports.reports_request_builder import ReportsRequestBuilder

        return ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_plans(self) -> ServicePlansRequestBuilder:
        """
        Provides operations to manage the servicePlans property of the microsoft.graph.virtualEndpoint entity.
        """
        from .service_plans.service_plans_request_builder import ServicePlansRequestBuilder

        return ServicePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_use_service_plans(self) -> SharedUseServicePlansRequestBuilder:
        """
        Provides operations to manage the sharedUseServicePlans property of the microsoft.graph.virtualEndpoint entity.
        """
        from .shared_use_service_plans.shared_use_service_plans_request_builder import SharedUseServicePlansRequestBuilder

        return SharedUseServicePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def snapshots(self) -> SnapshotsRequestBuilder:
        """
        Provides operations to manage the snapshots property of the microsoft.graph.virtualEndpoint entity.
        """
        from .snapshots.snapshots_request_builder import SnapshotsRequestBuilder

        return SnapshotsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supported_regions(self) -> SupportedRegionsRequestBuilder:
        """
        Provides operations to manage the supportedRegions property of the microsoft.graph.virtualEndpoint entity.
        """
        from .supported_regions.supported_regions_request_builder import SupportedRegionsRequestBuilder

        return SupportedRegionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_settings(self) -> UserSettingsRequestBuilder:
        """
        Provides operations to manage the userSettings property of the microsoft.graph.virtualEndpoint entity.
        """
        from .user_settings.user_settings_request_builder import UserSettingsRequestBuilder

        return UserSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class VirtualEndpointRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class VirtualEndpointRequestBuilderGetQueryParameters():
        """
        Get virtualEndpoint from deviceManagement
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
    class VirtualEndpointRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[VirtualEndpointRequestBuilder.VirtualEndpointRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class VirtualEndpointRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

