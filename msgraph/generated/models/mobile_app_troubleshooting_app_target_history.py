from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_troubleshooting_history_item, run_state

from . import mobile_app_troubleshooting_history_item

@dataclass
class MobileAppTroubleshootingAppTargetHistory(mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem):
    # Error code for the failure, empty if no failure.
    error_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution status of the device management script.
    run_state: Optional[run_state.RunState] = None
    # AAD security group id to which it was targeted.
    security_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingAppTargetHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingAppTargetHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppTroubleshootingAppTargetHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_troubleshooting_history_item, run_state

        fields: Dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "runState": lambda n : setattr(self, 'run_state', n.get_enum_value(run_state.RunState)),
            "securityGroupId": lambda n : setattr(self, 'security_group_id', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("runState", self.run_state)
        writer.write_str_value("securityGroupId", self.security_group_id)
    

