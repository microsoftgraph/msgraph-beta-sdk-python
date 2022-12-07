from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_wi_fi_security_type = lazy_import('msgraph.generated.models.android_wi_fi_security_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class AndroidWiFiConfiguration(device_configuration.DeviceConfiguration):
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
        Gets the connectWhenNetworkNameIsHidden property value. When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        Returns: Optional[bool]
        """
        return self._connect_when_network_name_is_hidden
    
    @connect_when_network_name_is_hidden.setter
    def connect_when_network_name_is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectWhenNetworkNameIsHidden property value. When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        Args:
            value: Value to set for the connectWhenNetworkNameIsHidden property.
        """
        self._connect_when_network_name_is_hidden = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidWiFiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidWiFiConfiguration"
        # Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
        self._connect_automatically: Optional[bool] = None
        # When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
        self._connect_when_network_name_is_hidden: Optional[bool] = None
        # Network Name
        self._network_name: Optional[str] = None
        # This is the name of the Wi-Fi network that is broadcast to all devices.
        self._ssid: Optional[str] = None
        # Wi-Fi Security Types for Android.
        self._wi_fi_security_type: Optional[android_wi_fi_security_type.AndroidWiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWiFiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidWiFiConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connect_automatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connect_when_network_name_is_hidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "network_name": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wi_fi_security_type": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(android_wi_fi_security_type.AndroidWiFiSecurityType)),
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
    def wi_fi_security_type(self,) -> Optional[android_wi_fi_security_type.AndroidWiFiSecurityType]:
        """
        Gets the wiFiSecurityType property value. Wi-Fi Security Types for Android.
        Returns: Optional[android_wi_fi_security_type.AndroidWiFiSecurityType]
        """
        return self._wi_fi_security_type
    
    @wi_fi_security_type.setter
    def wi_fi_security_type(self,value: Optional[android_wi_fi_security_type.AndroidWiFiSecurityType] = None) -> None:
        """
        Sets the wiFiSecurityType property value. Wi-Fi Security Types for Android.
        Args:
            value: Value to set for the wiFiSecurityType property.
        """
        self._wi_fi_security_type = value
    

