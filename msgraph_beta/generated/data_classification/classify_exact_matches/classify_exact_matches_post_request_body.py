from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.content_classification import ContentClassification

@dataclass
class ClassifyExactMatchesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The contentClassifications property
    content_classifications: Optional[List[ContentClassification]] = None
    # The sensitiveTypeIds property
    sensitive_type_ids: Optional[List[str]] = None
    # The text property
    text: Optional[str] = None
    # The timeoutInMs property
    timeout_in_ms: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClassifyExactMatchesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClassifyExactMatchesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClassifyExactMatchesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.content_classification import ContentClassification

        from ...models.content_classification import ContentClassification

        fields: Dict[str, Callable[[Any], None]] = {
            "contentClassifications": lambda n : setattr(self, 'content_classifications', n.get_collection_of_object_values(ContentClassification)),
            "sensitiveTypeIds": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "timeoutInMs": lambda n : setattr(self, 'timeout_in_ms', n.get_str_value()),
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
        writer.write_collection_of_object_values("contentClassifications", self.content_classifications)
        writer.write_collection_of_primitive_values("sensitiveTypeIds", self.sensitive_type_ids)
        writer.write_str_value("text", self.text)
        writer.write_str_value("timeoutInMs", self.timeout_in_ms)
        writer.write_additional_data_value(self.additional_data)
    

