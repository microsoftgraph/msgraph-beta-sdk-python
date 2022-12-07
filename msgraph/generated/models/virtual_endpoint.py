from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_p_c = lazy_import('msgraph.generated.models.cloud_p_c')
cloud_pc_audit_event = lazy_import('msgraph.generated.models.cloud_pc_audit_event')
cloud_pc_cross_cloud_government_organization_mapping = lazy_import('msgraph.generated.models.cloud_pc_cross_cloud_government_organization_mapping')
cloud_pc_device_image = lazy_import('msgraph.generated.models.cloud_pc_device_image')
cloud_pc_external_partner_setting = lazy_import('msgraph.generated.models.cloud_pc_external_partner_setting')
cloud_pc_gallery_image = lazy_import('msgraph.generated.models.cloud_pc_gallery_image')
cloud_pc_on_premises_connection = lazy_import('msgraph.generated.models.cloud_pc_on_premises_connection')
cloud_pc_organization_settings = lazy_import('msgraph.generated.models.cloud_pc_organization_settings')
cloud_pc_provisioning_policy = lazy_import('msgraph.generated.models.cloud_pc_provisioning_policy')
cloud_pc_reports = lazy_import('msgraph.generated.models.cloud_pc_reports')
cloud_pc_service_plan = lazy_import('msgraph.generated.models.cloud_pc_service_plan')
cloud_pc_shared_use_service_plan = lazy_import('msgraph.generated.models.cloud_pc_shared_use_service_plan')
cloud_pc_snapshot = lazy_import('msgraph.generated.models.cloud_pc_snapshot')
cloud_pc_supported_region = lazy_import('msgraph.generated.models.cloud_pc_supported_region')
cloud_pc_user_setting = lazy_import('msgraph.generated.models.cloud_pc_user_setting')
entity = lazy_import('msgraph.generated.models.entity')

class VirtualEndpoint(entity.Entity):
    @property
    def audit_events(self,) -> Optional[List[cloud_pc_audit_event.CloudPcAuditEvent]]:
        """
        Gets the auditEvents property value. Cloud PC audit event.
        Returns: Optional[List[cloud_pc_audit_event.CloudPcAuditEvent]]
        """
        return self._audit_events
    
    @audit_events.setter
    def audit_events(self,value: Optional[List[cloud_pc_audit_event.CloudPcAuditEvent]] = None) -> None:
        """
        Sets the auditEvents property value. Cloud PC audit event.
        Args:
            value: Value to set for the auditEvents property.
        """
        self._audit_events = value
    
    @property
    def cloud_p_cs(self,) -> Optional[List[cloud_p_c.CloudPC]]:
        """
        Gets the cloudPCs property value. Cloud managed virtual desktops.
        Returns: Optional[List[cloud_p_c.CloudPC]]
        """
        return self._cloud_p_cs
    
    @cloud_p_cs.setter
    def cloud_p_cs(self,value: Optional[List[cloud_p_c.CloudPC]] = None) -> None:
        """
        Sets the cloudPCs property value. Cloud managed virtual desktops.
        Args:
            value: Value to set for the cloudPCs property.
        """
        self._cloud_p_cs = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEndpoint and sets the default values.
        """
        super().__init__()
        # Cloud PC audit event.
        self._audit_events: Optional[List[cloud_pc_audit_event.CloudPcAuditEvent]] = None
        # Cloud managed virtual desktops.
        self._cloud_p_cs: Optional[List[cloud_p_c.CloudPC]] = None
        # Cloud PC organization mapping between public and US Government Community Cloud (GCC) organizations.
        self._cross_cloud_government_organization_mapping: Optional[cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping] = None
        # The image resource on Cloud PC.
        self._device_images: Optional[List[cloud_pc_device_image.CloudPcDeviceImage]] = None
        # The external partner settings on a Cloud PC.
        self._external_partner_settings: Optional[List[cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting]] = None
        # The gallery image resource on Cloud PC.
        self._gallery_images: Optional[List[cloud_pc_gallery_image.CloudPcGalleryImage]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A defined collection of Azure resource information that can be used to establish on-premises network connectivity for Cloud PCs.
        self._on_premises_connections: Optional[List[cloud_pc_on_premises_connection.CloudPcOnPremisesConnection]] = None
        # The Cloud PC organization settings for a tenant.
        self._organization_settings: Optional[cloud_pc_organization_settings.CloudPcOrganizationSettings] = None
        # Cloud PC provisioning policy.
        self._provisioning_policies: Optional[List[cloud_pc_provisioning_policy.CloudPcProvisioningPolicy]] = None
        # Cloud PC related reports.
        self._reports: Optional[cloud_pc_reports.CloudPcReports] = None
        # Cloud PC service plans.
        self._service_plans: Optional[List[cloud_pc_service_plan.CloudPcServicePlan]] = None
        # The sharedUseServicePlans property
        self._shared_use_service_plans: Optional[List[cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan]] = None
        # Cloud PC snapshots.
        self._snapshots: Optional[List[cloud_pc_snapshot.CloudPcSnapshot]] = None
        # Cloud PC supported regions.
        self._supported_regions: Optional[List[cloud_pc_supported_region.CloudPcSupportedRegion]] = None
        # Cloud PC user settings.
        self._user_settings: Optional[List[cloud_pc_user_setting.CloudPcUserSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEndpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEndpoint()
    
    @property
    def cross_cloud_government_organization_mapping(self,) -> Optional[cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping]:
        """
        Gets the crossCloudGovernmentOrganizationMapping property value. Cloud PC organization mapping between public and US Government Community Cloud (GCC) organizations.
        Returns: Optional[cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping]
        """
        return self._cross_cloud_government_organization_mapping
    
    @cross_cloud_government_organization_mapping.setter
    def cross_cloud_government_organization_mapping(self,value: Optional[cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping] = None) -> None:
        """
        Sets the crossCloudGovernmentOrganizationMapping property value. Cloud PC organization mapping between public and US Government Community Cloud (GCC) organizations.
        Args:
            value: Value to set for the crossCloudGovernmentOrganizationMapping property.
        """
        self._cross_cloud_government_organization_mapping = value
    
    @property
    def device_images(self,) -> Optional[List[cloud_pc_device_image.CloudPcDeviceImage]]:
        """
        Gets the deviceImages property value. The image resource on Cloud PC.
        Returns: Optional[List[cloud_pc_device_image.CloudPcDeviceImage]]
        """
        return self._device_images
    
    @device_images.setter
    def device_images(self,value: Optional[List[cloud_pc_device_image.CloudPcDeviceImage]] = None) -> None:
        """
        Sets the deviceImages property value. The image resource on Cloud PC.
        Args:
            value: Value to set for the deviceImages property.
        """
        self._device_images = value
    
    @property
    def external_partner_settings(self,) -> Optional[List[cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting]]:
        """
        Gets the externalPartnerSettings property value. The external partner settings on a Cloud PC.
        Returns: Optional[List[cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting]]
        """
        return self._external_partner_settings
    
    @external_partner_settings.setter
    def external_partner_settings(self,value: Optional[List[cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting]] = None) -> None:
        """
        Sets the externalPartnerSettings property value. The external partner settings on a Cloud PC.
        Args:
            value: Value to set for the externalPartnerSettings property.
        """
        self._external_partner_settings = value
    
    @property
    def gallery_images(self,) -> Optional[List[cloud_pc_gallery_image.CloudPcGalleryImage]]:
        """
        Gets the galleryImages property value. The gallery image resource on Cloud PC.
        Returns: Optional[List[cloud_pc_gallery_image.CloudPcGalleryImage]]
        """
        return self._gallery_images
    
    @gallery_images.setter
    def gallery_images(self,value: Optional[List[cloud_pc_gallery_image.CloudPcGalleryImage]] = None) -> None:
        """
        Sets the galleryImages property value. The gallery image resource on Cloud PC.
        Args:
            value: Value to set for the galleryImages property.
        """
        self._gallery_images = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audit_events": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(cloud_pc_audit_event.CloudPcAuditEvent)),
            "cloud_p_cs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(cloud_p_c.CloudPC)),
            "cross_cloud_government_organization_mapping": lambda n : setattr(self, 'cross_cloud_government_organization_mapping', n.get_object_value(cloud_pc_cross_cloud_government_organization_mapping.CloudPcCrossCloudGovernmentOrganizationMapping)),
            "device_images": lambda n : setattr(self, 'device_images', n.get_collection_of_object_values(cloud_pc_device_image.CloudPcDeviceImage)),
            "external_partner_settings": lambda n : setattr(self, 'external_partner_settings', n.get_collection_of_object_values(cloud_pc_external_partner_setting.CloudPcExternalPartnerSetting)),
            "gallery_images": lambda n : setattr(self, 'gallery_images', n.get_collection_of_object_values(cloud_pc_gallery_image.CloudPcGalleryImage)),
            "on_premises_connections": lambda n : setattr(self, 'on_premises_connections', n.get_collection_of_object_values(cloud_pc_on_premises_connection.CloudPcOnPremisesConnection)),
            "organization_settings": lambda n : setattr(self, 'organization_settings', n.get_object_value(cloud_pc_organization_settings.CloudPcOrganizationSettings)),
            "provisioning_policies": lambda n : setattr(self, 'provisioning_policies', n.get_collection_of_object_values(cloud_pc_provisioning_policy.CloudPcProvisioningPolicy)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(cloud_pc_reports.CloudPcReports)),
            "service_plans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(cloud_pc_service_plan.CloudPcServicePlan)),
            "shared_use_service_plans": lambda n : setattr(self, 'shared_use_service_plans', n.get_collection_of_object_values(cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan)),
            "snapshots": lambda n : setattr(self, 'snapshots', n.get_collection_of_object_values(cloud_pc_snapshot.CloudPcSnapshot)),
            "supported_regions": lambda n : setattr(self, 'supported_regions', n.get_collection_of_object_values(cloud_pc_supported_region.CloudPcSupportedRegion)),
            "user_settings": lambda n : setattr(self, 'user_settings', n.get_collection_of_object_values(cloud_pc_user_setting.CloudPcUserSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def on_premises_connections(self,) -> Optional[List[cloud_pc_on_premises_connection.CloudPcOnPremisesConnection]]:
        """
        Gets the onPremisesConnections property value. A defined collection of Azure resource information that can be used to establish on-premises network connectivity for Cloud PCs.
        Returns: Optional[List[cloud_pc_on_premises_connection.CloudPcOnPremisesConnection]]
        """
        return self._on_premises_connections
    
    @on_premises_connections.setter
    def on_premises_connections(self,value: Optional[List[cloud_pc_on_premises_connection.CloudPcOnPremisesConnection]] = None) -> None:
        """
        Sets the onPremisesConnections property value. A defined collection of Azure resource information that can be used to establish on-premises network connectivity for Cloud PCs.
        Args:
            value: Value to set for the onPremisesConnections property.
        """
        self._on_premises_connections = value
    
    @property
    def organization_settings(self,) -> Optional[cloud_pc_organization_settings.CloudPcOrganizationSettings]:
        """
        Gets the organizationSettings property value. The Cloud PC organization settings for a tenant.
        Returns: Optional[cloud_pc_organization_settings.CloudPcOrganizationSettings]
        """
        return self._organization_settings
    
    @organization_settings.setter
    def organization_settings(self,value: Optional[cloud_pc_organization_settings.CloudPcOrganizationSettings] = None) -> None:
        """
        Sets the organizationSettings property value. The Cloud PC organization settings for a tenant.
        Args:
            value: Value to set for the organizationSettings property.
        """
        self._organization_settings = value
    
    @property
    def provisioning_policies(self,) -> Optional[List[cloud_pc_provisioning_policy.CloudPcProvisioningPolicy]]:
        """
        Gets the provisioningPolicies property value. Cloud PC provisioning policy.
        Returns: Optional[List[cloud_pc_provisioning_policy.CloudPcProvisioningPolicy]]
        """
        return self._provisioning_policies
    
    @provisioning_policies.setter
    def provisioning_policies(self,value: Optional[List[cloud_pc_provisioning_policy.CloudPcProvisioningPolicy]] = None) -> None:
        """
        Sets the provisioningPolicies property value. Cloud PC provisioning policy.
        Args:
            value: Value to set for the provisioningPolicies property.
        """
        self._provisioning_policies = value
    
    @property
    def reports(self,) -> Optional[cloud_pc_reports.CloudPcReports]:
        """
        Gets the reports property value. Cloud PC related reports.
        Returns: Optional[cloud_pc_reports.CloudPcReports]
        """
        return self._reports
    
    @reports.setter
    def reports(self,value: Optional[cloud_pc_reports.CloudPcReports] = None) -> None:
        """
        Sets the reports property value. Cloud PC related reports.
        Args:
            value: Value to set for the reports property.
        """
        self._reports = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
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
    
    @property
    def service_plans(self,) -> Optional[List[cloud_pc_service_plan.CloudPcServicePlan]]:
        """
        Gets the servicePlans property value. Cloud PC service plans.
        Returns: Optional[List[cloud_pc_service_plan.CloudPcServicePlan]]
        """
        return self._service_plans
    
    @service_plans.setter
    def service_plans(self,value: Optional[List[cloud_pc_service_plan.CloudPcServicePlan]] = None) -> None:
        """
        Sets the servicePlans property value. Cloud PC service plans.
        Args:
            value: Value to set for the servicePlans property.
        """
        self._service_plans = value
    
    @property
    def shared_use_service_plans(self,) -> Optional[List[cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan]]:
        """
        Gets the sharedUseServicePlans property value. The sharedUseServicePlans property
        Returns: Optional[List[cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan]]
        """
        return self._shared_use_service_plans
    
    @shared_use_service_plans.setter
    def shared_use_service_plans(self,value: Optional[List[cloud_pc_shared_use_service_plan.CloudPcSharedUseServicePlan]] = None) -> None:
        """
        Sets the sharedUseServicePlans property value. The sharedUseServicePlans property
        Args:
            value: Value to set for the sharedUseServicePlans property.
        """
        self._shared_use_service_plans = value
    
    @property
    def snapshots(self,) -> Optional[List[cloud_pc_snapshot.CloudPcSnapshot]]:
        """
        Gets the snapshots property value. Cloud PC snapshots.
        Returns: Optional[List[cloud_pc_snapshot.CloudPcSnapshot]]
        """
        return self._snapshots
    
    @snapshots.setter
    def snapshots(self,value: Optional[List[cloud_pc_snapshot.CloudPcSnapshot]] = None) -> None:
        """
        Sets the snapshots property value. Cloud PC snapshots.
        Args:
            value: Value to set for the snapshots property.
        """
        self._snapshots = value
    
    @property
    def supported_regions(self,) -> Optional[List[cloud_pc_supported_region.CloudPcSupportedRegion]]:
        """
        Gets the supportedRegions property value. Cloud PC supported regions.
        Returns: Optional[List[cloud_pc_supported_region.CloudPcSupportedRegion]]
        """
        return self._supported_regions
    
    @supported_regions.setter
    def supported_regions(self,value: Optional[List[cloud_pc_supported_region.CloudPcSupportedRegion]] = None) -> None:
        """
        Sets the supportedRegions property value. Cloud PC supported regions.
        Args:
            value: Value to set for the supportedRegions property.
        """
        self._supported_regions = value
    
    @property
    def user_settings(self,) -> Optional[List[cloud_pc_user_setting.CloudPcUserSetting]]:
        """
        Gets the userSettings property value. Cloud PC user settings.
        Returns: Optional[List[cloud_pc_user_setting.CloudPcUserSetting]]
        """
        return self._user_settings
    
    @user_settings.setter
    def user_settings(self,value: Optional[List[cloud_pc_user_setting.CloudPcUserSetting]] = None) -> None:
        """
        Sets the userSettings property value. Cloud PC user settings.
        Args:
            value: Value to set for the userSettings property.
        """
        self._user_settings = value
    

