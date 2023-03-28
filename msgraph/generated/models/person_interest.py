from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet

from . import item_facet

class PersonInterest(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new PersonInterest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personInterest"
        # Contains categories a user has associated with the interest (for example, personal, recipies).
        self._categories: Optional[List[str]] = None
        # Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
        self._collaboration_tags: Optional[List[str]] = None
        # Contains a description of the interest.
        self._description: Optional[str] = None
        # Contains a friendly name for the interest.
        self._display_name: Optional[str] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
        # Contains a link to a web page or resource about the interest.
        self._web_url: Optional[str] = None
    
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. Contains categories a user has associated with the interest (for example, personal, recipies).
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. Contains categories a user has associated with the interest (for example, personal, recipies).
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def collaboration_tags(self,) -> Optional[List[str]]:
        """
        Gets the collaborationTags property value. Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
        Returns: Optional[List[str]]
        """
        return self._collaboration_tags
    
    @collaboration_tags.setter
    def collaboration_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the collaborationTags property value. Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
        Args:
            value: Value to set for the collaboration_tags property.
        """
        self._collaboration_tags = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonInterest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonInterest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonInterest()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Contains a description of the interest.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Contains a description of the interest.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Contains a friendly name for the interest.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Contains a friendly name for the interest.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "collaborationTags": lambda n : setattr(self, 'collaboration_tags', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_primitive_values("collaborationTags", self.collaboration_tags)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. The thumbnailUrl property
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. The thumbnailUrl property
        Args:
            value: Value to set for the thumbnail_url property.
        """
        self._thumbnail_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Contains a link to a web page or resource about the interest.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Contains a link to a web page or resource about the interest.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

