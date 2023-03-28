from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

class TooManyGlobalAdminsAssignedToTenantAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    def __init__(self,) -> None:
        """
        Instantiates a new TooManyGlobalAdminsAssignedToTenantAlertIncident and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident"
        # The assigneeDisplayName property
        self._assignee_display_name: Optional[str] = None
        # The assigneeId property
        self._assignee_id: Optional[str] = None
        # The assigneeUserPrincipalName property
        self._assignee_user_principal_name: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TooManyGlobalAdminsAssignedToTenantAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TooManyGlobalAdminsAssignedToTenantAlertIncident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TooManyGlobalAdminsAssignedToTenantAlertIncident()
    
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
        writer.write_str_value("assigneeDisplayName", self.assignee_display_name)
        writer.write_str_value("assigneeId", self.assignee_id)
        writer.write_str_value("assigneeUserPrincipalName", self.assignee_user_principal_name)
    

