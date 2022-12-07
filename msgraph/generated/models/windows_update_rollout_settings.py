from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WindowsUpdateRolloutSettings(AdditionalDataHolder, Parsable):
    """
    A complex type to store the windows update rollout settings including offer start date time, offer end date time, and days between each set of offers.
    """
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
        Instantiates a new windowsUpdateRolloutSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The feature update's ending  of release date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
        self._offer_end_date_time_in_u_t_c: Optional[datetime] = None
        # The number of day(s) between each set of offers to be set, updated, and displayed for a feature update profile, for example: if OfferStartDateTimeInUTC is 2020-06-09T10:00:00Z, and OfferIntervalInDays is 1, then the next two sets of offers will be made consecutively on 2020-06-10T10:00:00Z (next day at the same specified time) and 2020-06-11T10:00:00Z (next next day at the same specified time) with 1 day in between each set of offers.
        self._offer_interval_in_days: Optional[int] = None
        # The feature update's starting date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
        self._offer_start_date_time_in_u_t_c: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateRolloutSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUpdateRolloutSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offer_end_date_time_in_u_t_c": lambda n : setattr(self, 'offer_end_date_time_in_u_t_c', n.get_datetime_value()),
            "offer_interval_in_days": lambda n : setattr(self, 'offer_interval_in_days', n.get_int_value()),
            "offer_start_date_time_in_u_t_c": lambda n : setattr(self, 'offer_start_date_time_in_u_t_c', n.get_datetime_value()),
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
    def offer_end_date_time_in_u_t_c(self,) -> Optional[datetime]:
        """
        Gets the offerEndDateTimeInUTC property value. The feature update's ending  of release date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
        Returns: Optional[datetime]
        """
        return self._offer_end_date_time_in_u_t_c
    
    @offer_end_date_time_in_u_t_c.setter
    def offer_end_date_time_in_u_t_c(self,value: Optional[datetime] = None) -> None:
        """
        Sets the offerEndDateTimeInUTC property value. The feature update's ending  of release date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
        Args:
            value: Value to set for the offerEndDateTimeInUTC property.
        """
        self._offer_end_date_time_in_u_t_c = value
    
    @property
    def offer_interval_in_days(self,) -> Optional[int]:
        """
        Gets the offerIntervalInDays property value. The number of day(s) between each set of offers to be set, updated, and displayed for a feature update profile, for example: if OfferStartDateTimeInUTC is 2020-06-09T10:00:00Z, and OfferIntervalInDays is 1, then the next two sets of offers will be made consecutively on 2020-06-10T10:00:00Z (next day at the same specified time) and 2020-06-11T10:00:00Z (next next day at the same specified time) with 1 day in between each set of offers.
        Returns: Optional[int]
        """
        return self._offer_interval_in_days
    
    @offer_interval_in_days.setter
    def offer_interval_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the offerIntervalInDays property value. The number of day(s) between each set of offers to be set, updated, and displayed for a feature update profile, for example: if OfferStartDateTimeInUTC is 2020-06-09T10:00:00Z, and OfferIntervalInDays is 1, then the next two sets of offers will be made consecutively on 2020-06-10T10:00:00Z (next day at the same specified time) and 2020-06-11T10:00:00Z (next next day at the same specified time) with 1 day in between each set of offers.
        Args:
            value: Value to set for the offerIntervalInDays property.
        """
        self._offer_interval_in_days = value
    
    @property
    def offer_start_date_time_in_u_t_c(self,) -> Optional[datetime]:
        """
        Gets the offerStartDateTimeInUTC property value. The feature update's starting date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
        Returns: Optional[datetime]
        """
        return self._offer_start_date_time_in_u_t_c
    
    @offer_start_date_time_in_u_t_c.setter
    def offer_start_date_time_in_u_t_c(self,value: Optional[datetime] = None) -> None:
        """
        Sets the offerStartDateTimeInUTC property value. The feature update's starting date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
        Args:
            value: Value to set for the offerStartDateTimeInUTC property.
        """
        self._offer_start_date_time_in_u_t_c = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("offerEndDateTimeInUTC", self.offer_end_date_time_in_u_t_c)
        writer.write_int_value("offerIntervalInDays", self.offer_interval_in_days)
        writer.write_datetime_value("offerStartDateTimeInUTC", self.offer_start_date_time_in_u_t_c)
        writer.write_additional_data_value(self.additional_data)
    

