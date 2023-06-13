from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_enrollment_profile_assignment, apple_owner_type_enrollment_type, apple_user_initiated_enrollment_type, device_platform_type, entity

from . import entity

@dataclass
class AppleUserInitiatedEnrollmentProfile(entity.Entity):
    """
    The enrollmentProfile resource represents a collection of configurations which must be provided pre-enrollment to enable enrolling certain devices whose identities have been pre-staged. Pre-staged device identities are assigned to this type of profile to apply the profile's configurations at enrollment of the corresponding device.
    """
    # The list of assignments for this profile.
    assignments: Optional[List[apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment]] = None
    # List of available enrollment type options
    available_enrollment_type_options: Optional[List[apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType]] = None
    # Profile creation time
    created_date_time: Optional[datetime] = None
    # The defaultEnrollmentType property
    default_enrollment_type: Optional[apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType] = None
    # Description of the profile
    description: Optional[str] = None
    # Name of the profile
    display_name: Optional[str] = None
    # Profile last modified time
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types.
    platform: Optional[device_platform_type.DevicePlatformType] = None
    # Priority, 0 is highest
    priority: Optional[int] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_enrollment_profile_assignment, apple_owner_type_enrollment_type, apple_user_initiated_enrollment_type, device_platform_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(apple_enrollment_profile_assignment.AppleEnrollmentProfileAssignment)),
            "availableEnrollmentTypeOptions": lambda n : setattr(self, 'available_enrollment_type_options', n.get_collection_of_object_values(apple_owner_type_enrollment_type.AppleOwnerTypeEnrollmentType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultEnrollmentType": lambda n : setattr(self, 'default_enrollment_type', n.get_enum_value(apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        writer.write_collection_of_object_values("availableEnrollmentTypeOptions", self.available_enrollment_type_options)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("defaultEnrollmentType", self.default_enrollment_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platform", self.platform)
        writer.write_int_value("priority", self.priority)
    

