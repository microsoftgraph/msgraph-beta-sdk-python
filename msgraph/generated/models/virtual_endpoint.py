from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_audit_event import CloudPcAuditEvent
    from .cloud_pc_bulk_action import CloudPcBulkAction
    from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
    from .cloud_pc_device_image import CloudPcDeviceImage
    from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
    from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
    from .cloud_pc_gallery_image import CloudPcGalleryImage
    from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
    from .cloud_pc_organization_settings import CloudPcOrganizationSettings
    from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
    from .cloud_pc_reports import CloudPcReports
    from .cloud_pc_service_plan import CloudPcServicePlan
    from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
    from .cloud_pc_snapshot import CloudPcSnapshot
    from .cloud_pc_supported_region import CloudPcSupportedRegion
    from .cloud_pc_user_setting import CloudPcUserSetting
    from .cloud_p_c import CloudPC
    from .entity import Entity

from .entity import Entity

@dataclass
class VirtualEndpoint(Entity):
    # Cloud PC audit event.
    audit_events: Optional[List[CloudPcAuditEvent]] = None
    # The bulkActions property
    bulk_actions: Optional[List[CloudPcBulkAction]] = None
    # Cloud managed virtual desktops.
    cloud_p_cs: Optional[List[CloudPC]] = None
    # Cloud PC organization mapping between public and US Government Community Cloud (GCC) organizations.
    cross_cloud_government_organization_mapping: Optional[CloudPcCrossCloudGovernmentOrganizationMapping] = None
    # The image resource on Cloud PC.
    device_images: Optional[List[CloudPcDeviceImage]] = None
    # The external partner settings on a Cloud PC.
    external_partner_settings: Optional[List[CloudPcExternalPartnerSetting]] = None
    # Front-line service plans for a Cloud PC.
    front_line_service_plans: Optional[List[CloudPcFrontLineServicePlan]] = None
    # The gallery image resource on Cloud PC.
    gallery_images: Optional[List[CloudPcGalleryImage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A defined collection of Azure resource information that can be used to establish on-premises network connectivity for Cloud PCs.
    on_premises_connections: Optional[List[CloudPcOnPremisesConnection]] = None
    # The Cloud PC organization settings for a tenant.
    organization_settings: Optional[CloudPcOrganizationSettings] = None
    # Cloud PC provisioning policy.
    provisioning_policies: Optional[List[CloudPcProvisioningPolicy]] = None
    # Cloud PC related reports.
    reports: Optional[CloudPcReports] = None
    # Cloud PC service plans.
    service_plans: Optional[List[CloudPcServicePlan]] = None
    # The sharedUseServicePlans property
    shared_use_service_plans: Optional[List[CloudPcSharedUseServicePlan]] = None
    # Cloud PC snapshots.
    snapshots: Optional[List[CloudPcSnapshot]] = None
    # Cloud PC supported regions.
    supported_regions: Optional[List[CloudPcSupportedRegion]] = None
    # Cloud PC user settings.
    user_settings: Optional[List[CloudPcUserSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEndpoint
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEndpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
        from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_organization_settings import CloudPcOrganizationSettings
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_reports import CloudPcReports
        from .cloud_pc_service_plan import CloudPcServicePlan
        from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
        from .cloud_pc_snapshot import CloudPcSnapshot
        from .cloud_pc_supported_region import CloudPcSupportedRegion
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_p_c import CloudPC
        from .entity import Entity

        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
        from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_organization_settings import CloudPcOrganizationSettings
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_reports import CloudPcReports
        from .cloud_pc_service_plan import CloudPcServicePlan
        from .cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
        from .cloud_pc_snapshot import CloudPcSnapshot
        from .cloud_pc_supported_region import CloudPcSupportedRegion
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_p_c import CloudPC
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(CloudPcAuditEvent)),
            "bulkActions": lambda n : setattr(self, 'bulk_actions', n.get_collection_of_object_values(CloudPcBulkAction)),
            "cloudPCs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(CloudPC)),
            "crossCloudGovernmentOrganizationMapping": lambda n : setattr(self, 'cross_cloud_government_organization_mapping', n.get_object_value(CloudPcCrossCloudGovernmentOrganizationMapping)),
            "deviceImages": lambda n : setattr(self, 'device_images', n.get_collection_of_object_values(CloudPcDeviceImage)),
            "externalPartnerSettings": lambda n : setattr(self, 'external_partner_settings', n.get_collection_of_object_values(CloudPcExternalPartnerSetting)),
            "frontLineServicePlans": lambda n : setattr(self, 'front_line_service_plans', n.get_collection_of_object_values(CloudPcFrontLineServicePlan)),
            "galleryImages": lambda n : setattr(self, 'gallery_images', n.get_collection_of_object_values(CloudPcGalleryImage)),
            "onPremisesConnections": lambda n : setattr(self, 'on_premises_connections', n.get_collection_of_object_values(CloudPcOnPremisesConnection)),
            "organizationSettings": lambda n : setattr(self, 'organization_settings', n.get_object_value(CloudPcOrganizationSettings)),
            "provisioningPolicies": lambda n : setattr(self, 'provisioning_policies', n.get_collection_of_object_values(CloudPcProvisioningPolicy)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(CloudPcReports)),
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(CloudPcServicePlan)),
            "sharedUseServicePlans": lambda n : setattr(self, 'shared_use_service_plans', n.get_collection_of_object_values(CloudPcSharedUseServicePlan)),
            "snapshots": lambda n : setattr(self, 'snapshots', n.get_collection_of_object_values(CloudPcSnapshot)),
            "supportedRegions": lambda n : setattr(self, 'supported_regions', n.get_collection_of_object_values(CloudPcSupportedRegion)),
            "userSettings": lambda n : setattr(self, 'user_settings', n.get_collection_of_object_values(CloudPcUserSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("bulkActions", self.bulk_actions)
        writer.write_collection_of_object_values("cloudPCs", self.cloud_p_cs)
        writer.write_object_value("crossCloudGovernmentOrganizationMapping", self.cross_cloud_government_organization_mapping)
        writer.write_collection_of_object_values("deviceImages", self.device_images)
        writer.write_collection_of_object_values("externalPartnerSettings", self.external_partner_settings)
        writer.write_collection_of_object_values("frontLineServicePlans", self.front_line_service_plans)
        writer.write_collection_of_object_values("galleryImages", self.gallery_images)
        writer.write_collection_of_object_values("onPremisesConnections", self.on_premises_connections)
        writer.write_object_value("organizationSettings", self.organization_settings)
        writer.write_collection_of_object_values("provisioningPolicies", self.provisioning_policies)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("servicePlans", self.service_plans)
        writer.write_collection_of_object_values("sharedUseServicePlans", self.shared_use_service_plans)
        writer.write_collection_of_object_values("snapshots", self.snapshots)
        writer.write_collection_of_object_values("supportedRegions", self.supported_regions)
        writer.write_collection_of_object_values("userSettings", self.user_settings)
    

