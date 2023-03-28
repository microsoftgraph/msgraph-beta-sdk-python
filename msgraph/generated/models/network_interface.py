from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class NetworkInterface(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new networkInterface and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Description of the NIC (e.g. Ethernet adapter, Wireless LAN adapter Local Area Connection, and so on).
        self._description: Optional[str] = None
        # Last IPv4 address associated with this NIC.
        self._ip_v4_address: Optional[str] = None
        # Last Public (aka global) IPv6 address associated with this NIC.
        self._ip_v6_address: Optional[str] = None
        # Last local (link-local or site-local) IPv6 address associated with this NIC.
        self._local_ip_v6_address: Optional[str] = None
        # MAC address of the NIC on this host.
        self._mac_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkInterface:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NetworkInterface
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NetworkInterface()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the NIC (e.g. Ethernet adapter, Wireless LAN adapter Local Area Connection, and so on).
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the NIC (e.g. Ethernet adapter, Wireless LAN adapter Local Area Connection, and so on).
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "ipV4Address": lambda n : setattr(self, 'ip_v4_address', n.get_str_value()),
            "ipV6Address": lambda n : setattr(self, 'ip_v6_address', n.get_str_value()),
            "localIpV6Address": lambda n : setattr(self, 'local_ip_v6_address', n.get_str_value()),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def ip_v4_address(self,) -> Optional[str]:
        """
        Gets the ipV4Address property value. Last IPv4 address associated with this NIC.
        Returns: Optional[str]
        """
        return self._ip_v4_address
    
    @ip_v4_address.setter
    def ip_v4_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipV4Address property value. Last IPv4 address associated with this NIC.
        Args:
            value: Value to set for the ip_v4_address property.
        """
        self._ip_v4_address = value
    
    @property
    def ip_v6_address(self,) -> Optional[str]:
        """
        Gets the ipV6Address property value. Last Public (aka global) IPv6 address associated with this NIC.
        Returns: Optional[str]
        """
        return self._ip_v6_address
    
    @ip_v6_address.setter
    def ip_v6_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipV6Address property value. Last Public (aka global) IPv6 address associated with this NIC.
        Args:
            value: Value to set for the ip_v6_address property.
        """
        self._ip_v6_address = value
    
    @property
    def local_ip_v6_address(self,) -> Optional[str]:
        """
        Gets the localIpV6Address property value. Last local (link-local or site-local) IPv6 address associated with this NIC.
        Returns: Optional[str]
        """
        return self._local_ip_v6_address
    
    @local_ip_v6_address.setter
    def local_ip_v6_address(self,value: Optional[str] = None) -> None:
        """
        Sets the localIpV6Address property value. Last local (link-local or site-local) IPv6 address associated with this NIC.
        Args:
            value: Value to set for the local_ip_v6_address property.
        """
        self._local_ip_v6_address = value
    
    @property
    def mac_address(self,) -> Optional[str]:
        """
        Gets the macAddress property value. MAC address of the NIC on this host.
        Returns: Optional[str]
        """
        return self._mac_address
    
    @mac_address.setter
    def mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the macAddress property value. MAC address of the NIC on this host.
        Args:
            value: Value to set for the mac_address property.
        """
        self._mac_address = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("ipV4Address", self.ip_v4_address)
        writer.write_str_value("ipV6Address", self.ip_v6_address)
        writer.write_str_value("localIpV6Address", self.local_ip_v6_address)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

