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

audit_events_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.audit_events.audit_events_request_builder')
cloud_pc_audit_event_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.audit_events.item.cloud_pc_audit_event_item_request_builder')
cloud_p_cs_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.cloud_p_cs.cloud_p_cs_request_builder')
cloud_p_c_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.cloud_p_cs.item.cloud_p_c_item_request_builder')
cross_cloud_government_organization_mapping_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.cross_cloud_government_organization_mapping.cross_cloud_government_organization_mapping_request_builder')
device_images_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.device_images.device_images_request_builder')
cloud_pc_device_image_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.device_images.item.cloud_pc_device_image_item_request_builder')
external_partner_settings_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.external_partner_settings.external_partner_settings_request_builder')
cloud_pc_external_partner_setting_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.external_partner_settings.item.cloud_pc_external_partner_setting_item_request_builder')
gallery_images_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.gallery_images.gallery_images_request_builder')
cloud_pc_gallery_image_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.gallery_images.item.cloud_pc_gallery_image_item_request_builder')
get_effective_permissions_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.get_effective_permissions.get_effective_permissions_request_builder')
on_premises_connections_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.on_premises_connections.on_premises_connections_request_builder')
cloud_pc_on_premises_connection_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.on_premises_connections.item.cloud_pc_on_premises_connection_item_request_builder')
organization_settings_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.organization_settings.organization_settings_request_builder')
provisioning_policies_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.provisioning_policies.provisioning_policies_request_builder')
cloud_pc_provisioning_policy_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.provisioning_policies.item.cloud_pc_provisioning_policy_item_request_builder')
reports_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.reports.reports_request_builder')
service_plans_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.service_plans.service_plans_request_builder')
cloud_pc_service_plan_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.service_plans.item.cloud_pc_service_plan_item_request_builder')
shared_use_service_plans_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.shared_use_service_plans.shared_use_service_plans_request_builder')
cloud_pc_shared_use_service_plan_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.shared_use_service_plans.item.cloud_pc_shared_use_service_plan_item_request_builder')
snapshots_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.snapshots.snapshots_request_builder')
cloud_pc_snapshot_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.snapshots.item.cloud_pc_snapshot_item_request_builder')
supported_regions_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.supported_regions.supported_regions_request_builder')
cloud_pc_supported_region_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.supported_regions.item.cloud_pc_supported_region_item_request_builder')
user_settings_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.user_settings.user_settings_request_builder')
cloud_pc_user_setting_item_request_builder = lazy_import('msgraph.generated.device_management.virtual_endpoint.user_settings.item.cloud_pc_user_setting_item_request_builder')
virtual_endpoint = lazy_import('msgraph.generated.models.virtual_endpoint')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class VirtualEndpointRequestBuilder():
    """
    Provides operations to manage the virtualEndpoint property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def audit_events(self) -> audit_events_request_builder.AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.virtualEndpoint entity.
        """
        return audit_events_request_builder.AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_p_cs(self) -> cloud_p_cs_request_builder.CloudPCsRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.virtualEndpoint entity.
        """
        return cloud_p_cs_request_builder.CloudPCsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cross_cloud_government_organization_mapping(self) -> cross_cloud_government_organization_mapping_request_builder.CrossCloudGovernmentOrganizationMappingRequestBuilder:
        """
        Provides operations to manage the crossCloudGovernmentOrganizationMapping property of the microsoft.graph.virtualEndpoint entity.
        """
        return cross_cloud_government_organization_mapping_request_builder.CrossCloudGovernmentOrganizationMappingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_images(self) -> device_images_request_builder.DeviceImagesRequestBuilder:
        """
        Provides operations to manage the deviceImages property of the microsoft.graph.virtualEndpoint entity.
        """
        return device_images_request_builder.DeviceImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_partner_settings(self) -> external_partner_settings_request_builder.ExternalPartnerSettingsRequestBuilder:
        """
        Provides operations to manage the externalPartnerSettings property of the microsoft.graph.virtualEndpoint entity.
        """
        return external_partner_settings_request_builder.ExternalPartnerSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gallery_images(self) -> gallery_images_request_builder.GalleryImagesRequestBuilder:
        """
        Provides operations to manage the galleryImages property of the microsoft.graph.virtualEndpoint entity.
        """
        return gallery_images_request_builder.GalleryImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_connections(self) -> on_premises_connections_request_builder.OnPremisesConnectionsRequestBuilder:
        """
        Provides operations to manage the onPremisesConnections property of the microsoft.graph.virtualEndpoint entity.
        """
        return on_premises_connections_request_builder.OnPremisesConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def organization_settings(self) -> organization_settings_request_builder.OrganizationSettingsRequestBuilder:
        """
        Provides operations to manage the organizationSettings property of the microsoft.graph.virtualEndpoint entity.
        """
        return organization_settings_request_builder.OrganizationSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provisioning_policies(self) -> provisioning_policies_request_builder.ProvisioningPoliciesRequestBuilder:
        """
        Provides operations to manage the provisioningPolicies property of the microsoft.graph.virtualEndpoint entity.
        """
        return provisioning_policies_request_builder.ProvisioningPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.virtualEndpoint entity.
        """
        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_plans(self) -> service_plans_request_builder.ServicePlansRequestBuilder:
        """
        Provides operations to manage the servicePlans property of the microsoft.graph.virtualEndpoint entity.
        """
        return service_plans_request_builder.ServicePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_use_service_plans(self) -> shared_use_service_plans_request_builder.SharedUseServicePlansRequestBuilder:
        """
        Provides operations to manage the sharedUseServicePlans property of the microsoft.graph.virtualEndpoint entity.
        """
        return shared_use_service_plans_request_builder.SharedUseServicePlansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def snapshots(self) -> snapshots_request_builder.SnapshotsRequestBuilder:
        """
        Provides operations to manage the snapshots property of the microsoft.graph.virtualEndpoint entity.
        """
        return snapshots_request_builder.SnapshotsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supported_regions(self) -> supported_regions_request_builder.SupportedRegionsRequestBuilder:
        """
        Provides operations to manage the supportedRegions property of the microsoft.graph.virtualEndpoint entity.
        """
        return supported_regions_request_builder.SupportedRegionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_settings(self) -> user_settings_request_builder.UserSettingsRequestBuilder:
        """
        Provides operations to manage the userSettings property of the microsoft.graph.virtualEndpoint entity.
        """
        return user_settings_request_builder.UserSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def audit_events_by_id(self,id: str) -> cloud_pc_audit_event_item_request_builder.CloudPcAuditEventItemRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_audit_event_item_request_builder.CloudPcAuditEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcAuditEvent%2Did"] = id
        return cloud_pc_audit_event_item_request_builder.CloudPcAuditEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_p_cs_by_id(self,id: str) -> cloud_p_c_item_request_builder.CloudPCItemRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_p_c_item_request_builder.CloudPCItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPC%2Did"] = id
        return cloud_p_c_item_request_builder.CloudPCItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new VirtualEndpointRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/virtualEndpoint{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[VirtualEndpointRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property virtualEndpoint for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[VirtualEndpointRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get virtualEndpoint from deviceManagement
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
    
    def create_patch_request_information(self,body: Optional[virtual_endpoint.VirtualEndpoint] = None, request_configuration: Optional[VirtualEndpointRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property virtualEndpoint in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[VirtualEndpointRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property virtualEndpoint for deviceManagement
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
    
    def device_images_by_id(self,id: str) -> cloud_pc_device_image_item_request_builder.CloudPcDeviceImageItemRequestBuilder:
        """
        Provides operations to manage the deviceImages property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_device_image_item_request_builder.CloudPcDeviceImageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcDeviceImage%2Did"] = id
        return cloud_pc_device_image_item_request_builder.CloudPcDeviceImageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def external_partner_settings_by_id(self,id: str) -> cloud_pc_external_partner_setting_item_request_builder.CloudPcExternalPartnerSettingItemRequestBuilder:
        """
        Provides operations to manage the externalPartnerSettings property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_external_partner_setting_item_request_builder.CloudPcExternalPartnerSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcExternalPartnerSetting%2Did"] = id
        return cloud_pc_external_partner_setting_item_request_builder.CloudPcExternalPartnerSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def gallery_images_by_id(self,id: str) -> cloud_pc_gallery_image_item_request_builder.CloudPcGalleryImageItemRequestBuilder:
        """
        Provides operations to manage the galleryImages property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_gallery_image_item_request_builder.CloudPcGalleryImageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcGalleryImage%2Did"] = id
        return cloud_pc_gallery_image_item_request_builder.CloudPcGalleryImageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[VirtualEndpointRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[virtual_endpoint.VirtualEndpoint]:
        """
        Get virtualEndpoint from deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[virtual_endpoint.VirtualEndpoint]
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
        return await self.request_adapter.send_async(request_info, virtual_endpoint.VirtualEndpoint, response_handler, error_mapping)
    
    def get_effective_permissions(self,) -> get_effective_permissions_request_builder.GetEffectivePermissionsRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        Returns: get_effective_permissions_request_builder.GetEffectivePermissionsRequestBuilder
        """
        return get_effective_permissions_request_builder.GetEffectivePermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def on_premises_connections_by_id(self,id: str) -> cloud_pc_on_premises_connection_item_request_builder.CloudPcOnPremisesConnectionItemRequestBuilder:
        """
        Provides operations to manage the onPremisesConnections property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_on_premises_connection_item_request_builder.CloudPcOnPremisesConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcOnPremisesConnection%2Did"] = id
        return cloud_pc_on_premises_connection_item_request_builder.CloudPcOnPremisesConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[virtual_endpoint.VirtualEndpoint] = None, request_configuration: Optional[VirtualEndpointRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[virtual_endpoint.VirtualEndpoint]:
        """
        Update the navigation property virtualEndpoint in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[virtual_endpoint.VirtualEndpoint]
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
        return await self.request_adapter.send_async(request_info, virtual_endpoint.VirtualEndpoint, response_handler, error_mapping)
    
    def provisioning_policies_by_id(self,id: str) -> cloud_pc_provisioning_policy_item_request_builder.CloudPcProvisioningPolicyItemRequestBuilder:
        """
        Provides operations to manage the provisioningPolicies property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_provisioning_policy_item_request_builder.CloudPcProvisioningPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcProvisioningPolicy%2Did"] = id
        return cloud_pc_provisioning_policy_item_request_builder.CloudPcProvisioningPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def service_plans_by_id(self,id: str) -> cloud_pc_service_plan_item_request_builder.CloudPcServicePlanItemRequestBuilder:
        """
        Provides operations to manage the servicePlans property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_service_plan_item_request_builder.CloudPcServicePlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcServicePlan%2Did"] = id
        return cloud_pc_service_plan_item_request_builder.CloudPcServicePlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def shared_use_service_plans_by_id(self,id: str) -> cloud_pc_shared_use_service_plan_item_request_builder.CloudPcSharedUseServicePlanItemRequestBuilder:
        """
        Provides operations to manage the sharedUseServicePlans property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_shared_use_service_plan_item_request_builder.CloudPcSharedUseServicePlanItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcSharedUseServicePlan%2Did"] = id
        return cloud_pc_shared_use_service_plan_item_request_builder.CloudPcSharedUseServicePlanItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def snapshots_by_id(self,id: str) -> cloud_pc_snapshot_item_request_builder.CloudPcSnapshotItemRequestBuilder:
        """
        Provides operations to manage the snapshots property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_snapshot_item_request_builder.CloudPcSnapshotItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcSnapshot%2Did"] = id
        return cloud_pc_snapshot_item_request_builder.CloudPcSnapshotItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def supported_regions_by_id(self,id: str) -> cloud_pc_supported_region_item_request_builder.CloudPcSupportedRegionItemRequestBuilder:
        """
        Provides operations to manage the supportedRegions property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_supported_region_item_request_builder.CloudPcSupportedRegionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcSupportedRegion%2Did"] = id
        return cloud_pc_supported_region_item_request_builder.CloudPcSupportedRegionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_settings_by_id(self,id: str) -> cloud_pc_user_setting_item_request_builder.CloudPcUserSettingItemRequestBuilder:
        """
        Provides operations to manage the userSettings property of the microsoft.graph.virtualEndpoint entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_pc_user_setting_item_request_builder.CloudPcUserSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPcUserSetting%2Did"] = id
        return cloud_pc_user_setting_item_request_builder.CloudPcUserSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class VirtualEndpointRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class VirtualEndpointRequestBuilderGetQueryParameters():
        """
        Get virtualEndpoint from deviceManagement
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
    class VirtualEndpointRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[VirtualEndpointRequestBuilder.VirtualEndpointRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class VirtualEndpointRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

