from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
wi_fi_proxy_setting = lazy_import('msgraph.generated.models.wi_fi_proxy_setting')
wi_fi_security_type = lazy_import('msgraph.generated.models.wi_fi_security_type')

class IosWiFiConfiguration(device_configuration.DeviceConfiguration):
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
            value: Value to set for the connectAutomatically property.
        """
        self._connect_automatically = value
    
    @property
    def connect_when_network_name_is_hidden(self,) -> Optional[bool]:
        """
        Gets the connectWhenNetworkNameIsHidden property value. Connect when the network is not broadcasting its name (SSID). When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        Returns: Optional[bool]
        """
        return self._connect_when_network_name_is_hidden
    
    @connect_when_network_name_is_hidden.setter
    def connect_when_network_name_is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectWhenNetworkNameIsHidden property value. Connect when the network is not broadcasting its name (SSID). When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        Args:
            value: Value to set for the connectWhenNetworkNameIsHidden property.
        """
        self._connect_when_network_name_is_hidden = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosWiFiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosWiFiConfiguration"
        # Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
        self._connect_automatically: Optional[bool] = None
        # Connect when the network is not broadcasting its name (SSID). When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        self._connect_when_network_name_is_hidden: Optional[bool] = None
        # If set to true, forces devices connecting using this Wi-Fi profile to present their actual Wi-Fi MAC address instead of a random MAC address. Applies to iOS 14 and later.
        self._disable_mac_address_randomization: Optional[bool] = None
        # Network Name
        self._network_name: Optional[str] = None
        # This is the pre-shared key for WPA Personal Wi-Fi network.
        self._pre_shared_key: Optional[str] = None
        # URL of the proxy server automatic configuration script when automatic configuration is selected. This URL is typically the location of PAC (Proxy Auto Configuration) file.
        self._proxy_automatic_configuration_url: Optional[str] = None
        # IP Address or DNS hostname of the proxy server when manual configuration is selected.
        self._proxy_manual_address: Optional[str] = None
        # Port of the proxy server when manual configuration is selected.
        self._proxy_manual_port: Optional[int] = None
        # Wi-Fi Proxy Settings.
        self._proxy_settings: Optional[wi_fi_proxy_setting.WiFiProxySetting] = None
        # This is the name of the Wi-Fi network that is broadcast to all devices.
        self._ssid: Optional[str] = None
        # Wi-Fi Security Types.
        self._wi_fi_security_type: Optional[wi_fi_security_type.WiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosWiFiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosWiFiConfiguration()
    
    @property
    def disable_mac_address_randomization(self,) -> Optional[bool]:
        """
        Gets the disableMacAddressRandomization property value. If set to true, forces devices connecting using this Wi-Fi profile to present their actual Wi-Fi MAC address instead of a random MAC address. Applies to iOS 14 and later.
        Returns: Optional[bool]
        """
        return self._disable_mac_address_randomization
    
    @disable_mac_address_randomization.setter
    def disable_mac_address_randomization(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableMacAddressRandomization property value. If set to true, forces devices connecting using this Wi-Fi profile to present their actual Wi-Fi MAC address instead of a random MAC address. Applies to iOS 14 and later.
        Args:
            value: Value to set for the disableMacAddressRandomization property.
        """
        self._disable_mac_address_randomization = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connect_automatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connect_when_network_name_is_hidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "disable_mac_address_randomization": lambda n : setattr(self, 'disable_mac_address_randomization', n.get_bool_value()),
            "network_name": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "pre_shared_key": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "proxy_automatic_configuration_url": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxy_manual_address": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxy_manual_port": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxy_settings": lambda n : setattr(self, 'proxy_settings', n.get_enum_value(wi_fi_proxy_setting.WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wi_fi_security_type": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(wi_fi_security_type.WiFiSecurityType)),
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
            value: Value to set for the networkName property.
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
            value: Value to set for the preSharedKey property.
        """
        self._pre_shared_key = value
    
    @property
    def proxy_automatic_configuration_url(self,) -> Optional[str]:
        """
        Gets the proxyAutomaticConfigurationUrl property value. URL of the proxy server automatic configuration script when automatic configuration is selected. This URL is typically the location of PAC (Proxy Auto Configuration) file.
        Returns: Optional[str]
        """
        return self._proxy_automatic_configuration_url
    
    @proxy_automatic_configuration_url.setter
    def proxy_automatic_configuration_url(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyAutomaticConfigurationUrl property value. URL of the proxy server automatic configuration script when automatic configuration is selected. This URL is typically the location of PAC (Proxy Auto Configuration) file.
        Args:
            value: Value to set for the proxyAutomaticConfigurationUrl property.
        """
        self._proxy_automatic_configuration_url = value
    
    @property
    def proxy_manual_address(self,) -> Optional[str]:
        """
        Gets the proxyManualAddress property value. IP Address or DNS hostname of the proxy server when manual configuration is selected.
        Returns: Optional[str]
        """
        return self._proxy_manual_address
    
    @proxy_manual_address.setter
    def proxy_manual_address(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyManualAddress property value. IP Address or DNS hostname of the proxy server when manual configuration is selected.
        Args:
            value: Value to set for the proxyManualAddress property.
        """
        self._proxy_manual_address = value
    
    @property
    def proxy_manual_port(self,) -> Optional[int]:
        """
        Gets the proxyManualPort property value. Port of the proxy server when manual configuration is selected.
        Returns: Optional[int]
        """
        return self._proxy_manual_port
    
    @proxy_manual_port.setter
    def proxy_manual_port(self,value: Optional[int] = None) -> None:
        """
        Sets the proxyManualPort property value. Port of the proxy server when manual configuration is selected.
        Args:
            value: Value to set for the proxyManualPort property.
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
            value: Value to set for the proxySettings property.
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
        writer.write_bool_value("disableMacAddressRandomization", self.disable_mac_address_randomization)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
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
    def wi_fi_security_type(self,) -> Optional[wi_fi_security_type.WiFiSecurityType]:
        """
        Gets the wiFiSecurityType property value. Wi-Fi Security Types.
        Returns: Optional[wi_fi_security_type.WiFiSecurityType]
        """
        return self._wi_fi_security_type
    
    @wi_fi_security_type.setter
    def wi_fi_security_type(self,value: Optional[wi_fi_security_type.WiFiSecurityType] = None) -> None:
        """
        Sets the wiFiSecurityType property value. Wi-Fi Security Types.
        Args:
            value: Value to set for the wiFiSecurityType property.
        """
        self._wi_fi_security_type = value
    

