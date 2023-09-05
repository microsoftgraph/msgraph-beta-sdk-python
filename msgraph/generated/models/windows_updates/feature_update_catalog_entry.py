from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

@dataclass
class FeatureUpdateCatalogEntry(SoftwareUpdateCatalogEntry):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry"
    # The build number of the feature update. Read-only.
    build_number: Optional[str] = None
    # The version of the feature update. Read-only.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FeatureUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeatureUpdateCatalogEntry
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FeatureUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        fields: Dict[str, Callable[[Any], None]] = {
            "buildNumber": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("version", self.version)
    

