from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import autonomous_system, host

from . import host

class IpAddress(host.Host):
    def __init__(self,) -> None:
        """
        Instantiates a new IpAddress and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ipAddress"
        # The details about the autonomous system to which this IP address belongs.
        self._autonomous_system: Optional[autonomous_system.AutonomousSystem] = None
        # The country or region for this IP address.
        self._country_or_region: Optional[str] = None
        # The hosting company listed for this host.
        self._hosting_provider: Optional[str] = None
        # The block of IP addresses this IP address belongs to.
        self._netblock: Optional[str] = None
    
    @property
    def autonomous_system(self,) -> Optional[autonomous_system.AutonomousSystem]:
        """
        Gets the autonomousSystem property value. The details about the autonomous system to which this IP address belongs.
        Returns: Optional[autonomous_system.AutonomousSystem]
        """
        return self._autonomous_system
    
    @autonomous_system.setter
    def autonomous_system(self,value: Optional[autonomous_system.AutonomousSystem] = None) -> None:
        """
        Sets the autonomousSystem property value. The details about the autonomous system to which this IP address belongs.
        Args:
            value: Value to set for the autonomous_system property.
        """
        self._autonomous_system = value
    
    @property
    def country_or_region(self,) -> Optional[str]:
        """
        Gets the countryOrRegion property value. The country or region for this IP address.
        Returns: Optional[str]
        """
        return self._country_or_region
    
    @country_or_region.setter
    def country_or_region(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegion property value. The country or region for this IP address.
        Args:
            value: Value to set for the country_or_region property.
        """
        self._country_or_region = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import autonomous_system, host

        fields: Dict[str, Callable[[Any], None]] = {
            "autonomousSystem": lambda n : setattr(self, 'autonomous_system', n.get_object_value(autonomous_system.AutonomousSystem)),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "hostingProvider": lambda n : setattr(self, 'hosting_provider', n.get_str_value()),
            "netblock": lambda n : setattr(self, 'netblock', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hosting_provider(self,) -> Optional[str]:
        """
        Gets the hostingProvider property value. The hosting company listed for this host.
        Returns: Optional[str]
        """
        return self._hosting_provider
    
    @hosting_provider.setter
    def hosting_provider(self,value: Optional[str] = None) -> None:
        """
        Sets the hostingProvider property value. The hosting company listed for this host.
        Args:
            value: Value to set for the hosting_provider property.
        """
        self._hosting_provider = value
    
    @property
    def netblock(self,) -> Optional[str]:
        """
        Gets the netblock property value. The block of IP addresses this IP address belongs to.
        Returns: Optional[str]
        """
        return self._netblock
    
    @netblock.setter
    def netblock(self,value: Optional[str] = None) -> None:
        """
        Sets the netblock property value. The block of IP addresses this IP address belongs to.
        Args:
            value: Value to set for the netblock property.
        """
        self._netblock = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("autonomousSystem", self.autonomous_system)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_str_value("hostingProvider", self.hosting_provider)
        writer.write_str_value("netblock", self.netblock)
    

