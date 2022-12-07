from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VisualProperties(AdditionalDataHolder, Parsable):
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
    def body(self,) -> Optional[str]:
        """
        Gets the body property value. The body of a visual user notification. Body is optional.
        Returns: Optional[str]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[str] = None) -> None:
        """
        Sets the body property value. The body of a visual user notification. Body is optional.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new visualProperties and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The body of a visual user notification. Body is optional.
        self._body: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The title of a visual user notification. This field is required for visual notification payloads.
        self._title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VisualProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VisualProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VisualProperties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "body": lambda n : setattr(self, 'body', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("body", self.body)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of a visual user notification. This field is required for visual notification payloads.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of a visual user notification. This field is required for visual notification payloads.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

