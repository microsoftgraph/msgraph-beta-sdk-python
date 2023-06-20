from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import cloud_pc_review_status

@dataclass
class SetCloudPcReviewStatusPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The reviewStatus property
    review_status: Optional[cloud_pc_review_status.CloudPcReviewStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetCloudPcReviewStatusPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetCloudPcReviewStatusPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SetCloudPcReviewStatusPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import cloud_pc_review_status

        from .....models import cloud_pc_review_status

        fields: Dict[str, Callable[[Any], None]] = {
            "reviewStatus": lambda n : setattr(self, 'review_status', n.get_object_value(cloud_pc_review_status.CloudPcReviewStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("reviewStatus", self.review_status)
        writer.write_additional_data_value(self.additional_data)
    

