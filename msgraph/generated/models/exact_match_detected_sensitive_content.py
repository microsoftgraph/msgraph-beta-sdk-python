from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

detected_sensitive_content_base = lazy_import('msgraph.generated.models.detected_sensitive_content_base')
sensitive_content_location = lazy_import('msgraph.generated.models.sensitive_content_location')

class ExactMatchDetectedSensitiveContent(detected_sensitive_content_base.DetectedSensitiveContentBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ExactMatchDetectedSensitiveContent and sets the default values.
        """
        super().__init__()
        # The matches property
        self._matches: Optional[List[sensitive_content_location.SensitiveContentLocation]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
        fields = {
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(sensitive_content_location.SensitiveContentLocation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def matches(self,) -> Optional[List[sensitive_content_location.SensitiveContentLocation]]:
        """
        Gets the matches property value. The matches property
        Returns: Optional[List[sensitive_content_location.SensitiveContentLocation]]
        """
        return self._matches
    
    @matches.setter
    def matches(self,value: Optional[List[sensitive_content_location.SensitiveContentLocation]] = None) -> None:
        """
        Sets the matches property value. The matches property
        Args:
            value: Value to set for the matches property.
        """
        self._matches = value
    
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
    

