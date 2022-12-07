from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsUpdateCatalogItem(entity.Entity):
    """
    Windows update catalog item entity
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsUpdateCatalogItem and sets the default values.
        """
        super().__init__()
        # The display name for the catalog item.
        self._display_name: Optional[str] = None
        # The last supported date for a catalog item
        self._end_of_support_date: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date the catalog item was released
        self._release_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateCatalogItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateCatalogItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUpdateCatalogItem()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the catalog item.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the catalog item.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_of_support_date(self,) -> Optional[datetime]:
        """
        Gets the endOfSupportDate property value. The last supported date for a catalog item
        Returns: Optional[datetime]
        """
        return self._end_of_support_date
    
    @end_of_support_date.setter
    def end_of_support_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endOfSupportDate property value. The last supported date for a catalog item
        Args:
            value: Value to set for the endOfSupportDate property.
        """
        self._end_of_support_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_of_support_date": lambda n : setattr(self, 'end_of_support_date', n.get_datetime_value()),
            "release_date_time": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def release_date_time(self,) -> Optional[datetime]:
        """
        Gets the releaseDateTime property value. The date the catalog item was released
        Returns: Optional[datetime]
        """
        return self._release_date_time
    
    @release_date_time.setter
    def release_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the releaseDateTime property value. The date the catalog item was released
        Args:
            value: Value to set for the releaseDateTime property.
        """
        self._release_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endOfSupportDate", self.end_of_support_date)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
    

