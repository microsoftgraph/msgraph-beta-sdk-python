from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import threat_assessment_request

from . import threat_assessment_request

class UrlAssessmentRequest(threat_assessment_request.ThreatAssessmentRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new UrlAssessmentRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.urlAssessmentRequest"
        # The URL string.
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UrlAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UrlAssessmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UrlAssessmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import threat_assessment_request

        fields: Dict[str, Callable[[Any], None]] = {
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("url", self.url)
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. The URL string.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. The URL string.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

