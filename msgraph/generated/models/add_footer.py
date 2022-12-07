from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alignment = lazy_import('msgraph.generated.models.alignment')
mark_content = lazy_import('msgraph.generated.models.mark_content')

class AddFooter(mark_content.MarkContent):
    @property
    def alignment(self,) -> Optional[alignment.Alignment]:
        """
        Gets the alignment property value. The alignment property
        Returns: Optional[alignment.Alignment]
        """
        return self._alignment
    
    @alignment.setter
    def alignment(self,value: Optional[alignment.Alignment] = None) -> None:
        """
        Sets the alignment property value. The alignment property
        Args:
            value: Value to set for the alignment property.
        """
        self._alignment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AddFooter and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.addFooter"
        # The alignment property
        self._alignment: Optional[alignment.Alignment] = None
        # The margin property
        self._margin: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddFooter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddFooter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddFooter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alignment": lambda n : setattr(self, 'alignment', n.get_enum_value(alignment.Alignment)),
            "margin": lambda n : setattr(self, 'margin', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def margin(self,) -> Optional[int]:
        """
        Gets the margin property value. The margin property
        Returns: Optional[int]
        """
        return self._margin
    
    @margin.setter
    def margin(self,value: Optional[int] = None) -> None:
        """
        Sets the margin property value. The margin property
        Args:
            value: Value to set for the margin property.
        """
        self._margin = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("alignment", self.alignment)
        writer.write_int_value("margin", self.margin)
    

