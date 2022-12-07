from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_certificate_profile_base = lazy_import('msgraph.generated.models.android_device_owner_certificate_profile_base')
android_vpn_connection_type = lazy_import('msgraph.generated.models.android_vpn_connection_type')
app_list_item = lazy_import('msgraph.generated.models.app_list_item')
device_management_derived_credential_settings = lazy_import('msgraph.generated.models.device_management_derived_credential_settings')
key_value = lazy_import('msgraph.generated.models.key_value')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
vpn_configuration = lazy_import('msgraph.generated.models.vpn_configuration')
vpn_proxy_server = lazy_import('msgraph.generated.models.vpn_proxy_server')

class AndroidDeviceOwnerVpnConfiguration(vpn_configuration.VpnConfiguration):
    @property
    def always_on(self,) -> Optional[bool]:
        """
        Gets the alwaysOn property value. Whether or not to enable always-on VPN connection.
        Returns: Optional[bool]
        """
        return self._always_on
    
    @always_on.setter
    def always_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the alwaysOn property value. Whether or not to enable always-on VPN connection.
        Args:
            value: Value to set for the alwaysOn property.
        """
        self._always_on = value
    
    @property
    def always_on_lockdown(self,) -> Optional[bool]:
        """
        Gets the alwaysOnLockdown property value. If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
        Returns: Optional[bool]
        """
        return self._always_on_lockdown
    
    @always_on_lockdown.setter
    def always_on_lockdown(self,value: Optional[bool] = None) -> None:
        """
        Sets the alwaysOnLockdown property value. If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
        Args:
            value: Value to set for the alwaysOnLockdown property.
        """
        self._always_on_lockdown = value
    
    @property
    def connection_type(self,) -> Optional[android_vpn_connection_type.AndroidVpnConnectionType]:
        """
        Gets the connectionType property value. Android VPN connection type.
        Returns: Optional[android_vpn_connection_type.AndroidVpnConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[android_vpn_connection_type.AndroidVpnConnectionType] = None) -> None:
        """
        Sets the connectionType property value. Android VPN connection type.
        Args:
            value: Value to set for the connectionType property.
        """
        self._connection_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerVpnConfiguration"
        # Whether or not to enable always-on VPN connection.
        self._always_on: Optional[bool] = None
        # If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
        self._always_on_lockdown: Optional[bool] = None
        # Android VPN connection type.
        self._connection_type: Optional[android_vpn_connection_type.AndroidVpnConnectionType] = None
        # Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
        self._custom_data: Optional[List[key_value.KeyValue]] = None
        # Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
        self._custom_key_value_data: Optional[List[key_value_pair.KeyValuePair]] = None
        # Tenant level settings for the Derived Credentials to be used for authentication.
        self._derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase] = None
        # Microsoft Tunnel site ID.
        self._microsoft_tunnel_site_id: Optional[str] = None
        # Proxy server.
        self._proxy_server: Optional[vpn_proxy_server.VpnProxyServer] = None
        # Targeted mobile apps. This collection can contain a maximum of 500 elements.
        self._targeted_mobile_apps: Optional[List[app_list_item.AppListItem]] = None
        # Targeted App package IDs.
        self._targeted_package_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerVpnConfiguration()
    
    @property
    def custom_data(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the customData property value. Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._custom_data
    
    @custom_data.setter
    def custom_data(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the customData property value. Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
        Args:
            value: Value to set for the customData property.
        """
        self._custom_data = value
    
    @property
    def custom_key_value_data(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the customKeyValueData property value. Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._custom_key_value_data
    
    @custom_key_value_data.setter
    def custom_key_value_data(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the customKeyValueData property value. Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
        Args:
            value: Value to set for the customKeyValueData property.
        """
        self._custom_key_value_data = value
    
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
            value: Value to set for the derivedCredentialSettings property.
        """
        self._derived_credential_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "always_on": lambda n : setattr(self, 'always_on', n.get_bool_value()),
            "always_on_lockdown": lambda n : setattr(self, 'always_on_lockdown', n.get_bool_value()),
            "connection_type": lambda n : setattr(self, 'connection_type', n.get_enum_value(android_vpn_connection_type.AndroidVpnConnectionType)),
            "custom_data": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(key_value.KeyValue)),
            "custom_key_value_data": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "derived_credential_settings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase)),
            "microsoft_tunnel_site_id": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "proxy_server": lambda n : setattr(self, 'proxy_server', n.get_object_value(vpn_proxy_server.VpnProxyServer)),
            "targeted_mobile_apps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "targeted_package_ids": lambda n : setattr(self, 'targeted_package_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate(self,) -> Optional[android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identityCertificate property.
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
            value: Value to set for the microsoftTunnelSiteId property.
        """
        self._microsoft_tunnel_site_id = value
    
    @property
    def proxy_server(self,) -> Optional[vpn_proxy_server.VpnProxyServer]:
        """
        Gets the proxyServer property value. Proxy server.
        Returns: Optional[vpn_proxy_server.VpnProxyServer]
        """
        return self._proxy_server
    
    @proxy_server.setter
    def proxy_server(self,value: Optional[vpn_proxy_server.VpnProxyServer] = None) -> None:
        """
        Sets the proxyServer property value. Proxy server.
        Args:
            value: Value to set for the proxyServer property.
        """
        self._proxy_server = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
            value: Value to set for the targetedMobileApps property.
        """
        self._targeted_mobile_apps = value
    
    @property
    def targeted_package_ids(self,) -> Optional[List[str]]:
        """
        Gets the targetedPackageIds property value. Targeted App package IDs.
        Returns: Optional[List[str]]
        """
        return self._targeted_package_ids
    
    @targeted_package_ids.setter
    def targeted_package_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targetedPackageIds property value. Targeted App package IDs.
        Args:
            value: Value to set for the targetedPackageIds property.
        """
        self._targeted_package_ids = value
    

