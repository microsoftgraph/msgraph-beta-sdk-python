from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import catalog_entry
    from .. import entity

from .. import entity

class Catalog(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new catalog and sets the default values.
        """
        super().__init__()
        # Lists the content that you can approve for deployment. Read-only.
        self._entries: Optional[List[catalog_entry.CatalogEntry]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Catalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Catalog
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Catalog()
    
    @property
    def entries(self,) -> Optional[List[catalog_entry.CatalogEntry]]:
        """
        Gets the entries property value. Lists the content that you can approve for deployment. Read-only.
        Returns: Optional[List[catalog_entry.CatalogEntry]]
        """
        return self._entries
    
    @entries.setter
    def entries(self,value: Optional[List[catalog_entry.CatalogEntry]] = None) -> None:
        """
        Sets the entries property value. Lists the content that you can approve for deployment. Read-only.
        Args:
            value: Value to set for the entries property.
        """
        self._entries = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import catalog_entry
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "entries": lambda n : setattr(self, 'entries', n.get_collection_of_object_values(catalog_entry.CatalogEntry)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("entries", self.entries)
    

