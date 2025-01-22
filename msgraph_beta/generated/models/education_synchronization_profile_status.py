from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_synchronization_status import EducationSynchronizationStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationSynchronizationProfileStatus(Entity, Parsable):
    # The errorCount property
    error_count: Optional[int] = None
    # The lastActivityDateTime property
    last_activity_date_time: Optional[datetime.datetime] = None
    # The lastSynchronizationDateTime property
    last_synchronization_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[EducationSynchronizationStatus] = None
    # The statusMessage property
    status_message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationProfileStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationProfileStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationProfileStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_synchronization_status import EducationSynchronizationStatus
        from .entity import Entity

        from .education_synchronization_status import EducationSynchronizationStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "lastActivityDateTime": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "lastSynchronizationDateTime": lambda n : setattr(self, 'last_synchronization_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(EducationSynchronizationStatus)),
            "statusMessage": lambda n : setattr(self, 'status_message', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_datetime_value("lastSynchronizationDateTime", self.last_synchronization_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusMessage", self.status_message)
    

