from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import company_detail, item_facet, position_detail, related_person

from . import item_facet

class ProjectParticipation(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new ProjectParticipation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.projectParticipation"
        # Contains categories a user has associated with the project (for example, digital transformation, oil rig).
        self._categories: Optional[List[str]] = None
        # Contains detailed information about the client the project was for.
        self._client: Optional[company_detail.CompanyDetail] = None
        # Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
        self._collaboration_tags: Optional[List[str]] = None
        # Lists people that also worked on the project.
        self._colleagues: Optional[List[related_person.RelatedPerson]] = None
        # Contains detail about the user's role on the project.
        self._detail: Optional[position_detail.PositionDetail] = None
        # Contains a friendly name for the project.
        self._display_name: Optional[str] = None
        # The Person or people who sponsored the project.
        self._sponsors: Optional[List[related_person.RelatedPerson]] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
    
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. Contains categories a user has associated with the project (for example, digital transformation, oil rig).
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. Contains categories a user has associated with the project (for example, digital transformation, oil rig).
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def client(self,) -> Optional[company_detail.CompanyDetail]:
        """
        Gets the client property value. Contains detailed information about the client the project was for.
        Returns: Optional[company_detail.CompanyDetail]
        """
        return self._client
    
    @client.setter
    def client(self,value: Optional[company_detail.CompanyDetail] = None) -> None:
        """
        Sets the client property value. Contains detailed information about the client the project was for.
        Args:
            value: Value to set for the client property.
        """
        self._client = value
    
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
    
    @property
    def colleagues(self,) -> Optional[List[related_person.RelatedPerson]]:
        """
        Gets the colleagues property value. Lists people that also worked on the project.
        Returns: Optional[List[related_person.RelatedPerson]]
        """
        return self._colleagues
    
    @colleagues.setter
    def colleagues(self,value: Optional[List[related_person.RelatedPerson]] = None) -> None:
        """
        Sets the colleagues property value. Lists people that also worked on the project.
        Args:
            value: Value to set for the colleagues property.
        """
        self._colleagues = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProjectParticipation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProjectParticipation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProjectParticipation()
    
    @property
    def detail(self,) -> Optional[position_detail.PositionDetail]:
        """
        Gets the detail property value. Contains detail about the user's role on the project.
        Returns: Optional[position_detail.PositionDetail]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[position_detail.PositionDetail] = None) -> None:
        """
        Sets the detail property value. Contains detail about the user's role on the project.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Contains a friendly name for the project.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Contains a friendly name for the project.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import company_detail, item_facet, position_detail, related_person

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "client": lambda n : setattr(self, 'client', n.get_object_value(company_detail.CompanyDetail)),
            "collaborationTags": lambda n : setattr(self, 'collaboration_tags', n.get_collection_of_primitive_values(str)),
            "colleagues": lambda n : setattr(self, 'colleagues', n.get_collection_of_object_values(related_person.RelatedPerson)),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(position_detail.PositionDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "sponsors": lambda n : setattr(self, 'sponsors', n.get_collection_of_object_values(related_person.RelatedPerson)),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
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
        writer.write_object_value("client", self.client)
        writer.write_collection_of_primitive_values("collaborationTags", self.collaboration_tags)
        writer.write_collection_of_object_values("colleagues", self.colleagues)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
    
    @property
    def sponsors(self,) -> Optional[List[related_person.RelatedPerson]]:
        """
        Gets the sponsors property value. The Person or people who sponsored the project.
        Returns: Optional[List[related_person.RelatedPerson]]
        """
        return self._sponsors
    
    @sponsors.setter
    def sponsors(self,value: Optional[List[related_person.RelatedPerson]] = None) -> None:
        """
        Sets the sponsors property value. The Person or people who sponsored the project.
        Args:
            value: Value to set for the sponsors property.
        """
        self._sponsors = value
    
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
    

