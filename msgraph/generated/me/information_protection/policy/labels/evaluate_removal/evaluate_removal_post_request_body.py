from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_info = lazy_import('msgraph.generated.models.content_info')
downgrade_justification = lazy_import('msgraph.generated.models.downgrade_justification')

class EvaluateRemovalPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the evaluateRemoval method.
    """
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
        Instantiates a new evaluateRemovalPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The contentInfo property
        self._content_info: Optional[content_info.ContentInfo] = None
        # The downgradeJustification property
        self._downgrade_justification: Optional[downgrade_justification.DowngradeJustification] = None
    
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
            value: Value to set for the contentInfo property.
        """
        self._content_info = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateRemovalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateRemovalPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateRemovalPostRequestBody()
    
    @property
    def downgrade_justification(self,) -> Optional[downgrade_justification.DowngradeJustification]:
        """
        Gets the downgradeJustification property value. The downgradeJustification property
        Returns: Optional[downgrade_justification.DowngradeJustification]
        """
        return self._downgrade_justification
    
    @downgrade_justification.setter
    def downgrade_justification(self,value: Optional[downgrade_justification.DowngradeJustification] = None) -> None:
        """
        Sets the downgradeJustification property value. The downgradeJustification property
        Args:
            value: Value to set for the downgradeJustification property.
        """
        self._downgrade_justification = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_info": lambda n : setattr(self, 'content_info', n.get_object_value(content_info.ContentInfo)),
            "downgrade_justification": lambda n : setattr(self, 'downgrade_justification', n.get_object_value(downgrade_justification.DowngradeJustification)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_object_value("downgradeJustification", self.downgrade_justification)
        writer.write_additional_data_value(self.additional_data)
    

