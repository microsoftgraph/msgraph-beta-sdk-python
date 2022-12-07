from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_setting_scope = lazy_import('msgraph.generated.models.group_policy_setting_scope')
group_policy_setting_type = lazy_import('msgraph.generated.models.group_policy_setting_type')
mdm_supported_state = lazy_import('msgraph.generated.models.mdm_supported_state')

class GroupPolicySettingMapping(entity.Entity):
    """
    The Group Policy setting to MDM/Intune mapping.
    """
    @property
    def admx_setting_definition_id(self,) -> Optional[str]:
        """
        Gets the admxSettingDefinitionId property value. Admx Group Policy Id
        Returns: Optional[str]
        """
        return self._admx_setting_definition_id
    
    @admx_setting_definition_id.setter
    def admx_setting_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the admxSettingDefinitionId property value. Admx Group Policy Id
        Args:
            value: Value to set for the admxSettingDefinitionId property.
        """
        self._admx_setting_definition_id = value
    
    @property
    def child_id_list(self,) -> Optional[List[str]]:
        """
        Gets the childIdList property value. List of Child Ids of the group policy setting.
        Returns: Optional[List[str]]
        """
        return self._child_id_list
    
    @child_id_list.setter
    def child_id_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the childIdList property value. List of Child Ids of the group policy setting.
        Args:
            value: Value to set for the childIdList property.
        """
        self._child_id_list = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicySettingMapping and sets the default values.
        """
        super().__init__()
        # Admx Group Policy Id
        self._admx_setting_definition_id: Optional[str] = None
        # List of Child Ids of the group policy setting.
        self._child_id_list: Optional[List[str]] = None
        # The Intune Setting Definition Id
        self._intune_setting_definition_id: Optional[str] = None
        # The list of Intune Setting URIs this group policy setting maps to
        self._intune_setting_uri_list: Optional[List[str]] = None
        # Indicates if the setting is supported by Intune or not
        self._is_mdm_supported: Optional[bool] = None
        # The CSP name this group policy setting maps to.
        self._mdm_csp_name: Optional[str] = None
        # The minimum OS version this mdm setting supports.
        self._mdm_minimum_o_s_version: Optional[int] = None
        # The MDM CSP URI this group policy setting maps to.
        self._mdm_setting_uri: Optional[str] = None
        # Mdm Support Status of the setting.
        self._mdm_supported_state: Optional[mdm_supported_state.MdmSupportedState] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Parent Id of the group policy setting.
        self._parent_id: Optional[str] = None
        # The category the group policy setting is in.
        self._setting_category: Optional[str] = None
        # The display name of this group policy setting.
        self._setting_display_name: Optional[str] = None
        # The display value of this group policy setting.
        self._setting_display_value: Optional[str] = None
        # The display value type of this group policy setting.
        self._setting_display_value_type: Optional[str] = None
        # The name of this group policy setting.
        self._setting_name: Optional[str] = None
        # Scope of the group policy setting.
        self._setting_scope: Optional[group_policy_setting_scope.GroupPolicySettingScope] = None
        # Setting type of the group policy.
        self._setting_type: Optional[group_policy_setting_type.GroupPolicySettingType] = None
        # The value of this group policy setting.
        self._setting_value: Optional[str] = None
        # The display units of this group policy setting value
        self._setting_value_display_units: Optional[str] = None
        # The value type of this group policy setting.
        self._setting_value_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicySettingMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicySettingMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicySettingMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admx_setting_definition_id": lambda n : setattr(self, 'admx_setting_definition_id', n.get_str_value()),
            "child_id_list": lambda n : setattr(self, 'child_id_list', n.get_collection_of_primitive_values(str)),
            "intune_setting_definition_id": lambda n : setattr(self, 'intune_setting_definition_id', n.get_str_value()),
            "intune_setting_uri_list": lambda n : setattr(self, 'intune_setting_uri_list', n.get_collection_of_primitive_values(str)),
            "is_mdm_supported": lambda n : setattr(self, 'is_mdm_supported', n.get_bool_value()),
            "mdm_csp_name": lambda n : setattr(self, 'mdm_csp_name', n.get_str_value()),
            "mdm_minimum_o_s_version": lambda n : setattr(self, 'mdm_minimum_o_s_version', n.get_int_value()),
            "mdm_setting_uri": lambda n : setattr(self, 'mdm_setting_uri', n.get_str_value()),
            "mdm_supported_state": lambda n : setattr(self, 'mdm_supported_state', n.get_enum_value(mdm_supported_state.MdmSupportedState)),
            "parent_id": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "setting_category": lambda n : setattr(self, 'setting_category', n.get_str_value()),
            "setting_display_name": lambda n : setattr(self, 'setting_display_name', n.get_str_value()),
            "setting_display_value": lambda n : setattr(self, 'setting_display_value', n.get_str_value()),
            "setting_display_value_type": lambda n : setattr(self, 'setting_display_value_type', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "setting_scope": lambda n : setattr(self, 'setting_scope', n.get_enum_value(group_policy_setting_scope.GroupPolicySettingScope)),
            "setting_type": lambda n : setattr(self, 'setting_type', n.get_enum_value(group_policy_setting_type.GroupPolicySettingType)),
            "setting_value": lambda n : setattr(self, 'setting_value', n.get_str_value()),
            "setting_value_display_units": lambda n : setattr(self, 'setting_value_display_units', n.get_str_value()),
            "setting_value_type": lambda n : setattr(self, 'setting_value_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intune_setting_definition_id(self,) -> Optional[str]:
        """
        Gets the intuneSettingDefinitionId property value. The Intune Setting Definition Id
        Returns: Optional[str]
        """
        return self._intune_setting_definition_id
    
    @intune_setting_definition_id.setter
    def intune_setting_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the intuneSettingDefinitionId property value. The Intune Setting Definition Id
        Args:
            value: Value to set for the intuneSettingDefinitionId property.
        """
        self._intune_setting_definition_id = value
    
    @property
    def intune_setting_uri_list(self,) -> Optional[List[str]]:
        """
        Gets the intuneSettingUriList property value. The list of Intune Setting URIs this group policy setting maps to
        Returns: Optional[List[str]]
        """
        return self._intune_setting_uri_list
    
    @intune_setting_uri_list.setter
    def intune_setting_uri_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the intuneSettingUriList property value. The list of Intune Setting URIs this group policy setting maps to
        Args:
            value: Value to set for the intuneSettingUriList property.
        """
        self._intune_setting_uri_list = value
    
    @property
    def is_mdm_supported(self,) -> Optional[bool]:
        """
        Gets the isMdmSupported property value. Indicates if the setting is supported by Intune or not
        Returns: Optional[bool]
        """
        return self._is_mdm_supported
    
    @is_mdm_supported.setter
    def is_mdm_supported(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMdmSupported property value. Indicates if the setting is supported by Intune or not
        Args:
            value: Value to set for the isMdmSupported property.
        """
        self._is_mdm_supported = value
    
    @property
    def mdm_csp_name(self,) -> Optional[str]:
        """
        Gets the mdmCspName property value. The CSP name this group policy setting maps to.
        Returns: Optional[str]
        """
        return self._mdm_csp_name
    
    @mdm_csp_name.setter
    def mdm_csp_name(self,value: Optional[str] = None) -> None:
        """
        Sets the mdmCspName property value. The CSP name this group policy setting maps to.
        Args:
            value: Value to set for the mdmCspName property.
        """
        self._mdm_csp_name = value
    
    @property
    def mdm_minimum_o_s_version(self,) -> Optional[int]:
        """
        Gets the mdmMinimumOSVersion property value. The minimum OS version this mdm setting supports.
        Returns: Optional[int]
        """
        return self._mdm_minimum_o_s_version
    
    @mdm_minimum_o_s_version.setter
    def mdm_minimum_o_s_version(self,value: Optional[int] = None) -> None:
        """
        Sets the mdmMinimumOSVersion property value. The minimum OS version this mdm setting supports.
        Args:
            value: Value to set for the mdmMinimumOSVersion property.
        """
        self._mdm_minimum_o_s_version = value
    
    @property
    def mdm_setting_uri(self,) -> Optional[str]:
        """
        Gets the mdmSettingUri property value. The MDM CSP URI this group policy setting maps to.
        Returns: Optional[str]
        """
        return self._mdm_setting_uri
    
    @mdm_setting_uri.setter
    def mdm_setting_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the mdmSettingUri property value. The MDM CSP URI this group policy setting maps to.
        Args:
            value: Value to set for the mdmSettingUri property.
        """
        self._mdm_setting_uri = value
    
    @property
    def mdm_supported_state(self,) -> Optional[mdm_supported_state.MdmSupportedState]:
        """
        Gets the mdmSupportedState property value. Mdm Support Status of the setting.
        Returns: Optional[mdm_supported_state.MdmSupportedState]
        """
        return self._mdm_supported_state
    
    @mdm_supported_state.setter
    def mdm_supported_state(self,value: Optional[mdm_supported_state.MdmSupportedState] = None) -> None:
        """
        Sets the mdmSupportedState property value. Mdm Support Status of the setting.
        Args:
            value: Value to set for the mdmSupportedState property.
        """
        self._mdm_supported_state = value
    
    @property
    def parent_id(self,) -> Optional[str]:
        """
        Gets the parentId property value. Parent Id of the group policy setting.
        Returns: Optional[str]
        """
        return self._parent_id
    
    @parent_id.setter
    def parent_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentId property value. Parent Id of the group policy setting.
        Args:
            value: Value to set for the parentId property.
        """
        self._parent_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("admxSettingDefinitionId", self.admx_setting_definition_id)
        writer.write_collection_of_primitive_values("childIdList", self.child_id_list)
        writer.write_str_value("intuneSettingDefinitionId", self.intune_setting_definition_id)
        writer.write_collection_of_primitive_values("intuneSettingUriList", self.intune_setting_uri_list)
        writer.write_bool_value("isMdmSupported", self.is_mdm_supported)
        writer.write_str_value("mdmCspName", self.mdm_csp_name)
        writer.write_int_value("mdmMinimumOSVersion", self.mdm_minimum_o_s_version)
        writer.write_str_value("mdmSettingUri", self.mdm_setting_uri)
        writer.write_enum_value("mdmSupportedState", self.mdm_supported_state)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_str_value("settingCategory", self.setting_category)
        writer.write_str_value("settingDisplayName", self.setting_display_name)
        writer.write_str_value("settingDisplayValue", self.setting_display_value)
        writer.write_str_value("settingDisplayValueType", self.setting_display_value_type)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_enum_value("settingScope", self.setting_scope)
        writer.write_enum_value("settingType", self.setting_type)
        writer.write_str_value("settingValue", self.setting_value)
        writer.write_str_value("settingValueDisplayUnits", self.setting_value_display_units)
        writer.write_str_value("settingValueType", self.setting_value_type)
    
    @property
    def setting_category(self,) -> Optional[str]:
        """
        Gets the settingCategory property value. The category the group policy setting is in.
        Returns: Optional[str]
        """
        return self._setting_category
    
    @setting_category.setter
    def setting_category(self,value: Optional[str] = None) -> None:
        """
        Sets the settingCategory property value. The category the group policy setting is in.
        Args:
            value: Value to set for the settingCategory property.
        """
        self._setting_category = value
    
    @property
    def setting_display_name(self,) -> Optional[str]:
        """
        Gets the settingDisplayName property value. The display name of this group policy setting.
        Returns: Optional[str]
        """
        return self._setting_display_name
    
    @setting_display_name.setter
    def setting_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDisplayName property value. The display name of this group policy setting.
        Args:
            value: Value to set for the settingDisplayName property.
        """
        self._setting_display_name = value
    
    @property
    def setting_display_value(self,) -> Optional[str]:
        """
        Gets the settingDisplayValue property value. The display value of this group policy setting.
        Returns: Optional[str]
        """
        return self._setting_display_value
    
    @setting_display_value.setter
    def setting_display_value(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDisplayValue property value. The display value of this group policy setting.
        Args:
            value: Value to set for the settingDisplayValue property.
        """
        self._setting_display_value = value
    
    @property
    def setting_display_value_type(self,) -> Optional[str]:
        """
        Gets the settingDisplayValueType property value. The display value type of this group policy setting.
        Returns: Optional[str]
        """
        return self._setting_display_value_type
    
    @setting_display_value_type.setter
    def setting_display_value_type(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDisplayValueType property value. The display value type of this group policy setting.
        Args:
            value: Value to set for the settingDisplayValueType property.
        """
        self._setting_display_value_type = value
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. The name of this group policy setting.
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. The name of this group policy setting.
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    
    @property
    def setting_scope(self,) -> Optional[group_policy_setting_scope.GroupPolicySettingScope]:
        """
        Gets the settingScope property value. Scope of the group policy setting.
        Returns: Optional[group_policy_setting_scope.GroupPolicySettingScope]
        """
        return self._setting_scope
    
    @setting_scope.setter
    def setting_scope(self,value: Optional[group_policy_setting_scope.GroupPolicySettingScope] = None) -> None:
        """
        Sets the settingScope property value. Scope of the group policy setting.
        Args:
            value: Value to set for the settingScope property.
        """
        self._setting_scope = value
    
    @property
    def setting_type(self,) -> Optional[group_policy_setting_type.GroupPolicySettingType]:
        """
        Gets the settingType property value. Setting type of the group policy.
        Returns: Optional[group_policy_setting_type.GroupPolicySettingType]
        """
        return self._setting_type
    
    @setting_type.setter
    def setting_type(self,value: Optional[group_policy_setting_type.GroupPolicySettingType] = None) -> None:
        """
        Sets the settingType property value. Setting type of the group policy.
        Args:
            value: Value to set for the settingType property.
        """
        self._setting_type = value
    
    @property
    def setting_value(self,) -> Optional[str]:
        """
        Gets the settingValue property value. The value of this group policy setting.
        Returns: Optional[str]
        """
        return self._setting_value
    
    @setting_value.setter
    def setting_value(self,value: Optional[str] = None) -> None:
        """
        Sets the settingValue property value. The value of this group policy setting.
        Args:
            value: Value to set for the settingValue property.
        """
        self._setting_value = value
    
    @property
    def setting_value_display_units(self,) -> Optional[str]:
        """
        Gets the settingValueDisplayUnits property value. The display units of this group policy setting value
        Returns: Optional[str]
        """
        return self._setting_value_display_units
    
    @setting_value_display_units.setter
    def setting_value_display_units(self,value: Optional[str] = None) -> None:
        """
        Sets the settingValueDisplayUnits property value. The display units of this group policy setting value
        Args:
            value: Value to set for the settingValueDisplayUnits property.
        """
        self._setting_value_display_units = value
    
    @property
    def setting_value_type(self,) -> Optional[str]:
        """
        Gets the settingValueType property value. The value type of this group policy setting.
        Returns: Optional[str]
        """
        return self._setting_value_type
    
    @setting_value_type.setter
    def setting_value_type(self,value: Optional[str] = None) -> None:
        """
        Sets the settingValueType property value. The value type of this group policy setting.
        Args:
            value: Value to set for the settingValueType property.
        """
        self._setting_value_type = value
    

