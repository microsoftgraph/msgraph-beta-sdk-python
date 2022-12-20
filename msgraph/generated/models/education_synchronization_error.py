from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class EducationSynchronizationError(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new educationSynchronizationError and sets the default values.
        """
        super().__init__()
        # Represents the sync entity (school, section, student, teacher).
        self._entry_type: Optional[str] = None
        # Represents the error code for this error.
        self._error_code: Optional[str] = None
        # Contains a description of the error.
        self._error_message: Optional[str] = None
        # The unique identifier for the entry.
        self._joining_value: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The time of occurrence of this error.
        self._recorded_date_time: Optional[datetime] = None
        # The identifier of this error entry.
        self._reportable_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationError()
    
    @property
    def entry_type(self,) -> Optional[str]:
        """
        Gets the entryType property value. Represents the sync entity (school, section, student, teacher).
        Returns: Optional[str]
        """
        return self._entry_type
    
    @entry_type.setter
    def entry_type(self,value: Optional[str] = None) -> None:
        """
        Sets the entryType property value. Represents the sync entity (school, section, student, teacher).
        Args:
            value: Value to set for the entryType property.
        """
        self._entry_type = value
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. Represents the error code for this error.
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. Represents the error code for this error.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    @property
    def error_message(self,) -> Optional[str]:
        """
        Gets the errorMessage property value. Contains a description of the error.
        Returns: Optional[str]
        """
        return self._error_message
    
    @error_message.setter
    def error_message(self,value: Optional[str] = None) -> None:
        """
        Sets the errorMessage property value. Contains a description of the error.
        Args:
            value: Value to set for the errorMessage property.
        """
        self._error_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "entry_type": lambda n : setattr(self, 'entry_type', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "error_message": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "joining_value": lambda n : setattr(self, 'joining_value', n.get_str_value()),
            "recorded_date_time": lambda n : setattr(self, 'recorded_date_time', n.get_datetime_value()),
            "reportable_identifier": lambda n : setattr(self, 'reportable_identifier', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def joining_value(self,) -> Optional[str]:
        """
        Gets the joiningValue property value. The unique identifier for the entry.
        Returns: Optional[str]
        """
        return self._joining_value
    
    @joining_value.setter
    def joining_value(self,value: Optional[str] = None) -> None:
        """
        Sets the joiningValue property value. The unique identifier for the entry.
        Args:
            value: Value to set for the joiningValue property.
        """
        self._joining_value = value
    
    @property
    def recorded_date_time(self,) -> Optional[datetime]:
        """
        Gets the recordedDateTime property value. The time of occurrence of this error.
        Returns: Optional[datetime]
        """
        return self._recorded_date_time
    
    @recorded_date_time.setter
    def recorded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the recordedDateTime property value. The time of occurrence of this error.
        Args:
            value: Value to set for the recordedDateTime property.
        """
        self._recorded_date_time = value
    
    @property
    def reportable_identifier(self,) -> Optional[str]:
        """
        Gets the reportableIdentifier property value. The identifier of this error entry.
        Returns: Optional[str]
        """
        return self._reportable_identifier
    
    @reportable_identifier.setter
    def reportable_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the reportableIdentifier property value. The identifier of this error entry.
        Args:
            value: Value to set for the reportableIdentifier property.
        """
        self._reportable_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("entryType", self.entry_type)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_str_value("joiningValue", self.joining_value)
        writer.write_datetime_value("recordedDateTime", self.recorded_date_time)
        writer.write_str_value("reportableIdentifier", self.reportable_identifier)
    

