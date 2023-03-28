from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attachment_type

class AttachmentInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new attachmentInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of the attachment. The possible values are: file, item, reference. Required.
        self._attachment_type: Optional[attachment_type.AttachmentType] = None
        # The nature of the data in the attachment. Optional.
        self._content_type: Optional[str] = None
        # The display name of the attachment. This can be a descriptive string and does not have to be the actual file name. Required.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The length of the attachment in bytes. Required.
        self._size: Optional[int] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def attachment_type(self,) -> Optional[attachment_type.AttachmentType]:
        """
        Gets the attachmentType property value. The type of the attachment. The possible values are: file, item, reference. Required.
        Returns: Optional[attachment_type.AttachmentType]
        """
        return self._attachment_type
    
    @attachment_type.setter
    def attachment_type(self,value: Optional[attachment_type.AttachmentType] = None) -> None:
        """
        Sets the attachmentType property value. The type of the attachment. The possible values are: file, item, reference. Required.
        Args:
            value: Value to set for the attachment_type property.
        """
        self._attachment_type = value
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. The nature of the data in the attachment. Optional.
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. The nature of the data in the attachment. Optional.
        Args:
            value: Value to set for the content_type property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttachmentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttachmentInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attachment_type

        fields: Dict[str, Callable[[Any], None]] = {
            "attachmentType": lambda n : setattr(self, 'attachment_type', n.get_enum_value(attachment_type.AttachmentType)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The display name of the attachment. This can be a descriptive string and does not have to be the actual file name. Required.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The display name of the attachment. This can be a descriptive string and does not have to be the actual file name. Required.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("attachmentType", self.attachment_type)
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The length of the attachment in bytes. Required.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The length of the attachment in bytes. Required.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    

