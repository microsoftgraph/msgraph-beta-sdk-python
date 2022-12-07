from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_resource_access_profile_assignment = lazy_import('msgraph.generated.models.device_management_resource_access_profile_assignment')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementResourceAccessProfileBase(entity.Entity):
    """
    Base Profile Type for Resource Access
    """
    @property
    def assignments(self,) -> Optional[List[device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment]]:
        """
        Gets the assignments property value. The list of assignments for the device configuration profile.
        Returns: Optional[List[device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for the device configuration profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementResourceAccessProfileBase and sets the default values.
        """
        super().__init__()
        # The list of assignments for the device configuration profile.
        self._assignments: Optional[List[device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment]] = None
        # DateTime profile was created
        self._creation_date_time: Optional[datetime] = None
        # Profile description
        self._description: Optional[str] = None
        # Profile display name
        self._display_name: Optional[str] = None
        # DateTime profile was last modified
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Scope Tags
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Version of the profile
        self._version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementResourceAccessProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementResourceAccessProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementResourceAccessProfileBase()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. DateTime profile was created
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. DateTime profile was created
        Args:
            value: Value to set for the creationDateTime property.
        """
        self._creation_date_time = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Profile description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Profile description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Profile display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Profile display name
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment)),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime profile was last modified
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime profile was last modified
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. Scope Tags
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. Scope Tags
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
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("version", self.version)
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the profile
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the profile
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

