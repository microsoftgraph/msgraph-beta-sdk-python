from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliant_network_type import CompliantNetworkType
    from .named_location import NamedLocation

from .named_location import NamedLocation

@dataclass
class CompliantNetworkNamedLocation(NamedLocation, Parsable):
    # The compliantNetworkType property
    compliant_network_type: Optional[CompliantNetworkType] = None
    # true if this location is explicitly trusted. Optional. Default value is false.
    is_trusted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompliantNetworkNamedLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompliantNetworkNamedLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompliantNetworkNamedLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliant_network_type import CompliantNetworkType
        from .named_location import NamedLocation

        from .compliant_network_type import CompliantNetworkType
        from .named_location import NamedLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "compliantNetworkType": lambda n : setattr(self, 'compliant_network_type', n.get_enum_value(CompliantNetworkType)),
            "isTrusted": lambda n : setattr(self, 'is_trusted', n.get_bool_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .compliant_network_type import CompliantNetworkType
        from .named_location import NamedLocation

        writer.write_enum_value("compliantNetworkType", self.compliant_network_type)
        writer.write_bool_value("isTrusted", self.is_trusted)
    

