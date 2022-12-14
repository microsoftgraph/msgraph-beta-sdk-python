from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_domain_join_configuration = lazy_import('msgraph.generated.models.cloud_pc_domain_join_configuration')
cloud_pc_management_service = lazy_import('msgraph.generated.models.cloud_pc_management_service')
cloud_pc_provisioning_policy_assignment = lazy_import('msgraph.generated.models.cloud_pc_provisioning_policy_assignment')
cloud_pc_provisioning_policy_image_type = lazy_import('msgraph.generated.models.cloud_pc_provisioning_policy_image_type')
cloud_pc_provisioning_type = lazy_import('msgraph.generated.models.cloud_pc_provisioning_type')
cloud_pc_windows_settings = lazy_import('msgraph.generated.models.cloud_pc_windows_settings')
entity = lazy_import('msgraph.generated.models.entity')
microsoft_managed_desktop = lazy_import('msgraph.generated.models.microsoft_managed_desktop')

class CloudPcProvisioningPolicy(entity.Entity):
    @property
    def alternate_resource_url(self,) -> Optional[str]:
        """
        Gets the alternateResourceUrl property value. The URL of the alternate resource that links to this provisioning policy. Read-only.
        Returns: Optional[str]
        """
        return self._alternate_resource_url
    
    @alternate_resource_url.setter
    def alternate_resource_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateResourceUrl property value. The URL of the alternate resource that links to this provisioning policy. Read-only.
        Args:
            value: Value to set for the alternateResourceUrl property.
        """
        self._alternate_resource_url = value
    
    @property
    def assignments(self,) -> Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]]:
        """
        Gets the assignments property value. A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. See an example of getting the assignments relationship.
        Returns: Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. See an example of getting the assignments relationship.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def cloud_pc_group_display_name(self,) -> Optional[str]:
        """
        Gets the cloudPcGroupDisplayName property value. The display name of the Cloud PC group that the Cloud PCs reside in. Read-only.
        Returns: Optional[str]
        """
        return self._cloud_pc_group_display_name
    
    @cloud_pc_group_display_name.setter
    def cloud_pc_group_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcGroupDisplayName property value. The display name of the Cloud PC group that the Cloud PCs reside in. Read-only.
        Args:
            value: Value to set for the cloudPcGroupDisplayName property.
        """
        self._cloud_pc_group_display_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcProvisioningPolicy and sets the default values.
        """
        super().__init__()
        # The URL of the alternate resource that links to this provisioning policy. Read-only.
        self._alternate_resource_url: Optional[str] = None
        # A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. See an example of getting the assignments relationship.
        self._assignments: Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]] = None
        # The display name of the Cloud PC group that the Cloud PCs reside in. Read-only.
        self._cloud_pc_group_display_name: Optional[str] = None
        # The provisioning policy description.
        self._description: Optional[str] = None
        # The display name for the provisioning policy.
        self._display_name: Optional[str] = None
        # Specifies how Cloud PCs will join Azure Active Directory.
        self._domain_join_configuration: Optional[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration] = None
        # The enableSingleSignOn property
        self._enable_single_sign_on: Optional[bool] = None
        # The number of hours to wait before reprovisioning/deprovisioning happens. Read-only.
        self._grace_period_in_hours: Optional[int] = None
        # The display name for the OS image you’re provisioning.
        self._image_display_name: Optional[str] = None
        # The ID of the OS image you want to provision on Cloud PCs. The format for a gallery type image is: {publisher_offer_sku}. Supported values for each of the parameters are as follows:publisher: Microsoftwindowsdesktop. offer: windows-ent-cpc. sku: 21h1-ent-cpc-m365, 21h1-ent-cpc-os, 20h2-ent-cpc-m365, 20h2-ent-cpc-os, 20h1-ent-cpc-m365, 20h1-ent-cpc-os, 19h2-ent-cpc-m365 and 19h2-ent-cpc-os.
        self._image_id: Optional[str] = None
        # The imageType property
        self._image_type: Optional[cloud_pc_provisioning_policy_image_type.CloudPcProvisioningPolicyImageType] = None
        # Indicates whether the local admin option is enabled. If the local admin option is enabled, the end user can be an admin of the Cloud PC device. Read-only.
        self._local_admin_enabled: Optional[bool] = None
        # The managedBy property
        self._managed_by: Optional[cloud_pc_management_service.CloudPcManagementService] = None
        # The specific settings for the Microsoft Managed Desktop, which enables customers to get a managed device experience for the Cloud PC. Before you can enable Microsoft Managed Desktop, an admin must configure it.
        self._microsoft_managed_desktop: Optional[microsoft_managed_desktop.MicrosoftManagedDesktop] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ID of the cloudPcOnPremisesConnection. To ensure that Cloud PCs have network connectivity and that they domain join, choose a connection with a virtual network that’s validated by the Cloud PC service.
        self._on_premises_connection_id: Optional[str] = None
        # The provisioningType property
        self._provisioning_type: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None
        # Specific Windows settings to configure while creating Cloud PCs for this provisioning policy.
        self._windows_settings: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcProvisioningPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcProvisioningPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcProvisioningPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The provisioning policy description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The provisioning policy description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the provisioning policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the provisioning policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def domain_join_configuration(self,) -> Optional[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration]:
        """
        Gets the domainJoinConfiguration property value. Specifies how Cloud PCs will join Azure Active Directory.
        Returns: Optional[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration]
        """
        return self._domain_join_configuration
    
    @domain_join_configuration.setter
    def domain_join_configuration(self,value: Optional[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration] = None) -> None:
        """
        Sets the domainJoinConfiguration property value. Specifies how Cloud PCs will join Azure Active Directory.
        Args:
            value: Value to set for the domainJoinConfiguration property.
        """
        self._domain_join_configuration = value
    
    @property
    def enable_single_sign_on(self,) -> Optional[bool]:
        """
        Gets the enableSingleSignOn property value. The enableSingleSignOn property
        Returns: Optional[bool]
        """
        return self._enable_single_sign_on
    
    @enable_single_sign_on.setter
    def enable_single_sign_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSingleSignOn property value. The enableSingleSignOn property
        Args:
            value: Value to set for the enableSingleSignOn property.
        """
        self._enable_single_sign_on = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alternate_resource_url": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment)),
            "cloud_pc_group_display_name": lambda n : setattr(self, 'cloud_pc_group_display_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domain_join_configuration": lambda n : setattr(self, 'domain_join_configuration', n.get_object_value(cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration)),
            "enable_single_sign_on": lambda n : setattr(self, 'enable_single_sign_on', n.get_bool_value()),
            "grace_period_in_hours": lambda n : setattr(self, 'grace_period_in_hours', n.get_int_value()),
            "image_display_name": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "image_type": lambda n : setattr(self, 'image_type', n.get_enum_value(cloud_pc_provisioning_policy_image_type.CloudPcProvisioningPolicyImageType)),
            "local_admin_enabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "managed_by": lambda n : setattr(self, 'managed_by', n.get_enum_value(cloud_pc_management_service.CloudPcManagementService)),
            "microsoft_managed_desktop": lambda n : setattr(self, 'microsoft_managed_desktop', n.get_object_value(microsoft_managed_desktop.MicrosoftManagedDesktop)),
            "on_premises_connection_id": lambda n : setattr(self, 'on_premises_connection_id', n.get_str_value()),
            "provisioning_type": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(cloud_pc_provisioning_type.CloudPcProvisioningType)),
            "windows_settings": lambda n : setattr(self, 'windows_settings', n.get_object_value(cloud_pc_windows_settings.CloudPcWindowsSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grace_period_in_hours(self,) -> Optional[int]:
        """
        Gets the gracePeriodInHours property value. The number of hours to wait before reprovisioning/deprovisioning happens. Read-only.
        Returns: Optional[int]
        """
        return self._grace_period_in_hours
    
    @grace_period_in_hours.setter
    def grace_period_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the gracePeriodInHours property value. The number of hours to wait before reprovisioning/deprovisioning happens. Read-only.
        Args:
            value: Value to set for the gracePeriodInHours property.
        """
        self._grace_period_in_hours = value
    
    @property
    def image_display_name(self,) -> Optional[str]:
        """
        Gets the imageDisplayName property value. The display name for the OS image you’re provisioning.
        Returns: Optional[str]
        """
        return self._image_display_name
    
    @image_display_name.setter
    def image_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the imageDisplayName property value. The display name for the OS image you’re provisioning.
        Args:
            value: Value to set for the imageDisplayName property.
        """
        self._image_display_name = value
    
    @property
    def image_id(self,) -> Optional[str]:
        """
        Gets the imageId property value. The ID of the OS image you want to provision on Cloud PCs. The format for a gallery type image is: {publisher_offer_sku}. Supported values for each of the parameters are as follows:publisher: Microsoftwindowsdesktop. offer: windows-ent-cpc. sku: 21h1-ent-cpc-m365, 21h1-ent-cpc-os, 20h2-ent-cpc-m365, 20h2-ent-cpc-os, 20h1-ent-cpc-m365, 20h1-ent-cpc-os, 19h2-ent-cpc-m365 and 19h2-ent-cpc-os.
        Returns: Optional[str]
        """
        return self._image_id
    
    @image_id.setter
    def image_id(self,value: Optional[str] = None) -> None:
        """
        Sets the imageId property value. The ID of the OS image you want to provision on Cloud PCs. The format for a gallery type image is: {publisher_offer_sku}. Supported values for each of the parameters are as follows:publisher: Microsoftwindowsdesktop. offer: windows-ent-cpc. sku: 21h1-ent-cpc-m365, 21h1-ent-cpc-os, 20h2-ent-cpc-m365, 20h2-ent-cpc-os, 20h1-ent-cpc-m365, 20h1-ent-cpc-os, 19h2-ent-cpc-m365 and 19h2-ent-cpc-os.
        Args:
            value: Value to set for the imageId property.
        """
        self._image_id = value
    
    @property
    def image_type(self,) -> Optional[cloud_pc_provisioning_policy_image_type.CloudPcProvisioningPolicyImageType]:
        """
        Gets the imageType property value. The imageType property
        Returns: Optional[cloud_pc_provisioning_policy_image_type.CloudPcProvisioningPolicyImageType]
        """
        return self._image_type
    
    @image_type.setter
    def image_type(self,value: Optional[cloud_pc_provisioning_policy_image_type.CloudPcProvisioningPolicyImageType] = None) -> None:
        """
        Sets the imageType property value. The imageType property
        Args:
            value: Value to set for the imageType property.
        """
        self._image_type = value
    
    @property
    def local_admin_enabled(self,) -> Optional[bool]:
        """
        Gets the localAdminEnabled property value. Indicates whether the local admin option is enabled. If the local admin option is enabled, the end user can be an admin of the Cloud PC device. Read-only.
        Returns: Optional[bool]
        """
        return self._local_admin_enabled
    
    @local_admin_enabled.setter
    def local_admin_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the localAdminEnabled property value. Indicates whether the local admin option is enabled. If the local admin option is enabled, the end user can be an admin of the Cloud PC device. Read-only.
        Args:
            value: Value to set for the localAdminEnabled property.
        """
        self._local_admin_enabled = value
    
    @property
    def managed_by(self,) -> Optional[cloud_pc_management_service.CloudPcManagementService]:
        """
        Gets the managedBy property value. The managedBy property
        Returns: Optional[cloud_pc_management_service.CloudPcManagementService]
        """
        return self._managed_by
    
    @managed_by.setter
    def managed_by(self,value: Optional[cloud_pc_management_service.CloudPcManagementService] = None) -> None:
        """
        Sets the managedBy property value. The managedBy property
        Args:
            value: Value to set for the managedBy property.
        """
        self._managed_by = value
    
    @property
    def microsoft_managed_desktop(self,) -> Optional[microsoft_managed_desktop.MicrosoftManagedDesktop]:
        """
        Gets the microsoftManagedDesktop property value. The specific settings for the Microsoft Managed Desktop, which enables customers to get a managed device experience for the Cloud PC. Before you can enable Microsoft Managed Desktop, an admin must configure it.
        Returns: Optional[microsoft_managed_desktop.MicrosoftManagedDesktop]
        """
        return self._microsoft_managed_desktop
    
    @microsoft_managed_desktop.setter
    def microsoft_managed_desktop(self,value: Optional[microsoft_managed_desktop.MicrosoftManagedDesktop] = None) -> None:
        """
        Sets the microsoftManagedDesktop property value. The specific settings for the Microsoft Managed Desktop, which enables customers to get a managed device experience for the Cloud PC. Before you can enable Microsoft Managed Desktop, an admin must configure it.
        Args:
            value: Value to set for the microsoftManagedDesktop property.
        """
        self._microsoft_managed_desktop = value
    
    @property
    def on_premises_connection_id(self,) -> Optional[str]:
        """
        Gets the onPremisesConnectionId property value. The ID of the cloudPcOnPremisesConnection. To ensure that Cloud PCs have network connectivity and that they domain join, choose a connection with a virtual network that’s validated by the Cloud PC service.
        Returns: Optional[str]
        """
        return self._on_premises_connection_id
    
    @on_premises_connection_id.setter
    def on_premises_connection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesConnectionId property value. The ID of the cloudPcOnPremisesConnection. To ensure that Cloud PCs have network connectivity and that they domain join, choose a connection with a virtual network that’s validated by the Cloud PC service.
        Args:
            value: Value to set for the onPremisesConnectionId property.
        """
        self._on_premises_connection_id = value
    
    @property
    def provisioning_type(self,) -> Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]:
        """
        Gets the provisioningType property value. The provisioningType property
        Returns: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]
        """
        return self._provisioning_type
    
    @provisioning_type.setter
    def provisioning_type(self,value: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None) -> None:
        """
        Sets the provisioningType property value. The provisioningType property
        Args:
            value: Value to set for the provisioningType property.
        """
        self._provisioning_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("alternateResourceUrl", self.alternate_resource_url)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("cloudPcGroupDisplayName", self.cloud_pc_group_display_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("domainJoinConfiguration", self.domain_join_configuration)
        writer.write_bool_value("enableSingleSignOn", self.enable_single_sign_on)
        writer.write_int_value("gracePeriodInHours", self.grace_period_in_hours)
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_str_value("imageId", self.image_id)
        writer.write_enum_value("imageType", self.image_type)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_enum_value("managedBy", self.managed_by)
        writer.write_object_value("microsoftManagedDesktop", self.microsoft_managed_desktop)
        writer.write_str_value("onPremisesConnectionId", self.on_premises_connection_id)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_object_value("windowsSettings", self.windows_settings)
    
    @property
    def windows_settings(self,) -> Optional[cloud_pc_windows_settings.CloudPcWindowsSettings]:
        """
        Gets the windowsSettings property value. Specific Windows settings to configure while creating Cloud PCs for this provisioning policy.
        Returns: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings]
        """
        return self._windows_settings
    
    @windows_settings.setter
    def windows_settings(self,value: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings] = None) -> None:
        """
        Sets the windowsSettings property value. Specific Windows settings to configure while creating Cloud PCs for this provisioning policy.
        Args:
            value: Value to set for the windowsSettings property.
        """
        self._windows_settings = value
    

