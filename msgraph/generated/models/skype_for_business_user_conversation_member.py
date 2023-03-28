from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conversation_member

from . import conversation_member

class SkypeForBusinessUserConversationMember(conversation_member.ConversationMember):
    def __init__(self,) -> None:
        """
        Instantiates a new SkypeForBusinessUserConversationMember and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.skypeForBusinessUserConversationMember"
        # ID of the tenant that the user belongs to.
        self._tenant_id: Optional[str] = None
        # Azure Active Directory ID of the user.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SkypeForBusinessUserConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SkypeForBusinessUserConversationMember
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SkypeForBusinessUserConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conversation_member

        fields: Dict[str, Callable[[Any], None]] = {
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. ID of the tenant that the user belongs to.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. ID of the tenant that the user belongs to.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Azure Active Directory ID of the user.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Azure Active Directory ID of the user.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

