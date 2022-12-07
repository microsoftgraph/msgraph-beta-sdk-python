from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_enrollment_profile_assignment = lazy_import('msgraph.generated.models.apple_enrollment_profile_assignment')
apple_owner_type_enrollment_type = lazy_import('msgraph.generated.models.apple_owner_type_enrollment_type')
apple_user_initiated_enrollment_type = lazy_import('msgraph.generated.models.apple_user_initiated_enrollment_type')
device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')
entity = lazy_import('msgraph.generated.models.entity')

class AppleUserInitiatedEnrollmentProfile(entity.Entity):
    """
    The enrollmentProfile resource represents a collection of configurations which must be provided pre-enrollment to enable enrolling certain devices whose identities have been pre-staged. Pre-staged device identities are assigned to this type of profile to apply the profile's configurations at enrollment of the corresponding device.
    """
    @property
    def assignments(self,) -> Optional[List[apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment]]:
        """
        Gets the assignments property value. The list of assignments for this profile.
        Returns: Optional[List[apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for this profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def available_enrollment_type_options(self,) -> Optional[List[apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType]]:
        """
        Gets the availableEnrollmentTypeOptions property value. List of available enrollment type options
        Returns: Optional[List[apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType]]
        """
        return self._available_enrollment_type_options
    
    @available_enrollment_type_options.setter
    def available_enrollment_type_options(self,value: Optional[List[apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType]] = None) -> None:
        """
        Sets the availableEnrollmentTypeOptions property value. List of available enrollment type options
        Args:
            value: Value to set for the availableEnrollmentTypeOptions property.
        """
        self._available_enrollment_type_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appleUserInitiatedEnrollmentProfile and sets the default values.
        """
        super().__init__()
        # The list of assignments for this profile.
        self._assignments: Optional[List[apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment]] = None
        # List of available enrollment type options
        self._available_enrollment_type_options: Optional[List[apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType]] = None
        # Profile creation time
        self._created_date_time: Optional[datetime] = None
        # The defaultEnrollmentType property
        self._default_enrollment_type: Optional[apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType] = None
        # Description of the profile
        self._description: Optional[str] = None
        # Name of the profile
        self._display_name: Optional[str] = None
        # Profile last modified time
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types.
        self._platform: Optional[device_platform_type.DevicePlatformType] = None
        # Priority, 0 is highest
        self._priority: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Profile creation time
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Profile creation time
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleUserInitiatedEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleUserInitiatedEnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppleUserInitiatedEnrollmentProfile()
    
    @property
    def default_enrollment_type(self,) -> Optional[apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType]:
        """
        Gets the defaultEnrollmentType property value. The defaultEnrollmentType property
        Returns: Optional[apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType]
        """
        return self._default_enrollment_type
    
    @default_enrollment_type.setter
    def default_enrollment_type(self,value: Optional[apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType] = None) -> None:
        """
        Sets the defaultEnrollmentType property value. The defaultEnrollmentType property
        Args:
            value: Value to set for the defaultEnrollmentType property.
        """
        self._default_enrollment_type = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the profile
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the profile
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the profile
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the profile
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment)),
            "available_enrollment_type_options": lambda n : setattr(self, 'available_enrollment_type_options', n.get_collection_of_object_values(apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "default_enrollment_type": lambda n : setattr(self, 'default_enrollment_type', n.get_enum_value(apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Profile last modified time
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Profile last modified time
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the platform property value. Supported platform types.
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the platform property value. Supported platform types.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Priority, 0 is highest
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Priority, 0 is highest
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
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
        writer.write_collection_of_object_values("availableEnrollmentTypeOptions", self.available_enrollment_type_options)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("defaultEnrollmentType", self.default_enrollment_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platform", self.platform)
        writer.write_int_value("priority", self.priority)
    

