from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edge_home_button_configuration import EdgeHomeButtonConfiguration

from .edge_home_button_configuration import EdgeHomeButtonConfiguration

@dataclass
class EdgeHomeButtonOpensCustomURL(EdgeHomeButtonConfiguration):
    """
    Show the home button; clicking the home button loads a specific URL.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.edgeHomeButtonOpensCustomURL"
    # The specific URL to load.
    home_button_custom_u_r_l: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeHomeButtonOpensCustomURL:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeHomeButtonOpensCustomURL
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdgeHomeButtonOpensCustomURL()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .edge_home_button_configuration import EdgeHomeButtonConfiguration

        from .edge_home_button_configuration import EdgeHomeButtonConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "homeButtonCustomURL": lambda n : setattr(self, 'home_button_custom_u_r_l', n.get_str_value()),
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
        writer.write_str_value("homeButtonCustomURL", self.home_button_custom_u_r_l)
    

