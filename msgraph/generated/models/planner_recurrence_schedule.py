from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

recurrence_pattern = lazy_import('msgraph.generated.models.recurrence_pattern')

class PlannerRecurrenceSchedule(AdditionalDataHolder, Parsable):
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
        Instantiates a new plannerRecurrenceSchedule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The nextOccurrenceDateTime property
        self._next_occurrence_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The pattern property
        self._pattern: Optional[recurrence_pattern.RecurrencePattern] = None
        # The patternStartDateTime property
        self._pattern_start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerRecurrenceSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRecurrenceSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerRecurrenceSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "nextOccurrenceDateTime": lambda n : setattr(self, 'next_occurrence_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pattern": lambda n : setattr(self, 'pattern', n.get_object_value(recurrence_pattern.RecurrencePattern)),
            "patternStartDateTime": lambda n : setattr(self, 'pattern_start_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def next_occurrence_date_time(self,) -> Optional[datetime]:
        """
        Gets the nextOccurrenceDateTime property value. The nextOccurrenceDateTime property
        Returns: Optional[datetime]
        """
        return self._next_occurrence_date_time
    
    @next_occurrence_date_time.setter
    def next_occurrence_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the nextOccurrenceDateTime property value. The nextOccurrenceDateTime property
        Args:
            value: Value to set for the next_occurrence_date_time property.
        """
        self._next_occurrence_date_time = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def pattern(self,) -> Optional[recurrence_pattern.RecurrencePattern]:
        """
        Gets the pattern property value. The pattern property
        Returns: Optional[recurrence_pattern.RecurrencePattern]
        """
        return self._pattern
    
    @pattern.setter
    def pattern(self,value: Optional[recurrence_pattern.RecurrencePattern] = None) -> None:
        """
        Sets the pattern property value. The pattern property
        Args:
            value: Value to set for the pattern property.
        """
        self._pattern = value
    
    @property
    def pattern_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the patternStartDateTime property value. The patternStartDateTime property
        Returns: Optional[datetime]
        """
        return self._pattern_start_date_time
    
    @pattern_start_date_time.setter
    def pattern_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the patternStartDateTime property value. The patternStartDateTime property
        Args:
            value: Value to set for the pattern_start_date_time property.
        """
        self._pattern_start_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("nextOccurrenceDateTime", self.next_occurrence_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("pattern", self.pattern)
        writer.write_datetime_value("patternStartDateTime", self.pattern_start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

