from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CallTranscript(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new callTranscript and sets the default values.
        """
        super().__init__()
        # A field representing the content of the transcript. Read-only.
        self._content: Optional[bytes] = None
        # Date and time at which the transcript was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. A field representing the content of the transcript. Read-only.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. A field representing the content of the transcript. Read-only.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time at which the transcript was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time at which the transcript was created. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallTranscript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallTranscript
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallTranscript()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

