from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import company_detail, item_facet, position_detail, related_person

from . import item_facet

@dataclass
class ProjectParticipation(item_facet.ItemFacet):
    odata_type = "#microsoft.graph.projectParticipation"
    # Contains categories a user has associated with the project (for example, digital transformation, oil rig).
    categories: Optional[List[str]] = None
    # Contains detailed information about the client the project was for.
    client: Optional[company_detail.CompanyDetail] = None
    # Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
    collaboration_tags: Optional[List[str]] = None
    # Lists people that also worked on the project.
    colleagues: Optional[List[related_person.RelatedPerson]] = None
    # Contains detail about the user's role on the project.
    detail: Optional[position_detail.PositionDetail] = None
    # Contains a friendly name for the project.
    display_name: Optional[str] = None
    # The Person or people who sponsored the project.
    sponsors: Optional[List[related_person.RelatedPerson]] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProjectParticipation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProjectParticipation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProjectParticipation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import company_detail, item_facet, position_detail, related_person

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_object_value("client", self.client)
        writer.write_collection_of_primitive_values("collaborationTags", self.collaboration_tags)
        writer.write_collection_of_object_values("colleagues", self.colleagues)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
    

