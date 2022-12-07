from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
internet_explorer_mode = lazy_import('msgraph.generated.models.internet_explorer_mode')

class Edge(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new edge and sets the default values.
        """
        super().__init__()
        # A container for Internet Explorer mode resources.
        self._internet_explorer_mode: Optional[internet_explorer_mode.InternetExplorerMode] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Edge:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Edge
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Edge()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "internet_explorer_mode": lambda n : setattr(self, 'internet_explorer_mode', n.get_object_value(internet_explorer_mode.InternetExplorerMode)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internet_explorer_mode(self,) -> Optional[internet_explorer_mode.InternetExplorerMode]:
        """
        Gets the internetExplorerMode property value. A container for Internet Explorer mode resources.
        Returns: Optional[internet_explorer_mode.InternetExplorerMode]
        """
        return self._internet_explorer_mode
    
    @internet_explorer_mode.setter
    def internet_explorer_mode(self,value: Optional[internet_explorer_mode.InternetExplorerMode] = None) -> None:
        """
        Sets the internetExplorerMode property value. A container for Internet Explorer mode resources.
        Args:
            value: Value to set for the internetExplorerMode property.
        """
        self._internet_explorer_mode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("internetExplorerMode", self.internet_explorer_mode)
    

