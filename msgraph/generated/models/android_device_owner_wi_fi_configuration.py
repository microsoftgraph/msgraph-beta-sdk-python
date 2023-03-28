from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_enterprise_wi_fi_configuration, android_device_owner_wi_fi_security_type, device_configuration, wi_fi_proxy_setting

from . import device_configuration

class AndroidDeviceOwnerWiFiConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerWiFiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerWiFiConfiguration"
        # Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
        self._connect_automatically: Optional[bool] = None
        # When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        self._connect_when_network_name_is_hidden: Optional[bool] = None
        # Network Name
        self._network_name: Optional[str] = None
        # This is the pre-shared key for WPA Personal Wi-Fi network.
        self._pre_shared_key: Optional[str] = None
        # This is the pre-shared key for WPA Personal Wi-Fi network.
        self._pre_shared_key_is_set: Optional[bool] = None
        # Specify the proxy server configuration script URL.
        self._proxy_automatic_configuration_url: Optional[str] = None
        # List of hosts to exclude using the proxy on connections for. These hosts can use wildcards such as .example.com.
        self._proxy_exclusion_list: Optional[str] = None
        # Specify the proxy server IP address. Android documentation does not specify IPv4 or IPv6. For example: 192.168.1.1.
        self._proxy_manual_address: Optional[str] = None
        # Specify the proxy server port.
        self._proxy_manual_port: Optional[int] = None
        # Wi-Fi Proxy Settings.
        self._proxy_settings: Optional[wi_fi_proxy_setting.WiFiProxySetting] = None
        # This is the name of the Wi-Fi network that is broadcast to all devices.
        self._ssid: Optional[str] = None
        # Wi-Fi Security Types for Android Device Owner.
        self._wi_fi_security_type: Optional[android_device_owner_wi_fi_security_type.AndroidDeviceOwnerWiFiSecurityType] = None
    
    @property
    def connect_automatically(self,) -> Optional[bool]:
        """
        Gets the connectAutomatically property value. Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
        Returns: Optional[bool]
        """
        return self._connect_automatically
    
    @connect_automatically.setter
    def connect_automatically(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectAutomatically property value. Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
        Args:
            value: Value to set for the connect_automatically property.
        """
        self._connect_automatically = value
    
    @property
    def connect_when_network_name_is_hidden(self,) -> Optional[bool]:
        """
        Gets the connectWhenNetworkNameIsHidden property value. When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        Returns: Optional[bool]
        """
        return self._connect_when_network_name_is_hidden
    
    @connect_when_network_name_is_hidden.setter
    def connect_when_network_name_is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectWhenNetworkNameIsHidden property value. When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        Args:
            value: Value to set for the connect_when_network_name_is_hidden property.
        """
        self._connect_when_network_name_is_hidden = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerWiFiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration":
                from . import android_device_owner_enterprise_wi_fi_configuration

                return android_device_owner_enterprise_wi_fi_configuration.AndroidDeviceOwnerEnterpriseWiFiConfiguration()
        return AndroidDeviceOwnerWiFiConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_enterprise_wi_fi_configuration, android_device_owner_wi_fi_security_type, device_configuration, wi_fi_proxy_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "preSharedKeyIsSet": lambda n : setattr(self, 'pre_shared_key_is_set', n.get_bool_value()),
            "proxyAutomaticConfigurationUrl": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxyExclusionList": lambda n : setattr(self, 'proxy_exclusion_list', n.get_str_value()),
            "proxyManualAddress": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxyManualPort": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxySettings": lambda n : setattr(self, 'proxy_settings', n.get_enum_value(wi_fi_proxy_setting.WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wiFiSecurityType": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(android_device_owner_wi_fi_security_type.AndroidDeviceOwnerWiFiSecurityType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def network_name(self,) -> Optional[str]:
        """
        Gets the networkName property value. Network Name
        Returns: Optional[str]
        """
        return self._network_name
    
    @network_name.setter
    def network_name(self,value: Optional[str] = None) -> None:
        """
        Sets the networkName property value. Network Name
        Args:
            value: Value to set for the network_name property.
        """
        self._network_name = value
    
    @property
    def pre_shared_key(self,) -> Optional[str]:
        """
        Gets the preSharedKey property value. This is the pre-shared key for WPA Personal Wi-Fi network.
        Returns: Optional[str]
        """
        return self._pre_shared_key
    
    @pre_shared_key.setter
    def pre_shared_key(self,value: Optional[str] = None) -> None:
        """
        Sets the preSharedKey property value. This is the pre-shared key for WPA Personal Wi-Fi network.
        Args:
            value: Value to set for the pre_shared_key property.
        """
        self._pre_shared_key = value
    
    @property
    def pre_shared_key_is_set(self,) -> Optional[bool]:
        """
        Gets the preSharedKeyIsSet property value. This is the pre-shared key for WPA Personal Wi-Fi network.
        Returns: Optional[bool]
        """
        return self._pre_shared_key_is_set
    
    @pre_shared_key_is_set.setter
    def pre_shared_key_is_set(self,value: Optional[bool] = None) -> None:
        """
        Sets the preSharedKeyIsSet property value. This is the pre-shared key for WPA Personal Wi-Fi network.
        Args:
            value: Value to set for the pre_shared_key_is_set property.
        """
        self._pre_shared_key_is_set = value
    
    @property
    def proxy_automatic_configuration_url(self,) -> Optional[str]:
        """
        Gets the proxyAutomaticConfigurationUrl property value. Specify the proxy server configuration script URL.
        Returns: Optional[str]
        """
        return self._proxy_automatic_configuration_url
    
    @proxy_automatic_configuration_url.setter
    def proxy_automatic_configuration_url(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyAutomaticConfigurationUrl property value. Specify the proxy server configuration script URL.
        Args:
            value: Value to set for the proxy_automatic_configuration_url property.
        """
        self._proxy_automatic_configuration_url = value
    
    @property
    def proxy_exclusion_list(self,) -> Optional[str]:
        """
        Gets the proxyExclusionList property value. List of hosts to exclude using the proxy on connections for. These hosts can use wildcards such as .example.com.
        Returns: Optional[str]
        """
        return self._proxy_exclusion_list
    
    @proxy_exclusion_list.setter
    def proxy_exclusion_list(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyExclusionList property value. List of hosts to exclude using the proxy on connections for. These hosts can use wildcards such as .example.com.
        Args:
            value: Value to set for the proxy_exclusion_list property.
        """
        self._proxy_exclusion_list = value
    
    @property
    def proxy_manual_address(self,) -> Optional[str]:
        """
        Gets the proxyManualAddress property value. Specify the proxy server IP address. Android documentation does not specify IPv4 or IPv6. For example: 192.168.1.1.
        Returns: Optional[str]
        """
        return self._proxy_manual_address
    
    @proxy_manual_address.setter
    def proxy_manual_address(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyManualAddress property value. Specify the proxy server IP address. Android documentation does not specify IPv4 or IPv6. For example: 192.168.1.1.
        Args:
            value: Value to set for the proxy_manual_address property.
        """
        self._proxy_manual_address = value
    
    @property
    def proxy_manual_port(self,) -> Optional[int]:
        """
        Gets the proxyManualPort property value. Specify the proxy server port.
        Returns: Optional[int]
        """
        return self._proxy_manual_port
    
    @proxy_manual_port.setter
    def proxy_manual_port(self,value: Optional[int] = None) -> None:
        """
        Sets the proxyManualPort property value. Specify the proxy server port.
        Args:
            value: Value to set for the proxy_manual_port property.
        """
        self._proxy_manual_port = value
    
    @property
    def proxy_settings(self,) -> Optional[wi_fi_proxy_setting.WiFiProxySetting]:
        """
        Gets the proxySettings property value. Wi-Fi Proxy Settings.
        Returns: Optional[wi_fi_proxy_setting.WiFiProxySetting]
        """
        return self._proxy_settings
    
    @proxy_settings.setter
    def proxy_settings(self,value: Optional[wi_fi_proxy_setting.WiFiProxySetting] = None) -> None:
        """
        Sets the proxySettings property value. Wi-Fi Proxy Settings.
        Args:
            value: Value to set for the proxy_settings property.
        """
        self._proxy_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("connectAutomatically", self.connect_automatically)
        writer.write_bool_value("connectWhenNetworkNameIsHidden", self.connect_when_network_name_is_hidden)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_bool_value("preSharedKeyIsSet", self.pre_shared_key_is_set)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_str_value("proxyExclusionList", self.proxy_exclusion_list)
        writer.write_str_value("proxyManualAddress", self.proxy_manual_address)
        writer.write_int_value("proxyManualPort", self.proxy_manual_port)
        writer.write_enum_value("proxySettings", self.proxy_settings)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wiFiSecurityType", self.wi_fi_security_type)
    
    @property
    def ssid(self,) -> Optional[str]:
        """
        Gets the ssid property value. This is the name of the Wi-Fi network that is broadcast to all devices.
        Returns: Optional[str]
        """
        return self._ssid
    
    @ssid.setter
    def ssid(self,value: Optional[str] = None) -> None:
        """
        Sets the ssid property value. This is the name of the Wi-Fi network that is broadcast to all devices.
        Args:
            value: Value to set for the ssid property.
        """
        self._ssid = value
    
    @property
    def wi_fi_security_type(self,) -> Optional[android_device_owner_wi_fi_security_type.AndroidDeviceOwnerWiFiSecurityType]:
        """
        Gets the wiFiSecurityType property value. Wi-Fi Security Types for Android Device Owner.
        Returns: Optional[android_device_owner_wi_fi_security_type.AndroidDeviceOwnerWiFiSecurityType]
        """
        return self._wi_fi_security_type
    
    @wi_fi_security_type.setter
    def wi_fi_security_type(self,value: Optional[android_device_owner_wi_fi_security_type.AndroidDeviceOwnerWiFiSecurityType] = None) -> None:
        """
        Sets the wiFiSecurityType property value. Wi-Fi Security Types for Android Device Owner.
        Args:
            value: Value to set for the wi_fi_security_type property.
        """
        self._wi_fi_security_type = value
    

