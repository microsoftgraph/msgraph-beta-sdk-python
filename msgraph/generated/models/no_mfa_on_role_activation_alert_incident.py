from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

class NoMfaOnRoleActivationAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    def __init__(self,) -> None:
        """
        Instantiates a new NoMfaOnRoleActivationAlertIncident and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.noMfaOnRoleActivationAlertIncident"
        # The roleDisplayName property
        self._role_display_name: Optional[str] = None
        # The roleTemplateId property
        self._role_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NoMfaOnRoleActivationAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NoMfaOnRoleActivationAlertIncident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NoMfaOnRoleActivationAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "roleDisplayName": lambda n : setattr(self, 'role_display_name', n.get_str_value()),
            "roleTemplateId": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_str_value("roleDisplayName", self.role_display_name)
        writer.write_str_value("roleTemplateId", self.role_template_id)
    

