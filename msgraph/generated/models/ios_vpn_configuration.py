from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_vpn_configuration, app_list_item, device_management_derived_credential_settings, iosik_ev2_vpn_configuration, ios_certificate_profile_base

from . import apple_vpn_configuration

class IosVpnConfiguration(apple_vpn_configuration.AppleVpnConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IosVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosVpnConfiguration"
        # Zscaler only. Zscaler cloud which the user is assigned to.
        self._cloud_name: Optional[str] = None
        # Tenant level settings for the Derived Credentials to be used for authentication.
        self._derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
        # Zscaler only. List of network addresses which are not sent through the Zscaler cloud.
        self._exclude_list: Optional[List[str]] = None
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
        # Microsoft Tunnel site ID.
        self._microsoft_tunnel_site_id: Optional[str] = None
        # Zscaler only. Blocks network traffic until the user signs into Zscaler app. 'True' means traffic is blocked.
        self._strict_enforcement: Optional[bool] = None
        # Targeted mobile apps. This collection can contain a maximum of 500 elements.
        self._targeted_mobile_apps: Optional[List[app_list_item.AppListItem]] = None
        # Zscaler only. Enter a static domain to pre-populate the login field with in the Zscaler app. If this is left empty, the user's Azure Active Directory domain will be used instead.
        self._user_domain: Optional[str] = None
    
    @property
    def cloud_name(self,) -> Optional[str]:
        """
        Gets the cloudName property value. Zscaler only. Zscaler cloud which the user is assigned to.
        Returns: Optional[str]
        """
        return self._cloud_name
    
    @cloud_name.setter
    def cloud_name(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudName property value. Zscaler only. Zscaler cloud which the user is assigned to.
        Args:
            value: Value to set for the cloud_name property.
        """
        self._cloud_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosikEv2VpnConfiguration":
                from . import iosik_ev2_vpn_configuration

                return iosik_ev2_vpn_configuration.IosikEv2VpnConfiguration()
        return IosVpnConfiguration()
    
    @property
    def derived_credential_settings(self,) -> Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]:
        """
        Gets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Returns: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]
        """
        return self._derived_credential_settings
    
    @derived_credential_settings.setter
    def derived_credential_settings(self,value: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None) -> None:
        """
        Sets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Args:
            value: Value to set for the derived_credential_settings property.
        """
        self._derived_credential_settings = value
    
    @property
    def exclude_list(self,) -> Optional[List[str]]:
        """
        Gets the excludeList property value. Zscaler only. List of network addresses which are not sent through the Zscaler cloud.
        Returns: Optional[List[str]]
        """
        return self._exclude_list
    
    @exclude_list.setter
    def exclude_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeList property value. Zscaler only. List of network addresses which are not sent through the Zscaler cloud.
        Args:
            value: Value to set for the exclude_list property.
        """
        self._exclude_list = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_vpn_configuration, app_list_item, device_management_derived_credential_settings, iosik_ev2_vpn_configuration, ios_certificate_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudName": lambda n : setattr(self, 'cloud_name', n.get_str_value()),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "excludeList": lambda n : setattr(self, 'exclude_list', n.get_collection_of_primitive_values(str)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "microsoftTunnelSiteId": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "strictEnforcement": lambda n : setattr(self, 'strict_enforcement', n.get_bool_value()),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "userDomain": lambda n : setattr(self, 'user_domain', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate(self,) -> Optional[ios_certificate_profile_base.IosCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[ios_certificate_profile_base.IosCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identity_certificate property.
        """
        self._identity_certificate = value
    
    @property
    def microsoft_tunnel_site_id(self,) -> Optional[str]:
        """
        Gets the microsoftTunnelSiteId property value. Microsoft Tunnel site ID.
        Returns: Optional[str]
        """
        return self._microsoft_tunnel_site_id
    
    @microsoft_tunnel_site_id.setter
    def microsoft_tunnel_site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the microsoftTunnelSiteId property value. Microsoft Tunnel site ID.
        Args:
            value: Value to set for the microsoft_tunnel_site_id property.
        """
        self._microsoft_tunnel_site_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("cloudName", self.cloud_name)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_collection_of_primitive_values("excludeList", self.exclude_list)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_bool_value("strictEnforcement", self.strict_enforcement)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_str_value("userDomain", self.user_domain)
    
    @property
    def strict_enforcement(self,) -> Optional[bool]:
        """
        Gets the strictEnforcement property value. Zscaler only. Blocks network traffic until the user signs into Zscaler app. 'True' means traffic is blocked.
        Returns: Optional[bool]
        """
        return self._strict_enforcement
    
    @strict_enforcement.setter
    def strict_enforcement(self,value: Optional[bool] = None) -> None:
        """
        Sets the strictEnforcement property value. Zscaler only. Blocks network traffic until the user signs into Zscaler app. 'True' means traffic is blocked.
        Args:
            value: Value to set for the strict_enforcement property.
        """
        self._strict_enforcement = value
    
    @property
    def targeted_mobile_apps(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the targetedMobileApps property value. Targeted mobile apps. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._targeted_mobile_apps
    
    @targeted_mobile_apps.setter
    def targeted_mobile_apps(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the targetedMobileApps property value. Targeted mobile apps. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the targeted_mobile_apps property.
        """
        self._targeted_mobile_apps = value
    
    @property
    def user_domain(self,) -> Optional[str]:
        """
        Gets the userDomain property value. Zscaler only. Enter a static domain to pre-populate the login field with in the Zscaler app. If this is left empty, the user's Azure Active Directory domain will be used instead.
        Returns: Optional[str]
        """
        return self._user_domain
    
    @user_domain.setter
    def user_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the userDomain property value. Zscaler only. Enter a static domain to pre-populate the login field with in the Zscaler app. If this is left empty, the user's Azure Active Directory domain will be used instead.
        Args:
            value: Value to set for the user_domain property.
        """
        self._user_domain = value
    

