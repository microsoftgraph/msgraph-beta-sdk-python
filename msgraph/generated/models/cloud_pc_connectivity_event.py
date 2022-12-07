from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_connectivity_event_result = lazy_import('msgraph.generated.models.cloud_pc_connectivity_event_result')
cloud_pc_connectivity_event_type = lazy_import('msgraph.generated.models.cloud_pc_connectivity_event_type')

class CloudPcConnectivityEvent(AdditionalDataHolder, Parsable):
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
        Instantiates a new cloudPcConnectivityEvent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the date and time when this event was created. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        self._event_date_time: Optional[datetime] = None
        # Name of the event.
        self._event_name: Optional[str] = None
        # The eventResult property
        self._event_result: Optional[cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult] = None
        # The eventType property
        self._event_type: Optional[cloud_pc_connectivity_event_type.CloudPcConnectivityEventType] = None
        # Additional message for this event.
        self._message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcConnectivityEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnectivityEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcConnectivityEvent()
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. Indicates the date and time when this event was created. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. Indicates the date and time when this event was created. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the eventDateTime property.
        """
        self._event_date_time = value
    
    @property
    def event_name(self,) -> Optional[str]:
        """
        Gets the eventName property value. Name of the event.
        Returns: Optional[str]
        """
        return self._event_name
    
    @event_name.setter
    def event_name(self,value: Optional[str] = None) -> None:
        """
        Sets the eventName property value. Name of the event.
        Args:
            value: Value to set for the eventName property.
        """
        self._event_name = value
    
    @property
    def event_result(self,) -> Optional[cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult]:
        """
        Gets the eventResult property value. The eventResult property
        Returns: Optional[cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult]
        """
        return self._event_result
    
    @event_result.setter
    def event_result(self,value: Optional[cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult] = None) -> None:
        """
        Sets the eventResult property value. The eventResult property
        Args:
            value: Value to set for the eventResult property.
        """
        self._event_result = value
    
    @property
    def event_type(self,) -> Optional[cloud_pc_connectivity_event_type.CloudPcConnectivityEventType]:
        """
        Gets the eventType property value. The eventType property
        Returns: Optional[cloud_pc_connectivity_event_type.CloudPcConnectivityEventType]
        """
        return self._event_type
    
    @event_type.setter
    def event_type(self,value: Optional[cloud_pc_connectivity_event_type.CloudPcConnectivityEventType] = None) -> None:
        """
        Sets the eventType property value. The eventType property
        Args:
            value: Value to set for the eventType property.
        """
        self._event_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "event_date_time": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "event_name": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "event_result": lambda n : setattr(self, 'event_result', n.get_enum_value(cloud_pc_connectivity_event_result.CloudPcConnectivityEventResult)),
            "event_type": lambda n : setattr(self, 'event_type', n.get_enum_value(cloud_pc_connectivity_event_type.CloudPcConnectivityEventType)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. Additional message for this event.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. Additional message for this event.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
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
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_enum_value("eventResult", self.event_result)
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

