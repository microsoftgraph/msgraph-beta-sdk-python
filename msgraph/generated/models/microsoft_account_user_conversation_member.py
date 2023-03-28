from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conversation_member

from . import conversation_member

class MicrosoftAccountUserConversationMember(conversation_member.ConversationMember):
    def __init__(self,) -> None:
        """
        Instantiates a new MicrosoftAccountUserConversationMember and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.microsoftAccountUserConversationMember"
        # Microsoft Account ID of the user.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAccountUserConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAccountUserConversationMember
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftAccountUserConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conversation_member

        fields: Dict[str, Callable[[Any], None]] = {
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("userId", self.user_id)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Microsoft Account ID of the user.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Microsoft Account ID of the user.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

