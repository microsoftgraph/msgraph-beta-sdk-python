from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_scope_action_status import DeviceScopeActionStatus

@dataclass
class DeviceScopeActionResult(AdditionalDataHolder, BackedModel, Parsable):
    """
    The result of the triggered device scope action.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

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
    status: Optional[DeviceScopeActionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceScopeActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceScopeActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceScopeActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_scope_action_status import DeviceScopeActionStatus

        from .device_scope_action_status import DeviceScopeActionStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceScopeAction": lambda n : setattr(self, 'device_scope_action', n.get_str_value()),
            "deviceScopeId": lambda n : setattr(self, 'device_scope_id', n.get_str_value()),
            "failedMessage": lambda n : setattr(self, 'failed_message', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DeviceScopeActionStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("deviceScopeAction", self.device_scope_action)
        writer.write_str_value("deviceScopeId", self.device_scope_id)
        writer.write_str_value("failedMessage", self.failed_message)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

