from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_review_status = lazy_import('msgraph.generated.models.cloud_pc_review_status')

class SetCloudPcReviewStatusPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the setCloudPcReviewStatus method.
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
        Instantiates a new setCloudPcReviewStatusPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The reviewStatus property
        self._review_status: Optional[cloud_pc_review_status.CloudPcReviewStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetCloudPcReviewStatusPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetCloudPcReviewStatusPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetCloudPcReviewStatusPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "review_status": lambda n : setattr(self, 'review_status', n.get_object_value(cloud_pc_review_status.CloudPcReviewStatus)),
        }
        return fields
    
    @property
    def review_status(self,) -> Optional[cloud_pc_review_status.CloudPcReviewStatus]:
        """
        Gets the reviewStatus property value. The reviewStatus property
        Returns: Optional[cloud_pc_review_status.CloudPcReviewStatus]
        """
        return self._review_status
    
    @review_status.setter
    def review_status(self,value: Optional[cloud_pc_review_status.CloudPcReviewStatus] = None) -> None:
        """
        Sets the reviewStatus property value. The reviewStatus property
        Args:
            value: Value to set for the reviewStatus property.
        """
        self._review_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("reviewStatus", self.review_status)
        writer.write_additional_data_value(self.additional_data)
    

