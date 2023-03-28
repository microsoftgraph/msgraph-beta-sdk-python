from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import connector_health_state, connector_name

class ConnectorStatusDetails(AdditionalDataHolder, Parsable):
    """
    Represent connector status
    """
    def __init__(self,) -> None:
        """
        Instantiates a new connectorStatusDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Connector Instance Id
        self._connector_instance_id: Optional[str] = None
        # Connectors name for connector status
        self._connector_name: Optional[connector_name.ConnectorName] = None
        # Event datetime
        self._event_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Connector health state for connector status
        self._status: Optional[connector_health_state.ConnectorHealthState] = None
    
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
    def connector_instance_id(self,) -> Optional[str]:
        """
        Gets the connectorInstanceId property value. Connector Instance Id
        Returns: Optional[str]
        """
        return self._connector_instance_id
    
    @connector_instance_id.setter
    def connector_instance_id(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorInstanceId property value. Connector Instance Id
        Args:
            value: Value to set for the connector_instance_id property.
        """
        self._connector_instance_id = value
    
    @property
    def connector_name(self,) -> Optional[connector_name.ConnectorName]:
        """
        Gets the connectorName property value. Connectors name for connector status
        Returns: Optional[connector_name.ConnectorName]
        """
        return self._connector_name
    
    @connector_name.setter
    def connector_name(self,value: Optional[connector_name.ConnectorName] = None) -> None:
        """
        Sets the connectorName property value. Connectors name for connector status
        Args:
            value: Value to set for the connector_name property.
        """
        self._connector_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectorStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectorStatusDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectorStatusDetails()
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. Event datetime
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. Event datetime
        Args:
            value: Value to set for the event_date_time property.
        """
        self._event_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import connector_health_state, connector_name

        fields: Dict[str, Callable[[Any], None]] = {
            "connectorInstanceId": lambda n : setattr(self, 'connector_instance_id', n.get_str_value()),
            "connectorName": lambda n : setattr(self, 'connector_name', n.get_enum_value(connector_name.ConnectorName)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(connector_health_state.ConnectorHealthState)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("connectorInstanceId", self.connector_instance_id)
        writer.write_enum_value("connectorName", self.connector_name)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[connector_health_state.ConnectorHealthState]:
        """
        Gets the status property value. Connector health state for connector status
        Returns: Optional[connector_health_state.ConnectorHealthState]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[connector_health_state.ConnectorHealthState] = None) -> None:
        """
        Sets the status property value. Connector health state for connector status
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

