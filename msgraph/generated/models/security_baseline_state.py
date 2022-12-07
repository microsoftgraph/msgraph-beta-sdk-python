from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
security_baseline_compliance_state = lazy_import('msgraph.generated.models.security_baseline_compliance_state')
security_baseline_setting_state = lazy_import('msgraph.generated.models.security_baseline_setting_state')

class SecurityBaselineState(entity.Entity):
    """
    Security baseline state for a device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new securityBaselineState and sets the default values.
        """
        super().__init__()
        # The display name of the security baseline
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The security baseline template id
        self._security_baseline_template_id: Optional[str] = None
        # The security baseline state for different settings for a device
        self._setting_states: Optional[List[security_baseline_setting_state.SecurityBaselineSettingState]] = None
        # Security Baseline Compliance State
        self._state: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState] = None
        # User Principal Name
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineState()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the security baseline
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the security baseline
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "security_baseline_template_id": lambda n : setattr(self, 'security_baseline_template_id', n.get_str_value()),
            "setting_states": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(security_baseline_setting_state.SecurityBaselineSettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(security_baseline_compliance_state.SecurityBaselineComplianceState)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def security_baseline_template_id(self,) -> Optional[str]:
        """
        Gets the securityBaselineTemplateId property value. The security baseline template id
        Returns: Optional[str]
        """
        return self._security_baseline_template_id
    
    @security_baseline_template_id.setter
    def security_baseline_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the securityBaselineTemplateId property value. The security baseline template id
        Args:
            value: Value to set for the securityBaselineTemplateId property.
        """
        self._security_baseline_template_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("securityBaselineTemplateId", self.security_baseline_template_id)
        writer.write_collection_of_object_values("settingStates", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def setting_states(self,) -> Optional[List[security_baseline_setting_state.SecurityBaselineSettingState]]:
        """
        Gets the settingStates property value. The security baseline state for different settings for a device
        Returns: Optional[List[security_baseline_setting_state.SecurityBaselineSettingState]]
        """
        return self._setting_states
    
    @setting_states.setter
    def setting_states(self,value: Optional[List[security_baseline_setting_state.SecurityBaselineSettingState]] = None) -> None:
        """
        Sets the settingStates property value. The security baseline state for different settings for a device
        Args:
            value: Value to set for the settingStates property.
        """
        self._setting_states = value
    
    @property
    def state(self,) -> Optional[security_baseline_compliance_state.SecurityBaselineComplianceState]:
        """
        Gets the state property value. Security Baseline Compliance State
        Returns: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState] = None) -> None:
        """
        Sets the state property value. Security Baseline Compliance State
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

