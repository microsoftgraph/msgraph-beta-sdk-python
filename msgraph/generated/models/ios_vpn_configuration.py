from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_vpn_configuration, app_list_item, device_management_derived_credential_settings, iosik_ev2_vpn_configuration, ios_certificate_profile_base

from . import apple_vpn_configuration

@dataclass
class IosVpnConfiguration(apple_vpn_configuration.AppleVpnConfiguration):
    odata_type = "#microsoft.graph.iosVpnConfiguration"
    # Zscaler only. Zscaler cloud which the user is assigned to.
    cloud_name: Optional[str] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
    # Zscaler only. List of network addresses which are not sent through the Zscaler cloud.
    exclude_list: Optional[List[str]] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
    # Microsoft Tunnel site ID.
    microsoft_tunnel_site_id: Optional[str] = None
    # Zscaler only. Blocks network traffic until the user signs into Zscaler app. 'True' means traffic is blocked.
    strict_enforcement: Optional[bool] = None
    # Targeted mobile apps. This collection can contain a maximum of 500 elements.
    targeted_mobile_apps: Optional[List[app_list_item.AppListItem]] = None
    # Zscaler only. Enter a static domain to pre-populate the login field with in the Zscaler app. If this is left empty, the user's Azure Active Directory domain will be used instead.
    user_domain: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVpnConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosikEv2VpnConfiguration".casefold():
            from . import iosik_ev2_vpn_configuration

            return iosik_ev2_vpn_configuration.IosikEv2VpnConfiguration()
        return IosVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_vpn_configuration, app_list_item, device_management_derived_credential_settings, iosik_ev2_vpn_configuration, ios_certificate_profile_base

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("cloudName", self.cloud_name)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_collection_of_primitive_values("excludeList", self.exclude_list)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_bool_value("strictEnforcement", self.strict_enforcement)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_str_value("userDomain", self.user_domain)
    

