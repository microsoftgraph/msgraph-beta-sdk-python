from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

@dataclass
class NoMfaOnRoleActivationAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    odata_type = "#microsoft.graph.noMfaOnRoleActivationAlertIncident"
    # The roleDisplayName property
    role_display_name: Optional[str] = None
    # The roleTemplateId property
    role_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NoMfaOnRoleActivationAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NoMfaOnRoleActivationAlertIncident
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NoMfaOnRoleActivationAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_incident

        from . import unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "roleDisplayName": lambda n : setattr(self, 'role_display_name', n.get_str_value()),
            "roleTemplateId": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("roleDisplayName", self.role_display_name)
        writer.write_str_value("roleTemplateId", self.role_template_id)
    

