from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RolloutSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new rolloutSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies the number of devices that are offered at the same time. Has no effect when endDateTime is set. When endDateTime and devicesPerOffer are both not set, all devices in the deployment are offered content at the same time.
        self._devices_per_offer: Optional[int] = None
        # Specifies duration between each set of devices being offered the update. Has an effect when endDateTime or devicesPerOffer are defined. Default value is P1D (1 day).
        self._duration_between_offers: Optional[str] = None
        # Specifies the date before which all devices currently in the deployment are offered the update. Devices added after this date are offered immediately. When endDateTime and devicesPerOffer are both not set, all devices in the deployment are offered content at the same time.
        self._end_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Date on which devices in the deployment start receiving the update. When not set, the deployment starts as soon as devices are assigned.
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RolloutSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RolloutSettings()
    
    @property
    def devices_per_offer(self,) -> Optional[int]:
        """
        Gets the devicesPerOffer property value. Specifies the number of devices that are offered at the same time. Has no effect when endDateTime is set. When endDateTime and devicesPerOffer are both not set, all devices in the deployment are offered content at the same time.
        Returns: Optional[int]
        """
        return self._devices_per_offer
    
    @devices_per_offer.setter
    def devices_per_offer(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesPerOffer property value. Specifies the number of devices that are offered at the same time. Has no effect when endDateTime is set. When endDateTime and devicesPerOffer are both not set, all devices in the deployment are offered content at the same time.
        Args:
            value: Value to set for the devicesPerOffer property.
        """
        self._devices_per_offer = value
    
    @property
    def duration_between_offers(self,) -> Optional[str]:
        """
        Gets the durationBetweenOffers property value. Specifies duration between each set of devices being offered the update. Has an effect when endDateTime or devicesPerOffer are defined. Default value is P1D (1 day).
        Returns: Optional[str]
        """
        return self._duration_between_offers
    
    @duration_between_offers.setter
    def duration_between_offers(self,value: Optional[str] = None) -> None:
        """
        Sets the durationBetweenOffers property value. Specifies duration between each set of devices being offered the update. Has an effect when endDateTime or devicesPerOffer are defined. Default value is P1D (1 day).
        Args:
            value: Value to set for the durationBetweenOffers property.
        """
        self._duration_between_offers = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. Specifies the date before which all devices currently in the deployment are offered the update. Devices added after this date are offered immediately. When endDateTime and devicesPerOffer are both not set, all devices in the deployment are offered content at the same time.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. Specifies the date before which all devices currently in the deployment are offered the update. Devices added after this date are offered immediately. When endDateTime and devicesPerOffer are both not set, all devices in the deployment are offered content at the same time.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "devices_per_offer": lambda n : setattr(self, 'devices_per_offer', n.get_int_value()),
            "duration_between_offers": lambda n : setattr(self, 'duration_between_offers', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("devicesPerOffer", self.devices_per_offer)
        writer.write_str_value("durationBetweenOffers", self.duration_between_offers)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Date on which devices in the deployment start receiving the update. When not set, the deployment starts as soon as devices are assigned.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Date on which devices in the deployment start receiving the update. When not set, the deployment starts as soon as devices are assigned.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

