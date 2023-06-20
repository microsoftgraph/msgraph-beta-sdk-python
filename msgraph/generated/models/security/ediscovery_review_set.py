from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_set, ediscovery_file, ediscovery_review_set_query

from . import data_set

@dataclass
class EdiscoveryReviewSet(data_set.DataSet):
    odata_type = "#microsoft.graph.security.ediscoveryReviewSet"
    # Represents files within the review set.
    files: Optional[List[ediscovery_file.EdiscoveryFile]] = None
    # Represents queries within the review set.
    queries: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryReviewSet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryReviewSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_set, ediscovery_file, ediscovery_review_set_query

        from . import data_set, ediscovery_file, ediscovery_review_set_query

        fields: Dict[str, Callable[[Any], None]] = {
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(ediscovery_file.EdiscoveryFile)),
            "queries": lambda n : setattr(self, 'queries', n.get_collection_of_object_values(ediscovery_review_set_query.EdiscoveryReviewSetQuery)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_collection_of_object_values("queries", self.queries)
    

