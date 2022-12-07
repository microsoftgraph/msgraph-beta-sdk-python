from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
privileged_role = lazy_import('msgraph.generated.models.privileged_role')

class PrivilegedRoleAssignment(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedRoleAssignment and sets the default values.
        """
        super().__init__()
        # The UTC DateTime when the temporary privileged role assignment will be expired. For permanent role assignment, the value is null.
        self._expiration_date_time: Optional[datetime] = None
        # true if the role assignment is activated. false if the role assignment is deactivated.
        self._is_elevated: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Result message set by the service.
        self._result_message: Optional[str] = None
        # Role identifier. In GUID string format.
        self._role_id: Optional[str] = None
        # Read-only. Nullable. The associated role information.
        self._role_info: Optional[privileged_role.PrivilegedRole] = None
        # User identifier. In GUID string format.
        self._user_id: Optional[str] = None
    
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
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The UTC DateTime when the temporary privileged role assignment will be expired. For permanent role assignment, the value is null.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The UTC DateTime when the temporary privileged role assignment will be expired. For permanent role assignment, the value is null.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "is_elevated": lambda n : setattr(self, 'is_elevated', n.get_bool_value()),
            "result_message": lambda n : setattr(self, 'result_message', n.get_str_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_info": lambda n : setattr(self, 'role_info', n.get_object_value(privileged_role.PrivilegedRole)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_elevated(self,) -> Optional[bool]:
        """
        Gets the isElevated property value. true if the role assignment is activated. false if the role assignment is deactivated.
        Returns: Optional[bool]
        """
        return self._is_elevated
    
    @is_elevated.setter
    def is_elevated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isElevated property value. true if the role assignment is activated. false if the role assignment is deactivated.
        Args:
            value: Value to set for the isElevated property.
        """
        self._is_elevated = value
    
    @property
    def result_message(self,) -> Optional[str]:
        """
        Gets the resultMessage property value. Result message set by the service.
        Returns: Optional[str]
        """
        return self._result_message
    
    @result_message.setter
    def result_message(self,value: Optional[str] = None) -> None:
        """
        Sets the resultMessage property value. Result message set by the service.
        Args:
            value: Value to set for the resultMessage property.
        """
        self._result_message = value
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. Role identifier. In GUID string format.
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. Role identifier. In GUID string format.
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_info(self,) -> Optional[privileged_role.PrivilegedRole]:
        """
        Gets the roleInfo property value. Read-only. Nullable. The associated role information.
        Returns: Optional[privileged_role.PrivilegedRole]
        """
        return self._role_info
    
    @role_info.setter
    def role_info(self,value: Optional[privileged_role.PrivilegedRole] = None) -> None:
        """
        Sets the roleInfo property value. Read-only. Nullable. The associated role information.
        Args:
            value: Value to set for the roleInfo property.
        """
        self._role_info = value
    
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
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User identifier. In GUID string format.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User identifier. In GUID string format.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

