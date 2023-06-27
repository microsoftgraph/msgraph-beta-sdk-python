from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .quality_update_classification import QualityUpdateClassification
    from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

@dataclass
class QualityUpdateCatalogEntry(SoftwareUpdateCatalogEntry):
    odata_type = "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry"
    # Indicates whether the content can be deployed as an expedited quality update. Read-only.
    is_expeditable: Optional[bool] = None
    # The qualityUpdateClassification property
    quality_update_classification: Optional[QualityUpdateClassification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QualityUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: QualityUpdateCatalogEntry
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return QualityUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .quality_update_classification import QualityUpdateClassification
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        from .quality_update_classification import QualityUpdateClassification
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        fields: Dict[str, Callable[[Any], None]] = {
            "isExpeditable": lambda n : setattr(self, 'is_expeditable', n.get_bool_value()),
            "qualityUpdateClassification": lambda n : setattr(self, 'quality_update_classification', n.get_enum_value(QualityUpdateClassification)),
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
        writer.write_bool_value("isExpeditable", self.is_expeditable)
        writer.write_enum_value("qualityUpdateClassification", self.quality_update_classification)
    

