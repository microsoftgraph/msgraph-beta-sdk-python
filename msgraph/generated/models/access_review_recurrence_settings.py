from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AccessReviewRecurrenceSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new accessReviewRecurrenceSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The duration in days for recurrence.
        self._duration_in_days: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The count of recurrences, if the value of recurrenceEndType is occurrences, or 0 otherwise.
        self._recurrence_count: Optional[int] = None
        # How the recurrence ends. Possible values: never, endBy, occurrences, or recurrenceCount. If it is never, then there is no explicit end of the recurrence series. If it is endBy, then the recurrence ends at a certain date. If it is occurrences, then the series ends after recurrenceCount instances of the review have completed.
        self._recurrence_end_type: Optional[str] = None
        # The recurrence interval. Possible vaules: onetime, weekly, monthly, quarterly, halfyearly or annual.
        self._recurrence_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewRecurrenceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewRecurrenceSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewRecurrenceSettings()
    
    @property
    def duration_in_days(self,) -> Optional[int]:
        """
        Gets the durationInDays property value. The duration in days for recurrence.
        Returns: Optional[int]
        """
        return self._duration_in_days
    
    @duration_in_days.setter
    def duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInDays property value. The duration in days for recurrence.
        Args:
            value: Value to set for the durationInDays property.
        """
        self._duration_in_days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "duration_in_days": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence_count": lambda n : setattr(self, 'recurrence_count', n.get_int_value()),
            "recurrence_end_type": lambda n : setattr(self, 'recurrence_end_type', n.get_str_value()),
            "recurrence_type": lambda n : setattr(self, 'recurrence_type', n.get_str_value()),
        }
        return fields
    
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
    def recurrence_count(self,) -> Optional[int]:
        """
        Gets the recurrenceCount property value. The count of recurrences, if the value of recurrenceEndType is occurrences, or 0 otherwise.
        Returns: Optional[int]
        """
        return self._recurrence_count
    
    @recurrence_count.setter
    def recurrence_count(self,value: Optional[int] = None) -> None:
        """
        Sets the recurrenceCount property value. The count of recurrences, if the value of recurrenceEndType is occurrences, or 0 otherwise.
        Args:
            value: Value to set for the recurrenceCount property.
        """
        self._recurrence_count = value
    
    @property
    def recurrence_end_type(self,) -> Optional[str]:
        """
        Gets the recurrenceEndType property value. How the recurrence ends. Possible values: never, endBy, occurrences, or recurrenceCount. If it is never, then there is no explicit end of the recurrence series. If it is endBy, then the recurrence ends at a certain date. If it is occurrences, then the series ends after recurrenceCount instances of the review have completed.
        Returns: Optional[str]
        """
        return self._recurrence_end_type
    
    @recurrence_end_type.setter
    def recurrence_end_type(self,value: Optional[str] = None) -> None:
        """
        Sets the recurrenceEndType property value. How the recurrence ends. Possible values: never, endBy, occurrences, or recurrenceCount. If it is never, then there is no explicit end of the recurrence series. If it is endBy, then the recurrence ends at a certain date. If it is occurrences, then the series ends after recurrenceCount instances of the review have completed.
        Args:
            value: Value to set for the recurrenceEndType property.
        """
        self._recurrence_end_type = value
    
    @property
    def recurrence_type(self,) -> Optional[str]:
        """
        Gets the recurrenceType property value. The recurrence interval. Possible vaules: onetime, weekly, monthly, quarterly, halfyearly or annual.
        Returns: Optional[str]
        """
        return self._recurrence_type
    
    @recurrence_type.setter
    def recurrence_type(self,value: Optional[str] = None) -> None:
        """
        Sets the recurrenceType property value. The recurrence interval. Possible vaules: onetime, weekly, monthly, quarterly, halfyearly or annual.
        Args:
            value: Value to set for the recurrenceType property.
        """
        self._recurrence_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("recurrenceCount", self.recurrence_count)
        writer.write_str_value("recurrenceEndType", self.recurrence_end_type)
        writer.write_str_value("recurrenceType", self.recurrence_type)
        writer.write_additional_data_value(self.additional_data)
    

