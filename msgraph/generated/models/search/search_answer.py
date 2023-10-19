from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .acronym import Acronym
    from .bookmark import Bookmark
    from .identity_set import IdentitySet
    from .qna import Qna

from ..entity import Entity

@dataclass
class SearchAnswer(Entity):
    # Search answer description shown on search results page.
    description: Optional[str] = None
    # Search answer name displayed in search results.
    display_name: Optional[str] = None
    # Details of the user that created or last modified the search answer. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of when the search answer is created or edited. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Search answer URL link. When users click this search answer in search results, they'll go to this URL.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchAnswer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.acronym".casefold():
            from .acronym import Acronym

            return Acronym()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.bookmark".casefold():
            from .bookmark import Bookmark

            return Bookmark()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.qna".casefold():
            from .qna import Qna

            return Qna()
        return SearchAnswer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .acronym import Acronym
        from .bookmark import Bookmark
        from .identity_set import IdentitySet
        from .qna import Qna

        from ..entity import Entity
        from .acronym import Acronym
        from .bookmark import Bookmark
        from .identity_set import IdentitySet
        from .qna import Qna

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("webUrl", self.web_url)
    

