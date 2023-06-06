from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import key_value

@dataclass
class ContentCustomization(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The attributeCollection property
    attribute_collection: Optional[List[key_value.KeyValue]] = None
    # The attributeCollectionRelativeUrl property
    attribute_collection_relative_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentCustomization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentCustomization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentCustomization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import key_value

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeCollection": lambda n : setattr(self, 'attribute_collection', n.get_collection_of_object_values(key_value.KeyValue)),
            "attributeCollectionRelativeUrl": lambda n : setattr(self, 'attribute_collection_relative_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attributeCollection", self.attribute_collection)
        writer.write_str_value("attributeCollectionRelativeUrl", self.attribute_collection_relative_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

