from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audit_user_identity import AuditUserIdentity
    from .identity import Identity

from .identity import Identity

@dataclass
class UserIdentity(Identity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userIdentity"
    # Indicates the client IP address used by user performing the activity (audit log only).
    ip_address: Optional[str] = None
    # The userPrincipalName attribute of the user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditUserIdentity".casefold():
            from .audit_user_identity import AuditUserIdentity

            return AuditUserIdentity()
        return UserIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audit_user_identity import AuditUserIdentity
        from .identity import Identity

        from .audit_user_identity import AuditUserIdentity
        from .identity import Identity

        fields: Dict[str, Callable[[Any], None]] = {
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

