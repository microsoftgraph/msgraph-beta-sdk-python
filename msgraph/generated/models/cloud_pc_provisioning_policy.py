from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_domain_join_configuration, cloud_pc_management_service, cloud_pc_provisioning_policy_assignment, cloud_pc_provisioning_policy_image_type, cloud_pc_provisioning_type, cloud_pc_windows_settings, entity, microsoft_managed_desktop

from . import entity

class CloudPcProvisioningPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcProvisioningPolicy and sets the default values.
        """
        super().__init__()
        # The URL of the alternate resource that links to this provisioning policy. Read-only.
        self._alternate_resource_url: Optional[str] = None
        # A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. For an example about how to get the assignments relationship, see Get cloudPcProvisioningPolicy.
        self._assignments: Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]] = None
        # The display name of the Cloud PC group that the Cloud PCs reside in. Read-only.
        self._cloud_pc_group_display_name: Optional[str] = None
        # The cloudPcNamingTemplate property
        self._cloud_pc_naming_template: Optional[str] = None
        # The provisioning policy description.
        self._description: Optional[str] = None
        # The display name for the provisioning policy.
        self._display_name: Optional[str] = None
        # Specifies how Cloud PCs will join Azure Active Directory.
        self._domain_join_configuration: Optional[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration] = None
        # The domainJoinConfigurations property
        self._domain_join_configurations: Optional[List[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration]] = None
        # True if the provisioned Cloud PC can be accessed by single sign-on. False indicates that the provisioned Cloud PC doesn't support this feature. Default value is false. Windows 365 users can use single sign-on to authenticate to Azure Active Directory (Azure AD) with passwordless options (for example, FIDO keys) to access their Cloud PC. Optional.
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
        # Specifies the type of license used when provisioning Cloud PCs using this policy. By default, the license type is dedicated if the provisioningType isn't specified when you create the cloudPcProvisioningPolicy. You can't change this property after the cloudPcProvisioningPolicy was created. Possible values are: dedicated, shared, unknownFutureValue.
        self._provisioning_type: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None
        # Specific Windows settings to configure while creating Cloud PCs for this provisioning policy.
        self._windows_settings: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings] = None
    
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
            value: Value to set for the alternate_resource_url property.
        """
        self._alternate_resource_url = value
    
    @property
    def assignments(self,) -> Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]]:
        """
        Gets the assignments property value. A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. For an example about how to get the assignments relationship, see Get cloudPcProvisioningPolicy.
        Returns: Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Azure AD that have provisioning policy assigned. Returned only on $expand. For an example about how to get the assignments relationship, see Get cloudPcProvisioningPolicy.
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
            value: Value to set for the cloud_pc_group_display_name property.
        """
        self._cloud_pc_group_display_name = value
    
    @property
    def cloud_pc_naming_template(self,) -> Optional[str]:
        """
        Gets the cloudPcNamingTemplate property value. The cloudPcNamingTemplate property
        Returns: Optional[str]
        """
        return self._cloud_pc_naming_template
    
    @cloud_pc_naming_template.setter
    def cloud_pc_naming_template(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcNamingTemplate property value. The cloudPcNamingTemplate property
        Args:
            value: Value to set for the cloud_pc_naming_template property.
        """
        self._cloud_pc_naming_template = value
    
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
            value: Value to set for the display_name property.
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
            value: Value to set for the domain_join_configuration property.
        """
        self._domain_join_configuration = value
    
    @property
    def domain_join_configurations(self,) -> Optional[List[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration]]:
        """
        Gets the domainJoinConfigurations property value. The domainJoinConfigurations property
        Returns: Optional[List[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration]]
        """
        return self._domain_join_configurations
    
    @domain_join_configurations.setter
    def domain_join_configurations(self,value: Optional[List[cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration]] = None) -> None:
        """
        Sets the domainJoinConfigurations property value. The domainJoinConfigurations property
        Args:
            value: Value to set for the domain_join_configurations property.
        """
        self._domain_join_configurations = value
    
    @property
    def enable_single_sign_on(self,) -> Optional[bool]:
        """
        Gets the enableSingleSignOn property value. True if the provisioned Cloud PC can be accessed by single sign-on. False indicates that the provisioned Cloud PC doesn't support this feature. Default value is false. Windows 365 users can use single sign-on to authenticate to Azure Active Directory (Azure AD) with passwordless options (for example, FIDO keys) to access their Cloud PC. Optional.
        Returns: Optional[bool]
        """
        return self._enable_single_sign_on
    
    @enable_single_sign_on.setter
    def enable_single_sign_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSingleSignOn property value. True if the provisioned Cloud PC can be accessed by single sign-on. False indicates that the provisioned Cloud PC doesn't support this feature. Default value is false. Windows 365 users can use single sign-on to authenticate to Azure Active Directory (Azure AD) with passwordless options (for example, FIDO keys) to access their Cloud PC. Optional.
        Args:
            value: Value to set for the enable_single_sign_on property.
        """
        self._enable_single_sign_on = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_domain_join_configuration, cloud_pc_management_service, cloud_pc_provisioning_policy_assignment, cloud_pc_provisioning_policy_image_type, cloud_pc_provisioning_type, cloud_pc_windows_settings, entity, microsoft_managed_desktop

        fields: Dict[str, Callable[[Any], None]] = {
            "alternateResourceUrl": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(cloud_pc_provisioning_policy_assignment.CloudPcProvisioningPolicyAssignment)),
            "cloudPcGroupDisplayName": lambda n : setattr(self, 'cloud_pc_group_display_name', n.get_str_value()),
            "cloudPcNamingTemplate": lambda n : setattr(self, 'cloud_pc_naming_template', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainJoinConfiguration": lambda n : setattr(self, 'domain_join_configuration', n.get_object_value(cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration)),
            "domainJoinConfigurations": lambda n : setattr(self, 'domain_join_configurations', n.get_collection_of_object_values(cloud_pc_domain_join_configuration.CloudPcDomainJoinConfiguration)),
            "enableSingleSignOn": lambda n : setattr(self, 'enable_single_sign_on', n.get_bool_value()),
            "gracePeriodInHours": lambda n : setattr(self, 'grace_period_in_hours', n.get_int_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "imageId": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "imageType": lambda n : setattr(self, 'image_type', n.get_enum_value(cloud_pc_provisioning_policy_image_type.CloudPcProvisioningPolicyImageType)),
            "localAdminEnabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_enum_value(cloud_pc_management_service.CloudPcManagementService)),
            "microsoftManagedDesktop": lambda n : setattr(self, 'microsoft_managed_desktop', n.get_object_value(microsoft_managed_desktop.MicrosoftManagedDesktop)),
            "onPremisesConnectionId": lambda n : setattr(self, 'on_premises_connection_id', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(cloud_pc_provisioning_type.CloudPcProvisioningType)),
            "windowsSettings": lambda n : setattr(self, 'windows_settings', n.get_object_value(cloud_pc_windows_settings.CloudPcWindowsSettings)),
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
            value: Value to set for the grace_period_in_hours property.
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
            value: Value to set for the image_display_name property.
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
            value: Value to set for the image_id property.
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
            value: Value to set for the image_type property.
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
            value: Value to set for the local_admin_enabled property.
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
            value: Value to set for the managed_by property.
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
            value: Value to set for the microsoft_managed_desktop property.
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
            value: Value to set for the on_premises_connection_id property.
        """
        self._on_premises_connection_id = value
    
    @property
    def provisioning_type(self,) -> Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]:
        """
        Gets the provisioningType property value. Specifies the type of license used when provisioning Cloud PCs using this policy. By default, the license type is dedicated if the provisioningType isn't specified when you create the cloudPcProvisioningPolicy. You can't change this property after the cloudPcProvisioningPolicy was created. Possible values are: dedicated, shared, unknownFutureValue.
        Returns: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]
        """
        return self._provisioning_type
    
    @provisioning_type.setter
    def provisioning_type(self,value: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None) -> None:
        """
        Sets the provisioningType property value. Specifies the type of license used when provisioning Cloud PCs using this policy. By default, the license type is dedicated if the provisioningType isn't specified when you create the cloudPcProvisioningPolicy. You can't change this property after the cloudPcProvisioningPolicy was created. Possible values are: dedicated, shared, unknownFutureValue.
        Args:
            value: Value to set for the provisioning_type property.
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
        writer.write_str_value("cloudPcNamingTemplate", self.cloud_pc_naming_template)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("domainJoinConfiguration", self.domain_join_configuration)
        writer.write_collection_of_object_values("domainJoinConfigurations", self.domain_join_configurations)
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
            value: Value to set for the windows_settings property.
        """
        self._windows_settings = value
    

