from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.classification_result import ClassificationResult
    from .........models.content_info import ContentInfo

@dataclass
class EvaluateClassificationResultsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The classificationResults property
    classification_results: Optional[List[ClassificationResult]] = None
    # The contentInfo property
    content_info: Optional[ContentInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluateClassificationResultsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateClassificationResultsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluateClassificationResultsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .........models.classification_result import ClassificationResult
        from .........models.content_info import ContentInfo

        from .........models.classification_result import ClassificationResult
        from .........models.content_info import ContentInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationResults": lambda n : setattr(self, 'classification_results', n.get_collection_of_object_values(ClassificationResult)),
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(ContentInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("classificationResults", self.classification_results)
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_additional_data_value(self.additional_data)
    

