from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

media_source_content_category = lazy_import('msgraph.generated.models.media_source_content_category')

class MediaSource(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new mediaSource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Enumeration value that indicates the media content category.
        self._content_category: Optional[media_source_content_category.MediaSourceContentCategory] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def content_category(self,) -> Optional[media_source_content_category.MediaSourceContentCategory]:
        """
        Gets the contentCategory property value. Enumeration value that indicates the media content category.
        Returns: Optional[media_source_content_category.MediaSourceContentCategory]
        """
        return self._content_category
    
    @content_category.setter
    def content_category(self,value: Optional[media_source_content_category.MediaSourceContentCategory] = None) -> None:
        """
        Sets the contentCategory property value. Enumeration value that indicates the media content category.
        Args:
            value: Value to set for the contentCategory property.
        """
        self._content_category = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MediaSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MediaSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_category": lambda n : setattr(self, 'content_category', n.get_enum_value(media_source_content_category.MediaSourceContentCategory)),
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
        writer.write_enum_value("contentCategory", self.content_category)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

