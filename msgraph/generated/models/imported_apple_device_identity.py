from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

discovery_source = lazy_import('msgraph.generated.models.discovery_source')
enrollment_state = lazy_import('msgraph.generated.models.enrollment_state')
entity = lazy_import('msgraph.generated.models.entity')
platform = lazy_import('msgraph.generated.models.platform')

class ImportedAppleDeviceIdentity(entity.Entity):
    """
    The importedAppleDeviceIdentity resource represents the imported device identity of an Apple device .
    """
    def __init__(self,) -> None:
        """
        Instantiates a new importedAppleDeviceIdentity and sets the default values.
        """
        super().__init__()
        # Created Date Time of the device
        self._created_date_time: Optional[datetime] = None
        # The description of the device
        self._description: Optional[str] = None
        # The discoverySource property
        self._discovery_source: Optional[discovery_source.DiscoverySource] = None
        # The enrollmentState property
        self._enrollment_state: Optional[enrollment_state.EnrollmentState] = None
        # Indicates if the device is deleted from Apple Business Manager
        self._is_deleted: Optional[bool] = None
        # Indicates if the Apple device is supervised. More information is at: https://support.apple.com/en-us/HT202837
        self._is_supervised: Optional[bool] = None
        # Last Contacted Date Time of the device
        self._last_contacted_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The platform property
        self._platform: Optional[platform.Platform] = None
        # The time enrollment profile was assigned to the device
        self._requested_enrollment_profile_assignment_date_time: Optional[datetime] = None
        # Enrollment profile Id admin intends to apply to the device during next enrollment
        self._requested_enrollment_profile_id: Optional[str] = None
        # Device serial number
        self._serial_number: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Created Date Time of the device
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Created Date Time of the device
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedAppleDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedAppleDeviceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportedAppleDeviceIdentity()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the device
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the device
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def discovery_source(self,) -> Optional[discovery_source.DiscoverySource]:
        """
        Gets the discoverySource property value. The discoverySource property
        Returns: Optional[discovery_source.DiscoverySource]
        """
        return self._discovery_source
    
    @discovery_source.setter
    def discovery_source(self,value: Optional[discovery_source.DiscoverySource] = None) -> None:
        """
        Sets the discoverySource property value. The discoverySource property
        Args:
            value: Value to set for the discoverySource property.
        """
        self._discovery_source = value
    
    @property
    def enrollment_state(self,) -> Optional[enrollment_state.EnrollmentState]:
        """
        Gets the enrollmentState property value. The enrollmentState property
        Returns: Optional[enrollment_state.EnrollmentState]
        """
        return self._enrollment_state
    
    @enrollment_state.setter
    def enrollment_state(self,value: Optional[enrollment_state.EnrollmentState] = None) -> None:
        """
        Sets the enrollmentState property value. The enrollmentState property
        Args:
            value: Value to set for the enrollmentState property.
        """
        self._enrollment_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discovery_source": lambda n : setattr(self, 'discovery_source', n.get_enum_value(discovery_source.DiscoverySource)),
            "enrollment_state": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(enrollment_state.EnrollmentState)),
            "is_deleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "is_supervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "last_contacted_date_time": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(platform.Platform)),
            "requested_enrollment_profile_assignment_date_time": lambda n : setattr(self, 'requested_enrollment_profile_assignment_date_time', n.get_datetime_value()),
            "requested_enrollment_profile_id": lambda n : setattr(self, 'requested_enrollment_profile_id', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_deleted(self,) -> Optional[bool]:
        """
        Gets the isDeleted property value. Indicates if the device is deleted from Apple Business Manager
        Returns: Optional[bool]
        """
        return self._is_deleted
    
    @is_deleted.setter
    def is_deleted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeleted property value. Indicates if the device is deleted from Apple Business Manager
        Args:
            value: Value to set for the isDeleted property.
        """
        self._is_deleted = value
    
    @property
    def is_supervised(self,) -> Optional[bool]:
        """
        Gets the isSupervised property value. Indicates if the Apple device is supervised. More information is at: https://support.apple.com/en-us/HT202837
        Returns: Optional[bool]
        """
        return self._is_supervised
    
    @is_supervised.setter
    def is_supervised(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSupervised property value. Indicates if the Apple device is supervised. More information is at: https://support.apple.com/en-us/HT202837
        Args:
            value: Value to set for the isSupervised property.
        """
        self._is_supervised = value
    
    @property
    def last_contacted_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastContactedDateTime property value. Last Contacted Date Time of the device
        Returns: Optional[datetime]
        """
        return self._last_contacted_date_time
    
    @last_contacted_date_time.setter
    def last_contacted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastContactedDateTime property value. Last Contacted Date Time of the device
        Args:
            value: Value to set for the lastContactedDateTime property.
        """
        self._last_contacted_date_time = value
    
    @property
    def platform(self,) -> Optional[platform.Platform]:
        """
        Gets the platform property value. The platform property
        Returns: Optional[platform.Platform]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[platform.Platform] = None) -> None:
        """
        Sets the platform property value. The platform property
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def requested_enrollment_profile_assignment_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestedEnrollmentProfileAssignmentDateTime property value. The time enrollment profile was assigned to the device
        Returns: Optional[datetime]
        """
        return self._requested_enrollment_profile_assignment_date_time
    
    @requested_enrollment_profile_assignment_date_time.setter
    def requested_enrollment_profile_assignment_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestedEnrollmentProfileAssignmentDateTime property value. The time enrollment profile was assigned to the device
        Args:
            value: Value to set for the requestedEnrollmentProfileAssignmentDateTime property.
        """
        self._requested_enrollment_profile_assignment_date_time = value
    
    @property
    def requested_enrollment_profile_id(self,) -> Optional[str]:
        """
        Gets the requestedEnrollmentProfileId property value. Enrollment profile Id admin intends to apply to the device during next enrollment
        Returns: Optional[str]
        """
        return self._requested_enrollment_profile_id
    
    @requested_enrollment_profile_id.setter
    def requested_enrollment_profile_id(self,value: Optional[str] = None) -> None:
        """
        Sets the requestedEnrollmentProfileId property value. Enrollment profile Id admin intends to apply to the device during next enrollment
        Args:
            value: Value to set for the requestedEnrollmentProfileId property.
        """
        self._requested_enrollment_profile_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("discoverySource", self.discovery_source)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_bool_value("isSupervised", self.is_supervised)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_enum_value("platform", self.platform)
        writer.write_datetime_value("requestedEnrollmentProfileAssignmentDateTime", self.requested_enrollment_profile_assignment_date_time)
        writer.write_str_value("requestedEnrollmentProfileId", self.requested_enrollment_profile_id)
        writer.write_str_value("serialNumber", self.serial_number)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. Device serial number
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. Device serial number
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    

