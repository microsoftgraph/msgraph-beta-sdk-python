from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_severity, entity

from . import entity

@dataclass
class UnifiedRoleManagementAlertDefinition(entity.Entity):
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The howToPrevent property
    how_to_prevent: Optional[str] = None
    # The isConfigurable property
    is_configurable: Optional[bool] = None
    # The isRemediatable property
    is_remediatable: Optional[bool] = None
    # The mitigationSteps property
    mitigation_steps: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scopeId property
    scope_id: Optional[str] = None
    # The scopeType property
    scope_type: Optional[str] = None
    # The securityImpact property
    security_impact: Optional[str] = None
    # The severityLevel property
    severity_level: Optional[alert_severity.AlertSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementAlertDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementAlertDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_severity, entity

        from . import alert_severity, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "howToPrevent": lambda n : setattr(self, 'how_to_prevent', n.get_str_value()),
            "isConfigurable": lambda n : setattr(self, 'is_configurable', n.get_bool_value()),
            "isRemediatable": lambda n : setattr(self, 'is_remediatable', n.get_bool_value()),
            "mitigationSteps": lambda n : setattr(self, 'mitigation_steps', n.get_str_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
            "securityImpact": lambda n : setattr(self, 'security_impact', n.get_str_value()),
            "severityLevel": lambda n : setattr(self, 'severity_level', n.get_enum_value(alert_severity.AlertSeverity)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("howToPrevent", self.how_to_prevent)
        writer.write_bool_value("isConfigurable", self.is_configurable)
        writer.write_bool_value("isRemediatable", self.is_remediatable)
        writer.write_str_value("mitigationSteps", self.mitigation_steps)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
        writer.write_str_value("securityImpact", self.security_impact)
        writer.write_enum_value("severityLevel", self.severity_level)
    

