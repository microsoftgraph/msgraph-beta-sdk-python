from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_quality_update_classification, windows_update_catalog_item

from . import windows_update_catalog_item

@dataclass
class WindowsQualityUpdateCatalogItem(windows_update_catalog_item.WindowsUpdateCatalogItem):
    odata_type = "#microsoft.graph.windowsQualityUpdateCatalogItem"
    # Windows quality update classification
    classification: Optional[windows_quality_update_classification.WindowsQualityUpdateClassification] = None
    # Flag indicating if update qualifies for expedite
    is_expeditable: Optional[bool] = None
    # Knowledge base article id
    kb_article_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsQualityUpdateCatalogItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateCatalogItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsQualityUpdateCatalogItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_quality_update_classification, windows_update_catalog_item

        fields: Dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(windows_quality_update_classification.WindowsQualityUpdateClassification)),
            "isExpeditable": lambda n : setattr(self, 'is_expeditable', n.get_bool_value()),
            "kbArticleId": lambda n : setattr(self, 'kb_article_id', n.get_str_value()),
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
        writer.write_enum_value("classification", self.classification)
        writer.write_bool_value("isExpeditable", self.is_expeditable)
        writer.write_str_value("kbArticleId", self.kb_article_id)
    

