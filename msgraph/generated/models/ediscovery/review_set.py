from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import review_set_query
    from .. import entity, identity_set

from .. import entity

@dataclass
class ReviewSet(entity.Entity):
    # The user who created the review set. Read-only.
    created_by: Optional[identity_set.IdentitySet] = None
    # The datetime when the review set was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime] = None
    # The review set name. The name is unique with a maximum limit of 64 characters.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The queries property
    queries: Optional[List[review_set_query.ReviewSetQuery]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReviewSet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReviewSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import review_set_query
        from .. import entity, identity_set

        from . import review_set_query
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "queries": lambda n : setattr(self, 'queries', n.get_collection_of_object_values(review_set_query.ReviewSetQuery)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("queries", self.queries)
    

