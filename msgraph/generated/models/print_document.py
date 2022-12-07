from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
printer_document_configuration = lazy_import('msgraph.generated.models.printer_document_configuration')

class PrintDocument(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def configuration(self,) -> Optional[printer_document_configuration.PrinterDocumentConfiguration]:
        """
        Gets the configuration property value. The configuration property
        Returns: Optional[printer_document_configuration.PrinterDocumentConfiguration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[printer_document_configuration.PrinterDocumentConfiguration] = None) -> None:
        """
        Sets the configuration property value. The configuration property
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printDocument and sets the default values.
        """
        super().__init__()
        # The configuration property
        self._configuration: Optional[printer_document_configuration.PrinterDocumentConfiguration] = None
        # The document's content (MIME) type. Read-only.
        self._content_type: Optional[str] = None
        # The document's name. Read-only.
        self._display_name: Optional[str] = None
        # The downloadedDateTime property
        self._downloaded_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The document's size in bytes. Read-only.
        self._size: Optional[int] = None
        # The uploadedDateTime property
        self._uploaded_date_time: Optional[datetime] = None
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. The document's content (MIME) type. Read-only.
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. The document's content (MIME) type. Read-only.
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintDocument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintDocument
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintDocument()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The document's name. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The document's name. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def downloaded_date_time(self,) -> Optional[datetime]:
        """
        Gets the downloadedDateTime property value. The downloadedDateTime property
        Returns: Optional[datetime]
        """
        return self._downloaded_date_time
    
    @downloaded_date_time.setter
    def downloaded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the downloadedDateTime property value. The downloadedDateTime property
        Args:
            value: Value to set for the downloadedDateTime property.
        """
        self._downloaded_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(printer_document_configuration.PrinterDocumentConfiguration)),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "downloaded_date_time": lambda n : setattr(self, 'downloaded_date_time', n.get_datetime_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "uploaded_date_time": lambda n : setattr(self, 'uploaded_date_time', n.get_datetime_value()),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("downloadedDateTime", self.downloaded_date_time)
        writer.write_int_value("size", self.size)
        writer.write_datetime_value("uploadedDateTime", self.uploaded_date_time)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The document's size in bytes. Read-only.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The document's size in bytes. Read-only.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def uploaded_date_time(self,) -> Optional[datetime]:
        """
        Gets the uploadedDateTime property value. The uploadedDateTime property
        Returns: Optional[datetime]
        """
        return self._uploaded_date_time
    
    @uploaded_date_time.setter
    def uploaded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the uploadedDateTime property value. The uploadedDateTime property
        Args:
            value: Value to set for the uploadedDateTime property.
        """
        self._uploaded_date_time = value
    

