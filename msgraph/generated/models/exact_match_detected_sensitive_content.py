from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import detected_sensitive_content_base, sensitive_content_location

from . import detected_sensitive_content_base

@dataclass
class ExactMatchDetectedSensitiveContent(detected_sensitive_content_base.DetectedSensitiveContentBase):
    # The matches property
    matches: Optional[List[sensitive_content_location.SensitiveContentLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchDetectedSensitiveContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchDetectedSensitiveContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchDetectedSensitiveContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import detected_sensitive_content_base, sensitive_content_location

        fields: Dict[str, Callable[[Any], None]] = {
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(sensitive_content_location.SensitiveContentLocation)),
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
        writer.write_collection_of_object_values("matches", self.matches)
    

