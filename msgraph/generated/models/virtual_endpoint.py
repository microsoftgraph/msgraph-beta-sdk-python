from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_audit_event, cloud_pc_bulk_action, cloud_pc_cross_cloud_government_organization_mapping, cloud_pc_device_image, cloud_pc_external_partner_setting, cloud_pc_gallery_image, cloud_pc_on_premises_connection, cloud_pc_organization_settings, cloud_pc_provisioning_policy, cloud_pc_reports, cloud_pc_service_plan, cloud_pc_shared_use_service_plan, cloud_pc_snapshot, cloud_pc_supported_region, cloud_pc_user_setting, cloud_p_c, entity

from . import entity

@dataclass
class VirtualEndpoint(entity.Entity):
    # Cloud PC audit event.
    audit_events: Optional[List[cloud_pc_audit_event.CloudPcAuditEvent]] = None
    # The bulkActions property
    bulk_actions: Optional[List[cloud_pc_bulk_action.CloudPcBulkAction]] = None
    # Cloud managed virtual desktops.
    cloud_p_cs: Optional[List[cloud_p_c.CloudPC]] = None
    # Cloud PC organization mapping between public and US Government Community Cloud (GCC) organizations.
    cross_cloud_government_organization_mapping: Optional[cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping] = None
    # The image resource on Cloud PC.
    device_images: Optional[List[cloud_pc_device_image.CloudPcDeviceImage]] = None
    # The external partner settings on a Cloud PC.
    external_partner_settings: Optional[List[cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting]] = None
    # The gallery image resource on Cloud PC.
    gallery_images: Optional[List[cloud_pc_gallery_image.CloudPcGalleryImage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A defined collection of Azure resource information that can be used to establish on-premises network connectivity for Cloud PCs.
    on_premises_connections: Optional[List[cloud_pc_on_premises_connection.CloudPcOnPremisesConnection]] = None
    # The Cloud PC organization settings for a tenant.
    organization_settings: Optional[cloud_pc_organization_settings.CloudPcOrganizationSettings] = None
    # Cloud PC provisioning policy.
    provisioning_policies: Optional[List[cloud_pc_provisioning_policy.CloudPcProvisioningPolicy]] = None
    # Cloud PC related reports.
    reports: Optional[cloud_pc_reports.CloudPcReports] = None
    # Cloud PC service plans.
    service_plans: Optional[List[cloud_pc_service_plan.CloudPcServicePlan]] = None
    # Cloud PC shared-use service plans.
    shared_use_service_plans: Optional[List[cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan]] = None
    # Cloud PC snapshots.
    snapshots: Optional[List[cloud_pc_snapshot.CloudPcSnapshot]] = None
    # Cloud PC supported regions.
    supported_regions: Optional[List[cloud_pc_supported_region.CloudPcSupportedRegion]] = None
    # Cloud PC user settings.
    user_settings: Optional[List[cloud_pc_user_setting.CloudPcUserSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import cloud_pc_audit_event, cloud_pc_bulk_action, cloud_pc_cross_cloud_government_organization_mapping, cloud_pc_device_image, cloud_pc_external_partner_setting, cloud_pc_gallery_image, cloud_pc_on_premises_connection, cloud_pc_organization_settings, cloud_pc_provisioning_policy, cloud_pc_reports, cloud_pc_service_plan, cloud_pc_shared_use_service_plan, cloud_pc_snapshot, cloud_pc_supported_region, cloud_pc_user_setting, cloud_p_c, entity

        from . import cloud_pc_audit_event, cloud_pc_bulk_action, cloud_pc_cross_cloud_government_organization_mapping, cloud_pc_device_image, cloud_pc_external_partner_setting, cloud_pc_gallery_image, cloud_pc_on_premises_connection, cloud_pc_organization_settings, cloud_pc_provisioning_policy, cloud_pc_reports, cloud_pc_service_plan, cloud_pc_shared_use_service_plan, cloud_pc_snapshot, cloud_pc_supported_region, cloud_pc_user_setting, cloud_p_c, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(cloud_pc_audit_event.CloudPcAuditEvent)),
            "bulkActions": lambda n : setattr(self, 'bulk_actions', n.get_collection_of_object_values(cloud_pc_bulk_action.CloudPcBulkAction)),
            "cloudPCs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(cloud_p_c.CloudPC)),
            "crossCloudGovernmentOrganizationMapping": lambda n : setattr(self, 'cross_cloud_government_organization_mapping', n.get_object_value(cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping)),
            "deviceImages": lambda n : setattr(self, 'device_images', n.get_collection_of_object_values(cloud_pc_device_image.CloudPcDeviceImage)),
            "externalPartnerSettings": lambda n : setattr(self, 'external_partner_settings', n.get_collection_of_object_values(cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting)),
            "galleryImages": lambda n : setattr(self, 'gallery_images', n.get_collection_of_object_values(cloud_pc_gallery_image.CloudPcGalleryImage)),
            "onPremisesConnections": lambda n : setattr(self, 'on_premises_connections', n.get_collection_of_object_values(cloud_pc_on_premises_connection.CloudPcOnPremisesConnection)),
            "organizationSettings": lambda n : setattr(self, 'organization_settings', n.get_object_value(cloud_pc_organization_settings.CloudPcOrganizationSettings)),
            "provisioningPolicies": lambda n : setattr(self, 'provisioning_policies', n.get_collection_of_object_values(cloud_pc_provisioning_policy.CloudPcProvisioningPolicy)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(cloud_pc_reports.CloudPcReports)),
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(cloud_pc_service_plan.CloudPcServicePlan)),
            "sharedUseServicePlans": lambda n : setattr(self, 'shared_use_service_plans', n.get_collection_of_object_values(cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan)),
            "snapshots": lambda n : setattr(self, 'snapshots', n.get_collection_of_object_values(cloud_pc_snapshot.CloudPcSnapshot)),
            "supportedRegions": lambda n : setattr(self, 'supported_regions', n.get_collection_of_object_values(cloud_pc_supported_region.CloudPcSupportedRegion)),
            "userSettings": lambda n : setattr(self, 'user_settings', n.get_collection_of_object_values(cloud_pc_user_setting.CloudPcUserSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
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
    

