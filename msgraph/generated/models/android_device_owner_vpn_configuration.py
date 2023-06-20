from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_certificate_profile_base, android_vpn_connection_type, app_list_item, device_management_derived_credential_settings, key_value, key_value_pair, vpn_configuration, vpn_proxy_server

from . import vpn_configuration

@dataclass
class AndroidDeviceOwnerVpnConfiguration(vpn_configuration.VpnConfiguration):
    odata_type = "#microsoft.graph.androidDeviceOwnerVpnConfiguration"
    # Whether or not to enable always-on VPN connection.
    always_on: Optional[bool] = None
    # If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
    always_on_lockdown: Optional[bool] = None
    # Android VPN connection type.
    connection_type: Optional[android_vpn_connection_type.AndroidVpnConnectionType] = None
    # Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
    custom_data: Optional[List[key_value.KeyValue]] = None
    # Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase] = None
    # Microsoft Tunnel site ID.
    microsoft_tunnel_site_id: Optional[str] = None
    # Proxy server.
    proxy_server: Optional[vpn_proxy_server.VpnProxyServer] = None
    # Targeted mobile apps. This collection can contain a maximum of 500 elements.
    targeted_mobile_apps: Optional[List[app_list_item.AppListItem]] = None
    # Targeted App package IDs.
    targeted_package_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerVpnConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_certificate_profile_base, android_vpn_connection_type, app_list_item, device_management_derived_credential_settings, key_value, key_value_pair, vpn_configuration, vpn_proxy_server

        from . import android_device_owner_certificate_profile_base, android_vpn_connection_type, app_list_item, device_management_derived_credential_settings, key_value, key_value_pair, vpn_configuration, vpn_proxy_server

        fields: Dict[str, Callable[[Any], None]] = {
            "alwaysOn": lambda n : setattr(self, 'always_on', n.get_bool_value()),
            "alwaysOnLockdown": lambda n : setattr(self, 'always_on_lockdown', n.get_bool_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(android_vpn_connection_type.AndroidVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(key_value.KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase)),
            "microsoftTunnelSiteId": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(vpn_proxy_server.VpnProxyServer)),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "targetedPackageIds": lambda n : setattr(self, 'targeted_package_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("alwaysOn", self.always_on)
        writer.write_bool_value("alwaysOnLockdown", self.always_on_lockdown)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_collection_of_primitive_values("targetedPackageIds", self.targeted_package_ids)
    

