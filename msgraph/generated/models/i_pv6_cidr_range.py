from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ip_range

from . import ip_range

class IPv6CidrRange(ip_range.IpRange):
    def __init__(self,) -> None:
        """
        Instantiates a new IPv6CidrRange and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iPv6CidrRange"
        # IPv6 address in CIDR notation. Not nullable.
        self._cidr_address: Optional[str] = None
    
    @property
    def cidr_address(self,) -> Optional[str]:
        """
        Gets the cidrAddress property value. IPv6 address in CIDR notation. Not nullable.
        Returns: Optional[str]
        """
        return self._cidr_address
    
    @cidr_address.setter
    def cidr_address(self,value: Optional[str] = None) -> None:
        """
        Sets the cidrAddress property value. IPv6 address in CIDR notation. Not nullable.
        Args:
            value: Value to set for the cidr_address property.
        """
        self._cidr_address = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IPv6CidrRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IPv6CidrRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IPv6CidrRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ip_range

        fields: Dict[str, Callable[[Any], None]] = {
            "cidrAddress": lambda n : setattr(self, 'cidr_address', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("cidrAddress", self.cidr_address)
    

