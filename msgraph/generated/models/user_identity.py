from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audit_user_identity, identity

from . import identity

class UserIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new UserIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.userIdentity"
        # Indicates the client IP address used by user performing the activity (audit log only).
        self._ip_address: Optional[str] = None
        # The userPrincipalName attribute of the user.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.auditUserIdentity":
                from . import audit_user_identity

                return audit_user_identity.AuditUserIdentity()
        return UserIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audit_user_identity, identity

        fields: Dict[str, Callable[[Any], None]] = {
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. Indicates the client IP address used by user performing the activity (audit log only).
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. Indicates the client IP address used by user performing the activity (audit log only).
        Args:
            value: Value to set for the ip_address property.
        """
        self._ip_address = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The userPrincipalName attribute of the user.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The userPrincipalName attribute of the user.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

