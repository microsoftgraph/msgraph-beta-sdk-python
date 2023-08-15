from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .segment_configuration import SegmentConfiguration
    from .web_application_segment import WebApplicationSegment

from .segment_configuration import SegmentConfiguration

@dataclass
class WebSegmentConfiguration(SegmentConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.webSegmentConfiguration"
    # The applicationSegments property
    application_segments: Optional[List[WebApplicationSegment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebSegmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebSegmentConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WebSegmentConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .segment_configuration import SegmentConfiguration
        from .web_application_segment import WebApplicationSegment

        from .segment_configuration import SegmentConfiguration
        from .web_application_segment import WebApplicationSegment

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationSegments": lambda n : setattr(self, 'application_segments', n.get_collection_of_object_values(WebApplicationSegment)),
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
        writer.write_collection_of_object_values("applicationSegments", self.application_segments)
    

