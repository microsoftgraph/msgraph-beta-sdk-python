from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

@dataclass
class RedundantAssignmentAlertIncident(UnifiedRoleManagementAlertIncident):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.redundantAssignmentAlertIncident"
    # Display name of the subject that the incident applies to.
    assignee_display_name: Optional[str] = None
    # The identifier of the subject that the incident applies to.
    assignee_id: Optional[str] = None
    # User principal name of the subject that the incident applies to. Applies to user principals only.
    assignee_user_principal_name: Optional[str] = None
    # Date and time of the last activation of the eligible assignment.
    last_activation_date_time: Optional[datetime.datetime] = None
    # The identifier for the directory role definition that's in scope of this incident.
    role_definition_id: Optional[str] = None
    # The display name for the directory role.
    role_display_name: Optional[str] = None
    # The globally unique identifier for the directory role.
    role_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedundantAssignmentAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedundantAssignmentAlertIncident
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RedundantAssignmentAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

        fields: Dict[str, Callable[[Any], None]] = {
            "assigneeDisplayName": lambda n : setattr(self, 'assignee_display_name', n.get_str_value()),
            "assigneeId": lambda n : setattr(self, 'assignee_id', n.get_str_value()),
            "assigneeUserPrincipalName": lambda n : setattr(self, 'assignee_user_principal_name', n.get_str_value()),
            "lastActivationDateTime": lambda n : setattr(self, 'last_activation_date_time', n.get_datetime_value()),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("assigneeDisplayName", self.assignee_display_name)
        writer.write_str_value("assigneeId", self.assignee_id)
        writer.write_str_value("assigneeUserPrincipalName", self.assignee_user_principal_name)
        writer.write_datetime_value("lastActivationDateTime", self.last_activation_date_time)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("roleDisplayName", self.role_display_name)
        writer.write_str_value("roleTemplateId", self.role_template_id)
    

