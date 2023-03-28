from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import identity

from .. import identity

class SubmissionUserIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new SubmissionUserIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.submissionUserIdentity"
        # The email of user who is making the submission when logged in (delegated token case).
        self._email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubmissionUserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionUserIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubmissionUserIdentity()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email of user who is making the submission when logged in (delegated token case).
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email of user who is making the submission when logged in (delegated token case).
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import identity

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
    

