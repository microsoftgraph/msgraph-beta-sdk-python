from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .threat_submission import ThreatSubmission

from .threat_submission import ThreatSubmission

@dataclass
class UrlThreatSubmission(ThreatSubmission):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.urlThreatSubmission"
    # Denotes the webUrl that needs to be submitted.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UrlThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UrlThreatSubmission
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UrlThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .threat_submission import ThreatSubmission

        from .threat_submission import ThreatSubmission

        fields: Dict[str, Callable[[Any], None]] = {
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("webUrl", self.web_url)
    

