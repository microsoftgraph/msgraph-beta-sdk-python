from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, security_baseline_compliance_state, security_baseline_setting_state

from . import entity

@dataclass
class SecurityBaselineState(entity.Entity):
    """
    Security baseline state for a device.
    """
    # The display name of the security baseline
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The security baseline template id
    security_baseline_template_id: Optional[str] = None
    # The security baseline state for different settings for a device
    setting_states: Optional[List[security_baseline_setting_state.SecurityBaselineSettingState]] = None
    # Security Baseline Compliance State
    state: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState] = None
    # User Principal Name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, security_baseline_compliance_state, security_baseline_setting_state

        from . import entity, security_baseline_compliance_state, security_baseline_setting_state

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "securityBaselineTemplateId": lambda n : setattr(self, 'security_baseline_template_id', n.get_str_value()),
            "settingStates": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(security_baseline_setting_state.SecurityBaselineSettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(security_baseline_compliance_state.SecurityBaselineComplianceState)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("securityBaselineTemplateId", self.security_baseline_template_id)
        writer.write_collection_of_object_values("settingStates", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

