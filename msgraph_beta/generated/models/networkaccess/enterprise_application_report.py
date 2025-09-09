from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_type import AccessType
    from .traffic_type import TrafficType

@dataclass
class EnterpriseApplicationReport(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The type of accessed application. The possible values are: quickAccess, privateAccess, unknownFutureValue, appAccess. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: appAccess.
    access_type: Optional[AccessType] = None
    # The unique identifier for the enterprise application (appId) in Microsoft Entra ID.
    application_id: Optional[str] = None
    # Number of devices that accessed this application.
    device_count: Optional[int] = None
    # Timestamp of the first access to the application.
    first_access_date_time: Optional[datetime.datetime] = None
    # Timestamp of the last access to the application.
    last_access_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total bytes received from the application.
    total_bytes_received: Optional[int] = None
    # Total bytes sent to the application.
    total_bytes_sent: Optional[int] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # Number of transactions to this application.
    transaction_count: Optional[int] = None
    # Number of users that accessed this application.
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnterpriseApplicationReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnterpriseApplicationReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnterpriseApplicationReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_type import AccessType
        from .traffic_type import TrafficType

        from .access_type import AccessType
        from .traffic_type import TrafficType

        fields: dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(AccessType)),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "firstAccessDateTime": lambda n : setattr(self, 'first_access_date_time', n.get_datetime_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalBytesReceived": lambda n : setattr(self, 'total_bytes_received', n.get_int_value()),
            "totalBytesSent": lambda n : setattr(self, 'total_bytes_sent', n.get_int_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_datetime_value("firstAccessDateTime", self.first_access_date_time)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalBytesReceived", self.total_bytes_received)
        writer.write_int_value("totalBytesSent", self.total_bytes_sent)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

