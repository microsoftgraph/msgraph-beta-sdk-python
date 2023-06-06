from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_connectivity_status, cloud_pc_health_check_item

@dataclass
class CloudPcConnectivityResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A list of failed health check items. If the status property is available, this property will be empty.
    failed_health_check_items: Optional[List[cloud_pc_health_check_item.CloudPcHealthCheckItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[cloud_pc_connectivity_status.CloudPcConnectivityStatus] = None
    # Datetime when the status was updated. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
    updated_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcConnectivityResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnectivityResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcConnectivityResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_connectivity_status, cloud_pc_health_check_item

        fields: Dict[str, Callable[[Any], None]] = {
            "failedHealthCheckItems": lambda n : setattr(self, 'failed_health_check_items', n.get_collection_of_object_values(cloud_pc_health_check_item.CloudPcHealthCheckItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_connectivity_status.CloudPcConnectivityStatus)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("failedHealthCheckItems", self.failed_health_check_items)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    

