from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

file_threat_submission = lazy_import('msgraph.generated.models.security.file_threat_submission')

class FileContentThreatSubmission(file_threat_submission.FileThreatSubmission):
    def __init__(self,) -> None:
        """
        Instantiates a new FileContentThreatSubmission and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.fileContentThreatSubmission"
        # It specifies the file content in base 64 format.
        self._file_content: Optional[str] = None
    
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
    
    @property
    def file_content(self,) -> Optional[str]:
        """
        Gets the fileContent property value. It specifies the file content in base 64 format.
        Returns: Optional[str]
        """
        return self._file_content
    
    @file_content.setter
    def file_content(self,value: Optional[str] = None) -> None:
        """
        Sets the fileContent property value. It specifies the file content in base 64 format.
        Args:
            value: Value to set for the fileContent property.
        """
        self._file_content = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_content": lambda n : setattr(self, 'file_content', n.get_str_value()),
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
    

