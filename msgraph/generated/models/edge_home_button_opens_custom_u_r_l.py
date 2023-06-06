from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import edge_home_button_configuration

from . import edge_home_button_configuration

@dataclass
class EdgeHomeButtonOpensCustomURL(edge_home_button_configuration.EdgeHomeButtonConfiguration):
    odata_type = "#microsoft.graph.edgeHomeButtonOpensCustomURL"
    # The specific URL to load.
    home_button_custom_u_r_l: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeHomeButtonOpensCustomURL:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdgeHomeButtonOpensCustomURL
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdgeHomeButtonOpensCustomURL()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import edge_home_button_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "homeButtonCustomURL": lambda n : setattr(self, 'home_button_custom_u_r_l', n.get_str_value()),
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
        writer.write_str_value("homeButtonCustomURL", self.home_button_custom_u_r_l)
    

