from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..device_platform_type import DevicePlatformType
    from .answer_keyword import AnswerKeyword
    from .answer_state import AnswerState
    from .answer_variant import AnswerVariant
    from .search_answer import SearchAnswer

from .search_answer import SearchAnswer

@dataclass
class Qna(SearchAnswer):
    # Timestamp of when the qna stops to appear as a search result. Set as null for always available.
    availability_end_date_time: Optional[datetime.datetime] = None
    # Timestamp of when the qna starts to appear as a search result. Set as null for always available.
    availability_start_date_time: Optional[datetime.datetime] = None
    # List of security groups able to view this qna.
    group_ids: Optional[List[str]] = None
    # True if a user or Microsoft suggested this qna to the admin. Read-only.
    is_suggested: Optional[bool] = None
    # Keywords that trigger this qna to appear in search results.
    keywords: Optional[AnswerKeyword] = None
    # A list of language names that are geographically specific and that this QnA can be viewed in. Each language tag value follows the pattern {language}-{region}. As an example, en-us is English as used in the United States. For the list of possible values, see supported language tags.
    language_tags: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of devices and operating systems able to view this qna. Possible values are: unknown, android, androidForWork, ios, macOS, windowsPhone81, windowsPhone81AndLater, windows10AndLater, androidWorkProfile, androidASOP.
    platforms: Optional[List[DevicePlatformType]] = None
    # The state property
    state: Optional[AnswerState] = None
    # Variations of a qna for different countries or devices. Use when you need to show different content to users based on their device, country/region, or both. The date and group settings apply to all variations.
    targeted_variations: Optional[List[AnswerVariant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Qna:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Qna
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Qna()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..device_platform_type import DevicePlatformType
        from .answer_keyword import AnswerKeyword
        from .answer_state import AnswerState
        from .answer_variant import AnswerVariant
        from .search_answer import SearchAnswer

        from ..device_platform_type import DevicePlatformType
        from .answer_keyword import AnswerKeyword
        from .answer_state import AnswerState
        from .answer_variant import AnswerVariant
        from .search_answer import SearchAnswer

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityEndDateTime": lambda n : setattr(self, 'availability_end_date_time', n.get_datetime_value()),
            "availabilityStartDateTime": lambda n : setattr(self, 'availability_start_date_time', n.get_datetime_value()),
            "groupIds": lambda n : setattr(self, 'group_ids', n.get_collection_of_primitive_values(str)),
            "isSuggested": lambda n : setattr(self, 'is_suggested', n.get_bool_value()),
            "keywords": lambda n : setattr(self, 'keywords', n.get_object_value(AnswerKeyword)),
            "languageTags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "platforms": lambda n : setattr(self, 'platforms', n.get_collection_of_enum_values(DevicePlatformType)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AnswerState)),
            "targetedVariations": lambda n : setattr(self, 'targeted_variations', n.get_collection_of_object_values(AnswerVariant)),
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
        writer.write_datetime_value("availabilityEndDateTime", self.availability_end_date_time)
        writer.write_datetime_value("availabilityStartDateTime", self.availability_start_date_time)
        writer.write_collection_of_primitive_values("groupIds", self.group_ids)
        writer.write_bool_value("isSuggested", self.is_suggested)
        writer.write_object_value("keywords", self.keywords)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_collection_of_enum_values("platforms", self.platforms)
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_object_values("targetedVariations", self.targeted_variations)
    

