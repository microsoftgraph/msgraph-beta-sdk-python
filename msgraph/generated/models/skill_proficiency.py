from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet, skill_proficiency_level

from . import item_facet

@dataclass
class SkillProficiency(item_facet.ItemFacet):
    odata_type = "#microsoft.graph.skillProficiency"
    # Contains categories a user has associated with the skill (for example, personal, professional, hobby).
    categories: Optional[List[str]] = None
    # Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
    collaboration_tags: Optional[List[str]] = None
    # Contains a friendly name for the skill.
    display_name: Optional[str] = None
    # Detail of the users proficiency with this skill. Possible values are: elementary, limitedWorking, generalProfessional, advancedProfessional, expert, unknownFutureValue.
    proficiency: Optional[skill_proficiency_level.SkillProficiencyLevel] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # Contains a link to an information source about the skill.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SkillProficiency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SkillProficiency
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SkillProficiency()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet, skill_proficiency_level

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "collaborationTags": lambda n : setattr(self, 'collaboration_tags', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "proficiency": lambda n : setattr(self, 'proficiency', n.get_enum_value(skill_proficiency_level.SkillProficiencyLevel)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("proficiency", self.proficiency)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    

