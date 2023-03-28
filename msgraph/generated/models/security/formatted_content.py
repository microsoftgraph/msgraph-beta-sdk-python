from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_format

class FormattedContent(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new formattedContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The content of this formattedContent.
        self._content: Optional[str] = None
        # The format of the content. The possible values are: text, html, markdown, unknownFutureValue.
        self._format: Optional[content_format.ContentFormat] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. The content of this formattedContent.
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. The content of this formattedContent.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FormattedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FormattedContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FormattedContent()
    
    @property
    def format(self,) -> Optional[content_format.ContentFormat]:
        """
        Gets the format property value. The format of the content. The possible values are: text, html, markdown, unknownFutureValue.
        Returns: Optional[content_format.ContentFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[content_format.ContentFormat] = None) -> None:
        """
        Sets the format property value. The format of the content. The possible values are: text, html, markdown, unknownFutureValue.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_format

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(content_format.ContentFormat)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
        writer.write_str_value("content", self.content)
        writer.write_enum_value("format", self.format)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

