from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

@dataclass
class AndroidDeviceOwnerKioskModeManagedFolder(AdditionalDataHolder, BackedModel, Parsable):
    """
    A folder containing pages of apps and weblinks on the Managed Home Screen
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Unique identifier for the folder
    folder_identifier: Optional[str] = None
    # Display name for the folder
    folder_name: Optional[str] = None
    # Items to be added to managed folder. This collection can contain a maximum of 500 elements.
    items: Optional[List[AndroidDeviceOwnerKioskModeFolderItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeManagedFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeManagedFolder
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerKioskModeManagedFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        fields: Dict[str, Callable[[Any], None]] = {
            "folderIdentifier": lambda n : setattr(self, 'folder_identifier', n.get_str_value()),
            "folderName": lambda n : setattr(self, 'folder_name', n.get_str_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(AndroidDeviceOwnerKioskModeFolderItem)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("folderIdentifier", self.folder_identifier)
        writer.write_str_value("folderName", self.folder_name)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

