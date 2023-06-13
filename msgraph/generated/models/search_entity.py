from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity
    from .search import acronym, bookmark, qna

from . import entity

@dataclass
class SearchEntity(entity.Entity):
    # Administrative answer in Microsoft Search results to define common acronyms in a organization.
    acronyms: Optional[List[acronym.Acronym]] = None
    # Administrative answer in Microsoft Search results for common search queries in an organization.
    bookmarks: Optional[List[bookmark.Bookmark]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Administrative answer in Microsoft Search results which provide answers for specific search keywords in an organization.
    qnas: Optional[List[qna.Qna]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchEntity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity
        from .search import acronym, bookmark, qna

        fields: Dict[str, Callable[[Any], None]] = {
            "acronyms": lambda n : setattr(self, 'acronyms', n.get_collection_of_object_values(acronym.Acronym)),
            "bookmarks": lambda n : setattr(self, 'bookmarks', n.get_collection_of_object_values(bookmark.Bookmark)),
            "qnas": lambda n : setattr(self, 'qnas', n.get_collection_of_object_values(qna.Qna)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("acronyms", self.acronyms)
        writer.write_collection_of_object_values("bookmarks", self.bookmarks)
        writer.write_collection_of_object_values("qnas", self.qnas)
    

