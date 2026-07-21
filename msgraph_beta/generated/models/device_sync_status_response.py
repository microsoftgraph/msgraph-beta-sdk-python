from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sync_component import SyncComponent

@dataclass
class DeviceSyncStatusResponse(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates the collection of sync component statuses representing infrastructure and policy progress. Each entry represents a component that has started reporting during this sync operation. Components appear in the collection only after they begin executing. Read-only. Not nullable.
    components: Optional[list[SyncComponent]] = None
    # Indicates the managed device identifier. Used to correlate this sync status snapshot with the device that was synced. This is the same id used in the managedDevice entity. Example: 'd1e2f3a4-b5c6-7890-abcd-ef1234567890'. Read-only. Not nullable.
    device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceSyncStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceSyncStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceSyncStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sync_component import SyncComponent

        from .sync_component import SyncComponent

        fields: dict[str, Callable[[Any], None]] = {
            "components": lambda n : setattr(self, 'components', n.get_collection_of_object_values(SyncComponent)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

