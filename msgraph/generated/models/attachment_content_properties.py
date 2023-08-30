from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_properties import ContentProperties
    from .current_label import CurrentLabel
    from .discovered_sensitive_type import DiscoveredSensitiveType

from .content_properties import ContentProperties

@dataclass
class AttachmentContentProperties(ContentProperties):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.attachmentContentProperties"
    # The currentLabel property
    current_label: Optional[CurrentLabel] = None
    # The discoveredSensitiveTypes property
    discovered_sensitive_types: Optional[List[DiscoveredSensitiveType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttachmentContentProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .content_properties import ContentProperties
        from .current_label import CurrentLabel
        from .discovered_sensitive_type import DiscoveredSensitiveType

        from .content_properties import ContentProperties
        from .current_label import CurrentLabel
        from .discovered_sensitive_type import DiscoveredSensitiveType

        fields: Dict[str, Callable[[Any], None]] = {
            "currentLabel": lambda n : setattr(self, 'current_label', n.get_object_value(CurrentLabel)),
            "discoveredSensitiveTypes": lambda n : setattr(self, 'discovered_sensitive_types', n.get_collection_of_object_values(DiscoveredSensitiveType)),
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
        writer.write_object_value("currentLabel", self.current_label)
        writer.write_collection_of_object_values("discoveredSensitiveTypes", self.discovered_sensitive_types)
    

