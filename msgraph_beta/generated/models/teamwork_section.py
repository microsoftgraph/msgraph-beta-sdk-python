from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .section_display_icon import SectionDisplayIcon
    from .section_sort_type import SectionSortType
    from .section_type import SectionType
    from .teamwork_section_item import TeamworkSectionItem

from .entity import Entity

@dataclass
class TeamworkSection(Entity, Parsable):
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The displayIcon property
    display_icon: Optional[SectionDisplayIcon] = None
    # The displayName property
    display_name: Optional[str] = None
    # The isExpanded property
    is_expanded: Optional[bool] = None
    # The isHierarchicalViewEnabled property
    is_hierarchical_view_enabled: Optional[bool] = None
    # The items property
    items: Optional[list[TeamworkSectionItem]] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sectionType property
    section_type: Optional[SectionType] = None
    # The sortType property
    sort_type: Optional[SectionSortType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkSection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .section_display_icon import SectionDisplayIcon
        from .section_sort_type import SectionSortType
        from .section_type import SectionType
        from .teamwork_section_item import TeamworkSectionItem

        from .entity import Entity
        from .section_display_icon import SectionDisplayIcon
        from .section_sort_type import SectionSortType
        from .section_type import SectionType
        from .teamwork_section_item import TeamworkSectionItem

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayIcon": lambda n : setattr(self, 'display_icon', n.get_object_value(SectionDisplayIcon)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isExpanded": lambda n : setattr(self, 'is_expanded', n.get_bool_value()),
            "isHierarchicalViewEnabled": lambda n : setattr(self, 'is_hierarchical_view_enabled', n.get_bool_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(TeamworkSectionItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "sectionType": lambda n : setattr(self, 'section_type', n.get_enum_value(SectionType)),
            "sortType": lambda n : setattr(self, 'sort_type', n.get_enum_value(SectionSortType)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("displayIcon", self.display_icon)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExpanded", self.is_expanded)
        writer.write_bool_value("isHierarchicalViewEnabled", self.is_hierarchical_view_enabled)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("sectionType", self.section_type)
        writer.write_enum_value("sortType", self.sort_type)
    

