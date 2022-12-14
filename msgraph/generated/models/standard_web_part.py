from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

web_part = lazy_import('msgraph.generated.models.web_part')
web_part_data = lazy_import('msgraph.generated.models.web_part_data')

class StandardWebPart(web_part.WebPart):
    def __init__(self,) -> None:
        """
        Instantiates a new StandardWebPart and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.standardWebPart"
        # Data of the webPart.
        self._data: Optional[web_part_data.WebPartData] = None
        # A Guid which indicates the type of the webParts
        self._web_part_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StandardWebPart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StandardWebPart
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StandardWebPart()
    
    @property
    def data(self,) -> Optional[web_part_data.WebPartData]:
        """
        Gets the data property value. Data of the webPart.
        Returns: Optional[web_part_data.WebPartData]
        """
        return self._data
    
    @data.setter
    def data(self,value: Optional[web_part_data.WebPartData] = None) -> None:
        """
        Sets the data property value. Data of the webPart.
        Args:
            value: Value to set for the data property.
        """
        self._data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(web_part_data.WebPartData)),
            "web_part_type": lambda n : setattr(self, 'web_part_type', n.get_str_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_str_value("webPartType", self.web_part_type)
    
    @property
    def web_part_type(self,) -> Optional[str]:
        """
        Gets the webPartType property value. A Guid which indicates the type of the webParts
        Returns: Optional[str]
        """
        return self._web_part_type
    
    @web_part_type.setter
    def web_part_type(self,value: Optional[str] = None) -> None:
        """
        Sets the webPartType property value. A Guid which indicates the type of the webParts
        Args:
            value: Value to set for the webPartType property.
        """
        self._web_part_type = value
    

