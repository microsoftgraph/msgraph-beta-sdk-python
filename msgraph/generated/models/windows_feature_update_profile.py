from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
windows_feature_update_profile_assignment = lazy_import('msgraph.generated.models.windows_feature_update_profile_assignment')
windows_update_rollout_settings = lazy_import('msgraph.generated.models.windows_update_rollout_settings')

class WindowsFeatureUpdateProfile(entity.Entity):
    """
    Windows Feature Update Profile
    """
    @property
    def assignments(self,) -> Optional[List[windows_feature_update_profile_assignment.WindowsFeatureUpdateProfileAssignment]]:
        """
        Gets the assignments property value. The list of group assignments of the profile.
        Returns: Optional[List[windows_feature_update_profile_assignment.WindowsFeatureUpdateProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[windows_feature_update_profile_assignment.WindowsFeatureUpdateProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments of the profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsFeatureUpdateProfile and sets the default values.
        """
        super().__init__()
        # The list of group assignments of the profile.
        self._assignments: Optional[List[windows_feature_update_profile_assignment.WindowsFeatureUpdateProfileAssignment]] = None
        # The date time that the profile was created.
        self._created_date_time: Optional[datetime] = None
        # Friendly display name of the quality update profile deployable content
        self._deployable_content_display_name: Optional[str] = None
        # The description of the profile which is specified by the user.
        self._description: Optional[str] = None
        # The display name of the profile.
        self._display_name: Optional[str] = None
        # The last supported date for a feature update
        self._end_of_support_date: Optional[datetime] = None
        # The feature update version that will be deployed to the devices targeted by this profile. The version could be any supported version for example 1709, 1803 or 1809 and so on.
        self._feature_update_version: Optional[str] = None
        # The date time that the profile was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Feature Update entity.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The windows update rollout settings, including offer start date time, offer end date time, and days between each set of offers.
        self._rollout_settings: Optional[windows_update_rollout_settings.WindowsUpdateRolloutSettings] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date time that the profile was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date time that the profile was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsFeatureUpdateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsFeatureUpdateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsFeatureUpdateProfile()
    
    @property
    def deployable_content_display_name(self,) -> Optional[str]:
        """
        Gets the deployableContentDisplayName property value. Friendly display name of the quality update profile deployable content
        Returns: Optional[str]
        """
        return self._deployable_content_display_name
    
    @deployable_content_display_name.setter
    def deployable_content_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deployableContentDisplayName property value. Friendly display name of the quality update profile deployable content
        Args:
            value: Value to set for the deployableContentDisplayName property.
        """
        self._deployable_content_display_name = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the profile which is specified by the user.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the profile which is specified by the user.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the profile.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the profile.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_of_support_date(self,) -> Optional[datetime]:
        """
        Gets the endOfSupportDate property value. The last supported date for a feature update
        Returns: Optional[datetime]
        """
        return self._end_of_support_date
    
    @end_of_support_date.setter
    def end_of_support_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endOfSupportDate property value. The last supported date for a feature update
        Args:
            value: Value to set for the endOfSupportDate property.
        """
        self._end_of_support_date = value
    
    @property
    def feature_update_version(self,) -> Optional[str]:
        """
        Gets the featureUpdateVersion property value. The feature update version that will be deployed to the devices targeted by this profile. The version could be any supported version for example 1709, 1803 or 1809 and so on.
        Returns: Optional[str]
        """
        return self._feature_update_version
    
    @feature_update_version.setter
    def feature_update_version(self,value: Optional[str] = None) -> None:
        """
        Sets the featureUpdateVersion property value. The feature update version that will be deployed to the devices targeted by this profile. The version could be any supported version for example 1709, 1803 or 1809 and so on.
        Args:
            value: Value to set for the featureUpdateVersion property.
        """
        self._feature_update_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(windows_feature_update_profile_assignment.WindowsFeatureUpdateProfileAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployable_content_display_name": lambda n : setattr(self, 'deployable_content_display_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_of_support_date": lambda n : setattr(self, 'end_of_support_date', n.get_datetime_value()),
            "feature_update_version": lambda n : setattr(self, 'feature_update_version', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "rollout_settings": lambda n : setattr(self, 'rollout_settings', n.get_object_value(windows_update_rollout_settings.WindowsUpdateRolloutSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date time that the profile was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date time that the profile was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Feature Update entity.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Feature Update entity.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    @property
    def rollout_settings(self,) -> Optional[windows_update_rollout_settings.WindowsUpdateRolloutSettings]:
        """
        Gets the rolloutSettings property value. The windows update rollout settings, including offer start date time, offer end date time, and days between each set of offers.
        Returns: Optional[windows_update_rollout_settings.WindowsUpdateRolloutSettings]
        """
        return self._rollout_settings
    
    @rollout_settings.setter
    def rollout_settings(self,value: Optional[windows_update_rollout_settings.WindowsUpdateRolloutSettings] = None) -> None:
        """
        Sets the rolloutSettings property value. The windows update rollout settings, including offer start date time, offer end date time, and days between each set of offers.
        Args:
            value: Value to set for the rolloutSettings property.
        """
        self._rollout_settings = value
    
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
        writer.write_str_value("deployableContentDisplayName", self.deployable_content_display_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endOfSupportDate", self.end_of_support_date)
        writer.write_str_value("featureUpdateVersion", self.feature_update_version)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_object_value("rolloutSettings", self.rollout_settings)
    

