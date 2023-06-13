from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import formatted_content, intelligence_profile_indicator, intelligence_profile_kind, intelligence_profile_sponsor_state
    from .. import entity

from .. import entity

@dataclass
class IntelligenceProfile(entity.Entity):
    # A list of commonly-known aliases for the threat intelligence included in the intelligenceProfile.
    aliases: Optional[List[str]] = None
    # The description property
    description: Optional[formatted_content.FormattedContent] = None
    # The date and time when this intelligenceProfile was first active.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_active_date_time: Optional[datetime] = None
    # Includes an assemblage of high-fidelity network indicators of compromise.
    indicators: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]] = None
    # The kind property
    kind: Optional[intelligence_profile_kind.IntelligenceProfileKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Known states (such as a country or government) who have sponsored threat actors associated with this intelligenceProfile. This is also known as the country/region of origin for the given actor or threat.
    sponsor_states: Optional[List[intelligence_profile_sponsor_state.IntelligenceProfileSponsorState]] = None
    # The summary property
    summary: Optional[formatted_content.FormattedContent] = None
    # Known targets related to this intelligenceProfile.
    targets: Optional[List[str]] = None
    # The title of this intelligenceProfile.
    title: Optional[str] = None
    # Formatted information featuring a description of the distinctive tactics, techniques, and procedures (TTP) of the group, followed by a list of all known custom, commodity, and publicly available implants used by the group.
    tradecraft: Optional[formatted_content.FormattedContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IntelligenceProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IntelligenceProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IntelligenceProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import formatted_content, intelligence_profile_indicator, intelligence_profile_kind, intelligence_profile_sponsor_state
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "aliases": lambda n : setattr(self, 'aliases', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_object_value(formatted_content.FormattedContent)),
            "firstActiveDateTime": lambda n : setattr(self, 'first_active_date_time', n.get_datetime_value()),
            "indicators": lambda n : setattr(self, 'indicators', n.get_collection_of_object_values(intelligence_profile_indicator.IntelligenceProfileIndicator)),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(intelligence_profile_kind.IntelligenceProfileKind)),
            "sponsorStates": lambda n : setattr(self, 'sponsor_states', n.get_collection_of_object_values(intelligence_profile_sponsor_state.IntelligenceProfileSponsorState)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(formatted_content.FormattedContent)),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "tradecraft": lambda n : setattr(self, 'tradecraft', n.get_object_value(formatted_content.FormattedContent)),
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
        writer.write_collection_of_primitive_values("aliases", self.aliases)
        writer.write_object_value("description", self.description)
        writer.write_datetime_value("firstActiveDateTime", self.first_active_date_time)
        writer.write_collection_of_object_values("indicators", self.indicators)
        writer.write_enum_value("kind", self.kind)
        writer.write_collection_of_object_values("sponsorStates", self.sponsor_states)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_primitive_values("targets", self.targets)
        writer.write_str_value("title", self.title)
        writer.write_object_value("tradecraft", self.tradecraft)
    

