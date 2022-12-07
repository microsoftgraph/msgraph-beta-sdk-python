from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

software_update_catalog_entry = lazy_import('msgraph.generated.models.windows_updates.software_update_catalog_entry')

class FeatureUpdateCatalogEntry(software_update_catalog_entry.SoftwareUpdateCatalogEntry):
    def __init__(self,) -> None:
        """
        Instantiates a new FeatureUpdateCatalogEntry and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry"
        # The version of the feature update. Read-only.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FeatureUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FeatureUpdateCatalogEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FeatureUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version of the feature update. Read-only.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version of the feature update. Read-only.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

