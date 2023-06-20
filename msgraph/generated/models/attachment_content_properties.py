from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_properties, current_label

from . import content_properties

@dataclass
class AttachmentContentProperties(content_properties.ContentProperties):
    odata_type = "#microsoft.graph.attachmentContentProperties"
    # The currentLabel property
    current_label: Optional[current_label.CurrentLabel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttachmentContentProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentContentProperties
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttachmentContentProperties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_properties, current_label

        from . import content_properties, current_label

        fields: Dict[str, Callable[[Any], None]] = {
            "currentLabel": lambda n : setattr(self, 'current_label', n.get_object_value(current_label.CurrentLabel)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("currentLabel", self.current_label)
    

