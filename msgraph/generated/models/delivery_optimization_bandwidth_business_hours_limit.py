from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeliveryOptimizationBandwidthBusinessHoursLimit(AdditionalDataHolder, Parsable):
    """
    Bandwidth business hours and percentages type
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
    
    @property
    def bandwidth_begin_business_hours(self,) -> Optional[int]:
        """
        Gets the bandwidthBeginBusinessHours property value. Specifies the beginning of business hours using a 24-hour clock (0-23). Valid values 0 to 23
        Returns: Optional[int]
        """
        return self._bandwidth_begin_business_hours
    
    @bandwidth_begin_business_hours.setter
    def bandwidth_begin_business_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the bandwidthBeginBusinessHours property value. Specifies the beginning of business hours using a 24-hour clock (0-23). Valid values 0 to 23
        Args:
            value: Value to set for the bandwidthBeginBusinessHours property.
        """
        self._bandwidth_begin_business_hours = value
    
    @property
    def bandwidth_end_business_hours(self,) -> Optional[int]:
        """
        Gets the bandwidthEndBusinessHours property value. Specifies the end of business hours using a 24-hour clock (0-23). Valid values 0 to 23
        Returns: Optional[int]
        """
        return self._bandwidth_end_business_hours
    
    @bandwidth_end_business_hours.setter
    def bandwidth_end_business_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the bandwidthEndBusinessHours property value. Specifies the end of business hours using a 24-hour clock (0-23). Valid values 0 to 23
        Args:
            value: Value to set for the bandwidthEndBusinessHours property.
        """
        self._bandwidth_end_business_hours = value
    
    @property
    def bandwidth_percentage_during_business_hours(self,) -> Optional[int]:
        """
        Gets the bandwidthPercentageDuringBusinessHours property value. Specifies the percentage of bandwidth to limit during business hours (0-100). Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._bandwidth_percentage_during_business_hours
    
    @bandwidth_percentage_during_business_hours.setter
    def bandwidth_percentage_during_business_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the bandwidthPercentageDuringBusinessHours property value. Specifies the percentage of bandwidth to limit during business hours (0-100). Valid values 0 to 100
        Args:
            value: Value to set for the bandwidthPercentageDuringBusinessHours property.
        """
        self._bandwidth_percentage_during_business_hours = value
    
    @property
    def bandwidth_percentage_outside_business_hours(self,) -> Optional[int]:
        """
        Gets the bandwidthPercentageOutsideBusinessHours property value. Specifies the percentage of bandwidth to limit outsidse business hours (0-100). Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._bandwidth_percentage_outside_business_hours
    
    @bandwidth_percentage_outside_business_hours.setter
    def bandwidth_percentage_outside_business_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the bandwidthPercentageOutsideBusinessHours property value. Specifies the percentage of bandwidth to limit outsidse business hours (0-100). Valid values 0 to 100
        Args:
            value: Value to set for the bandwidthPercentageOutsideBusinessHours property.
        """
        self._bandwidth_percentage_outside_business_hours = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deliveryOptimizationBandwidthBusinessHoursLimit and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies the beginning of business hours using a 24-hour clock (0-23). Valid values 0 to 23
        self._bandwidth_begin_business_hours: Optional[int] = None
        # Specifies the end of business hours using a 24-hour clock (0-23). Valid values 0 to 23
        self._bandwidth_end_business_hours: Optional[int] = None
        # Specifies the percentage of bandwidth to limit during business hours (0-100). Valid values 0 to 100
        self._bandwidth_percentage_during_business_hours: Optional[int] = None
        # Specifies the percentage of bandwidth to limit outsidse business hours (0-100). Valid values 0 to 100
        self._bandwidth_percentage_outside_business_hours: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationBandwidthBusinessHoursLimit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthBusinessHoursLimit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationBandwidthBusinessHoursLimit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bandwidth_begin_business_hours": lambda n : setattr(self, 'bandwidth_begin_business_hours', n.get_int_value()),
            "bandwidth_end_business_hours": lambda n : setattr(self, 'bandwidth_end_business_hours', n.get_int_value()),
            "bandwidth_percentage_during_business_hours": lambda n : setattr(self, 'bandwidth_percentage_during_business_hours', n.get_int_value()),
            "bandwidth_percentage_outside_business_hours": lambda n : setattr(self, 'bandwidth_percentage_outside_business_hours', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("bandwidthBeginBusinessHours", self.bandwidth_begin_business_hours)
        writer.write_int_value("bandwidthEndBusinessHours", self.bandwidth_end_business_hours)
        writer.write_int_value("bandwidthPercentageDuringBusinessHours", self.bandwidth_percentage_during_business_hours)
        writer.write_int_value("bandwidthPercentageOutsideBusinessHours", self.bandwidth_percentage_outside_business_hours)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

