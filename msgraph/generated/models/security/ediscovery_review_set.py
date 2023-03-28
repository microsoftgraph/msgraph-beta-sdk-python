from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_set, ediscovery_file, ediscovery_review_set_query

from . import data_set

class EdiscoveryReviewSet(data_set.DataSet):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryReviewSet and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryReviewSet"
        # Represents files within the review set.
        self._files: Optional[List[ediscovery_file.EdiscoveryFile]] = None
        # Represents queries within the review set.
        self._queries: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryReviewSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryReviewSet()
    
    @property
    def files(self,) -> Optional[List[ediscovery_file.EdiscoveryFile]]:
        """
        Gets the files property value. Represents files within the review set.
        Returns: Optional[List[ediscovery_file.EdiscoveryFile]]
        """
        return self._files
    
    @files.setter
    def files(self,value: Optional[List[ediscovery_file.EdiscoveryFile]] = None) -> None:
        """
        Sets the files property value. Represents files within the review set.
        Args:
            value: Value to set for the files property.
        """
        self._files = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_set, ediscovery_file, ediscovery_review_set_query

        fields: Dict[str, Callable[[Any], None]] = {
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(ediscovery_file.EdiscoveryFile)),
            "queries": lambda n : setattr(self, 'queries', n.get_collection_of_object_values(ediscovery_review_set_query.EdiscoveryReviewSetQuery)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def queries(self,) -> Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]]:
        """
        Gets the queries property value. Represents queries within the review set.
        Returns: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]]
        """
        return self._queries
    
    @queries.setter
    def queries(self,value: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]] = None) -> None:
        """
        Sets the queries property value. Represents queries within the review set.
        Args:
            value: Value to set for the queries property.
        """
        self._queries = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_collection_of_object_values("queries", self.queries)
    

