from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

enrollment_state = lazy_import('msgraph.generated.models.enrollment_state')
entity = lazy_import('msgraph.generated.models.entity')
imported_device_identity_type = lazy_import('msgraph.generated.models.imported_device_identity_type')
platform = lazy_import('msgraph.generated.models.platform')

class ImportedDeviceIdentity(entity.Entity):
    """
    The importedDeviceIdentity resource represents a unique hardware identity of a device that has been pre-staged for pre-enrollment configuration.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new importedDeviceIdentity and sets the default values.
        """
        super().__init__()
        # Created Date Time of the device
        self._created_date_time: Optional[datetime] = None
        # The description of the device
        self._description: Optional[str] = None
        # The enrollmentState property
        self._enrollment_state: Optional[enrollment_state.EnrollmentState] = None
        # Imported Device Identifier
        self._imported_device_identifier: Optional[str] = None
        # The importedDeviceIdentityType property
        self._imported_device_identity_type: Optional[imported_device_identity_type.ImportedDeviceIdentityType] = None
        # Last Contacted Date Time of the device
        self._last_contacted_date_time: Optional[datetime] = None
        # Last Modified DateTime of the description
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The platform property
        self._platform: Optional[platform.Platform] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedDeviceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportedDeviceIdentity()
    
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
            "enrollment_state": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(enrollment_state.EnrollmentState)),
            "imported_device_identifier": lambda n : setattr(self, 'imported_device_identifier', n.get_str_value()),
            "imported_device_identity_type": lambda n : setattr(self, 'imported_device_identity_type', n.get_enum_value(imported_device_identity_type.ImportedDeviceIdentityType)),
            "last_contacted_date_time": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(platform.Platform)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def imported_device_identifier(self,) -> Optional[str]:
        """
        Gets the importedDeviceIdentifier property value. Imported Device Identifier
        Returns: Optional[str]
        """
        return self._imported_device_identifier
    
    @imported_device_identifier.setter
    def imported_device_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the importedDeviceIdentifier property value. Imported Device Identifier
        Args:
            value: Value to set for the importedDeviceIdentifier property.
        """
        self._imported_device_identifier = value
    
    @property
    def imported_device_identity_type(self,) -> Optional[imported_device_identity_type.ImportedDeviceIdentityType]:
        """
        Gets the importedDeviceIdentityType property value. The importedDeviceIdentityType property
        Returns: Optional[imported_device_identity_type.ImportedDeviceIdentityType]
        """
        return self._imported_device_identity_type
    
    @imported_device_identity_type.setter
    def imported_device_identity_type(self,value: Optional[imported_device_identity_type.ImportedDeviceIdentityType] = None) -> None:
        """
        Sets the importedDeviceIdentityType property value. The importedDeviceIdentityType property
        Args:
            value: Value to set for the importedDeviceIdentityType property.
        """
        self._imported_device_identity_type = value
    
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
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last Modified DateTime of the description
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last Modified DateTime of the description
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
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
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_str_value("importedDeviceIdentifier", self.imported_device_identifier)
        writer.write_enum_value("importedDeviceIdentityType", self.imported_device_identity_type)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platform", self.platform)
    

