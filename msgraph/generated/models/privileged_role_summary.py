from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .role_summary_status import RoleSummaryStatus

from .entity import Entity

@dataclass
class PrivilegedRoleSummary(Entity):
    # The elevatedCount property
    elevated_count: Optional[int] = None
    # The managedCount property
    managed_count: Optional[int] = None
    # The mfaEnabled property
    mfa_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[RoleSummaryStatus] = None
    # The usersCount property
    users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedRoleSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedRoleSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .role_summary_status import RoleSummaryStatus

        from .entity import Entity
        from .role_summary_status import RoleSummaryStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "elevatedCount": lambda n : setattr(self, 'elevated_count', n.get_int_value()),
            "managedCount": lambda n : setattr(self, 'managed_count', n.get_int_value()),
            "mfaEnabled": lambda n : setattr(self, 'mfa_enabled', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RoleSummaryStatus)),
            "usersCount": lambda n : setattr(self, 'users_count', n.get_int_value()),
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
        writer.write_int_value("elevatedCount", self.elevated_count)
        writer.write_int_value("managedCount", self.managed_count)
        writer.write_bool_value("mfaEnabled", self.mfa_enabled)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("usersCount", self.users_count)
    

