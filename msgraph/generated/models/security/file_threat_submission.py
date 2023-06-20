from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import file_content_threat_submission, file_url_threat_submission, threat_submission

from . import threat_submission

@dataclass
class FileThreatSubmission(threat_submission.ThreatSubmission):
    odata_type = "#microsoft.graph.security.fileThreatSubmission"
    # It specifies the file name to be submitted.
    file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileThreatSubmission
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileContentThreatSubmission".casefold():
            from . import file_content_threat_submission

            return file_content_threat_submission.FileContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileUrlThreatSubmission".casefold():
            from . import file_url_threat_submission

            return file_url_threat_submission.FileUrlThreatSubmission()
        return FileThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import file_content_threat_submission, file_url_threat_submission, threat_submission

        from . import file_content_threat_submission, file_url_threat_submission, threat_submission

        fields: Dict[str, Callable[[Any], None]] = {
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
        writer.write_str_value("fileName", self.file_name)
    

