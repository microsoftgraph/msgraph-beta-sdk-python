from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

case_operation = lazy_import('msgraph.generated.models.ediscovery.case_operation')
review_set = lazy_import('msgraph.generated.models.ediscovery.review_set')
source_collection = lazy_import('msgraph.generated.models.ediscovery.source_collection')

class AddToReviewSetOperation(case_operation.CaseOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new AddToReviewSetOperation and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The review set to which items matching the source collection query are added to.
        self._review_set: Optional[review_set.ReviewSet] = None
        # The sourceCollection that items are being added from.
        self._source_collection: Optional[source_collection.SourceCollection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddToReviewSetOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddToReviewSetOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "review_set": lambda n : setattr(self, 'review_set', n.get_object_value(review_set.ReviewSet)),
            "source_collection": lambda n : setattr(self, 'source_collection', n.get_object_value(source_collection.SourceCollection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def review_set(self,) -> Optional[review_set.ReviewSet]:
        """
        Gets the reviewSet property value. The review set to which items matching the source collection query are added to.
        Returns: Optional[review_set.ReviewSet]
        """
        return self._review_set
    
    @review_set.setter
    def review_set(self,value: Optional[review_set.ReviewSet] = None) -> None:
        """
        Sets the reviewSet property value. The review set to which items matching the source collection query are added to.
        Args:
            value: Value to set for the reviewSet property.
        """
        self._review_set = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("reviewSet", self.review_set)
        writer.write_object_value("sourceCollection", self.source_collection)
    
    @property
    def source_collection(self,) -> Optional[source_collection.SourceCollection]:
        """
        Gets the sourceCollection property value. The sourceCollection that items are being added from.
        Returns: Optional[source_collection.SourceCollection]
        """
        return self._source_collection
    
    @source_collection.setter
    def source_collection(self,value: Optional[source_collection.SourceCollection] = None) -> None:
        """
        Sets the sourceCollection property value. The sourceCollection that items are being added from.
        Args:
            value: Value to set for the sourceCollection property.
        """
        self._source_collection = value
    

