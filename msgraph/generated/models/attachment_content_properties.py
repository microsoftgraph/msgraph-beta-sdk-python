from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_properties = lazy_import('msgraph.generated.models.content_properties')
current_label = lazy_import('msgraph.generated.models.current_label')

class AttachmentContentProperties(content_properties.ContentProperties):
    def __init__(self,) -> None:
        """
        Instantiates a new AttachmentContentProperties and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.attachmentContentProperties"
        # The currentLabel property
        self._current_label: Optional[current_label.CurrentLabel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttachmentContentProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentContentProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttachmentContentProperties()
    
    @property
    def current_label(self,) -> Optional[current_label.CurrentLabel]:
        """
        Gets the currentLabel property value. The currentLabel property
        Returns: Optional[current_label.CurrentLabel]
        """
        return self._current_label
    
    @current_label.setter
    def current_label(self,value: Optional[current_label.CurrentLabel] = None) -> None:
        """
        Sets the currentLabel property value. The currentLabel property
        Args:
            value: Value to set for the currentLabel property.
        """
        self._current_label = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "current_label": lambda n : setattr(self, 'current_label', n.get_object_value(current_label.CurrentLabel)),
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
        writer.write_object_value("currentLabel", self.current_label)
    

