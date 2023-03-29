from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, locale_info, regional_format_overrides, translation_preferences

from . import entity

class RegionalAndLanguageSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new regionalAndLanguageSettings and sets the default values.
        """
        super().__init__()
        # Prioritized list of languages the user reads and authors in.Returned by default. Not nullable.
        self._authoring_languages: Optional[List[locale_info.LocaleInfo]] = None
        # The  user's preferred user interface language (menus, buttons, ribbons, warning messages) for Microsoft web applications.Returned by default. Not nullable.
        self._default_display_language: Optional[locale_info.LocaleInfo] = None
        # The locale that drives the default date, time, and calendar formatting.Returned by default.
        self._default_regional_format: Optional[locale_info.LocaleInfo] = None
        # The language a user expected to use as input for text to speech scenarios.Returned by default.
        self._default_speech_input_language: Optional[locale_info.LocaleInfo] = None
        # The language a user expects to have documents, emails, and messages translated into.Returned by default.
        self._default_translation_language: Optional[locale_info.LocaleInfo] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Allows a user to override their defaultRegionalFormat with field specific formats.Returned by default.
        self._regional_format_overrides: Optional[regional_format_overrides.RegionalFormatOverrides] = None
        # The user's preferred settings when consuming translated documents, emails, messages, and websites.Returned by default. Not nullable.
        self._translation_preferences: Optional[translation_preferences.TranslationPreferences] = None
    
    @property
    def authoring_languages(self,) -> Optional[List[locale_info.LocaleInfo]]:
        """
        Gets the authoringLanguages property value. Prioritized list of languages the user reads and authors in.Returned by default. Not nullable.
        Returns: Optional[List[locale_info.LocaleInfo]]
        """
        return self._authoring_languages
    
    @authoring_languages.setter
    def authoring_languages(self,value: Optional[List[locale_info.LocaleInfo]] = None) -> None:
        """
        Sets the authoringLanguages property value. Prioritized list of languages the user reads and authors in.Returned by default. Not nullable.
        Args:
            value: Value to set for the authoring_languages property.
        """
        self._authoring_languages = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegionalAndLanguageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RegionalAndLanguageSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RegionalAndLanguageSettings()
    
    @property
    def default_display_language(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the defaultDisplayLanguage property value. The  user's preferred user interface language (menus, buttons, ribbons, warning messages) for Microsoft web applications.Returned by default. Not nullable.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._default_display_language
    
    @default_display_language.setter
    def default_display_language(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the defaultDisplayLanguage property value. The  user's preferred user interface language (menus, buttons, ribbons, warning messages) for Microsoft web applications.Returned by default. Not nullable.
        Args:
            value: Value to set for the default_display_language property.
        """
        self._default_display_language = value
    
    @property
    def default_regional_format(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the defaultRegionalFormat property value. The locale that drives the default date, time, and calendar formatting.Returned by default.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._default_regional_format
    
    @default_regional_format.setter
    def default_regional_format(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the defaultRegionalFormat property value. The locale that drives the default date, time, and calendar formatting.Returned by default.
        Args:
            value: Value to set for the default_regional_format property.
        """
        self._default_regional_format = value
    
    @property
    def default_speech_input_language(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the defaultSpeechInputLanguage property value. The language a user expected to use as input for text to speech scenarios.Returned by default.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._default_speech_input_language
    
    @default_speech_input_language.setter
    def default_speech_input_language(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the defaultSpeechInputLanguage property value. The language a user expected to use as input for text to speech scenarios.Returned by default.
        Args:
            value: Value to set for the default_speech_input_language property.
        """
        self._default_speech_input_language = value
    
    @property
    def default_translation_language(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the defaultTranslationLanguage property value. The language a user expects to have documents, emails, and messages translated into.Returned by default.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._default_translation_language
    
    @default_translation_language.setter
    def default_translation_language(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the defaultTranslationLanguage property value. The language a user expects to have documents, emails, and messages translated into.Returned by default.
        Args:
            value: Value to set for the default_translation_language property.
        """
        self._default_translation_language = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, locale_info, regional_format_overrides, translation_preferences

        fields: Dict[str, Callable[[Any], None]] = {
            "authoringLanguages": lambda n : setattr(self, 'authoring_languages', n.get_collection_of_object_values(locale_info.LocaleInfo)),
            "defaultDisplayLanguage": lambda n : setattr(self, 'default_display_language', n.get_object_value(locale_info.LocaleInfo)),
            "defaultRegionalFormat": lambda n : setattr(self, 'default_regional_format', n.get_object_value(locale_info.LocaleInfo)),
            "defaultSpeechInputLanguage": lambda n : setattr(self, 'default_speech_input_language', n.get_object_value(locale_info.LocaleInfo)),
            "defaultTranslationLanguage": lambda n : setattr(self, 'default_translation_language', n.get_object_value(locale_info.LocaleInfo)),
            "regionalFormatOverrides": lambda n : setattr(self, 'regional_format_overrides', n.get_object_value(regional_format_overrides.RegionalFormatOverrides)),
            "translationPreferences": lambda n : setattr(self, 'translation_preferences', n.get_object_value(translation_preferences.TranslationPreferences)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def regional_format_overrides(self,) -> Optional[regional_format_overrides.RegionalFormatOverrides]:
        """
        Gets the regionalFormatOverrides property value. Allows a user to override their defaultRegionalFormat with field specific formats.Returned by default.
        Returns: Optional[regional_format_overrides.RegionalFormatOverrides]
        """
        return self._regional_format_overrides
    
    @regional_format_overrides.setter
    def regional_format_overrides(self,value: Optional[regional_format_overrides.RegionalFormatOverrides] = None) -> None:
        """
        Sets the regionalFormatOverrides property value. Allows a user to override their defaultRegionalFormat with field specific formats.Returned by default.
        Args:
            value: Value to set for the regional_format_overrides property.
        """
        self._regional_format_overrides = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("authoringLanguages", self.authoring_languages)
        writer.write_object_value("defaultDisplayLanguage", self.default_display_language)
        writer.write_object_value("defaultRegionalFormat", self.default_regional_format)
        writer.write_object_value("defaultSpeechInputLanguage", self.default_speech_input_language)
        writer.write_object_value("defaultTranslationLanguage", self.default_translation_language)
        writer.write_object_value("regionalFormatOverrides", self.regional_format_overrides)
        writer.write_object_value("translationPreferences", self.translation_preferences)
    
    @property
    def translation_preferences(self,) -> Optional[translation_preferences.TranslationPreferences]:
        """
        Gets the translationPreferences property value. The user's preferred settings when consuming translated documents, emails, messages, and websites.Returned by default. Not nullable.
        Returns: Optional[translation_preferences.TranslationPreferences]
        """
        return self._translation_preferences
    
    @translation_preferences.setter
    def translation_preferences(self,value: Optional[translation_preferences.TranslationPreferences] = None) -> None:
        """
        Sets the translationPreferences property value. The user's preferred settings when consuming translated documents, emails, messages, and websites.Returned by default. Not nullable.
        Args:
            value: Value to set for the translation_preferences property.
        """
        self._translation_preferences = value
    

