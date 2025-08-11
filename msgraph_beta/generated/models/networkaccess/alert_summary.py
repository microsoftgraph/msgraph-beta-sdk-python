from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_severity import AlertSeverity
    from .alert_type import AlertType

@dataclass
class AlertSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The alertType property
    alert_type: Optional[AlertType] = None
    # Total number of alerts with this specific severity and type. Required.
    count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlertSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_severity import AlertSeverity
        from .alert_type import AlertType

        from .alert_severity import AlertSeverity
        from .alert_type import AlertType

        fields: dict[str, Callable[[Any], None]] = {
            "alertType": lambda n : setattr(self, 'alert_type', n.get_enum_value(AlertType)),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
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
        writer.write_enum_value("alertType", self.alert_type)
        writer.write_int_value("count", self.count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

