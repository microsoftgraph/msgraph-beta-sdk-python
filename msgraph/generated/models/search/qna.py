from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')
answer_keyword = lazy_import('msgraph.generated.models.search.answer_keyword')
answer_state = lazy_import('msgraph.generated.models.search.answer_state')
answer_variant = lazy_import('msgraph.generated.models.search.answer_variant')
search_answer = lazy_import('msgraph.generated.models.search.search_answer')

class Qna(search_answer.SearchAnswer):
    @property
    def availability_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the availabilityEndDateTime property value. Timestamp of when the qna will stop to appear as a search result. Set as null for always available.
        Returns: Optional[datetime]
        """
        return self._availability_end_date_time
    
    @availability_end_date_time.setter
    def availability_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the availabilityEndDateTime property value. Timestamp of when the qna will stop to appear as a search result. Set as null for always available.
        Args:
            value: Value to set for the availabilityEndDateTime property.
        """
        self._availability_end_date_time = value
    
    @property
    def availability_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the availabilityStartDateTime property value. Timestamp of when the qna will start to appear as a search result. Set as null for always available.
        Returns: Optional[datetime]
        """
        return self._availability_start_date_time
    
    @availability_start_date_time.setter
    def availability_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the availabilityStartDateTime property value. Timestamp of when the qna will start to appear as a search result. Set as null for always available.
        Args:
            value: Value to set for the availabilityStartDateTime property.
        """
        self._availability_start_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Qna and sets the default values.
        """
        super().__init__()
        # Timestamp of when the qna will stop to appear as a search result. Set as null for always available.
        self._availability_end_date_time: Optional[datetime] = None
        # Timestamp of when the qna will start to appear as a search result. Set as null for always available.
        self._availability_start_date_time: Optional[datetime] = None
        # List of security groups able to view this qna.
        self._group_ids: Optional[List[str]] = None
        # True if this qna was suggested to the admin by a user or was mined and suggested by Microsoft. Read-only.
        self._is_suggested: Optional[bool] = None
        # Keywords that trigger this qna to appear in search results.
        self._keywords: Optional[answer_keyword.AnswerKeyword] = None
        # A list of language names that are geographically specific and that this QnA can be viewed in. Each language tag value follows the pattern {language}-{region}. As an example, en-us is English as used in the United States. See supported language tags for the list of possible values.
        self._language_tags: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of devices and operating systems able to view this qna. Possible values are: unknown, android, androidForWork, ios, macOS, windowsPhone81, windowsPhone81AndLater, windows10AndLater, androidWorkProfile, androidASOP.
        self._platforms: Optional[List[device_platform_type.DevicePlatformType]] = None
        # The state property
        self._state: Optional[answer_state.AnswerState] = None
        # Variations of a qna for different countries or devices. Use when you need to show different content to users based on their device, country/region, or both. The date and group settings will apply to all variations.
        self._targeted_variations: Optional[List[answer_variant.AnswerVariant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Qna:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Qna
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Qna()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "availability_end_date_time": lambda n : setattr(self, 'availability_end_date_time', n.get_datetime_value()),
            "availability_start_date_time": lambda n : setattr(self, 'availability_start_date_time', n.get_datetime_value()),
            "group_ids": lambda n : setattr(self, 'group_ids', n.get_collection_of_primitive_values(str)),
            "is_suggested": lambda n : setattr(self, 'is_suggested', n.get_bool_value()),
            "keywords": lambda n : setattr(self, 'keywords', n.get_object_value(answer_keyword.AnswerKeyword)),
            "language_tags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "platforms": lambda n : setattr(self, 'platforms', n.get_collection_of_enum_values(device_platform_type.DevicePlatformType)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(answer_state.AnswerState)),
            "targeted_variations": lambda n : setattr(self, 'targeted_variations', n.get_collection_of_object_values(answer_variant.AnswerVariant)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_ids(self,) -> Optional[List[str]]:
        """
        Gets the groupIds property value. List of security groups able to view this qna.
        Returns: Optional[List[str]]
        """
        return self._group_ids
    
    @group_ids.setter
    def group_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the groupIds property value. List of security groups able to view this qna.
        Args:
            value: Value to set for the groupIds property.
        """
        self._group_ids = value
    
    @property
    def is_suggested(self,) -> Optional[bool]:
        """
        Gets the isSuggested property value. True if this qna was suggested to the admin by a user or was mined and suggested by Microsoft. Read-only.
        Returns: Optional[bool]
        """
        return self._is_suggested
    
    @is_suggested.setter
    def is_suggested(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSuggested property value. True if this qna was suggested to the admin by a user or was mined and suggested by Microsoft. Read-only.
        Args:
            value: Value to set for the isSuggested property.
        """
        self._is_suggested = value
    
    @property
    def keywords(self,) -> Optional[answer_keyword.AnswerKeyword]:
        """
        Gets the keywords property value. Keywords that trigger this qna to appear in search results.
        Returns: Optional[answer_keyword.AnswerKeyword]
        """
        return self._keywords
    
    @keywords.setter
    def keywords(self,value: Optional[answer_keyword.AnswerKeyword] = None) -> None:
        """
        Sets the keywords property value. Keywords that trigger this qna to appear in search results.
        Args:
            value: Value to set for the keywords property.
        """
        self._keywords = value
    
    @property
    def language_tags(self,) -> Optional[List[str]]:
        """
        Gets the languageTags property value. A list of language names that are geographically specific and that this QnA can be viewed in. Each language tag value follows the pattern {language}-{region}. As an example, en-us is English as used in the United States. See supported language tags for the list of possible values.
        Returns: Optional[List[str]]
        """
        return self._language_tags
    
    @language_tags.setter
    def language_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the languageTags property value. A list of language names that are geographically specific and that this QnA can be viewed in. Each language tag value follows the pattern {language}-{region}. As an example, en-us is English as used in the United States. See supported language tags for the list of possible values.
        Args:
            value: Value to set for the languageTags property.
        """
        self._language_tags = value
    
    @property
    def platforms(self,) -> Optional[List[device_platform_type.DevicePlatformType]]:
        """
        Gets the platforms property value. List of devices and operating systems able to view this qna. Possible values are: unknown, android, androidForWork, ios, macOS, windowsPhone81, windowsPhone81AndLater, windows10AndLater, androidWorkProfile, androidASOP.
        Returns: Optional[List[device_platform_type.DevicePlatformType]]
        """
        return self._platforms
    
    @platforms.setter
    def platforms(self,value: Optional[List[device_platform_type.DevicePlatformType]] = None) -> None:
        """
        Sets the platforms property value. List of devices and operating systems able to view this qna. Possible values are: unknown, android, androidForWork, ios, macOS, windowsPhone81, windowsPhone81AndLater, windows10AndLater, androidWorkProfile, androidASOP.
        Args:
            value: Value to set for the platforms property.
        """
        self._platforms = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("availabilityEndDateTime", self.availability_end_date_time)
        writer.write_datetime_value("availabilityStartDateTime", self.availability_start_date_time)
        writer.write_collection_of_primitive_values("groupIds", self.group_ids)
        writer.write_bool_value("isSuggested", self.is_suggested)
        writer.write_object_value("keywords", self.keywords)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_enum_value("platforms", self.platforms)
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_object_values("targetedVariations", self.targeted_variations)
    
    @property
    def state(self,) -> Optional[answer_state.AnswerState]:
        """
        Gets the state property value. The state property
        Returns: Optional[answer_state.AnswerState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[answer_state.AnswerState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def targeted_variations(self,) -> Optional[List[answer_variant.AnswerVariant]]:
        """
        Gets the targetedVariations property value. Variations of a qna for different countries or devices. Use when you need to show different content to users based on their device, country/region, or both. The date and group settings will apply to all variations.
        Returns: Optional[List[answer_variant.AnswerVariant]]
        """
        return self._targeted_variations
    
    @targeted_variations.setter
    def targeted_variations(self,value: Optional[List[answer_variant.AnswerVariant]] = None) -> None:
        """
        Sets the targetedVariations property value. Variations of a qna for different countries or devices. Use when you need to show different content to users based on their device, country/region, or both. The date and group settings will apply to all variations.
        Args:
            value: Value to set for the targetedVariations property.
        """
        self._targeted_variations = value
    

