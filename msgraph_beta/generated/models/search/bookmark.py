from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..device_platform_type import DevicePlatformType
    from .answer_keyword import AnswerKeyword
    from .answer_state import AnswerState
    from .answer_variant import AnswerVariant
    from .search_answer import SearchAnswer

from .search_answer import SearchAnswer

@dataclass
class Bookmark(SearchAnswer, Parsable):
    # Date and time when the bookmark stops appearing as a search result. Set as null for always available. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    availability_end_date_time: Optional[datetime.datetime] = None
    # Date and time when the bookmark starts to appear as a search result. Set as null for always available. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    availability_start_date_time: Optional[datetime.datetime] = None
    # Categories commonly used to describe this bookmark. For example, IT and HR.
    categories: Optional[list[str]] = None
    # The list of security groups that are able to view this bookmark.
    group_ids: Optional[list[str]] = None
    # True if this bookmark was suggested to the admin, by a user, or was mined and suggested by Microsoft. Read-only.
    is_suggested: Optional[bool] = None
    # Keywords that trigger this bookmark to appear in search results.
    keywords: Optional[AnswerKeyword] = None
    # A list of geographically specific language names in which this bookmark can be viewed. Each language tag value follows the pattern {language}-{region}. For example, en-us is English as used in the United States. For the list of possible values, see Supported language tags.
    language_tags: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of devices and operating systems that are able to view this bookmark. Possible values are: android, androidForWork, ios, macOS, windowsPhone81, windowsPhone81AndLater, windows10AndLater, androidWorkProfile, unknown, androidASOP, androidMobileApplicationManagement, iOSMobileApplicationManagement, unknownFutureValue.
    platforms: Optional[list[DevicePlatformType]] = None
    # List of Power Apps associated with this bookmark. If users add existing Power Apps to a bookmark, they can complete tasks directly on the search results page, such as entering vacation time or reporting expenses.
    power_app_ids: Optional[list[str]] = None
    # The state property
    state: Optional[AnswerState] = None
    # Variations of a bookmark for different countries/regions or devices. Use when you need to show different content to users based on their device, country/region, or both. The date and group settings apply to all variations.
    targeted_variations: Optional[list[AnswerVariant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Bookmark:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Bookmark
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Bookmark()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
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

        fields: dict[str, Callable[[Any], None]] = {
            "availabilityEndDateTime": lambda n : setattr(self, 'availability_end_date_time', n.get_datetime_value()),
            "availabilityStartDateTime": lambda n : setattr(self, 'availability_start_date_time', n.get_datetime_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "groupIds": lambda n : setattr(self, 'group_ids', n.get_collection_of_primitive_values(str)),
            "isSuggested": lambda n : setattr(self, 'is_suggested', n.get_bool_value()),
            "keywords": lambda n : setattr(self, 'keywords', n.get_object_value(AnswerKeyword)),
            "languageTags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "platforms": lambda n : setattr(self, 'platforms', n.get_collection_of_enum_values(DevicePlatformType)),
            "powerAppIds": lambda n : setattr(self, 'power_app_ids', n.get_collection_of_primitive_values(str)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("availabilityEndDateTime", self.availability_end_date_time)
        writer.write_datetime_value("availabilityStartDateTime", self.availability_start_date_time)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_primitive_values("groupIds", self.group_ids)
        writer.write_bool_value("isSuggested", self.is_suggested)
        writer.write_object_value("keywords", self.keywords)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_collection_of_enum_values("platforms", self.platforms)
        writer.write_collection_of_primitive_values("powerAppIds", self.power_app_ids)
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_object_values("targetedVariations", self.targeted_variations)
    

