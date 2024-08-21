from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .monitoring_action import MonitoringAction
    from .monitoring_signal import MonitoringSignal

@dataclass
class MonitoringRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The action triggered when the threshold for the given signal is reached. Possible values are: alertError, pauseDeployment, offerFallback, unknownFutureValue. The offerFallback member is only supported on feature update deployments of Windows 11 and must be paired with the ineligible signal. The fallback version offered is the version 22H2 of Windows 10.
    action: Optional[MonitoringAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The signal to monitor. Possible values are: rollback, ineligible, unknownFutureValue. The ineligible member is only supported on feature update deployments of Windows 11 and must be paired with the offerFallback action.
    signal: Optional[MonitoringSignal] = None
    # The threshold for a signal at which to trigger the action. An integer from 1 to 100 (inclusive). This value is ignored when the signal is ineligible and the action is offerFallback.
    threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MonitoringRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MonitoringRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MonitoringRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .monitoring_action import MonitoringAction
        from .monitoring_signal import MonitoringSignal

        from .monitoring_action import MonitoringAction
        from .monitoring_signal import MonitoringSignal

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(MonitoringAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signal": lambda n : setattr(self, 'signal', n.get_enum_value(MonitoringSignal)),
            "threshold": lambda n : setattr(self, 'threshold', n.get_int_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("signal", self.signal)
        writer.write_int_value("threshold", self.threshold)
        writer.write_additional_data_value(self.additional_data)
    

