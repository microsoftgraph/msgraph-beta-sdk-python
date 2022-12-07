from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TimeSeriesParameter(AdditionalDataHolder, Parsable):
    """
    Parameter passed to GetHealthMetricTimeSeries when requesting snapshot time series.
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
        Instantiates a new timeSeriesParameter and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # End time of the series being requested. Optional; if not specified, current time is used.
        self._end_date_time: Optional[datetime] = None
        # The name of the metric for which a time series is requested.
        self._metric_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Start time of the series being requested.
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeSeriesParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeSeriesParameter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeSeriesParameter()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. End time of the series being requested. Optional; if not specified, current time is used.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. End time of the series being requested. Optional; if not specified, current time is used.
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
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "metric_name": lambda n : setattr(self, 'metric_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def metric_name(self,) -> Optional[str]:
        """
        Gets the metricName property value. The name of the metric for which a time series is requested.
        Returns: Optional[str]
        """
        return self._metric_name
    
    @metric_name.setter
    def metric_name(self,value: Optional[str] = None) -> None:
        """
        Sets the metricName property value. The name of the metric for which a time series is requested.
        Args:
            value: Value to set for the metricName property.
        """
        self._metric_name = value
    
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("metricName", self.metric_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Start time of the series being requested.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Start time of the series being requested.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

