from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, locale_info, regional_format_overrides, translation_preferences

from . import entity

@dataclass
class RegionalAndLanguageSettings(entity.Entity):
    # Prioritized list of languages the user reads and authors in.Returned by default. Not nullable.
    authoring_languages: Optional[List[locale_info.LocaleInfo]] = None
    # The  user's preferred user interface language (menus, buttons, ribbons, warning messages) for Microsoft web applications.Returned by default. Not nullable.
    default_display_language: Optional[locale_info.LocaleInfo] = None
    # The locale that drives the default date, time, and calendar formatting.Returned by default.
    default_regional_format: Optional[locale_info.LocaleInfo] = None
    # The language a user expected to use as input for text to speech scenarios.Returned by default.
    default_speech_input_language: Optional[locale_info.LocaleInfo] = None
    # The language a user expects to have documents, emails, and messages translated into.Returned by default.
    default_translation_language: Optional[locale_info.LocaleInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Allows a user to override their defaultRegionalFormat with field specific formats.Returned by default.
    regional_format_overrides: Optional[regional_format_overrides.RegionalFormatOverrides] = None
    # The user's preferred settings when consuming translated documents, emails, messages, and websites.Returned by default. Not nullable.
    translation_preferences: Optional[translation_preferences.TranslationPreferences] = None
    
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
    

