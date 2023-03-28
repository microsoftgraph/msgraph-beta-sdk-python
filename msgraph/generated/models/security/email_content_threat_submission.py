from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_threat_submission

from . import email_threat_submission

class EmailContentThreatSubmission(email_threat_submission.EmailThreatSubmission):
    def __init__(self,) -> None:
        """
        Instantiates a new EmailContentThreatSubmission and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.emailContentThreatSubmission"
        # Base64 encoded file content.
        self._file_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailContentThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailContentThreatSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailContentThreatSubmission()
    
    @property
    def file_content(self,) -> Optional[str]:
        """
        Gets the fileContent property value. Base64 encoded file content.
        Returns: Optional[str]
        """
        return self._file_content
    
    @file_content.setter
    def file_content(self,value: Optional[str] = None) -> None:
        """
        Sets the fileContent property value. Base64 encoded file content.
        Args:
            value: Value to set for the file_content property.
        """
        self._file_content = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_threat_submission

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
    

