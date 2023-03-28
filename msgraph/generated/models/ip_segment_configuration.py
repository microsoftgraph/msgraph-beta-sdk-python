from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ip_application_segment, segment_configuration

from . import segment_configuration

class IpSegmentConfiguration(segment_configuration.SegmentConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IpSegmentConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.ipSegmentConfiguration"
        # The applicationSegments property
        self._application_segments: Optional[List[ip_application_segment.IpApplicationSegment]] = None
    
    @property
    def application_segments(self,) -> Optional[List[ip_application_segment.IpApplicationSegment]]:
        """
        Gets the applicationSegments property value. The applicationSegments property
        Returns: Optional[List[ip_application_segment.IpApplicationSegment]]
        """
        return self._application_segments
    
    @application_segments.setter
    def application_segments(self,value: Optional[List[ip_application_segment.IpApplicationSegment]] = None) -> None:
        """
        Sets the applicationSegments property value. The applicationSegments property
        Args:
            value: Value to set for the application_segments property.
        """
        self._application_segments = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpSegmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpSegmentConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpSegmentConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ip_application_segment, segment_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationSegments": lambda n : setattr(self, 'application_segments', n.get_collection_of_object_values(ip_application_segment.IpApplicationSegment)),
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
        writer.write_collection_of_object_values("applicationSegments", self.application_segments)
    

