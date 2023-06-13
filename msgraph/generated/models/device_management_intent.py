from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_intent_assignment, device_management_intent_device_setting_state_summary, device_management_intent_device_state, device_management_intent_device_state_summary, device_management_intent_setting_category, device_management_intent_user_state, device_management_intent_user_state_summary, device_management_setting_instance, entity

from . import entity

@dataclass
class DeviceManagementIntent(entity.Entity):
    """
    Entity that represents an intent to apply settings to a device
    """
    # Collection of assignments
    assignments: Optional[List[device_management_intent_assignment.DeviceManagementIntentAssignment]] = None
    # Collection of setting categories within the intent
    categories: Optional[List[device_management_intent_setting_category.DeviceManagementIntentSettingCategory]] = None
    # The user given description
    description: Optional[str] = None
    # Collection of settings and their states and counts of devices that belong to corresponding state for all settings within the intent
    device_setting_state_summaries: Optional[List[device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary]] = None
    # A summary of device states and counts of devices that belong to corresponding state for all devices that the intent is applied to
    device_state_summary: Optional[device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary] = None
    # Collection of states of all devices that the intent is applied to
    device_states: Optional[List[device_management_intent_device_state.DeviceManagementIntentDeviceState]] = None
    # The user given display name
    display_name: Optional[str] = None
    # Signifies whether or not the intent is assigned to users
    is_assigned: Optional[bool] = None
    # Signifies whether or not the intent is being migrated to the configurationPolicies endpoint
    is_migrating_to_configuration_policy: Optional[bool] = None
    # When the intent was last modified
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # Collection of all settings to be applied
    settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
    # The ID of the template this intent was created from (if any)
    template_id: Optional[str] = None
    # A summary of user states and counts of users that belong to corresponding state for all users that the intent is applied to
    user_state_summary: Optional[device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary] = None
    # Collection of states of all users that the intent is applied to
    user_states: Optional[List[device_management_intent_user_state.DeviceManagementIntentUserState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementIntent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementIntent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_intent_assignment, device_management_intent_device_setting_state_summary, device_management_intent_device_state, device_management_intent_device_state_summary, device_management_intent_setting_category, device_management_intent_user_state, device_management_intent_user_state_summary, device_management_setting_instance, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_intent_assignment.DeviceManagementIntentAssignment)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(device_management_intent_setting_category.DeviceManagementIntentSettingCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary)),
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(device_management_intent_device_state.DeviceManagementIntentDeviceState)),
            "deviceStateSummary": lambda n : setattr(self, 'device_state_summary', n.get_object_value(device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "isMigratingToConfigurationPolicy": lambda n : setattr(self, 'is_migrating_to_configuration_policy', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "userStates": lambda n : setattr(self, 'user_states', n.get_collection_of_object_values(device_management_intent_user_state.DeviceManagementIntentUserState)),
            "userStateSummary": lambda n : setattr(self, 'user_state_summary', n.get_object_value(device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_object_value("deviceStateSummary", self.device_state_summary)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_bool_value("isMigratingToConfigurationPolicy", self.is_migrating_to_configuration_policy)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_str_value("templateId", self.template_id)
        writer.write_collection_of_object_values("userStates", self.user_states)
        writer.write_object_value("userStateSummary", self.user_state_summary)
    

