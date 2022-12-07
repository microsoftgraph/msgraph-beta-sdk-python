from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_intent_assignment = lazy_import('msgraph.generated.models.device_management_intent_assignment')
device_management_intent_device_setting_state_summary = lazy_import('msgraph.generated.models.device_management_intent_device_setting_state_summary')
device_management_intent_device_state = lazy_import('msgraph.generated.models.device_management_intent_device_state')
device_management_intent_device_state_summary = lazy_import('msgraph.generated.models.device_management_intent_device_state_summary')
device_management_intent_setting_category = lazy_import('msgraph.generated.models.device_management_intent_setting_category')
device_management_intent_user_state = lazy_import('msgraph.generated.models.device_management_intent_user_state')
device_management_intent_user_state_summary = lazy_import('msgraph.generated.models.device_management_intent_user_state_summary')
device_management_setting_instance = lazy_import('msgraph.generated.models.device_management_setting_instance')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementIntent(entity.Entity):
    """
    Entity that represents an intent to apply settings to a device
    """
    @property
    def assignments(self,) -> Optional[List[device_management_intent_assignment.DeviceManagementIntentAssignment]]:
        """
        Gets the assignments property value. Collection of assignments
        Returns: Optional[List[device_management_intent_assignment.DeviceManagementIntentAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_management_intent_assignment.DeviceManagementIntentAssignment]] = None) -> None:
        """
        Sets the assignments property value. Collection of assignments
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def categories(self,) -> Optional[List[device_management_intent_setting_category.DeviceManagementIntentSettingCategory]]:
        """
        Gets the categories property value. Collection of setting categories within the intent
        Returns: Optional[List[device_management_intent_setting_category.DeviceManagementIntentSettingCategory]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[device_management_intent_setting_category.DeviceManagementIntentSettingCategory]] = None) -> None:
        """
        Sets the categories property value. Collection of setting categories within the intent
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementIntent and sets the default values.
        """
        super().__init__()
        # Collection of assignments
        self._assignments: Optional[List[device_management_intent_assignment.DeviceManagementIntentAssignment]] = None
        # Collection of setting categories within the intent
        self._categories: Optional[List[device_management_intent_setting_category.DeviceManagementIntentSettingCategory]] = None
        # The user given description
        self._description: Optional[str] = None
        # Collection of settings and their states and counts of devices that belong to corresponding state for all settings within the intent
        self._device_setting_state_summaries: Optional[List[device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary]] = None
        # Collection of states of all devices that the intent is applied to
        self._device_states: Optional[List[device_management_intent_device_state.DeviceManagementIntentDeviceState]] = None
        # A summary of device states and counts of devices that belong to corresponding state for all devices that the intent is applied to
        self._device_state_summary: Optional[device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary] = None
        # The user given display name
        self._display_name: Optional[str] = None
        # Signifies whether or not the intent is assigned to users
        self._is_assigned: Optional[bool] = None
        # When the intent was last modified
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Collection of all settings to be applied
        self._settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
        # The ID of the template this intent was created from (if any)
        self._template_id: Optional[str] = None
        # Collection of states of all users that the intent is applied to
        self._user_states: Optional[List[device_management_intent_user_state.DeviceManagementIntentUserState]] = None
        # A summary of user states and counts of users that belong to corresponding state for all users that the intent is applied to
        self._user_state_summary: Optional[device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary] = None
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The user given description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The user given description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_setting_state_summaries(self,) -> Optional[List[device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary]]:
        """
        Gets the deviceSettingStateSummaries property value. Collection of settings and their states and counts of devices that belong to corresponding state for all settings within the intent
        Returns: Optional[List[device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary]]
        """
        return self._device_setting_state_summaries
    
    @device_setting_state_summaries.setter
    def device_setting_state_summaries(self,value: Optional[List[device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary]] = None) -> None:
        """
        Sets the deviceSettingStateSummaries property value. Collection of settings and their states and counts of devices that belong to corresponding state for all settings within the intent
        Args:
            value: Value to set for the deviceSettingStateSummaries property.
        """
        self._device_setting_state_summaries = value
    
    @property
    def device_states(self,) -> Optional[List[device_management_intent_device_state.DeviceManagementIntentDeviceState]]:
        """
        Gets the deviceStates property value. Collection of states of all devices that the intent is applied to
        Returns: Optional[List[device_management_intent_device_state.DeviceManagementIntentDeviceState]]
        """
        return self._device_states
    
    @device_states.setter
    def device_states(self,value: Optional[List[device_management_intent_device_state.DeviceManagementIntentDeviceState]] = None) -> None:
        """
        Sets the deviceStates property value. Collection of states of all devices that the intent is applied to
        Args:
            value: Value to set for the deviceStates property.
        """
        self._device_states = value
    
    @property
    def device_state_summary(self,) -> Optional[device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary]:
        """
        Gets the deviceStateSummary property value. A summary of device states and counts of devices that belong to corresponding state for all devices that the intent is applied to
        Returns: Optional[device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary]
        """
        return self._device_state_summary
    
    @device_state_summary.setter
    def device_state_summary(self,value: Optional[device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary] = None) -> None:
        """
        Sets the deviceStateSummary property value. A summary of device states and counts of devices that belong to corresponding state for all devices that the intent is applied to
        Args:
            value: Value to set for the deviceStateSummary property.
        """
        self._device_state_summary = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The user given display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The user given display name
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_intent_assignment.DeviceManagementIntentAssignment)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(device_management_intent_setting_category.DeviceManagementIntentSettingCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_setting_state_summaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(device_management_intent_device_setting_state_summary.DeviceManagementIntentDeviceSettingStateSummary)),
            "device_states": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(device_management_intent_device_state.DeviceManagementIntentDeviceState)),
            "device_state_summary": lambda n : setattr(self, 'device_state_summary', n.get_object_value(device_management_intent_device_state_summary.DeviceManagementIntentDeviceStateSummary)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_assigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "user_states": lambda n : setattr(self, 'user_states', n.get_collection_of_object_values(device_management_intent_user_state.DeviceManagementIntentUserState)),
            "user_state_summary": lambda n : setattr(self, 'user_state_summary', n.get_object_value(device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_assigned(self,) -> Optional[bool]:
        """
        Gets the isAssigned property value. Signifies whether or not the intent is assigned to users
        Returns: Optional[bool]
        """
        return self._is_assigned
    
    @is_assigned.setter
    def is_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssigned property value. Signifies whether or not the intent is assigned to users
        Args:
            value: Value to set for the isAssigned property.
        """
        self._is_assigned = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. When the intent was last modified
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. When the intent was last modified
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
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
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_str_value("templateId", self.template_id)
        writer.write_collection_of_object_values("userStates", self.user_states)
        writer.write_object_value("userStateSummary", self.user_state_summary)
    
    @property
    def settings(self,) -> Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]:
        """
        Gets the settings property value. Collection of all settings to be applied
        Returns: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None) -> None:
        """
        Sets the settings property value. Collection of all settings to be applied
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. The ID of the template this intent was created from (if any)
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. The ID of the template this intent was created from (if any)
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    
    @property
    def user_states(self,) -> Optional[List[device_management_intent_user_state.DeviceManagementIntentUserState]]:
        """
        Gets the userStates property value. Collection of states of all users that the intent is applied to
        Returns: Optional[List[device_management_intent_user_state.DeviceManagementIntentUserState]]
        """
        return self._user_states
    
    @user_states.setter
    def user_states(self,value: Optional[List[device_management_intent_user_state.DeviceManagementIntentUserState]] = None) -> None:
        """
        Sets the userStates property value. Collection of states of all users that the intent is applied to
        Args:
            value: Value to set for the userStates property.
        """
        self._user_states = value
    
    @property
    def user_state_summary(self,) -> Optional[device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary]:
        """
        Gets the userStateSummary property value. A summary of user states and counts of users that belong to corresponding state for all users that the intent is applied to
        Returns: Optional[device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary]
        """
        return self._user_state_summary
    
    @user_state_summary.setter
    def user_state_summary(self,value: Optional[device_management_intent_user_state_summary.DeviceManagementIntentUserStateSummary] = None) -> None:
        """
        Sets the userStateSummary property value. A summary of user states and counts of users that belong to corresponding state for all users that the intent is applied to
        Args:
            value: Value to set for the userStateSummary property.
        """
        self._user_state_summary = value
    

