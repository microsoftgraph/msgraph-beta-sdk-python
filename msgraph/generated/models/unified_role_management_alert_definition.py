from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_severity, entity

from . import entity

class UnifiedRoleManagementAlertDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementAlertDefinition and sets the default values.
        """
        super().__init__()
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The howToPrevent property
        self._how_to_prevent: Optional[str] = None
        # The isConfigurable property
        self._is_configurable: Optional[bool] = None
        # The isRemediatable property
        self._is_remediatable: Optional[bool] = None
        # The mitigationSteps property
        self._mitigation_steps: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scopeId property
        self._scope_id: Optional[str] = None
        # The scopeType property
        self._scope_type: Optional[str] = None
        # The securityImpact property
        self._security_impact: Optional[str] = None
        # The severityLevel property
        self._severity_level: Optional[alert_severity.AlertSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementAlertDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementAlertDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def how_to_prevent(self,) -> Optional[str]:
        """
        Gets the howToPrevent property value. The howToPrevent property
        Returns: Optional[str]
        """
        return self._how_to_prevent
    
    @how_to_prevent.setter
    def how_to_prevent(self,value: Optional[str] = None) -> None:
        """
        Sets the howToPrevent property value. The howToPrevent property
        Args:
            value: Value to set for the how_to_prevent property.
        """
        self._how_to_prevent = value
    
    @property
    def is_configurable(self,) -> Optional[bool]:
        """
        Gets the isConfigurable property value. The isConfigurable property
        Returns: Optional[bool]
        """
        return self._is_configurable
    
    @is_configurable.setter
    def is_configurable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isConfigurable property value. The isConfigurable property
        Args:
            value: Value to set for the is_configurable property.
        """
        self._is_configurable = value
    
    @property
    def is_remediatable(self,) -> Optional[bool]:
        """
        Gets the isRemediatable property value. The isRemediatable property
        Returns: Optional[bool]
        """
        return self._is_remediatable
    
    @is_remediatable.setter
    def is_remediatable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRemediatable property value. The isRemediatable property
        Args:
            value: Value to set for the is_remediatable property.
        """
        self._is_remediatable = value
    
    @property
    def mitigation_steps(self,) -> Optional[str]:
        """
        Gets the mitigationSteps property value. The mitigationSteps property
        Returns: Optional[str]
        """
        return self._mitigation_steps
    
    @mitigation_steps.setter
    def mitigation_steps(self,value: Optional[str] = None) -> None:
        """
        Sets the mitigationSteps property value. The mitigationSteps property
        Args:
            value: Value to set for the mitigation_steps property.
        """
        self._mitigation_steps = value
    
    @property
    def scope_id(self,) -> Optional[str]:
        """
        Gets the scopeId property value. The scopeId property
        Returns: Optional[str]
        """
        return self._scope_id
    
    @scope_id.setter
    def scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeId property value. The scopeId property
        Args:
            value: Value to set for the scope_id property.
        """
        self._scope_id = value
    
    @property
    def scope_type(self,) -> Optional[str]:
        """
        Gets the scopeType property value. The scopeType property
        Returns: Optional[str]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeType property value. The scopeType property
        Args:
            value: Value to set for the scope_type property.
        """
        self._scope_type = value
    
    @property
    def security_impact(self,) -> Optional[str]:
        """
        Gets the securityImpact property value. The securityImpact property
        Returns: Optional[str]
        """
        return self._security_impact
    
    @security_impact.setter
    def security_impact(self,value: Optional[str] = None) -> None:
        """
        Sets the securityImpact property value. The securityImpact property
        Args:
            value: Value to set for the security_impact property.
        """
        self._security_impact = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def severity_level(self,) -> Optional[alert_severity.AlertSeverity]:
        """
        Gets the severityLevel property value. The severityLevel property
        Returns: Optional[alert_severity.AlertSeverity]
        """
        return self._severity_level
    
    @severity_level.setter
    def severity_level(self,value: Optional[alert_severity.AlertSeverity] = None) -> None:
        """
        Sets the severityLevel property value. The severityLevel property
        Args:
            value: Value to set for the severity_level property.
        """
        self._severity_level = value
    

