from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')
skill_proficiency_level = lazy_import('msgraph.generated.models.skill_proficiency_level')

class SkillProficiency(item_facet.ItemFacet):
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. Contains categories a user has associated with the skill (for example, personal, professional, hobby).
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. Contains categories a user has associated with the skill (for example, personal, professional, hobby).
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
            value: Value to set for the collaborationTags property.
        """
        self._collaboration_tags = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SkillProficiency and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.skillProficiency"
        # Contains categories a user has associated with the skill (for example, personal, professional, hobby).
        self._categories: Optional[List[str]] = None
        # Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
        self._collaboration_tags: Optional[List[str]] = None
        # Contains a friendly name for the skill.
        self._display_name: Optional[str] = None
        # Detail of the users proficiency with this skill. Possible values are: elementary, limitedWorking, generalProfessional, advancedProfessional, expert, unknownFutureValue.
        self._proficiency: Optional[skill_proficiency_level.SkillProficiencyLevel] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
        # Contains a link to an information source about the skill.
        self._web_url: Optional[str] = None
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Contains a friendly name for the skill.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Contains a friendly name for the skill.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "collaboration_tags": lambda n : setattr(self, 'collaboration_tags', n.get_collection_of_primitive_values(str)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "proficiency": lambda n : setattr(self, 'proficiency', n.get_enum_value(skill_proficiency_level.SkillProficiencyLevel)),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def proficiency(self,) -> Optional[skill_proficiency_level.SkillProficiencyLevel]:
        """
        Gets the proficiency property value. Detail of the users proficiency with this skill. Possible values are: elementary, limitedWorking, generalProfessional, advancedProfessional, expert, unknownFutureValue.
        Returns: Optional[skill_proficiency_level.SkillProficiencyLevel]
        """
        return self._proficiency
    
    @proficiency.setter
    def proficiency(self,value: Optional[skill_proficiency_level.SkillProficiencyLevel] = None) -> None:
        """
        Sets the proficiency property value. Detail of the users proficiency with this skill. Possible values are: elementary, limitedWorking, generalProfessional, advancedProfessional, expert, unknownFutureValue.
        Args:
            value: Value to set for the proficiency property.
        """
        self._proficiency = value
    
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
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Contains a link to an information source about the skill.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Contains a link to an information source about the skill.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

