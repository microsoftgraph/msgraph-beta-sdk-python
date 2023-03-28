from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import payload_detail

from . import payload_detail

class EmailPayloadDetail(payload_detail.PayloadDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new EmailPayloadDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.emailPayloadDetail"
        # Email address of the user.
        self._from_email: Optional[str] = None
        # Display name of the user.
        self._from_name: Optional[str] = None
        # Indicates whether the sender is not from the user's organization.
        self._is_external_sender: Optional[bool] = None
        # The subject of the email address sent to the user.
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailPayloadDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailPayloadDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailPayloadDetail()
    
    @property
    def from_email(self,) -> Optional[str]:
        """
        Gets the fromEmail property value. Email address of the user.
        Returns: Optional[str]
        """
        return self._from_email
    
    @from_email.setter
    def from_email(self,value: Optional[str] = None) -> None:
        """
        Sets the fromEmail property value. Email address of the user.
        Args:
            value: Value to set for the from_email property.
        """
        self._from_email = value
    
    @property
    def from_name(self,) -> Optional[str]:
        """
        Gets the fromName property value. Display name of the user.
        Returns: Optional[str]
        """
        return self._from_name
    
    @from_name.setter
    def from_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fromName property value. Display name of the user.
        Args:
            value: Value to set for the from_name property.
        """
        self._from_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import payload_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "fromEmail": lambda n : setattr(self, 'from_email', n.get_str_value()),
            "fromName": lambda n : setattr(self, 'from_name', n.get_str_value()),
            "isExternalSender": lambda n : setattr(self, 'is_external_sender', n.get_bool_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_external_sender(self,) -> Optional[bool]:
        """
        Gets the isExternalSender property value. Indicates whether the sender is not from the user's organization.
        Returns: Optional[bool]
        """
        return self._is_external_sender
    
    @is_external_sender.setter
    def is_external_sender(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExternalSender property value. Indicates whether the sender is not from the user's organization.
        Args:
            value: Value to set for the is_external_sender property.
        """
        self._is_external_sender = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("fromEmail", self.from_email)
        writer.write_str_value("fromName", self.from_name)
        writer.write_bool_value("isExternalSender", self.is_external_sender)
        writer.write_str_value("subject", self.subject)
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject of the email address sent to the user.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject of the email address sent to the user.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

