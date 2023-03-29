from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_quality_update_classification, windows_update_catalog_item

from . import windows_update_catalog_item

class WindowsQualityUpdateCatalogItem(windows_update_catalog_item.WindowsUpdateCatalogItem):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsQualityUpdateCatalogItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsQualityUpdateCatalogItem"
        # Windows quality update classification
        self._classification: Optional[windows_quality_update_classification.WindowsQualityUpdateClassification] = None
        # Flag indicating if update qualifies for expedite
        self._is_expeditable: Optional[bool] = None
        # Knowledge base article id
        self._kb_article_id: Optional[str] = None
    
    @property
    def classification(self,) -> Optional[windows_quality_update_classification.WindowsQualityUpdateClassification]:
        """
        Gets the classification property value. Windows quality update classification
        Returns: Optional[windows_quality_update_classification.WindowsQualityUpdateClassification]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[windows_quality_update_classification.WindowsQualityUpdateClassification] = None) -> None:
        """
        Sets the classification property value. Windows quality update classification
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
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
    
    @property
    def is_expeditable(self,) -> Optional[bool]:
        """
        Gets the isExpeditable property value. Flag indicating if update qualifies for expedite
        Returns: Optional[bool]
        """
        return self._is_expeditable
    
    @is_expeditable.setter
    def is_expeditable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExpeditable property value. Flag indicating if update qualifies for expedite
        Args:
            value: Value to set for the is_expeditable property.
        """
        self._is_expeditable = value
    
    @property
    def kb_article_id(self,) -> Optional[str]:
        """
        Gets the kbArticleId property value. Knowledge base article id
        Returns: Optional[str]
        """
        return self._kb_article_id
    
    @kb_article_id.setter
    def kb_article_id(self,value: Optional[str] = None) -> None:
        """
        Sets the kbArticleId property value. Knowledge base article id
        Args:
            value: Value to set for the kb_article_id property.
        """
        self._kb_article_id = value
    
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
    

