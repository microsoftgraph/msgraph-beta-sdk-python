from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
security_baseline_compliance_state = lazy_import('msgraph.generated.models.security_baseline_compliance_state')
security_baseline_contributing_policy = lazy_import('msgraph.generated.models.security_baseline_contributing_policy')
setting_source = lazy_import('msgraph.generated.models.setting_source')

class SecurityBaselineSettingState(entity.Entity):
    """
    The security baseline compliance state of a setting for a device
    """
    def __init__(self,) -> None:
        """
        Instantiates a new securityBaselineSettingState and sets the default values.
        """
        super().__init__()
        # The policies that contribute to this setting instance
        self._contributing_policies: Optional[List[security_baseline_contributing_policy.SecurityBaselineContributingPolicy]] = None
        # The error code if the setting is in error state
        self._error_code: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The setting category id which this setting belongs to
        self._setting_category_id: Optional[str] = None
        # The setting category name which this setting belongs to
        self._setting_category_name: Optional[str] = None
        # The setting id guid
        self._setting_id: Optional[str] = None
        # The setting name that is being reported
        self._setting_name: Optional[str] = None
        # The policies that contribute to this setting instance
        self._source_policies: Optional[List[setting_source.SettingSource]] = None
        # Security Baseline Compliance State
        self._state: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState] = None
    
    @property
    def contributing_policies(self,) -> Optional[List[security_baseline_contributing_policy.SecurityBaselineContributingPolicy]]:
        """
        Gets the contributingPolicies property value. The policies that contribute to this setting instance
        Returns: Optional[List[security_baseline_contributing_policy.SecurityBaselineContributingPolicy]]
        """
        return self._contributing_policies
    
    @contributing_policies.setter
    def contributing_policies(self,value: Optional[List[security_baseline_contributing_policy.SecurityBaselineContributingPolicy]] = None) -> None:
        """
        Sets the contributingPolicies property value. The policies that contribute to this setting instance
        Args:
            value: Value to set for the contributingPolicies property.
        """
        self._contributing_policies = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineSettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineSettingState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineSettingState()
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. The error code if the setting is in error state
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. The error code if the setting is in error state
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contributing_policies": lambda n : setattr(self, 'contributing_policies', n.get_collection_of_object_values(security_baseline_contributing_policy.SecurityBaselineContributingPolicy)),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "setting_category_id": lambda n : setattr(self, 'setting_category_id', n.get_str_value()),
            "setting_category_name": lambda n : setattr(self, 'setting_category_name', n.get_str_value()),
            "setting_id": lambda n : setattr(self, 'setting_id', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "source_policies": lambda n : setattr(self, 'source_policies', n.get_collection_of_object_values(setting_source.SettingSource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(security_baseline_compliance_state.SecurityBaselineComplianceState)),
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
        writer.write_collection_of_object_values("contributingPolicies", self.contributing_policies)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("settingCategoryId", self.setting_category_id)
        writer.write_str_value("settingCategoryName", self.setting_category_name)
        writer.write_str_value("settingId", self.setting_id)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_collection_of_object_values("sourcePolicies", self.source_policies)
        writer.write_enum_value("state", self.state)
    
    @property
    def setting_category_id(self,) -> Optional[str]:
        """
        Gets the settingCategoryId property value. The setting category id which this setting belongs to
        Returns: Optional[str]
        """
        return self._setting_category_id
    
    @setting_category_id.setter
    def setting_category_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingCategoryId property value. The setting category id which this setting belongs to
        Args:
            value: Value to set for the settingCategoryId property.
        """
        self._setting_category_id = value
    
    @property
    def setting_category_name(self,) -> Optional[str]:
        """
        Gets the settingCategoryName property value. The setting category name which this setting belongs to
        Returns: Optional[str]
        """
        return self._setting_category_name
    
    @setting_category_name.setter
    def setting_category_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingCategoryName property value. The setting category name which this setting belongs to
        Args:
            value: Value to set for the settingCategoryName property.
        """
        self._setting_category_name = value
    
    @property
    def setting_id(self,) -> Optional[str]:
        """
        Gets the settingId property value. The setting id guid
        Returns: Optional[str]
        """
        return self._setting_id
    
    @setting_id.setter
    def setting_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingId property value. The setting id guid
        Args:
            value: Value to set for the settingId property.
        """
        self._setting_id = value
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. The setting name that is being reported
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. The setting name that is being reported
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    
    @property
    def source_policies(self,) -> Optional[List[setting_source.SettingSource]]:
        """
        Gets the sourcePolicies property value. The policies that contribute to this setting instance
        Returns: Optional[List[setting_source.SettingSource]]
        """
        return self._source_policies
    
    @source_policies.setter
    def source_policies(self,value: Optional[List[setting_source.SettingSource]] = None) -> None:
        """
        Sets the sourcePolicies property value. The policies that contribute to this setting instance
        Args:
            value: Value to set for the sourcePolicies property.
        """
        self._source_policies = value
    
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
    

