from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

@dataclass
class StaleSignInAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    odata_type = "#microsoft.graph.staleSignInAlertIncident"
    # The assigneeDisplayName property
    assignee_display_name: Optional[str] = None
    # The assigneeId property
    assignee_id: Optional[str] = None
    # The assigneeUserPrincipalName property
    assignee_user_principal_name: Optional[str] = None
    # The assignmentCreatedDateTime property
    assignment_created_date_time: Optional[datetime] = None
    # The lastSignInDateTime property
    last_sign_in_date_time: Optional[datetime] = None
    # The roleDefinitionId property
    role_definition_id: Optional[str] = None
    # The roleDisplayName property
    role_display_name: Optional[str] = None
    # The roleTemplateId property
    role_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StaleSignInAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StaleSignInAlertIncident
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StaleSignInAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_incident

        from . import unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "assigneeDisplayName": lambda n : setattr(self, 'assignee_display_name', n.get_str_value()),
            "assigneeId": lambda n : setattr(self, 'assignee_id', n.get_str_value()),
            "assigneeUserPrincipalName": lambda n : setattr(self, 'assignee_user_principal_name', n.get_str_value()),
            "assignmentCreatedDateTime": lambda n : setattr(self, 'assignment_created_date_time', n.get_datetime_value()),
            "lastSignInDateTime": lambda n : setattr(self, 'last_sign_in_date_time', n.get_datetime_value()),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
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
        writer.write_str_value("assigneeDisplayName", self.assignee_display_name)
        writer.write_str_value("assigneeId", self.assignee_id)
        writer.write_str_value("assigneeUserPrincipalName", self.assignee_user_principal_name)
        writer.write_datetime_value("assignmentCreatedDateTime", self.assignment_created_date_time)
        writer.write_datetime_value("lastSignInDateTime", self.last_sign_in_date_time)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("roleDisplayName", self.role_display_name)
        writer.write_str_value("roleTemplateId", self.role_template_id)
    

