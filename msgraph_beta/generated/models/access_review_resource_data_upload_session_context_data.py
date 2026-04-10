from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_data import CustomExtensionData

from .custom_extension_data import CustomExtensionData

@dataclass
class AccessReviewResourceDataUploadSessionContextData(CustomExtensionData, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewResourceDataUploadSessionContextData"
    # The access review definition id.
    access_review_id: Optional[str] = None
    # The access review instance id.
    access_review_instance_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewResourceDataUploadSessionContextData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewResourceDataUploadSessionContextData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewResourceDataUploadSessionContextData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_data import CustomExtensionData

        from .custom_extension_data import CustomExtensionData

        fields: dict[str, Callable[[Any], None]] = {
            "accessReviewId": lambda n : setattr(self, 'access_review_id', n.get_str_value()),
            "accessReviewInstanceId": lambda n : setattr(self, 'access_review_instance_id', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("accessReviewId", self.access_review_id)
        writer.write_str_value("accessReviewInstanceId", self.access_review_instance_id)
    

