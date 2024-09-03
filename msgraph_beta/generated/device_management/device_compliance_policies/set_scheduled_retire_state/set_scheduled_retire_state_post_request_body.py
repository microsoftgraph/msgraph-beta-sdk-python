from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.scheduled_retire_state import ScheduledRetireState

@dataclass
class SetScheduledRetireStatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The managedDeviceIds property
    managed_device_ids: Optional[List[str]] = None
    # The scopedToAllDevices property
    scoped_to_all_devices: Optional[bool] = None
    # Cancel or confirm scheduled retire 
    state: Optional[ScheduledRetireState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SetScheduledRetireStatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetScheduledRetireStatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SetScheduledRetireStatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.scheduled_retire_state import ScheduledRetireState

        from ....models.scheduled_retire_state import ScheduledRetireState

        fields: Dict[str, Callable[[Any], None]] = {
            "managedDeviceIds": lambda n : setattr(self, 'managed_device_ids', n.get_collection_of_primitive_values(str)),
            "scopedToAllDevices": lambda n : setattr(self, 'scoped_to_all_devices', n.get_bool_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ScheduledRetireState)),
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
        writer.write_collection_of_primitive_values("managedDeviceIds", self.managed_device_ids)
        writer.write_bool_value("scopedToAllDevices", self.scoped_to_all_devices)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

