from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import quality_update_classification, software_update_catalog_entry

from . import software_update_catalog_entry

class QualityUpdateCatalogEntry(software_update_catalog_entry.SoftwareUpdateCatalogEntry):
    def __init__(self,) -> None:
        """
        Instantiates a new QualityUpdateCatalogEntry and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry"
        # Indicates whether the content can be deployed as an expedited quality update. Read-only.
        self._is_expeditable: Optional[bool] = None
        # The qualityUpdateClassification property
        self._quality_update_classification: Optional[quality_update_classification.QualityUpdateClassification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QualityUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: QualityUpdateCatalogEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return QualityUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import quality_update_classification, software_update_catalog_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "isExpeditable": lambda n : setattr(self, 'is_expeditable', n.get_bool_value()),
            "qualityUpdateClassification": lambda n : setattr(self, 'quality_update_classification', n.get_enum_value(quality_update_classification.QualityUpdateClassification)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_expeditable(self,) -> Optional[bool]:
        """
        Gets the isExpeditable property value. Indicates whether the content can be deployed as an expedited quality update. Read-only.
        Returns: Optional[bool]
        """
        return self._is_expeditable
    
    @is_expeditable.setter
    def is_expeditable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExpeditable property value. Indicates whether the content can be deployed as an expedited quality update. Read-only.
        Args:
            value: Value to set for the is_expeditable property.
        """
        self._is_expeditable = value
    
    @property
    def quality_update_classification(self,) -> Optional[quality_update_classification.QualityUpdateClassification]:
        """
        Gets the qualityUpdateClassification property value. The qualityUpdateClassification property
        Returns: Optional[quality_update_classification.QualityUpdateClassification]
        """
        return self._quality_update_classification
    
    @quality_update_classification.setter
    def quality_update_classification(self,value: Optional[quality_update_classification.QualityUpdateClassification] = None) -> None:
        """
        Sets the qualityUpdateClassification property value. The qualityUpdateClassification property
        Args:
            value: Value to set for the quality_update_classification property.
        """
        self._quality_update_classification = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isExpeditable", self.is_expeditable)
        writer.write_enum_value("qualityUpdateClassification", self.quality_update_classification)
    

