from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

class RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    def __init__(self,) -> None:
        """
        Instantiates a new RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident"
        # The assigneeDisplayName property
        self._assignee_display_name: Optional[str] = None
        # The assigneeId property
        self._assignee_id: Optional[str] = None
        # The assigneeUserPrincipalName property
        self._assignee_user_principal_name: Optional[str] = None
        # The assignmentCreatedDateTime property
        self._assignment_created_date_time: Optional[datetime] = None
        # The roleDefinitionId property
        self._role_definition_id: Optional[str] = None
        # The roleDisplayName property
        self._role_display_name: Optional[str] = None
        # The roleTemplateId property
        self._role_template_id: Optional[str] = None
    
    @property
    def assignee_display_name(self,) -> Optional[str]:
        """
        Gets the assigneeDisplayName property value. The assigneeDisplayName property
        Returns: Optional[str]
        """
        return self._assignee_display_name
    
    @assignee_display_name.setter
    def assignee_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneeDisplayName property value. The assigneeDisplayName property
        Args:
            value: Value to set for the assignee_display_name property.
        """
        self._assignee_display_name = value
    
    @property
    def assignee_id(self,) -> Optional[str]:
        """
        Gets the assigneeId property value. The assigneeId property
        Returns: Optional[str]
        """
        return self._assignee_id
    
    @assignee_id.setter
    def assignee_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneeId property value. The assigneeId property
        Args:
            value: Value to set for the assignee_id property.
        """
        self._assignee_id = value
    
    @property
    def assignee_user_principal_name(self,) -> Optional[str]:
        """
        Gets the assigneeUserPrincipalName property value. The assigneeUserPrincipalName property
        Returns: Optional[str]
        """
        return self._assignee_user_principal_name
    
    @assignee_user_principal_name.setter
    def assignee_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneeUserPrincipalName property value. The assigneeUserPrincipalName property
        Args:
            value: Value to set for the assignee_user_principal_name property.
        """
        self._assignee_user_principal_name = value
    
    @property
    def assignment_created_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignmentCreatedDateTime property value. The assignmentCreatedDateTime property
        Returns: Optional[datetime]
        """
        return self._assignment_created_date_time
    
    @assignment_created_date_time.setter
    def assignment_created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignmentCreatedDateTime property value. The assignmentCreatedDateTime property
        Args:
            value: Value to set for the assignment_created_date_time property.
        """
        self._assignment_created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "assigneeDisplayName": lambda n : setattr(self, 'assignee_display_name', n.get_str_value()),
            "assigneeId": lambda n : setattr(self, 'assignee_id', n.get_str_value()),
            "assigneeUserPrincipalName": lambda n : setattr(self, 'assignee_user_principal_name', n.get_str_value()),
            "assignmentCreatedDateTime": lambda n : setattr(self, 'assignment_created_date_time', n.get_datetime_value()),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "roleDisplayName": lambda n : setattr(self, 'role_display_name', n.get_str_value()),
            "roleTemplateId": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. The roleDefinitionId property
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. The roleDefinitionId property
        Args:
            value: Value to set for the role_definition_id property.
        """
        self._role_definition_id = value
    
    @property
    def role_display_name(self,) -> Optional[str]:
        """
        Gets the roleDisplayName property value. The roleDisplayName property
        Returns: Optional[str]
        """
        return self._role_display_name
    
    @role_display_name.setter
    def role_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDisplayName property value. The roleDisplayName property
        Args:
            value: Value to set for the role_display_name property.
        """
        self._role_display_name = value
    
    @property
    def role_template_id(self,) -> Optional[str]:
        """
        Gets the roleTemplateId property value. The roleTemplateId property
        Returns: Optional[str]
        """
        return self._role_template_id
    
    @role_template_id.setter
    def role_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleTemplateId property value. The roleTemplateId property
        Args:
            value: Value to set for the role_template_id property.
        """
        self._role_template_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("assigneeDisplayName", self.assignee_display_name)
        writer.write_str_value("assigneeId", self.assignee_id)
        writer.write_str_value("assigneeUserPrincipalName", self.assignee_user_principal_name)
        writer.write_datetime_value("assignmentCreatedDateTime", self.assignment_created_date_time)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("roleDisplayName", self.role_display_name)
        writer.write_str_value("roleTemplateId", self.role_template_id)
    

