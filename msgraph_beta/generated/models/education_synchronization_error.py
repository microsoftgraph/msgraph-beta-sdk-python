from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationSynchronizationError(Entity):
    # Represents the sync entity (school, section, student, teacher).
    entry_type: Optional[str] = None
    # Represents the error code for this error.
    error_code: Optional[str] = None
    # Contains a description of the error.
    error_message: Optional[str] = None
    # The unique identifier for the entry.
    joining_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time of occurrence of this error.
    recorded_date_time: Optional[datetime.datetime] = None
    # The identifier of this error entry.
    reportable_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "entryType": lambda n : setattr(self, 'entry_type', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "joiningValue": lambda n : setattr(self, 'joining_value', n.get_str_value()),
            "recordedDateTime": lambda n : setattr(self, 'recorded_date_time', n.get_datetime_value()),
            "reportableIdentifier": lambda n : setattr(self, 'reportable_identifier', n.get_str_value()),
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
        writer.write_str_value("entryType", self.entry_type)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_str_value("joiningValue", self.joining_value)
        writer.write_datetime_value("recordedDateTime", self.recorded_date_time)
        writer.write_str_value("reportableIdentifier", self.reportable_identifier)
    

