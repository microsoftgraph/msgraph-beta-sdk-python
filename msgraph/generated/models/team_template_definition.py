from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, team, team_template_audience

from . import entity

class TeamTemplateDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new teamTemplateDefinition and sets the default values.
        """
        super().__init__()
        # The audience property
        self._audience: Optional[team_template_audience.TeamTemplateAudience] = None
        # The categories property
        self._categories: Optional[List[str]] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The iconUrl property
        self._icon_url: Optional[str] = None
        # The languageTag property
        self._language_tag: Optional[str] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The parentTemplateId property
        self._parent_template_id: Optional[str] = None
        # The publisherName property
        self._publisher_name: Optional[str] = None
        # The shortDescription property
        self._short_description: Optional[str] = None
        # The teamDefinition property
        self._team_definition: Optional[team.Team] = None
    
    @property
    def audience(self,) -> Optional[team_template_audience.TeamTemplateAudience]:
        """
        Gets the audience property value. The audience property
        Returns: Optional[team_template_audience.TeamTemplateAudience]
        """
        return self._audience
    
    @audience.setter
    def audience(self,value: Optional[team_template_audience.TeamTemplateAudience] = None) -> None:
        """
        Sets the audience property value. The audience property
        Args:
            value: Value to set for the audience property.
        """
        self._audience = value
    
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. The categories property
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. The categories property
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamTemplateDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamTemplateDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamTemplateDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, team, team_template_audience

        fields: Dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(team_template_audience.TeamTemplateAudience)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "iconUrl": lambda n : setattr(self, 'icon_url', n.get_str_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "parentTemplateId": lambda n : setattr(self, 'parent_template_id', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "shortDescription": lambda n : setattr(self, 'short_description', n.get_str_value()),
            "teamDefinition": lambda n : setattr(self, 'team_definition', n.get_object_value(team.Team)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def icon_url(self,) -> Optional[str]:
        """
        Gets the iconUrl property value. The iconUrl property
        Returns: Optional[str]
        """
        return self._icon_url
    
    @icon_url.setter
    def icon_url(self,value: Optional[str] = None) -> None:
        """
        Sets the iconUrl property value. The iconUrl property
        Args:
            value: Value to set for the icon_url property.
        """
        self._icon_url = value
    
    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. The languageTag property
        Returns: Optional[str]
        """
        return self._language_tag
    
    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. The languageTag property
        Args:
            value: Value to set for the language_tag property.
        """
        self._language_tag = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The lastModifiedBy property
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def parent_template_id(self,) -> Optional[str]:
        """
        Gets the parentTemplateId property value. The parentTemplateId property
        Returns: Optional[str]
        """
        return self._parent_template_id
    
    @parent_template_id.setter
    def parent_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentTemplateId property value. The parentTemplateId property
        Args:
            value: Value to set for the parent_template_id property.
        """
        self._parent_template_id = value
    
    @property
    def publisher_name(self,) -> Optional[str]:
        """
        Gets the publisherName property value. The publisherName property
        Returns: Optional[str]
        """
        return self._publisher_name
    
    @publisher_name.setter
    def publisher_name(self,value: Optional[str] = None) -> None:
        """
        Sets the publisherName property value. The publisherName property
        Args:
            value: Value to set for the publisher_name property.
        """
        self._publisher_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("audience", self.audience)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("parentTemplateId", self.parent_template_id)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_str_value("shortDescription", self.short_description)
        writer.write_object_value("teamDefinition", self.team_definition)
    
    @property
    def short_description(self,) -> Optional[str]:
        """
        Gets the shortDescription property value. The shortDescription property
        Returns: Optional[str]
        """
        return self._short_description
    
    @short_description.setter
    def short_description(self,value: Optional[str] = None) -> None:
        """
        Sets the shortDescription property value. The shortDescription property
        Args:
            value: Value to set for the short_description property.
        """
        self._short_description = value
    
    @property
    def team_definition(self,) -> Optional[team.Team]:
        """
        Gets the teamDefinition property value. The teamDefinition property
        Returns: Optional[team.Team]
        """
        return self._team_definition
    
    @team_definition.setter
    def team_definition(self,value: Optional[team.Team] = None) -> None:
        """
        Sets the teamDefinition property value. The teamDefinition property
        Args:
            value: Value to set for the team_definition property.
        """
        self._team_definition = value
    

