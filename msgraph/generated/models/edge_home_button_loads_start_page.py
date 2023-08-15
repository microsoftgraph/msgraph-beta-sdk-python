from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edge_home_button_configuration import EdgeHomeButtonConfiguration

from .edge_home_button_configuration import EdgeHomeButtonConfiguration

@dataclass
class EdgeHomeButtonLoadsStartPage(EdgeHomeButtonConfiguration):
    """
    Show the home button; clicking the home button loads the Start page - this is also the default value.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.edgeHomeButtonLoadsStartPage"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeHomeButtonLoadsStartPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeHomeButtonLoadsStartPage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdgeHomeButtonLoadsStartPage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .edge_home_button_configuration import EdgeHomeButtonConfiguration

        from .edge_home_button_configuration import EdgeHomeButtonConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
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
    

