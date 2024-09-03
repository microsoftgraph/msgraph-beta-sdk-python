from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem

@dataclass
class AndroidDeviceOwnerKioskModeAppPositionItem(AdditionalDataHolder, BackedModel, Parsable):
    """
    An item in the list of app positions that sets the order of items on the Managed Home Screen
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents an item on the Android Device Owner Managed Home Screen (application, weblink or folder
    item: Optional[AndroidDeviceOwnerKioskModeHomeScreenItem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Position of the item on the grid. Valid values 0 to 9999999
    position: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerKioskModeAppPositionItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeAppPositionItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerKioskModeAppPositionItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem

        from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem

        fields: Dict[str, Callable[[Any], None]] = {
            "item": lambda n : setattr(self, 'item', n.get_object_value(AndroidDeviceOwnerKioskModeHomeScreenItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
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
        writer.write_object_value("item", self.item)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("position", self.position)
        writer.write_additional_data_value(self.additional_data)
    

