from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_status, device_compliance_policy_setting_state, entity, policy_platform_type

from . import entity

class DeviceCompliancePolicyState(entity.Entity):
    """
    Device Compliance Policy State for a given device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceCompliancePolicyState and sets the default values.
        """
        super().__init__()
        # The name of the policy for this policyBase
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types for policies.
        self._platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
        # Count of how many setting a policy holds
        self._setting_count: Optional[int] = None
        # The settingStates property
        self._setting_states: Optional[List[device_compliance_policy_setting_state.DeviceCompliancePolicySettingState]] = None
        # The state property
        self._state: Optional[compliance_status.ComplianceStatus] = None
        # User unique identifier, must be Guid
        self._user_id: Optional[str] = None
        # User Principal Name
        self._user_principal_name: Optional[str] = None
        # The version of the policy
        self._version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyState()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the policy for this policyBase
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the policy for this policyBase
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_status, device_compliance_policy_setting_state, entity, policy_platform_type

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
            "settingCount": lambda n : setattr(self, 'setting_count', n.get_int_value()),
            "settingStates": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(device_compliance_policy_setting_state.DeviceCompliancePolicySettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def platform_type(self,) -> Optional[policy_platform_type.PolicyPlatformType]:
        """
        Gets the platformType property value. Supported platform types for policies.
        Returns: Optional[policy_platform_type.PolicyPlatformType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[policy_platform_type.PolicyPlatformType] = None) -> None:
        """
        Sets the platformType property value. Supported platform types for policies.
        Args:
            value: Value to set for the platform_type property.
        """
        self._platform_type = value
    
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
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_int_value("settingCount", self.setting_count)
        writer.write_collection_of_object_values("settingStates", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_int_value("version", self.version)
    
    @property
    def setting_count(self,) -> Optional[int]:
        """
        Gets the settingCount property value. Count of how many setting a policy holds
        Returns: Optional[int]
        """
        return self._setting_count
    
    @setting_count.setter
    def setting_count(self,value: Optional[int] = None) -> None:
        """
        Sets the settingCount property value. Count of how many setting a policy holds
        Args:
            value: Value to set for the setting_count property.
        """
        self._setting_count = value
    
    @property
    def setting_states(self,) -> Optional[List[device_compliance_policy_setting_state.DeviceCompliancePolicySettingState]]:
        """
        Gets the settingStates property value. The settingStates property
        Returns: Optional[List[device_compliance_policy_setting_state.DeviceCompliancePolicySettingState]]
        """
        return self._setting_states
    
    @setting_states.setter
    def setting_states(self,value: Optional[List[device_compliance_policy_setting_state.DeviceCompliancePolicySettingState]] = None) -> None:
        """
        Sets the settingStates property value. The settingStates property
        Args:
            value: Value to set for the setting_states property.
        """
        self._setting_states = value
    
    @property
    def state(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the state property value. The state property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User unique identifier, must be Guid
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User unique identifier, must be Guid
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
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
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The version of the policy
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The version of the policy
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

