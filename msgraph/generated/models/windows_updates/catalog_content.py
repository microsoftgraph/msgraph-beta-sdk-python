from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import catalog_entry, deployable_content

from . import deployable_content

class CatalogContent(deployable_content.DeployableContent):
    def __init__(self,) -> None:
        """
        Instantiates a new CatalogContent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.catalogContent"
        # The catalogEntry property
        self._catalog_entry: Optional[catalog_entry.CatalogEntry] = None
    
    @property
    def catalog_entry(self,) -> Optional[catalog_entry.CatalogEntry]:
        """
        Gets the catalogEntry property value. The catalogEntry property
        Returns: Optional[catalog_entry.CatalogEntry]
        """
        return self._catalog_entry
    
    @catalog_entry.setter
    def catalog_entry(self,value: Optional[catalog_entry.CatalogEntry] = None) -> None:
        """
        Sets the catalogEntry property value. The catalogEntry property
        Args:
            value: Value to set for the catalog_entry property.
        """
        self._catalog_entry = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CatalogContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CatalogContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CatalogContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import catalog_entry, deployable_content

        fields: Dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(catalog_entry.CatalogEntry)),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
    

