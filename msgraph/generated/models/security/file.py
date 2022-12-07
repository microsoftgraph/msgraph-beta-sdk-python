from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
file_processing_status = lazy_import('msgraph.generated.models.security.file_processing_status')
source_type = lazy_import('msgraph.generated.models.security.source_type')
string_value_dictionary = lazy_import('msgraph.generated.models.security.string_value_dictionary')

class File(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new file and sets the default values.
        """
        super().__init__()
        # The content property
        self._content: Optional[bytes] = None
        # The dateTime property
        self._date_time: Optional[datetime] = None
        # The extension property
        self._extension: Optional[str] = None
        # The extractedTextContent property
        self._extracted_text_content: Optional[bytes] = None
        # The mediaType property
        self._media_type: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The otherProperties property
        self._other_properties: Optional[string_value_dictionary.StringValueDictionary] = None
        # The processingStatus property
        self._processing_status: Optional[file_processing_status.FileProcessingStatus] = None
        # The senderOrAuthors property
        self._sender_or_authors: Optional[List[str]] = None
        # The size property
        self._size: Optional[int] = None
        # The sourceType property
        self._source_type: Optional[source_type.SourceType] = None
        # The subjectTitle property
        self._subject_title: Optional[str] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content property
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content property
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
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
        return File()
    
    @property
    def date_time(self,) -> Optional[datetime]:
        """
        Gets the dateTime property value. The dateTime property
        Returns: Optional[datetime]
        """
        return self._date_time
    
    @date_time.setter
    def date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dateTime property value. The dateTime property
        Args:
            value: Value to set for the dateTime property.
        """
        self._date_time = value
    
    @property
    def extension(self,) -> Optional[str]:
        """
        Gets the extension property value. The extension property
        Returns: Optional[str]
        """
        return self._extension
    
    @extension.setter
    def extension(self,value: Optional[str] = None) -> None:
        """
        Sets the extension property value. The extension property
        Args:
            value: Value to set for the extension property.
        """
        self._extension = value
    
    @property
    def extracted_text_content(self,) -> Optional[bytes]:
        """
        Gets the extractedTextContent property value. The extractedTextContent property
        Returns: Optional[bytes]
        """
        return self._extracted_text_content
    
    @extracted_text_content.setter
    def extracted_text_content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the extractedTextContent property value. The extractedTextContent property
        Args:
            value: Value to set for the extractedTextContent property.
        """
        self._extracted_text_content = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "date_time": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_str_value()),
            "extracted_text_content": lambda n : setattr(self, 'extracted_text_content', n.get_bytes_value()),
            "media_type": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "other_properties": lambda n : setattr(self, 'other_properties', n.get_object_value(string_value_dictionary.StringValueDictionary)),
            "processing_status": lambda n : setattr(self, 'processing_status', n.get_enum_value(file_processing_status.FileProcessingStatus)),
            "sender_or_authors": lambda n : setattr(self, 'sender_or_authors', n.get_collection_of_primitive_values(str)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "source_type": lambda n : setattr(self, 'source_type', n.get_enum_value(source_type.SourceType)),
            "subject_title": lambda n : setattr(self, 'subject_title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def media_type(self,) -> Optional[str]:
        """
        Gets the mediaType property value. The mediaType property
        Returns: Optional[str]
        """
        return self._media_type
    
    @media_type.setter
    def media_type(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaType property value. The mediaType property
        Args:
            value: Value to set for the mediaType property.
        """
        self._media_type = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def other_properties(self,) -> Optional[string_value_dictionary.StringValueDictionary]:
        """
        Gets the otherProperties property value. The otherProperties property
        Returns: Optional[string_value_dictionary.StringValueDictionary]
        """
        return self._other_properties
    
    @other_properties.setter
    def other_properties(self,value: Optional[string_value_dictionary.StringValueDictionary] = None) -> None:
        """
        Sets the otherProperties property value. The otherProperties property
        Args:
            value: Value to set for the otherProperties property.
        """
        self._other_properties = value
    
    @property
    def processing_status(self,) -> Optional[file_processing_status.FileProcessingStatus]:
        """
        Gets the processingStatus property value. The processingStatus property
        Returns: Optional[file_processing_status.FileProcessingStatus]
        """
        return self._processing_status
    
    @processing_status.setter
    def processing_status(self,value: Optional[file_processing_status.FileProcessingStatus] = None) -> None:
        """
        Sets the processingStatus property value. The processingStatus property
        Args:
            value: Value to set for the processingStatus property.
        """
        self._processing_status = value
    
    @property
    def sender_or_authors(self,) -> Optional[List[str]]:
        """
        Gets the senderOrAuthors property value. The senderOrAuthors property
        Returns: Optional[List[str]]
        """
        return self._sender_or_authors
    
    @sender_or_authors.setter
    def sender_or_authors(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the senderOrAuthors property value. The senderOrAuthors property
        Args:
            value: Value to set for the senderOrAuthors property.
        """
        self._sender_or_authors = value
    
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
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size property
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size property
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def source_type(self,) -> Optional[source_type.SourceType]:
        """
        Gets the sourceType property value. The sourceType property
        Returns: Optional[source_type.SourceType]
        """
        return self._source_type
    
    @source_type.setter
    def source_type(self,value: Optional[source_type.SourceType] = None) -> None:
        """
        Sets the sourceType property value. The sourceType property
        Args:
            value: Value to set for the sourceType property.
        """
        self._source_type = value
    
    @property
    def subject_title(self,) -> Optional[str]:
        """
        Gets the subjectTitle property value. The subjectTitle property
        Returns: Optional[str]
        """
        return self._subject_title
    
    @subject_title.setter
    def subject_title(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectTitle property value. The subjectTitle property
        Args:
            value: Value to set for the subjectTitle property.
        """
        self._subject_title = value
    

