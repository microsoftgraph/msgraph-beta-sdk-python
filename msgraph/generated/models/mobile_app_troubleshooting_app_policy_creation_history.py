from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_troubleshooting_history_item, run_state

from . import mobile_app_troubleshooting_history_item

class MobileAppTroubleshootingAppPolicyCreationHistory(mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem):
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppTroubleshootingAppPolicyCreationHistory and sets the default values.
        """
        super().__init__()
        # Error code for the failure, empty if no failure.
        self._error_code: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the type of execution status of the device management script.
        self._run_state: Optional[run_state.RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingAppPolicyCreationHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingAppPolicyCreationHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppTroubleshootingAppPolicyCreationHistory()
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. Error code for the failure, empty if no failure.
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. Error code for the failure, empty if no failure.
        Args:
            value: Value to set for the error_code property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_troubleshooting_history_item, run_state

        fields: Dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "runState": lambda n : setattr(self, 'run_state', n.get_enum_value(run_state.RunState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def run_state(self,) -> Optional[run_state.RunState]:
        """
        Gets the runState property value. Indicates the type of execution status of the device management script.
        Returns: Optional[run_state.RunState]
        """
        return self._run_state
    
    @run_state.setter
    def run_state(self,value: Optional[run_state.RunState] = None) -> None:
        """
        Sets the runState property value. Indicates the type of execution status of the device management script.
        Args:
            value: Value to set for the run_state property.
        """
        self._run_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("runState", self.run_state)
    

