from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import time_series_parameter

class GetHealthMetricTimeSeriesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new getHealthMetricTimeSeriesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The timeSeries property
        self._time_series: Optional[time_series_parameter.TimeSeriesParameter] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetHealthMetricTimeSeriesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetHealthMetricTimeSeriesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetHealthMetricTimeSeriesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import time_series_parameter

        fields: Dict[str, Callable[[Any], None]] = {
            "timeSeries": lambda n : setattr(self, 'time_series', n.get_object_value(time_series_parameter.TimeSeriesParameter)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("timeSeries", self.time_series)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_series(self,) -> Optional[time_series_parameter.TimeSeriesParameter]:
        """
        Gets the timeSeries property value. The timeSeries property
        Returns: Optional[time_series_parameter.TimeSeriesParameter]
        """
        return self._time_series
    
    @time_series.setter
    def time_series(self,value: Optional[time_series_parameter.TimeSeriesParameter] = None) -> None:
        """
        Sets the timeSeries property value. The timeSeries property
        Args:
            value: Value to set for the time_series property.
        """
        self._time_series = value
    

