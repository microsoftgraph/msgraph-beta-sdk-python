from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_script_run_state import DeviceManagementScriptRunState

@dataclass
class ManagedDeviceSummarizedAppState(AdditionalDataHolder, BackedModel, Parsable):
    """
    The summarized information associated with managed device app installation status.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The unique identifier (DeviceId) associated with the device.
    device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution status of the device management script. This status provides insights into whether the script has been successfully executed, encountered errors, or is pending execution.
    summarized_app_state: Optional[DeviceManagementScriptRunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceSummarizedAppState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceSummarizedAppState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceSummarizedAppState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_script_run_state import DeviceManagementScriptRunState

        from .device_management_script_run_state import DeviceManagementScriptRunState

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "summarizedAppState": lambda n : setattr(self, 'summarized_app_state', n.get_enum_value(DeviceManagementScriptRunState)),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("summarizedAppState", self.summarized_app_state)
        writer.write_additional_data_value(self.additional_data)
    

