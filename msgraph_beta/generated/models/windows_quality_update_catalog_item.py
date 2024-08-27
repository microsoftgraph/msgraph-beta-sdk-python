from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_quality_update_classification import WindowsQualityUpdateClassification
    from .windows_update_catalog_item import WindowsUpdateCatalogItem

from .windows_update_catalog_item import WindowsUpdateCatalogItem

@dataclass
class WindowsQualityUpdateCatalogItem(WindowsUpdateCatalogItem):
    """
    Windows update catalog item entity
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsQualityUpdateCatalogItem"
    # Windows quality update classification
    classification: Optional[WindowsQualityUpdateClassification] = None
    # Flag indicating if update qualifies for expedite
    is_expeditable: Optional[bool] = None
    # Knowledge base article id
    kb_article_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateCatalogItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateCatalogItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateCatalogItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_quality_update_classification import WindowsQualityUpdateClassification
        from .windows_update_catalog_item import WindowsUpdateCatalogItem

        from .windows_quality_update_classification import WindowsQualityUpdateClassification
        from .windows_update_catalog_item import WindowsUpdateCatalogItem

        fields: Dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(WindowsQualityUpdateClassification)),
            "isExpeditable": lambda n : setattr(self, 'is_expeditable', n.get_bool_value()),
            "kbArticleId": lambda n : setattr(self, 'kb_article_id', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("classification", self.classification)
        writer.write_bool_value("isExpeditable", self.is_expeditable)
        writer.write_str_value("kbArticleId", self.kb_article_id)
    

