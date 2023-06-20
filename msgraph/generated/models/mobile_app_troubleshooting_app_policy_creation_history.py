from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_troubleshooting_history_item, run_state

from . import mobile_app_troubleshooting_history_item

@dataclass
class MobileAppTroubleshootingAppPolicyCreationHistory(mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem):
    # Error code for the failure, empty if no failure.
    error_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution status of the device management script.
    run_state: Optional[run_state.RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingAppPolicyCreationHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingAppPolicyCreationHistory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MobileAppTroubleshootingAppPolicyCreationHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_troubleshooting_history_item, run_state

        from . import mobile_app_troubleshooting_history_item, run_state

        fields: Dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "runState": lambda n : setattr(self, 'run_state', n.get_enum_value(run_state.RunState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("runState", self.run_state)
    

