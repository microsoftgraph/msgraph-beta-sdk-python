from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import formatted_content, intelligence_profile_indicator, intelligence_profile_kind, intelligence_profile_sponsor_state
    from .. import entity

from .. import entity

class IntelligenceProfile(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new intelligenceProfile and sets the default values.
        """
        super().__init__()
        # A list of commonly-known aliases for the threat intelligence included in the intelligenceProfile.
        self._aliases: Optional[List[str]] = None
        # The description property
        self._description: Optional[formatted_content.FormattedContent] = None
        # The date and time when this intelligenceProfile was first active.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._first_active_date_time: Optional[datetime] = None
        # Includes an assemblage of high-fidelity network indicators of compromise.
        self._indicators: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]] = None
        # The kind property
        self._kind: Optional[intelligence_profile_kind.IntelligenceProfileKind] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Known states (such as a country or government) who have sponsored threat actors associated with this intelligenceProfile. This is also known as the country/region of origin for the given actor or threat.
        self._sponsor_states: Optional[List[intelligence_profile_sponsor_state.IntelligenceProfileSponsorState]] = None
        # The summary property
        self._summary: Optional[formatted_content.FormattedContent] = None
        # Known targets related to this intelligenceProfile.
        self._targets: Optional[List[str]] = None
        # The title of this intelligenceProfile.
        self._title: Optional[str] = None
        # Formatted information featuring a description of the distinctive tactics, techniques, and procedures (TTP) of the group, followed by a list of all known custom, commodity, and publicly available implants used by the group.
        self._tradecraft: Optional[formatted_content.FormattedContent] = None
    
    @property
    def aliases(self,) -> Optional[List[str]]:
        """
        Gets the aliases property value. A list of commonly-known aliases for the threat intelligence included in the intelligenceProfile.
        Returns: Optional[List[str]]
        """
        return self._aliases
    
    @aliases.setter
    def aliases(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the aliases property value. A list of commonly-known aliases for the threat intelligence included in the intelligenceProfile.
        Args:
            value: Value to set for the aliases property.
        """
        self._aliases = value
    
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
    
    @property
    def description(self,) -> Optional[formatted_content.FormattedContent]:
        """
        Gets the description property value. The description property
        Returns: Optional[formatted_content.FormattedContent]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[formatted_content.FormattedContent] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def first_active_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstActiveDateTime property value. The date and time when this intelligenceProfile was first active.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._first_active_date_time
    
    @first_active_date_time.setter
    def first_active_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstActiveDateTime property value. The date and time when this intelligenceProfile was first active.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the first_active_date_time property.
        """
        self._first_active_date_time = value
    
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
    
    @property
    def indicators(self,) -> Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]]:
        """
        Gets the indicators property value. Includes an assemblage of high-fidelity network indicators of compromise.
        Returns: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]]
        """
        return self._indicators
    
    @indicators.setter
    def indicators(self,value: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]] = None) -> None:
        """
        Sets the indicators property value. Includes an assemblage of high-fidelity network indicators of compromise.
        Args:
            value: Value to set for the indicators property.
        """
        self._indicators = value
    
    @property
    def kind(self,) -> Optional[intelligence_profile_kind.IntelligenceProfileKind]:
        """
        Gets the kind property value. The kind property
        Returns: Optional[intelligence_profile_kind.IntelligenceProfileKind]
        """
        return self._kind
    
    @kind.setter
    def kind(self,value: Optional[intelligence_profile_kind.IntelligenceProfileKind] = None) -> None:
        """
        Sets the kind property value. The kind property
        Args:
            value: Value to set for the kind property.
        """
        self._kind = value
    
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
    
    @property
    def sponsor_states(self,) -> Optional[List[intelligence_profile_sponsor_state.IntelligenceProfileSponsorState]]:
        """
        Gets the sponsorStates property value. Known states (such as a country or government) who have sponsored threat actors associated with this intelligenceProfile. This is also known as the country/region of origin for the given actor or threat.
        Returns: Optional[List[intelligence_profile_sponsor_state.IntelligenceProfileSponsorState]]
        """
        return self._sponsor_states
    
    @sponsor_states.setter
    def sponsor_states(self,value: Optional[List[intelligence_profile_sponsor_state.IntelligenceProfileSponsorState]] = None) -> None:
        """
        Sets the sponsorStates property value. Known states (such as a country or government) who have sponsored threat actors associated with this intelligenceProfile. This is also known as the country/region of origin for the given actor or threat.
        Args:
            value: Value to set for the sponsor_states property.
        """
        self._sponsor_states = value
    
    @property
    def summary(self,) -> Optional[formatted_content.FormattedContent]:
        """
        Gets the summary property value. The summary property
        Returns: Optional[formatted_content.FormattedContent]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[formatted_content.FormattedContent] = None) -> None:
        """
        Sets the summary property value. The summary property
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    
    @property
    def targets(self,) -> Optional[List[str]]:
        """
        Gets the targets property value. Known targets related to this intelligenceProfile.
        Returns: Optional[List[str]]
        """
        return self._targets
    
    @targets.setter
    def targets(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targets property value. Known targets related to this intelligenceProfile.
        Args:
            value: Value to set for the targets property.
        """
        self._targets = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of this intelligenceProfile.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of this intelligenceProfile.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def tradecraft(self,) -> Optional[formatted_content.FormattedContent]:
        """
        Gets the tradecraft property value. Formatted information featuring a description of the distinctive tactics, techniques, and procedures (TTP) of the group, followed by a list of all known custom, commodity, and publicly available implants used by the group.
        Returns: Optional[formatted_content.FormattedContent]
        """
        return self._tradecraft
    
    @tradecraft.setter
    def tradecraft(self,value: Optional[formatted_content.FormattedContent] = None) -> None:
        """
        Sets the tradecraft property value. Formatted information featuring a description of the distinctive tactics, techniques, and procedures (TTP) of the group, followed by a list of all known custom, commodity, and publicly available implants used by the group.
        Args:
            value: Value to set for the tradecraft property.
        """
        self._tradecraft = value
    

