from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import expiration_pattern, patterned_recurrence

class RequestSchedule(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new requestSchedule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # In entitlement management, when the access should expire.
        self._expiration: Optional[expiration_pattern.ExpirationPattern] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For recurring access, or eligible or active assignment. This property is currently unsupported in both PIM and entitlement management.
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. In PIM, when the  eligible or active assignment becomes active.
        self._start_date_time: Optional[datetime] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequestSchedule()
    
    @property
    def expiration(self,) -> Optional[expiration_pattern.ExpirationPattern]:
        """
        Gets the expiration property value. In entitlement management, when the access should expire.
        Returns: Optional[expiration_pattern.ExpirationPattern]
        """
        return self._expiration
    
    @expiration.setter
    def expiration(self,value: Optional[expiration_pattern.ExpirationPattern] = None) -> None:
        """
        Sets the expiration property value. In entitlement management, when the access should expire.
        Args:
            value: Value to set for the expiration property.
        """
        self._expiration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import expiration_pattern, patterned_recurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "expiration": lambda n : setattr(self, 'expiration', n.get_object_value(expiration_pattern.ExpirationPattern)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. For recurring access, or eligible or active assignment. This property is currently unsupported in both PIM and entitlement management.
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. For recurring access, or eligible or active assignment. This property is currently unsupported in both PIM and entitlement management.
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("expiration", self.expiration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. In PIM, when the  eligible or active assignment becomes active.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. In PIM, when the  eligible or active assignment becomes active.
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    

