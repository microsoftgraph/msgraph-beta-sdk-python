from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, expedited_windows_quality_update_settings, windows_quality_update_profile_assignment

from . import entity

class WindowsQualityUpdateProfile(entity.Entity):
    """
    Windows Quality Update Profile
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsQualityUpdateProfile and sets the default values.
        """
        super().__init__()
        # The list of group assignments of the profile.
        self._assignments: Optional[List[windows_quality_update_profile_assignment.WindowsQualityUpdateProfileAssignment]] = None
        # The date time that the profile was created.
        self._created_date_time: Optional[datetime] = None
        # Friendly display name of the quality update profile deployable content
        self._deployable_content_display_name: Optional[str] = None
        # The description of the profile which is specified by the user.
        self._description: Optional[str] = None
        # The display name for the profile.
        self._display_name: Optional[str] = None
        # Expedited update settings.
        self._expedited_update_settings: Optional[expedited_windows_quality_update_settings.ExpeditedWindowsQualityUpdateSettings] = None
        # The date time that the profile was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Friendly release date to display for a Quality Update release
        self._release_date_display_name: Optional[str] = None
        # List of Scope Tags for this Quality Update entity.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @property
    def assignments(self,) -> Optional[List[windows_quality_update_profile_assignment.WindowsQualityUpdateProfileAssignment]]:
        """
        Gets the assignments property value. The list of group assignments of the profile.
        Returns: Optional[List[windows_quality_update_profile_assignment.WindowsQualityUpdateProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[windows_quality_update_profile_assignment.WindowsQualityUpdateProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments of the profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
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
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsQualityUpdateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsQualityUpdateProfile()
    
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
            value: Value to set for the deployable_content_display_name property.
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
        Gets the displayName property value. The display name for the profile.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the profile.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def expedited_update_settings(self,) -> Optional[expedited_windows_quality_update_settings.ExpeditedWindowsQualityUpdateSettings]:
        """
        Gets the expeditedUpdateSettings property value. Expedited update settings.
        Returns: Optional[expedited_windows_quality_update_settings.ExpeditedWindowsQualityUpdateSettings]
        """
        return self._expedited_update_settings
    
    @expedited_update_settings.setter
    def expedited_update_settings(self,value: Optional[expedited_windows_quality_update_settings.ExpeditedWindowsQualityUpdateSettings] = None) -> None:
        """
        Sets the expeditedUpdateSettings property value. Expedited update settings.
        Args:
            value: Value to set for the expedited_update_settings property.
        """
        self._expedited_update_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, expedited_windows_quality_update_settings, windows_quality_update_profile_assignment

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(windows_quality_update_profile_assignment.WindowsQualityUpdateProfileAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployableContentDisplayName": lambda n : setattr(self, 'deployable_content_display_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expeditedUpdateSettings": lambda n : setattr(self, 'expedited_update_settings', n.get_object_value(expedited_windows_quality_update_settings.ExpeditedWindowsQualityUpdateSettings)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "releaseDateDisplayName": lambda n : setattr(self, 'release_date_display_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def release_date_display_name(self,) -> Optional[str]:
        """
        Gets the releaseDateDisplayName property value. Friendly release date to display for a Quality Update release
        Returns: Optional[str]
        """
        return self._release_date_display_name
    
    @release_date_display_name.setter
    def release_date_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the releaseDateDisplayName property value. Friendly release date to display for a Quality Update release
        Args:
            value: Value to set for the release_date_display_name property.
        """
        self._release_date_display_name = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Quality Update entity.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Quality Update entity.
        Args:
            value: Value to set for the role_scope_tag_ids property.
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
        writer.write_str_value("deployableContentDisplayName", self.deployable_content_display_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("expeditedUpdateSettings", self.expedited_update_settings)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("releaseDateDisplayName", self.release_date_display_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

