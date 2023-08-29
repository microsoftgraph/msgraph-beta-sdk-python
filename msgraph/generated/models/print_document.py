from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .printer_document_configuration import PrinterDocumentConfiguration

from .entity import Entity

@dataclass
class PrintDocument(Entity):
    # The configuration property
    configuration: Optional[PrinterDocumentConfiguration] = None
    # The document's content (MIME) type. Read-only.
    content_type: Optional[str] = None
    # The document's name. Read-only.
    display_name: Optional[str] = None
    # The downloadedDateTime property
    downloaded_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The document's size in bytes. Read-only.
    size: Optional[int] = None
    # The uploadedDateTime property
    uploaded_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintDocument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintDocument
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrintDocument()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .printer_document_configuration import PrinterDocumentConfiguration

        from .entity import Entity
        from .printer_document_configuration import PrinterDocumentConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(PrinterDocumentConfiguration)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "downloadedDateTime": lambda n : setattr(self, 'downloaded_date_time', n.get_datetime_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "uploadedDateTime": lambda n : setattr(self, 'uploaded_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("downloadedDateTime", self.downloaded_date_time)
        writer.write_int_value("size", self.size)
        writer.write_datetime_value("uploadedDateTime", self.uploaded_date_time)
    

