from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration_assignment = lazy_import('msgraph.generated.models.device_configuration_assignment')
device_configuration_device_overview = lazy_import('msgraph.generated.models.device_configuration_device_overview')
device_configuration_device_status = lazy_import('msgraph.generated.models.device_configuration_device_status')
device_configuration_group_assignment = lazy_import('msgraph.generated.models.device_configuration_group_assignment')
device_configuration_user_overview = lazy_import('msgraph.generated.models.device_configuration_user_overview')
device_configuration_user_status = lazy_import('msgraph.generated.models.device_configuration_user_status')
device_management_applicability_rule_device_mode = lazy_import('msgraph.generated.models.device_management_applicability_rule_device_mode')
device_management_applicability_rule_os_edition = lazy_import('msgraph.generated.models.device_management_applicability_rule_os_edition')
device_management_applicability_rule_os_version = lazy_import('msgraph.generated.models.device_management_applicability_rule_os_version')
entity = lazy_import('msgraph.generated.models.entity')
setting_state_device_summary = lazy_import('msgraph.generated.models.setting_state_device_summary')

class DeviceConfiguration(entity.Entity):
    """
    Device Configuration.
    """
    @property
    def assignments(self,) -> Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of assignments for the device configuration profile.
        Returns: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for the device configuration profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfiguration and sets the default values.
        """
        super().__init__()
        # The list of assignments for the device configuration profile.
        self._assignments: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the Device Configuration.
        self._description: Optional[str] = None
        # The device mode applicability rule for this Policy.
        self._device_management_applicability_rule_device_mode: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode] = None
        # The OS edition applicability for this Policy.
        self._device_management_applicability_rule_os_edition: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition] = None
        # The OS version applicability rule for this Policy.
        self._device_management_applicability_rule_os_version: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion] = None
        # Device Configuration Setting State Device Summary
        self._device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
        # Device configuration installation status by device.
        self._device_statuses: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None
        # Device Configuration devices status overview
        self._device_status_overview: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # The list of group assignments for the device configuration profile.
        self._group_assignments: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
        self._supports_scope_tags: Optional[bool] = None
        # Device configuration installation status by user.
        self._user_statuses: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None
        # Device Configuration users status overview
        self._user_status_overview: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None
        # Version of the device configuration.
        self._version: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin provided description of the Device Configuration.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin provided description of the Device Configuration.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_management_applicability_rule_device_mode(self,) -> Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode]:
        """
        Gets the deviceManagementApplicabilityRuleDeviceMode property value. The device mode applicability rule for this Policy.
        Returns: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode]
        """
        return self._device_management_applicability_rule_device_mode
    
    @device_management_applicability_rule_device_mode.setter
    def device_management_applicability_rule_device_mode(self,value: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode] = None) -> None:
        """
        Sets the deviceManagementApplicabilityRuleDeviceMode property value. The device mode applicability rule for this Policy.
        Args:
            value: Value to set for the deviceManagementApplicabilityRuleDeviceMode property.
        """
        self._device_management_applicability_rule_device_mode = value
    
    @property
    def device_management_applicability_rule_os_edition(self,) -> Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition]:
        """
        Gets the deviceManagementApplicabilityRuleOsEdition property value. The OS edition applicability for this Policy.
        Returns: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition]
        """
        return self._device_management_applicability_rule_os_edition
    
    @device_management_applicability_rule_os_edition.setter
    def device_management_applicability_rule_os_edition(self,value: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition] = None) -> None:
        """
        Sets the deviceManagementApplicabilityRuleOsEdition property value. The OS edition applicability for this Policy.
        Args:
            value: Value to set for the deviceManagementApplicabilityRuleOsEdition property.
        """
        self._device_management_applicability_rule_os_edition = value
    
    @property
    def device_management_applicability_rule_os_version(self,) -> Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion]:
        """
        Gets the deviceManagementApplicabilityRuleOsVersion property value. The OS version applicability rule for this Policy.
        Returns: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion]
        """
        return self._device_management_applicability_rule_os_version
    
    @device_management_applicability_rule_os_version.setter
    def device_management_applicability_rule_os_version(self,value: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion] = None) -> None:
        """
        Sets the deviceManagementApplicabilityRuleOsVersion property value. The OS version applicability rule for this Policy.
        Args:
            value: Value to set for the deviceManagementApplicabilityRuleOsVersion property.
        """
        self._device_management_applicability_rule_os_version = value
    
    @property
    def device_setting_state_summaries(self,) -> Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]:
        """
        Gets the deviceSettingStateSummaries property value. Device Configuration Setting State Device Summary
        Returns: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]
        """
        return self._device_setting_state_summaries
    
    @device_setting_state_summaries.setter
    def device_setting_state_summaries(self,value: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None) -> None:
        """
        Sets the deviceSettingStateSummaries property value. Device Configuration Setting State Device Summary
        Args:
            value: Value to set for the deviceSettingStateSummaries property.
        """
        self._device_setting_state_summaries = value
    
    @property
    def device_statuses(self,) -> Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]]:
        """
        Gets the deviceStatuses property value. Device configuration installation status by device.
        Returns: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. Device configuration installation status by device.
        Args:
            value: Value to set for the deviceStatuses property.
        """
        self._device_statuses = value
    
    @property
    def device_status_overview(self,) -> Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview]:
        """
        Gets the deviceStatusOverview property value. Device Configuration devices status overview
        Returns: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview]
        """
        return self._device_status_overview
    
    @device_status_overview.setter
    def device_status_overview(self,value: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None) -> None:
        """
        Sets the deviceStatusOverview property value. Device Configuration devices status overview
        Args:
            value: Value to set for the deviceStatusOverview property.
        """
        self._device_status_overview = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided name of the device configuration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided name of the device configuration.
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_configuration_assignment.DeviceConfigurationAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_management_applicability_rule_device_mode": lambda n : setattr(self, 'device_management_applicability_rule_device_mode', n.get_object_value(device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode)),
            "device_management_applicability_rule_os_edition": lambda n : setattr(self, 'device_management_applicability_rule_os_edition', n.get_object_value(device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition)),
            "device_management_applicability_rule_os_version": lambda n : setattr(self, 'device_management_applicability_rule_os_version', n.get_object_value(device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion)),
            "device_setting_state_summaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "device_statuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_configuration_device_status.DeviceConfigurationDeviceStatus)),
            "device_status_overview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_configuration_device_overview.DeviceConfigurationDeviceOverview)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group_assignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(device_configuration_group_assignment.DeviceConfigurationGroupAssignment)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supports_scope_tags": lambda n : setattr(self, 'supports_scope_tags', n.get_bool_value()),
            "user_statuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_configuration_user_status.DeviceConfigurationUserStatus)),
            "user_status_overview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_configuration_user_overview.DeviceConfigurationUserOverview)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_assignments(self,) -> Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]]:
        """
        Gets the groupAssignments property value. The list of group assignments for the device configuration profile.
        Returns: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]]
        """
        return self._group_assignments
    
    @group_assignments.setter
    def group_assignments(self,value: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None) -> None:
        """
        Sets the groupAssignments property value. The list of group assignments for the device configuration profile.
        Args:
            value: Value to set for the groupAssignments property.
        """
        self._group_assignments = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("deviceManagementApplicabilityRuleDeviceMode", self.device_management_applicability_rule_device_mode)
        writer.write_object_value("deviceManagementApplicabilityRuleOsEdition", self.device_management_applicability_rule_os_edition)
        writer.write_object_value("deviceManagementApplicabilityRuleOsVersion", self.device_management_applicability_rule_os_version)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_int_value("version", self.version)
    
    @property
    def supports_scope_tags(self,) -> Optional[bool]:
        """
        Gets the supportsScopeTags property value. Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
        Returns: Optional[bool]
        """
        return self._supports_scope_tags
    
    @supports_scope_tags.setter
    def supports_scope_tags(self,value: Optional[bool] = None) -> None:
        """
        Sets the supportsScopeTags property value. Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
        Args:
            value: Value to set for the supportsScopeTags property.
        """
        self._supports_scope_tags = value
    
    @property
    def user_statuses(self,) -> Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]]:
        """
        Gets the userStatuses property value. Device configuration installation status by user.
        Returns: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None) -> None:
        """
        Sets the userStatuses property value. Device configuration installation status by user.
        Args:
            value: Value to set for the userStatuses property.
        """
        self._user_statuses = value
    
    @property
    def user_status_overview(self,) -> Optional[device_configuration_user_overview.DeviceConfigurationUserOverview]:
        """
        Gets the userStatusOverview property value. Device Configuration users status overview
        Returns: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview]
        """
        return self._user_status_overview
    
    @user_status_overview.setter
    def user_status_overview(self,value: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None) -> None:
        """
        Sets the userStatusOverview property value. Device Configuration users status overview
        Args:
            value: Value to set for the userStatusOverview property.
        """
        self._user_status_overview = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the device configuration.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the device configuration.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

