from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_result_part

from . import action_result_part

class AadUserConversationMemberResult(action_result_part.ActionResultPart):
    def __init__(self,) -> None:
        """
        Instantiates a new AadUserConversationMemberResult and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.aadUserConversationMemberResult"
        # The user object ID of the Azure AD user that was being added as part of the bulk operation.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AadUserConversationMemberResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AadUserConversationMemberResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AadUserConversationMemberResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_result_part

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
        Gets the userId property value. The user object ID of the Azure AD user that was being added as part of the bulk operation.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user object ID of the Azure AD user that was being added as part of the bulk operation.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

