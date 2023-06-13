from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_scope_action_status

@dataclass
class DeviceScopeActionResult(AdditionalDataHolder, Parsable):
    """
    The result of the triggered device scope action.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
    device_scope_action: Optional[str] = None
    # The unique identifier of the device scope the action was triggered on.
    device_scope_id: Optional[str] = None
    # The message indicates the reason the device scope action failed to trigger.
    failed_message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the status of the attempted device scope action
    status: Optional[device_scope_action_status.DeviceScopeActionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceScopeActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceScopeActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceScopeActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_scope_action_status

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceScopeAction": lambda n : setattr(self, 'device_scope_action', n.get_str_value()),
            "deviceScopeId": lambda n : setattr(self, 'device_scope_id', n.get_str_value()),
            "failedMessage": lambda n : setattr(self, 'failed_message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_scope_action_status.DeviceScopeActionStatus)),
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
        writer.write_str_value("deviceScopeAction", self.device_scope_action)
        writer.write_str_value("deviceScopeId", self.device_scope_id)
        writer.write_str_value("failedMessage", self.failed_message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

