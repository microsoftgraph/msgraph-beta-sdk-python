from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, privileged_role

from . import entity

@dataclass
class PrivilegedRoleAssignment(entity.Entity):
    # The expirationDateTime property
    expiration_date_time: Optional[datetime] = None
    # The isElevated property
    is_elevated: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resultMessage property
    result_message: Optional[str] = None
    # The roleId property
    role_id: Optional[str] = None
    # The roleInfo property
    role_info: Optional[privileged_role.PrivilegedRole] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedRoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, privileged_role

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "isElevated": lambda n : setattr(self, 'is_elevated', n.get_bool_value()),
            "resultMessage": lambda n : setattr(self, 'result_message', n.get_str_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleInfo": lambda n : setattr(self, 'role_info', n.get_object_value(privileged_role.PrivilegedRole)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("isElevated", self.is_elevated)
        writer.write_str_value("resultMessage", self.result_message)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleInfo", self.role_info)
        writer.write_str_value("userId", self.user_id)
    

