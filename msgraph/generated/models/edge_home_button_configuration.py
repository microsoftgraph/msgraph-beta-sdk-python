from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import edge_home_button_hidden, edge_home_button_loads_start_page, edge_home_button_opens_custom_u_r_l, edge_home_button_opens_new_tab

class EdgeHomeButtonConfiguration(AdditionalDataHolder, Parsable):
    """
    The home button configuration base class used to identify the available options
    """
    def __init__(self,) -> None:
        """
        Instantiates a new edgeHomeButtonConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeHomeButtonConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdgeHomeButtonConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.edgeHomeButtonHidden":
                from . import edge_home_button_hidden

                return edge_home_button_hidden.EdgeHomeButtonHidden()
            if mapping_value == "#microsoft.graph.edgeHomeButtonLoadsStartPage":
                from . import edge_home_button_loads_start_page

                return edge_home_button_loads_start_page.EdgeHomeButtonLoadsStartPage()
            if mapping_value == "#microsoft.graph.edgeHomeButtonOpensCustomURL":
                from . import edge_home_button_opens_custom_u_r_l

                return edge_home_button_opens_custom_u_r_l.EdgeHomeButtonOpensCustomURL()
            if mapping_value == "#microsoft.graph.edgeHomeButtonOpensNewTab":
                from . import edge_home_button_opens_new_tab

                return edge_home_button_opens_new_tab.EdgeHomeButtonOpensNewTab()
        return EdgeHomeButtonConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import edge_home_button_hidden, edge_home_button_loads_start_page, edge_home_button_opens_custom_u_r_l, edge_home_button_opens_new_tab

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

