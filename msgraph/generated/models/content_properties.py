from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attachment_content_properties, content_metadata, file_content_properties

@dataclass
class ContentProperties(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The extensions property
    extensions: Optional[List[str]] = None
    # The lastModifiedBy property
    last_modified_by: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The metadata property
    metadata: Optional[content_metadata.ContentMetadata] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentProperties
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentContentProperties".casefold():
            from . import attachment_content_properties

            return attachment_content_properties.AttachmentContentProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileContentProperties".casefold():
            from . import file_content_properties

            return file_content_properties.FileContentProperties()
        return ContentProperties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attachment_content_properties, content_metadata, file_content_properties

        from . import attachment_content_properties, content_metadata, file_content_properties

        fields: Dict[str, Callable[[Any], None]] = {
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_primitive_values(str)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(content_metadata.ContentMetadata)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("extensions", self.extensions)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

