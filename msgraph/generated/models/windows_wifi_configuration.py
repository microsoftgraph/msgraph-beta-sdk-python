from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
metered_connection_limit_type = lazy_import('msgraph.generated.models.metered_connection_limit_type')
wi_fi_proxy_setting = lazy_import('msgraph.generated.models.wi_fi_proxy_setting')
wi_fi_security_type = lazy_import('msgraph.generated.models.wi_fi_security_type')

class WindowsWifiConfiguration(device_configuration.DeviceConfiguration):
    @property
    def connect_automatically(self,) -> Optional[bool]:
        """
        Gets the connectAutomatically property value. Specify whether the wifi connection should connect automatically when in range.
        Returns: Optional[bool]
        """
        return self._connect_automatically
    
    @connect_automatically.setter
    def connect_automatically(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectAutomatically property value. Specify whether the wifi connection should connect automatically when in range.
        Args:
            value: Value to set for the connectAutomatically property.
        """
        self._connect_automatically = value
    
    @property
    def connect_to_preferred_network(self,) -> Optional[bool]:
        """
        Gets the connectToPreferredNetwork property value. Specify whether the wifi connection should connect to more preferred networks when already connected to this one.  Requires ConnectAutomatically to be true.
        Returns: Optional[bool]
        """
        return self._connect_to_preferred_network
    
    @connect_to_preferred_network.setter
    def connect_to_preferred_network(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectToPreferredNetwork property value. Specify whether the wifi connection should connect to more preferred networks when already connected to this one.  Requires ConnectAutomatically to be true.
        Args:
            value: Value to set for the connectToPreferredNetwork property.
        """
        self._connect_to_preferred_network = value
    
    @property
    def connect_when_network_name_is_hidden(self,) -> Optional[bool]:
        """
        Gets the connectWhenNetworkNameIsHidden property value. Specify whether the wifi connection should connect automatically even when the SSID is not broadcasting.
        Returns: Optional[bool]
        """
        return self._connect_when_network_name_is_hidden
    
    @connect_when_network_name_is_hidden.setter
    def connect_when_network_name_is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectWhenNetworkNameIsHidden property value. Specify whether the wifi connection should connect automatically even when the SSID is not broadcasting.
        Args:
            value: Value to set for the connectWhenNetworkNameIsHidden property.
        """
        self._connect_when_network_name_is_hidden = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsWifiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsWifiConfiguration"
        # Specify whether the wifi connection should connect automatically when in range.
        self._connect_automatically: Optional[bool] = None
        # Specify whether the wifi connection should connect to more preferred networks when already connected to this one.  Requires ConnectAutomatically to be true.
        self._connect_to_preferred_network: Optional[bool] = None
        # Specify whether the wifi connection should connect automatically even when the SSID is not broadcasting.
        self._connect_when_network_name_is_hidden: Optional[bool] = None
        # Specify whether to force FIPS compliance.
        self._force_f_i_p_s_compliance: Optional[bool] = None
        # Specify the metered connection limit type for the wifi connection. Possible values are: unrestricted, fixed, variable.
        self._metered_connection_limit: Optional[metered_connection_limit_type.MeteredConnectionLimitType] = None
        # Specify the network configuration name.
        self._network_name: Optional[str] = None
        # This is the pre-shared key for WPA Personal Wi-Fi network.
        self._pre_shared_key: Optional[str] = None
        # Specify the URL for the proxy server configuration script.
        self._proxy_automatic_configuration_url: Optional[str] = None
        # Specify the IP address for the proxy server.
        self._proxy_manual_address: Optional[str] = None
        # Specify the port for the proxy server.
        self._proxy_manual_port: Optional[int] = None
        # Specify the proxy setting for Wi-Fi configuration. Possible values are: none, manual, automatic.
        self._proxy_setting: Optional[wi_fi_proxy_setting.WiFiProxySetting] = None
        # Specify the SSID of the wifi connection.
        self._ssid: Optional[str] = None
        # Specify the Wifi Security Type. Possible values are: open, wpaPersonal, wpaEnterprise, wep, wpa2Personal, wpa2Enterprise.
        self._wifi_security_type: Optional[wi_fi_security_type.WiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsWifiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWifiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsWifiConfiguration()
    
    @property
    def force_f_i_p_s_compliance(self,) -> Optional[bool]:
        """
        Gets the forceFIPSCompliance property value. Specify whether to force FIPS compliance.
        Returns: Optional[bool]
        """
        return self._force_f_i_p_s_compliance
    
    @force_f_i_p_s_compliance.setter
    def force_f_i_p_s_compliance(self,value: Optional[bool] = None) -> None:
        """
        Sets the forceFIPSCompliance property value. Specify whether to force FIPS compliance.
        Args:
            value: Value to set for the forceFIPSCompliance property.
        """
        self._force_f_i_p_s_compliance = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connect_automatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connect_to_preferred_network": lambda n : setattr(self, 'connect_to_preferred_network', n.get_bool_value()),
            "connect_when_network_name_is_hidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "force_f_i_p_s_compliance": lambda n : setattr(self, 'force_f_i_p_s_compliance', n.get_bool_value()),
            "metered_connection_limit": lambda n : setattr(self, 'metered_connection_limit', n.get_enum_value(metered_connection_limit_type.MeteredConnectionLimitType)),
            "network_name": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "pre_shared_key": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "proxy_automatic_configuration_url": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxy_manual_address": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxy_manual_port": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxy_setting": lambda n : setattr(self, 'proxy_setting', n.get_enum_value(wi_fi_proxy_setting.WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wifi_security_type": lambda n : setattr(self, 'wifi_security_type', n.get_enum_value(wi_fi_security_type.WiFiSecurityType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def metered_connection_limit(self,) -> Optional[metered_connection_limit_type.MeteredConnectionLimitType]:
        """
        Gets the meteredConnectionLimit property value. Specify the metered connection limit type for the wifi connection. Possible values are: unrestricted, fixed, variable.
        Returns: Optional[metered_connection_limit_type.MeteredConnectionLimitType]
        """
        return self._metered_connection_limit
    
    @metered_connection_limit.setter
    def metered_connection_limit(self,value: Optional[metered_connection_limit_type.MeteredConnectionLimitType] = None) -> None:
        """
        Sets the meteredConnectionLimit property value. Specify the metered connection limit type for the wifi connection. Possible values are: unrestricted, fixed, variable.
        Args:
            value: Value to set for the meteredConnectionLimit property.
        """
        self._metered_connection_limit = value
    
    @property
    def network_name(self,) -> Optional[str]:
        """
        Gets the networkName property value. Specify the network configuration name.
        Returns: Optional[str]
        """
        return self._network_name
    
    @network_name.setter
    def network_name(self,value: Optional[str] = None) -> None:
        """
        Sets the networkName property value. Specify the network configuration name.
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
        Gets the proxyAutomaticConfigurationUrl property value. Specify the URL for the proxy server configuration script.
        Returns: Optional[str]
        """
        return self._proxy_automatic_configuration_url
    
    @proxy_automatic_configuration_url.setter
    def proxy_automatic_configuration_url(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyAutomaticConfigurationUrl property value. Specify the URL for the proxy server configuration script.
        Args:
            value: Value to set for the proxyAutomaticConfigurationUrl property.
        """
        self._proxy_automatic_configuration_url = value
    
    @property
    def proxy_manual_address(self,) -> Optional[str]:
        """
        Gets the proxyManualAddress property value. Specify the IP address for the proxy server.
        Returns: Optional[str]
        """
        return self._proxy_manual_address
    
    @proxy_manual_address.setter
    def proxy_manual_address(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyManualAddress property value. Specify the IP address for the proxy server.
        Args:
            value: Value to set for the proxyManualAddress property.
        """
        self._proxy_manual_address = value
    
    @property
    def proxy_manual_port(self,) -> Optional[int]:
        """
        Gets the proxyManualPort property value. Specify the port for the proxy server.
        Returns: Optional[int]
        """
        return self._proxy_manual_port
    
    @proxy_manual_port.setter
    def proxy_manual_port(self,value: Optional[int] = None) -> None:
        """
        Sets the proxyManualPort property value. Specify the port for the proxy server.
        Args:
            value: Value to set for the proxyManualPort property.
        """
        self._proxy_manual_port = value
    
    @property
    def proxy_setting(self,) -> Optional[wi_fi_proxy_setting.WiFiProxySetting]:
        """
        Gets the proxySetting property value. Specify the proxy setting for Wi-Fi configuration. Possible values are: none, manual, automatic.
        Returns: Optional[wi_fi_proxy_setting.WiFiProxySetting]
        """
        return self._proxy_setting
    
    @proxy_setting.setter
    def proxy_setting(self,value: Optional[wi_fi_proxy_setting.WiFiProxySetting] = None) -> None:
        """
        Sets the proxySetting property value. Specify the proxy setting for Wi-Fi configuration. Possible values are: none, manual, automatic.
        Args:
            value: Value to set for the proxySetting property.
        """
        self._proxy_setting = value
    
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
        writer.write_bool_value("connectToPreferredNetwork", self.connect_to_preferred_network)
        writer.write_bool_value("connectWhenNetworkNameIsHidden", self.connect_when_network_name_is_hidden)
        writer.write_bool_value("forceFIPSCompliance", self.force_f_i_p_s_compliance)
        writer.write_enum_value("meteredConnectionLimit", self.metered_connection_limit)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_str_value("proxyManualAddress", self.proxy_manual_address)
        writer.write_int_value("proxyManualPort", self.proxy_manual_port)
        writer.write_enum_value("proxySetting", self.proxy_setting)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wifiSecurityType", self.wifi_security_type)
    
    @property
    def ssid(self,) -> Optional[str]:
        """
        Gets the ssid property value. Specify the SSID of the wifi connection.
        Returns: Optional[str]
        """
        return self._ssid
    
    @ssid.setter
    def ssid(self,value: Optional[str] = None) -> None:
        """
        Sets the ssid property value. Specify the SSID of the wifi connection.
        Args:
            value: Value to set for the ssid property.
        """
        self._ssid = value
    
    @property
    def wifi_security_type(self,) -> Optional[wi_fi_security_type.WiFiSecurityType]:
        """
        Gets the wifiSecurityType property value. Specify the Wifi Security Type. Possible values are: open, wpaPersonal, wpaEnterprise, wep, wpa2Personal, wpa2Enterprise.
        Returns: Optional[wi_fi_security_type.WiFiSecurityType]
        """
        return self._wifi_security_type
    
    @wifi_security_type.setter
    def wifi_security_type(self,value: Optional[wi_fi_security_type.WiFiSecurityType] = None) -> None:
        """
        Sets the wifiSecurityType property value. Specify the Wifi Security Type. Possible values are: open, wpaPersonal, wpaEnterprise, wep, wpa2Personal, wpa2Enterprise.
        Args:
            value: Value to set for the wifiSecurityType property.
        """
        self._wifi_security_type = value
    

