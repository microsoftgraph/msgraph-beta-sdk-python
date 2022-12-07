from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mark_content = lazy_import('msgraph.generated.models.mark_content')
page_orientation = lazy_import('msgraph.generated.models.page_orientation')

class AddWatermark(mark_content.MarkContent):
    def __init__(self,) -> None:
        """
        Instantiates a new AddWatermark and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.addWatermark"
        # The orientation property
        self._orientation: Optional[page_orientation.PageOrientation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddWatermark:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddWatermark
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddWatermark()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(page_orientation.PageOrientation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def orientation(self,) -> Optional[page_orientation.PageOrientation]:
        """
        Gets the orientation property value. The orientation property
        Returns: Optional[page_orientation.PageOrientation]
        """
        return self._orientation
    
    @orientation.setter
    def orientation(self,value: Optional[page_orientation.PageOrientation] = None) -> None:
        """
        Sets the orientation property value. The orientation property
        Args:
            value: Value to set for the orientation property.
        """
        self._orientation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("orientation", self.orientation)
    

