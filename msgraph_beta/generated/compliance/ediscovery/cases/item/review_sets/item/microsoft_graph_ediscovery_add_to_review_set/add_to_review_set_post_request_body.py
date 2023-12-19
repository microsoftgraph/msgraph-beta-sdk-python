from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.ediscovery.source_collection import SourceCollection
    from .add_to_review_set_post_request_body_additional_data_options import AddToReviewSetPostRequestBody_additionalDataOptions

@dataclass
class AddToReviewSetPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The additionalDataOptions property
    additional_data_options: Optional[AddToReviewSetPostRequestBody_additionalDataOptions] = None
    # The sourceCollection property
    source_collection: Optional[SourceCollection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddToReviewSetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AddToReviewSetPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.ediscovery.source_collection import SourceCollection
        from .add_to_review_set_post_request_body_additional_data_options import AddToReviewSetPostRequestBody_additionalDataOptions

        from ........models.ediscovery.source_collection import SourceCollection
        from .add_to_review_set_post_request_body_additional_data_options import AddToReviewSetPostRequestBody_additionalDataOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalDataOptions": lambda n : setattr(self, 'additional_data_options', n.get_enum_value(AddToReviewSetPostRequestBody_additionalDataOptions)),
            "sourceCollection": lambda n : setattr(self, 'source_collection', n.get_object_value(SourceCollection)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("additionalDataOptions", self.additional_data_options)
        writer.write_object_value("sourceCollection", self.source_collection)
        writer.write_additional_data_value(self.additional_data)
    

