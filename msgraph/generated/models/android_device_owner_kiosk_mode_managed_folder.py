from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_kiosk_mode_folder_item = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_folder_item')

class AndroidDeviceOwnerKioskModeManagedFolder(AdditionalDataHolder, Parsable):
    """
    A folder containing pages of apps and weblinks on the Managed Home Screen
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidDeviceOwnerKioskModeManagedFolder and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Unique identifier for the folder
        self._folder_identifier: Optional[str] = None
        # Display name for the folder
        self._folder_name: Optional[str] = None
        # Items to be added to managed folder. This collection can contain a maximum of 500 elements.
        self._items: Optional[List[android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeManagedFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeManagedFolder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerKioskModeManagedFolder()
    
    @property
    def folder_identifier(self,) -> Optional[str]:
        """
        Gets the folderIdentifier property value. Unique identifier for the folder
        Returns: Optional[str]
        """
        return self._folder_identifier
    
    @folder_identifier.setter
    def folder_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the folderIdentifier property value. Unique identifier for the folder
        Args:
            value: Value to set for the folderIdentifier property.
        """
        self._folder_identifier = value
    
    @property
    def folder_name(self,) -> Optional[str]:
        """
        Gets the folderName property value. Display name for the folder
        Returns: Optional[str]
        """
        return self._folder_name
    
    @folder_name.setter
    def folder_name(self,value: Optional[str] = None) -> None:
        """
        Sets the folderName property value. Display name for the folder
        Args:
            value: Value to set for the folderName property.
        """
        self._folder_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "folder_identifier": lambda n : setattr(self, 'folder_identifier', n.get_str_value()),
            "folder_name": lambda n : setattr(self, 'folder_name', n.get_str_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def items(self,) -> Optional[List[android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem]]:
        """
        Gets the items property value. Items to be added to managed folder. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem]] = None) -> None:
        """
        Sets the items property value. Items to be added to managed folder. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("folderIdentifier", self.folder_identifier)
        writer.write_str_value("folderName", self.folder_name)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

