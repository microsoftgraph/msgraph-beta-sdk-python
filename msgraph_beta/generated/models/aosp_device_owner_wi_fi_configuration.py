from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
    from .aosp_device_owner_wi_fi_security_type import AospDeviceOwnerWiFiSecurityType
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class AospDeviceOwnerWiFiConfiguration(DeviceConfiguration):
    """
    By providing the configurations in this profile you can instruct the AOSP device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user. This profile provides limited and simpler security types than Enterprise Wi-Fi profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.aospDeviceOwnerWiFiConfiguration"
    # Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
    connect_automatically: Optional[bool] = None
    # When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
    connect_when_network_name_is_hidden: Optional[bool] = None
    # Network Name
    network_name: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key_is_set: Optional[bool] = None
    # This is the name of the Wi-Fi network that is broadcast to all devices.
    ssid: Optional[str] = None
    # Wi-Fi Security Types for AOSP Device Owner.
    wi_fi_security_type: Optional[AospDeviceOwnerWiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AospDeviceOwnerWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AospDeviceOwnerWiFiConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration

            return AospDeviceOwnerEnterpriseWiFiConfiguration()
        return AospDeviceOwnerWiFiConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
        from .aosp_device_owner_wi_fi_security_type import AospDeviceOwnerWiFiSecurityType
        from .device_configuration import DeviceConfiguration

        from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
        from .aosp_device_owner_wi_fi_security_type import AospDeviceOwnerWiFiSecurityType
        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "preSharedKeyIsSet": lambda n : setattr(self, 'pre_shared_key_is_set', n.get_bool_value()),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wiFiSecurityType": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(AospDeviceOwnerWiFiSecurityType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("connectAutomatically", self.connect_automatically)
        writer.write_bool_value("connectWhenNetworkNameIsHidden", self.connect_when_network_name_is_hidden)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_bool_value("preSharedKeyIsSet", self.pre_shared_key_is_set)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wiFiSecurityType", self.wi_fi_security_type)
    

