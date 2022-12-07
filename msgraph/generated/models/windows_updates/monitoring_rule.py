from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

monitoring_action = lazy_import('msgraph.generated.models.windows_updates.monitoring_action')
monitoring_signal = lazy_import('msgraph.generated.models.windows_updates.monitoring_signal')

class MonitoringRule(AdditionalDataHolder, Parsable):
    @property
    def action(self,) -> Optional[monitoring_action.MonitoringAction]:
        """
        Gets the action property value. The action triggered when the threshold for the given signal is met. Possible values are: alertError, pauseDeployment, unknownFutureValue.
        Returns: Optional[monitoring_action.MonitoringAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[monitoring_action.MonitoringAction] = None) -> None:
        """
        Sets the action property value. The action triggered when the threshold for the given signal is met. Possible values are: alertError, pauseDeployment, unknownFutureValue.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
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
        Instantiates a new monitoringRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The action triggered when the threshold for the given signal is met. Possible values are: alertError, pauseDeployment, unknownFutureValue.
        self._action: Optional[monitoring_action.MonitoringAction] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The signal to monitor. Possible values are: rollback, unknownFutureValue.
        self._signal: Optional[monitoring_signal.MonitoringSignal] = None
        # The threshold for a signal at which to trigger action. An integer from 1 to 100 (inclusive).
        self._threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MonitoringRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MonitoringRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MonitoringRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(monitoring_action.MonitoringAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signal": lambda n : setattr(self, 'signal', n.get_enum_value(monitoring_signal.MonitoringSignal)),
            "threshold": lambda n : setattr(self, 'threshold', n.get_int_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("signal", self.signal)
        writer.write_int_value("threshold", self.threshold)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def signal(self,) -> Optional[monitoring_signal.MonitoringSignal]:
        """
        Gets the signal property value. The signal to monitor. Possible values are: rollback, unknownFutureValue.
        Returns: Optional[monitoring_signal.MonitoringSignal]
        """
        return self._signal
    
    @signal.setter
    def signal(self,value: Optional[monitoring_signal.MonitoringSignal] = None) -> None:
        """
        Sets the signal property value. The signal to monitor. Possible values are: rollback, unknownFutureValue.
        Args:
            value: Value to set for the signal property.
        """
        self._signal = value
    
    @property
    def threshold(self,) -> Optional[int]:
        """
        Gets the threshold property value. The threshold for a signal at which to trigger action. An integer from 1 to 100 (inclusive).
        Returns: Optional[int]
        """
        return self._threshold
    
    @threshold.setter
    def threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the threshold property value. The threshold for a signal at which to trigger action. An integer from 1 to 100 (inclusive).
        Args:
            value: Value to set for the threshold property.
        """
        self._threshold = value
    

