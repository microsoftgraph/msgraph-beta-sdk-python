from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_synchronization_status, entity

from . import entity

@dataclass
class EducationSynchronizationProfileStatus(entity.Entity):
    # Number of errors during synchronization.
    error_count: Optional[int] = None
    # Date and time when most recent changes were observed in the profile.
    last_activity_date_time: Optional[datetime] = None
    # Date and time of the most recent successful synchronization.
    last_synchronization_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of a sync. The possible values are: paused, inProgress, success, error, validationError, quarantined, unknownFutureValue, extracting, validating. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: extracting, validating.
    status: Optional[education_synchronization_status.EducationSynchronizationStatus] = None
    # Status message for the synchronization stage of the current profile.
    status_message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationProfileStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationProfileStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationProfileStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_synchronization_status, entity

        from . import education_synchronization_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "lastActivityDateTime": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "lastSynchronizationDateTime": lambda n : setattr(self, 'last_synchronization_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(education_synchronization_status.EducationSynchronizationStatus)),
            "statusMessage": lambda n : setattr(self, 'status_message', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_datetime_value("lastSynchronizationDateTime", self.last_synchronization_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusMessage", self.status_message)
    

