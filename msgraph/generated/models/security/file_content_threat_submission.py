from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import file_threat_submission

from . import file_threat_submission

@dataclass
class FileContentThreatSubmission(file_threat_submission.FileThreatSubmission):
    odata_type = "#microsoft.graph.security.fileContentThreatSubmission"
    # It specifies the file content in base 64 format.
    file_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileContentThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileContentThreatSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileContentThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import file_threat_submission

        fields: Dict[str, Callable[[Any], None]] = {
            "fileContent": lambda n : setattr(self, 'file_content', n.get_str_value()),
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
        writer.write_str_value("fileContent", self.file_content)
    

