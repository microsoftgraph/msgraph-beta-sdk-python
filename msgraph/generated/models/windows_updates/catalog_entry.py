from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CatalogEntry(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new catalogEntry and sets the default values.
        """
        super().__init__()
        # The date on which the content is no longer available to deploy using the service. Read-only.
        self._deployable_until_date_time: Optional[datetime] = None
        # The display name of the content. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The release date for the content. Read-only.
        self._release_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CatalogEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CatalogEntry()
    
    @property
    def deployable_until_date_time(self,) -> Optional[datetime]:
        """
        Gets the deployableUntilDateTime property value. The date on which the content is no longer available to deploy using the service. Read-only.
        Returns: Optional[datetime]
        """
        return self._deployable_until_date_time
    
    @deployable_until_date_time.setter
    def deployable_until_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deployableUntilDateTime property value. The date on which the content is no longer available to deploy using the service. Read-only.
        Args:
            value: Value to set for the deployableUntilDateTime property.
        """
        self._deployable_until_date_time = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the content. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the content. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deployable_until_date_time": lambda n : setattr(self, 'deployable_until_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "release_date_time": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def release_date_time(self,) -> Optional[datetime]:
        """
        Gets the releaseDateTime property value. The release date for the content. Read-only.
        Returns: Optional[datetime]
        """
        return self._release_date_time
    
    @release_date_time.setter
    def release_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the releaseDateTime property value. The release date for the content. Read-only.
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
        writer.write_datetime_value("deployableUntilDateTime", self.deployable_until_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
    

