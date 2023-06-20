from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import edge_home_button_hidden, edge_home_button_loads_start_page, edge_home_button_opens_custom_u_r_l, edge_home_button_opens_new_tab

@dataclass
class EdgeHomeButtonConfiguration(AdditionalDataHolder, Parsable):
    """
    The home button configuration base class used to identify the available options
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeHomeButtonConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdgeHomeButtonConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonHidden".casefold():
            from . import edge_home_button_hidden

            return edge_home_button_hidden.EdgeHomeButtonHidden()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonLoadsStartPage".casefold():
            from . import edge_home_button_loads_start_page

            return edge_home_button_loads_start_page.EdgeHomeButtonLoadsStartPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonOpensCustomURL".casefold():
            from . import edge_home_button_opens_custom_u_r_l

            return edge_home_button_opens_custom_u_r_l.EdgeHomeButtonOpensCustomURL()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonOpensNewTab".casefold():
            from . import edge_home_button_opens_new_tab

            return edge_home_button_opens_new_tab.EdgeHomeButtonOpensNewTab()
        return EdgeHomeButtonConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import edge_home_button_hidden, edge_home_button_loads_start_page, edge_home_button_opens_custom_u_r_l, edge_home_button_opens_new_tab

        from . import edge_home_button_hidden, edge_home_button_loads_start_page, edge_home_button_opens_custom_u_r_l, edge_home_button_opens_new_tab

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

