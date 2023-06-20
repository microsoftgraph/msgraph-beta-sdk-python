from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import catalog_entry
    from .. import entity

from .. import entity

@dataclass
class Catalog(entity.Entity):
    # Lists the content that you can approve for deployment. Read-only.
    entries: Optional[List[catalog_entry.CatalogEntry]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Catalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Catalog
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Catalog()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import catalog_entry
        from .. import entity

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("entries", self.entries)
    

