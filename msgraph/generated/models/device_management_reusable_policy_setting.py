from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_policy = lazy_import('msgraph.generated.models.device_management_configuration_policy')
device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementReusablePolicySetting(entity.Entity):
    """
    Graph model for a reusable setting
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementReusablePolicySetting and sets the default values.
        """
        super().__init__()
        # reusable setting creation date and time. This property is read-only.
        self._created_date_time: Optional[datetime] = None
        # reusable setting description supplied by user.
        self._description: Optional[str] = None
        # reusable setting display name supplied by user.
        self._display_name: Optional[str] = None
        # date and time when reusable setting was last modified. This property is read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # configuration policies referencing the current reusable setting. This property is read-only.
        self._referencing_configuration_policies: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]] = None
        # count of configuration policies referencing the current reusable setting. Valid values 0 to 2147483647. This property is read-only.
        self._referencing_configuration_policy_count: Optional[int] = None
        # setting definition id associated with this reusable setting.
        self._setting_definition_id: Optional[str] = None
        # reusable setting configuration instance
        self._setting_instance: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance] = None
        # version number for reusable setting. Valid values 0 to 2147483647. This property is read-only.
        self._version: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. reusable setting creation date and time. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. reusable setting creation date and time. This property is read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementReusablePolicySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementReusablePolicySetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementReusablePolicySetting()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. reusable setting description supplied by user.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. reusable setting description supplied by user.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. reusable setting display name supplied by user.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. reusable setting display name supplied by user.
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
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "referencing_configuration_policies": lambda n : setattr(self, 'referencing_configuration_policies', n.get_collection_of_object_values(device_management_configuration_policy.DeviceManagementConfigurationPolicy)),
            "referencing_configuration_policy_count": lambda n : setattr(self, 'referencing_configuration_policy_count', n.get_int_value()),
            "setting_definition_id": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "setting_instance": lambda n : setattr(self, 'setting_instance', n.get_object_value(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. date and time when reusable setting was last modified. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. date and time when reusable setting was last modified. This property is read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def referencing_configuration_policies(self,) -> Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]]:
        """
        Gets the referencingConfigurationPolicies property value. configuration policies referencing the current reusable setting. This property is read-only.
        Returns: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]]
        """
        return self._referencing_configuration_policies
    
    @referencing_configuration_policies.setter
    def referencing_configuration_policies(self,value: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]] = None) -> None:
        """
        Sets the referencingConfigurationPolicies property value. configuration policies referencing the current reusable setting. This property is read-only.
        Args:
            value: Value to set for the referencingConfigurationPolicies property.
        """
        self._referencing_configuration_policies = value
    
    @property
    def referencing_configuration_policy_count(self,) -> Optional[int]:
        """
        Gets the referencingConfigurationPolicyCount property value. count of configuration policies referencing the current reusable setting. Valid values 0 to 2147483647. This property is read-only.
        Returns: Optional[int]
        """
        return self._referencing_configuration_policy_count
    
    @referencing_configuration_policy_count.setter
    def referencing_configuration_policy_count(self,value: Optional[int] = None) -> None:
        """
        Sets the referencingConfigurationPolicyCount property value. count of configuration policies referencing the current reusable setting. Valid values 0 to 2147483647. This property is read-only.
        Args:
            value: Value to set for the referencingConfigurationPolicyCount property.
        """
        self._referencing_configuration_policy_count = value
    
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
        writer.write_collection_of_object_values("referencingConfigurationPolicies", self.referencing_configuration_policies)
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_object_value("settingInstance", self.setting_instance)
    
    @property
    def setting_definition_id(self,) -> Optional[str]:
        """
        Gets the settingDefinitionId property value. setting definition id associated with this reusable setting.
        Returns: Optional[str]
        """
        return self._setting_definition_id
    
    @setting_definition_id.setter
    def setting_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDefinitionId property value. setting definition id associated with this reusable setting.
        Args:
            value: Value to set for the settingDefinitionId property.
        """
        self._setting_definition_id = value
    
    @property
    def setting_instance(self,) -> Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]:
        """
        Gets the settingInstance property value. reusable setting configuration instance
        Returns: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]
        """
        return self._setting_instance
    
    @setting_instance.setter
    def setting_instance(self,value: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance] = None) -> None:
        """
        Sets the settingInstance property value. reusable setting configuration instance
        Args:
            value: Value to set for the settingInstance property.
        """
        self._setting_instance = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. version number for reusable setting. Valid values 0 to 2147483647. This property is read-only.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. version number for reusable setting. Valid values 0 to 2147483647. This property is read-only.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

