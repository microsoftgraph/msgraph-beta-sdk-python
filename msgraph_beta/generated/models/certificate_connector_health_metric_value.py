from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CertificateConnectorHealthMetricValue(AdditionalDataHolder, BackedModel, Parsable):
    """
    Metric snapshot value returned in response to a GetHealthMetricTimeSeries request.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Timestamp for this metric data-point.
    date_time: Optional[datetime.datetime] = None
    # Count of failed requests/operations.
    failure_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of successful requests/operations.
    success_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateConnectorHealthMetricValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateConnectorHealthMetricValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateConnectorHealthMetricValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "failureCount": lambda n : setattr(self, 'failure_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successCount": lambda n : setattr(self, 'success_count', n.get_int_value()),
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
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_int_value("failureCount", self.failure_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successCount", self.success_count)
        writer.write_additional_data_value(self.additional_data)
    

