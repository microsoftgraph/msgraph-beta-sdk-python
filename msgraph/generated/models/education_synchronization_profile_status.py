from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_synchronization_status = lazy_import('msgraph.generated.models.education_synchronization_status')
entity = lazy_import('msgraph.generated.models.entity')

class EducationSynchronizationProfileStatus(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new educationSynchronizationProfileStatus and sets the default values.
        """
        super().__init__()
        # Number of errors during synchronization.
        self._error_count: Optional[int] = None
        # Date and time when most recent changes were observed in the profile.
        self._last_activity_date_time: Optional[datetime] = None
        # Date and time of the most recent successful synchronization.
        self._last_synchronization_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of a sync. The possible values are: paused, inProgress, success, error, validationError, quarantined, unknownFutureValue, extracting, validating. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: extracting, validating.
        self._status: Optional[education_synchronization_status.EducationSynchronizationStatus] = None
        # Status message for the synchronization stage of the current profile.
        self._status_message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationProfileStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationProfileStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationProfileStatus()
    
    @property
    def error_count(self,) -> Optional[int]:
        """
        Gets the errorCount property value. Number of errors during synchronization.
        Returns: Optional[int]
        """
        return self._error_count
    
    @error_count.setter
    def error_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCount property value. Number of errors during synchronization.
        Args:
            value: Value to set for the errorCount property.
        """
        self._error_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error_count": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "last_activity_date_time": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "last_synchronization_date_time": lambda n : setattr(self, 'last_synchronization_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(education_synchronization_status.EducationSynchronizationStatus)),
            "status_message": lambda n : setattr(self, 'status_message', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActivityDateTime property value. Date and time when most recent changes were observed in the profile.
        Returns: Optional[datetime]
        """
        return self._last_activity_date_time
    
    @last_activity_date_time.setter
    def last_activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActivityDateTime property value. Date and time when most recent changes were observed in the profile.
        Args:
            value: Value to set for the lastActivityDateTime property.
        """
        self._last_activity_date_time = value
    
    @property
    def last_synchronization_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSynchronizationDateTime property value. Date and time of the most recent successful synchronization.
        Returns: Optional[datetime]
        """
        return self._last_synchronization_date_time
    
    @last_synchronization_date_time.setter
    def last_synchronization_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSynchronizationDateTime property value. Date and time of the most recent successful synchronization.
        Args:
            value: Value to set for the lastSynchronizationDateTime property.
        """
        self._last_synchronization_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_datetime_value("lastSynchronizationDateTime", self.last_synchronization_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusMessage", self.status_message)
    
    @property
    def status(self,) -> Optional[education_synchronization_status.EducationSynchronizationStatus]:
        """
        Gets the status property value. The status of a sync. The possible values are: paused, inProgress, success, error, validationError, quarantined, unknownFutureValue, extracting, validating. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: extracting, validating.
        Returns: Optional[education_synchronization_status.EducationSynchronizationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[education_synchronization_status.EducationSynchronizationStatus] = None) -> None:
        """
        Sets the status property value. The status of a sync. The possible values are: paused, inProgress, success, error, validationError, quarantined, unknownFutureValue, extracting, validating. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: extracting, validating.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def status_message(self,) -> Optional[str]:
        """
        Gets the statusMessage property value. Status message for the synchronization stage of the current profile.
        Returns: Optional[str]
        """
        return self._status_message
    
    @status_message.setter
    def status_message(self,value: Optional[str] = None) -> None:
        """
        Sets the statusMessage property value. Status message for the synchronization stage of the current profile.
        Args:
            value: Value to set for the statusMessage property.
        """
        self._status_message = value
    

