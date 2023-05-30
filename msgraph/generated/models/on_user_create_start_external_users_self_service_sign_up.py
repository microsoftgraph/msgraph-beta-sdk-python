from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import on_user_create_start_handler, user_type

from . import on_user_create_start_handler

class OnUserCreateStartExternalUsersSelfServiceSignUp(on_user_create_start_handler.OnUserCreateStartHandler):
    def __init__(self,) -> None:
        """
        Instantiates a new OnUserCreateStartExternalUsersSelfServiceSignUp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onUserCreateStartExternalUsersSelfServiceSignUp"
        # The type of user object to create. The possible values are: member, guest, unknownFutureValue.
        self._user_type_to_create: Optional[user_type.UserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnUserCreateStartExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnUserCreateStartExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnUserCreateStartExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import on_user_create_start_handler, user_type

        fields: Dict[str, Callable[[Any], None]] = {
            "userTypeToCreate": lambda n : setattr(self, 'user_type_to_create', n.get_enum_value(user_type.UserType)),
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
        writer.write_enum_value("userTypeToCreate", self.user_type_to_create)
    
    @property
    def user_type_to_create(self,) -> Optional[user_type.UserType]:
        """
        Gets the userTypeToCreate property value. The type of user object to create. The possible values are: member, guest, unknownFutureValue.
        Returns: Optional[user_type.UserType]
        """
        return self._user_type_to_create
    
    @user_type_to_create.setter
    def user_type_to_create(self,value: Optional[user_type.UserType] = None) -> None:
        """
        Sets the userTypeToCreate property value. The type of user object to create. The possible values are: member, guest, unknownFutureValue.
        Args:
            value: Value to set for the user_type_to_create property.
        """
        self._user_type_to_create = value
    

