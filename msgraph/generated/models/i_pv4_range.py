from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ip_range

from . import ip_range

class IPv4Range(ip_range.IpRange):
    def __init__(self,) -> None:
        """
        Instantiates a new IPv4Range and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iPv4Range"
        # Lower address.
        self._lower_address: Optional[str] = None
        # Upper address.
        self._upper_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IPv4Range:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IPv4Range
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IPv4Range()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ip_range

        fields: Dict[str, Callable[[Any], None]] = {
            "lowerAddress": lambda n : setattr(self, 'lower_address', n.get_str_value()),
            "upperAddress": lambda n : setattr(self, 'upper_address', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def lower_address(self,) -> Optional[str]:
        """
        Gets the lowerAddress property value. Lower address.
        Returns: Optional[str]
        """
        return self._lower_address
    
    @lower_address.setter
    def lower_address(self,value: Optional[str] = None) -> None:
        """
        Sets the lowerAddress property value. Lower address.
        Args:
            value: Value to set for the lower_address property.
        """
        self._lower_address = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("lowerAddress", self.lower_address)
        writer.write_str_value("upperAddress", self.upper_address)
    
    @property
    def upper_address(self,) -> Optional[str]:
        """
        Gets the upperAddress property value. Upper address.
        Returns: Optional[str]
        """
        return self._upper_address
    
    @upper_address.setter
    def upper_address(self,value: Optional[str] = None) -> None:
        """
        Sets the upperAddress property value. Upper address.
        Args:
            value: Value to set for the upper_address property.
        """
        self._upper_address = value
    

