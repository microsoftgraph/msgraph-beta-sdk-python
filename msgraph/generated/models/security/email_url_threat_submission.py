from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_threat_submission = lazy_import('msgraph.generated.models.security.email_threat_submission')

class EmailUrlThreatSubmission(email_threat_submission.EmailThreatSubmission):
    def __init__(self,) -> None:
        """
        Instantiates a new EmailUrlThreatSubmission and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.emailUrlThreatSubmission"
        # Specifies the url of the message to be submitted.
        self._message_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailUrlThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailUrlThreatSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailUrlThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message_url": lambda n : setattr(self, 'message_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message_url(self,) -> Optional[str]:
        """
        Gets the messageUrl property value. Specifies the url of the message to be submitted.
        Returns: Optional[str]
        """
        return self._message_url
    
    @message_url.setter
    def message_url(self,value: Optional[str] = None) -> None:
        """
        Sets the messageUrl property value. Specifies the url of the message to be submitted.
        Args:
            value: Value to set for the messageUrl property.
        """
        self._message_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("messageUrl", self.message_url)
    

