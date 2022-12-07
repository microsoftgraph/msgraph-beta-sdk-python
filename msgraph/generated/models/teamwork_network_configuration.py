from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkNetworkConfiguration(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkNetworkConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The default gateway is the path used to pass information when the destination is unknown to the device.
        self._default_gateway: Optional[str] = None
        # The network domain of the device, for example, contoso.com.
        self._domain_name: Optional[str] = None
        # The device name on a network.
        self._host_name: Optional[str] = None
        # The IP address is a numerical label that uniquely identifies every device connected to the internet.
        self._ip_address: Optional[str] = None
        # True if DHCP is enabled.
        self._is_dhcp_enabled: Optional[bool] = None
        # True if the PC port is enabled.
        self._is_p_c_port_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A primary DNS is the first point of contact for a device that translates the hostname into an IP address.
        self._primary_dns: Optional[str] = None
        # A secondary DNS is used when the primary DNS is not available.
        self._secondary_dns: Optional[str] = None
        # A subnet mask is a number that distinguishes the network address and the host address within an IP address.
        self._subnet_mask: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkNetworkConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkNetworkConfiguration()
    
    @property
    def default_gateway(self,) -> Optional[str]:
        """
        Gets the defaultGateway property value. The default gateway is the path used to pass information when the destination is unknown to the device.
        Returns: Optional[str]
        """
        return self._default_gateway
    
    @default_gateway.setter
    def default_gateway(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultGateway property value. The default gateway is the path used to pass information when the destination is unknown to the device.
        Args:
            value: Value to set for the defaultGateway property.
        """
        self._default_gateway = value
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. The network domain of the device, for example, contoso.com.
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. The network domain of the device, for example, contoso.com.
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_gateway": lambda n : setattr(self, 'default_gateway', n.get_str_value()),
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "host_name": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "is_dhcp_enabled": lambda n : setattr(self, 'is_dhcp_enabled', n.get_bool_value()),
            "is_p_c_port_enabled": lambda n : setattr(self, 'is_p_c_port_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primary_dns": lambda n : setattr(self, 'primary_dns', n.get_str_value()),
            "secondary_dns": lambda n : setattr(self, 'secondary_dns', n.get_str_value()),
            "subnet_mask": lambda n : setattr(self, 'subnet_mask', n.get_str_value()),
        }
        return fields
    
    @property
    def host_name(self,) -> Optional[str]:
        """
        Gets the hostName property value. The device name on a network.
        Returns: Optional[str]
        """
        return self._host_name
    
    @host_name.setter
    def host_name(self,value: Optional[str] = None) -> None:
        """
        Sets the hostName property value. The device name on a network.
        Args:
            value: Value to set for the hostName property.
        """
        self._host_name = value
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. The IP address is a numerical label that uniquely identifies every device connected to the internet.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. The IP address is a numerical label that uniquely identifies every device connected to the internet.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def is_dhcp_enabled(self,) -> Optional[bool]:
        """
        Gets the isDhcpEnabled property value. True if DHCP is enabled.
        Returns: Optional[bool]
        """
        return self._is_dhcp_enabled
    
    @is_dhcp_enabled.setter
    def is_dhcp_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDhcpEnabled property value. True if DHCP is enabled.
        Args:
            value: Value to set for the isDhcpEnabled property.
        """
        self._is_dhcp_enabled = value
    
    @property
    def is_p_c_port_enabled(self,) -> Optional[bool]:
        """
        Gets the isPCPortEnabled property value. True if the PC port is enabled.
        Returns: Optional[bool]
        """
        return self._is_p_c_port_enabled
    
    @is_p_c_port_enabled.setter
    def is_p_c_port_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPCPortEnabled property value. True if the PC port is enabled.
        Args:
            value: Value to set for the isPCPortEnabled property.
        """
        self._is_p_c_port_enabled = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def primary_dns(self,) -> Optional[str]:
        """
        Gets the primaryDns property value. A primary DNS is the first point of contact for a device that translates the hostname into an IP address.
        Returns: Optional[str]
        """
        return self._primary_dns
    
    @primary_dns.setter
    def primary_dns(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryDns property value. A primary DNS is the first point of contact for a device that translates the hostname into an IP address.
        Args:
            value: Value to set for the primaryDns property.
        """
        self._primary_dns = value
    
    @property
    def secondary_dns(self,) -> Optional[str]:
        """
        Gets the secondaryDns property value. A secondary DNS is used when the primary DNS is not available.
        Returns: Optional[str]
        """
        return self._secondary_dns
    
    @secondary_dns.setter
    def secondary_dns(self,value: Optional[str] = None) -> None:
        """
        Sets the secondaryDns property value. A secondary DNS is used when the primary DNS is not available.
        Args:
            value: Value to set for the secondaryDns property.
        """
        self._secondary_dns = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("defaultGateway", self.default_gateway)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("hostName", self.host_name)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isDhcpEnabled", self.is_dhcp_enabled)
        writer.write_bool_value("isPCPortEnabled", self.is_p_c_port_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("primaryDns", self.primary_dns)
        writer.write_str_value("secondaryDns", self.secondary_dns)
        writer.write_str_value("subnetMask", self.subnet_mask)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subnet_mask(self,) -> Optional[str]:
        """
        Gets the subnetMask property value. A subnet mask is a number that distinguishes the network address and the host address within an IP address.
        Returns: Optional[str]
        """
        return self._subnet_mask
    
    @subnet_mask.setter
    def subnet_mask(self,value: Optional[str] = None) -> None:
        """
        Sets the subnetMask property value. A subnet mask is a number that distinguishes the network address and the host address within an IP address.
        Args:
            value: Value to set for the subnetMask property.
        """
        self._subnet_mask = value
    

