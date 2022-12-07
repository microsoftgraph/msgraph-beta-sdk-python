from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

quarantine_reason = lazy_import('msgraph.generated.models.quarantine_reason')
synchronization_error = lazy_import('msgraph.generated.models.synchronization_error')

class SynchronizationQuarantine(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationQuarantine and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Date and time when the quarantine was last evaluated and imposed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._current_began: Optional[datetime] = None
        # Describes the error(s) that occurred when putting the synchronization job into quarantine.
        self._error: Optional[synchronization_error.SynchronizationError] = None
        # Date and time when the next attempt to re-evaluate the quarantine will be made. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._next_attempt: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The reason property
        self._reason: Optional[quarantine_reason.QuarantineReason] = None
        # Date and time when the quarantine was first imposed in this series (a series starts when a quarantine is first imposed, and is reset as soon as the quarantine is lifted). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._series_began: Optional[datetime] = None
        # Number of times in this series the quarantine was re-evaluated and left in effect (a series starts when quarantine is first imposed, and is reset as soon as quarantine is lifted).
        self._series_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationQuarantine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationQuarantine
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationQuarantine()
    
    @property
    def current_began(self,) -> Optional[datetime]:
        """
        Gets the currentBegan property value. Date and time when the quarantine was last evaluated and imposed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._current_began
    
    @current_began.setter
    def current_began(self,value: Optional[datetime] = None) -> None:
        """
        Sets the currentBegan property value. Date and time when the quarantine was last evaluated and imposed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the currentBegan property.
        """
        self._current_began = value
    
    @property
    def error(self,) -> Optional[synchronization_error.SynchronizationError]:
        """
        Gets the error property value. Describes the error(s) that occurred when putting the synchronization job into quarantine.
        Returns: Optional[synchronization_error.SynchronizationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[synchronization_error.SynchronizationError] = None) -> None:
        """
        Sets the error property value. Describes the error(s) that occurred when putting the synchronization job into quarantine.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "current_began": lambda n : setattr(self, 'current_began', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(synchronization_error.SynchronizationError)),
            "next_attempt": lambda n : setattr(self, 'next_attempt', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(quarantine_reason.QuarantineReason)),
            "series_began": lambda n : setattr(self, 'series_began', n.get_datetime_value()),
            "series_count": lambda n : setattr(self, 'series_count', n.get_int_value()),
        }
        return fields
    
    @property
    def next_attempt(self,) -> Optional[datetime]:
        """
        Gets the nextAttempt property value. Date and time when the next attempt to re-evaluate the quarantine will be made. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._next_attempt
    
    @next_attempt.setter
    def next_attempt(self,value: Optional[datetime] = None) -> None:
        """
        Sets the nextAttempt property value. Date and time when the next attempt to re-evaluate the quarantine will be made. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the nextAttempt property.
        """
        self._next_attempt = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def reason(self,) -> Optional[quarantine_reason.QuarantineReason]:
        """
        Gets the reason property value. The reason property
        Returns: Optional[quarantine_reason.QuarantineReason]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[quarantine_reason.QuarantineReason] = None) -> None:
        """
        Sets the reason property value. The reason property
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("currentBegan", self.current_began)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("nextAttempt", self.next_attempt)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("reason", self.reason)
        writer.write_datetime_value("seriesBegan", self.series_began)
        writer.write_int_value("seriesCount", self.series_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def series_began(self,) -> Optional[datetime]:
        """
        Gets the seriesBegan property value. Date and time when the quarantine was first imposed in this series (a series starts when a quarantine is first imposed, and is reset as soon as the quarantine is lifted). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._series_began
    
    @series_began.setter
    def series_began(self,value: Optional[datetime] = None) -> None:
        """
        Sets the seriesBegan property value. Date and time when the quarantine was first imposed in this series (a series starts when a quarantine is first imposed, and is reset as soon as the quarantine is lifted). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the seriesBegan property.
        """
        self._series_began = value
    
    @property
    def series_count(self,) -> Optional[int]:
        """
        Gets the seriesCount property value. Number of times in this series the quarantine was re-evaluated and left in effect (a series starts when quarantine is first imposed, and is reset as soon as quarantine is lifted).
        Returns: Optional[int]
        """
        return self._series_count
    
    @series_count.setter
    def series_count(self,value: Optional[int] = None) -> None:
        """
        Sets the seriesCount property value. Number of times in this series the quarantine was re-evaluated and left in effect (a series starts when quarantine is first imposed, and is reset as soon as quarantine is lifted).
        Args:
            value: Value to set for the seriesCount property.
        """
        self._series_count = value
    

