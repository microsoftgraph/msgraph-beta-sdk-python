from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import connector_health_state, connector_name

@dataclass
class ConnectorStatusDetails(AdditionalDataHolder, Parsable):
    """
    Represent connector status
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Connector Instance Id
    connector_instance_id: Optional[str] = None
    # Connectors name for connector status
    connector_name: Optional[connector_name.ConnectorName] = None
    # Event datetime
    event_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Connector health state for connector status
    status: Optional[connector_health_state.ConnectorHealthState] = None
    
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
    

