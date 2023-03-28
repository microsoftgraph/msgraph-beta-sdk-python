from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_collection_pagination_count_response, web_application_segment

from . import base_collection_pagination_count_response

class WebApplicationSegmentCollectionResponse(base_collection_pagination_count_response.BaseCollectionPaginationCountResponse):
    def __init__(self,) -> None:
        """
        Instantiates a new WebApplicationSegmentCollectionResponse and sets the default values.
        """
        super().__init__()
        # The value property
        self._value: Optional[List[web_application_segment.WebApplicationSegment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebApplicationSegmentCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationSegmentCollectionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebApplicationSegmentCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_collection_pagination_count_response, web_application_segment

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(web_application_segment.WebApplicationSegment)),
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
        writer.write_collection_of_object_values("value", self.value)
    
    @property
    def value(self,) -> Optional[List[web_application_segment.WebApplicationSegment]]:
        """
        Gets the value property value. The value property
        Returns: Optional[List[web_application_segment.WebApplicationSegment]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[web_application_segment.WebApplicationSegment]] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

