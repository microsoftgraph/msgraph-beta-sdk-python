from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
acronym = lazy_import('msgraph.generated.models.search.acronym')
bookmark = lazy_import('msgraph.generated.models.search.bookmark')
qna = lazy_import('msgraph.generated.models.search.qna')

class SearchEntity(entity.Entity):
    @property
    def acronyms(self,) -> Optional[List[acronym.Acronym]]:
        """
        Gets the acronyms property value. Administrative answer in Microsoft Search results to define common acronyms in a organization.
        Returns: Optional[List[acronym.Acronym]]
        """
        return self._acronyms
    
    @acronyms.setter
    def acronyms(self,value: Optional[List[acronym.Acronym]] = None) -> None:
        """
        Sets the acronyms property value. Administrative answer in Microsoft Search results to define common acronyms in a organization.
        Args:
            value: Value to set for the acronyms property.
        """
        self._acronyms = value
    
    @property
    def bookmarks(self,) -> Optional[List[bookmark.Bookmark]]:
        """
        Gets the bookmarks property value. Administrative answer in Microsoft Search results for common search queries in an organization.
        Returns: Optional[List[bookmark.Bookmark]]
        """
        return self._bookmarks
    
    @bookmarks.setter
    def bookmarks(self,value: Optional[List[bookmark.Bookmark]] = None) -> None:
        """
        Sets the bookmarks property value. Administrative answer in Microsoft Search results for common search queries in an organization.
        Args:
            value: Value to set for the bookmarks property.
        """
        self._bookmarks = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SearchEntity and sets the default values.
        """
        super().__init__()
        # Administrative answer in Microsoft Search results to define common acronyms in a organization.
        self._acronyms: Optional[List[acronym.Acronym]] = None
        # Administrative answer in Microsoft Search results for common search queries in an organization.
        self._bookmarks: Optional[List[bookmark.Bookmark]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Administrative answer in Microsoft Search results which provide answers for specific search keywords in an organization.
        self._qnas: Optional[List[qna.Qna]] = None
    
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
        fields = {
            "acronyms": lambda n : setattr(self, 'acronyms', n.get_collection_of_object_values(acronym.Acronym)),
            "bookmarks": lambda n : setattr(self, 'bookmarks', n.get_collection_of_object_values(bookmark.Bookmark)),
            "qnas": lambda n : setattr(self, 'qnas', n.get_collection_of_object_values(qna.Qna)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def qnas(self,) -> Optional[List[qna.Qna]]:
        """
        Gets the qnas property value. Administrative answer in Microsoft Search results which provide answers for specific search keywords in an organization.
        Returns: Optional[List[qna.Qna]]
        """
        return self._qnas
    
    @qnas.setter
    def qnas(self,value: Optional[List[qna.Qna]] = None) -> None:
        """
        Sets the qnas property value. Administrative answer in Microsoft Search results which provide answers for specific search keywords in an organization.
        Args:
            value: Value to set for the qnas property.
        """
        self._qnas = value
    
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
    

