from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_policy, device_management_configuration_setting_instance, entity

from . import entity

@dataclass
class DeviceManagementReusablePolicySetting(entity.Entity):
    """
    Graph model for a reusable setting
    """
    # reusable setting creation date and time. This property is read-only.
    created_date_time: Optional[datetime] = None
    # reusable setting description supplied by user.
    description: Optional[str] = None
    # reusable setting display name supplied by user.
    display_name: Optional[str] = None
    # date and time when reusable setting was last modified. This property is read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # configuration policies referencing the current reusable setting. This property is read-only.
    referencing_configuration_policies: Optional[List[device_management_configuration_policy.DeviceManagementConfigurationPolicy]] = None
    # count of configuration policies referencing the current reusable setting. Valid values 0 to 2147483647. This property is read-only.
    referencing_configuration_policy_count: Optional[int] = None
    # setting definition id associated with this reusable setting.
    setting_definition_id: Optional[str] = None
    # reusable setting configuration instance
    setting_instance: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance] = None
    # version number for reusable setting. Valid values 0 to 2147483647. This property is read-only.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementReusablePolicySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementReusablePolicySetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementReusablePolicySetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_policy, device_management_configuration_setting_instance, entity

        from . import device_management_configuration_policy, device_management_configuration_setting_instance, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "referencingConfigurationPolicies": lambda n : setattr(self, 'referencing_configuration_policies', n.get_collection_of_object_values(device_management_configuration_policy.DeviceManagementConfigurationPolicy)),
            "referencingConfigurationPolicyCount": lambda n : setattr(self, 'referencing_configuration_policy_count', n.get_int_value()),
            "settingDefinitionId": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "settingInstance": lambda n : setattr(self, 'setting_instance', n.get_object_value(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_object_values("referencingConfigurationPolicies", self.referencing_configuration_policies)
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_object_value("settingInstance", self.setting_instance)
    

