from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ediscovery_file, file_processing_status, source_type, string_value_dictionary
    from .. import entity

from .. import entity

@dataclass
class File(entity.Entity):
    # The content property
    content: Optional[bytes] = None
    # The dateTime property
    date_time: Optional[datetime] = None
    # The extension property
    extension: Optional[str] = None
    # The extractedTextContent property
    extracted_text_content: Optional[bytes] = None
    # The mediaType property
    media_type: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The otherProperties property
    other_properties: Optional[string_value_dictionary.StringValueDictionary] = None
    # The processingStatus property
    processing_status: Optional[file_processing_status.FileProcessingStatus] = None
    # The senderOrAuthors property
    sender_or_authors: Optional[List[str]] = None
    # The size property
    size: Optional[int] = None
    # The sourceType property
    source_type: Optional[source_type.SourceType] = None
    # The subjectTitle property
    subject_title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.security.ediscoveryFile":
                from . import ediscovery_file

                return ediscovery_file.EdiscoveryFile()
        return File()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ediscovery_file, file_processing_status, source_type, string_value_dictionary
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_str_value()),
            "extractedTextContent": lambda n : setattr(self, 'extracted_text_content', n.get_bytes_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "otherProperties": lambda n : setattr(self, 'other_properties', n.get_object_value(string_value_dictionary.StringValueDictionary)),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(file_processing_status.FileProcessingStatus)),
            "senderOrAuthors": lambda n : setattr(self, 'sender_or_authors', n.get_collection_of_primitive_values(str)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(source_type.SourceType)),
            "subjectTitle": lambda n : setattr(self, 'subject_title', n.get_str_value()),
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
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_str_value("extension", self.extension)
        writer.write_object_value("extractedTextContent", self.extracted_text_content)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_str_value("name", self.name)
        writer.write_object_value("otherProperties", self.other_properties)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_collection_of_primitive_values("senderOrAuthors", self.sender_or_authors)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_str_value("subjectTitle", self.subject_title)
    

