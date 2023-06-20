from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import monitoring_action, monitoring_signal

@dataclass
class MonitoringRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The action triggered when the threshold for the given signal is met. Possible values are: alertError, pauseDeployment, unknownFutureValue.
    action: Optional[monitoring_action.MonitoringAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The signal to monitor. Possible values are: rollback, unknownFutureValue.
    signal: Optional[monitoring_signal.MonitoringSignal] = None
    # The threshold for a signal at which to trigger action. An integer from 1 to 100 (inclusive).
    threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MonitoringRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MonitoringRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MonitoringRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import monitoring_action, monitoring_signal

        from . import monitoring_action, monitoring_signal

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(monitoring_action.MonitoringAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signal": lambda n : setattr(self, 'signal', n.get_enum_value(monitoring_signal.MonitoringSignal)),
            "threshold": lambda n : setattr(self, 'threshold', n.get_int_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("signal", self.signal)
        writer.write_int_value("threshold", self.threshold)
        writer.write_additional_data_value(self.additional_data)
    

