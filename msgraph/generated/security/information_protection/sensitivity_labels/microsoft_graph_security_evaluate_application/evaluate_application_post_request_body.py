from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.security import content_info, labeling_options

class EvaluateApplicationPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new evaluateApplicationPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The contentInfo property
        self._content_info: Optional[content_info.ContentInfo] = None
        # The labelingOptions property
        self._labeling_options: Optional[labeling_options.LabelingOptions] = None
    
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
    def content_info(self,) -> Optional[content_info.ContentInfo]:
        """
        Gets the contentInfo property value. The contentInfo property
        Returns: Optional[content_info.ContentInfo]
        """
        return self._content_info
    
    @content_info.setter
    def content_info(self,value: Optional[content_info.ContentInfo] = None) -> None:
        """
        Sets the contentInfo property value. The contentInfo property
        Args:
            value: Value to set for the content_info property.
        """
        self._content_info = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateApplicationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateApplicationPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateApplicationPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.security import content_info, labeling_options

        fields: Dict[str, Callable[[Any], None]] = {
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(content_info.ContentInfo)),
            "labelingOptions": lambda n : setattr(self, 'labeling_options', n.get_object_value(labeling_options.LabelingOptions)),
        }
        return fields
    
    @property
    def labeling_options(self,) -> Optional[labeling_options.LabelingOptions]:
        """
        Gets the labelingOptions property value. The labelingOptions property
        Returns: Optional[labeling_options.LabelingOptions]
        """
        return self._labeling_options
    
    @labeling_options.setter
    def labeling_options(self,value: Optional[labeling_options.LabelingOptions] = None) -> None:
        """
        Sets the labelingOptions property value. The labelingOptions property
        Args:
            value: Value to set for the labeling_options property.
        """
        self._labeling_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_object_value("labelingOptions", self.labeling_options)
        writer.write_additional_data_value(self.additional_data)
    

