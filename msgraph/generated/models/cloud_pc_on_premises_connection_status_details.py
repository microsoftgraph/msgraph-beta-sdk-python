from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_on_premises_connection_health_check

@dataclass
class CloudPcOnPremisesConnectionStatusDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The end time of the connection health check. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    end_date_time: Optional[datetime] = None
    # All checks that are done on the connection.
    health_checks: Optional[List[cloud_pc_on_premises_connection_health_check.CloudPcOnPremisesConnectionHealthCheck]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The start time of the connection health check. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcOnPremisesConnectionStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnectionStatusDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOnPremisesConnectionStatusDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_on_premises_connection_health_check

        from . import cloud_pc_on_premises_connection_health_check

        fields: Dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "healthChecks": lambda n : setattr(self, 'health_checks', n.get_collection_of_object_values(cloud_pc_on_premises_connection_health_check.CloudPcOnPremisesConnectionHealthCheck)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("healthChecks", self.health_checks)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

