from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

translation_behavior = lazy_import('msgraph.generated.models.translation_behavior')
translation_language_override = lazy_import('msgraph.generated.models.translation_language_override')

class TranslationPreferences(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new translationPreferences and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Translation override behavior for languages, if any.Returned by default.
        self._language_overrides: Optional[List[translation_language_override.TranslationLanguageOverride]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The user's preferred translation behavior.Returned by default. Not nullable.
        self._translation_behavior: Optional[translation_behavior.TranslationBehavior] = None
        # The list of languages the user does not need translated. This is computed from the authoringLanguages collection in regionalAndLanguageSettings, and the languageOverrides collection in translationPreferences. The list specifies neutral culture values that include the language code without any country or region association. For example, it would specify 'fr' for the neutral French culture, but not 'fr-FR' for the French culture in France. Returned by default. Read only.
        self._untranslated_languages: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TranslationPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TranslationPreferences
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TranslationPreferences()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "language_overrides": lambda n : setattr(self, 'language_overrides', n.get_collection_of_object_values(translation_language_override.TranslationLanguageOverride)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "translation_behavior": lambda n : setattr(self, 'translation_behavior', n.get_enum_value(translation_behavior.TranslationBehavior)),
            "untranslated_languages": lambda n : setattr(self, 'untranslated_languages', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def language_overrides(self,) -> Optional[List[translation_language_override.TranslationLanguageOverride]]:
        """
        Gets the languageOverrides property value. Translation override behavior for languages, if any.Returned by default.
        Returns: Optional[List[translation_language_override.TranslationLanguageOverride]]
        """
        return self._language_overrides
    
    @language_overrides.setter
    def language_overrides(self,value: Optional[List[translation_language_override.TranslationLanguageOverride]] = None) -> None:
        """
        Sets the languageOverrides property value. Translation override behavior for languages, if any.Returned by default.
        Args:
            value: Value to set for the languageOverrides property.
        """
        self._language_overrides = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("languageOverrides", self.language_overrides)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("translationBehavior", self.translation_behavior)
        writer.write_collection_of_primitive_values("untranslatedLanguages", self.untranslated_languages)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def translation_behavior(self,) -> Optional[translation_behavior.TranslationBehavior]:
        """
        Gets the translationBehavior property value. The user's preferred translation behavior.Returned by default. Not nullable.
        Returns: Optional[translation_behavior.TranslationBehavior]
        """
        return self._translation_behavior
    
    @translation_behavior.setter
    def translation_behavior(self,value: Optional[translation_behavior.TranslationBehavior] = None) -> None:
        """
        Sets the translationBehavior property value. The user's preferred translation behavior.Returned by default. Not nullable.
        Args:
            value: Value to set for the translationBehavior property.
        """
        self._translation_behavior = value
    
    @property
    def untranslated_languages(self,) -> Optional[List[str]]:
        """
        Gets the untranslatedLanguages property value. The list of languages the user does not need translated. This is computed from the authoringLanguages collection in regionalAndLanguageSettings, and the languageOverrides collection in translationPreferences. The list specifies neutral culture values that include the language code without any country or region association. For example, it would specify 'fr' for the neutral French culture, but not 'fr-FR' for the French culture in France. Returned by default. Read only.
        Returns: Optional[List[str]]
        """
        return self._untranslated_languages
    
    @untranslated_languages.setter
    def untranslated_languages(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the untranslatedLanguages property value. The list of languages the user does not need translated. This is computed from the authoringLanguages collection in regionalAndLanguageSettings, and the languageOverrides collection in translationPreferences. The list specifies neutral culture values that include the language code without any country or region association. For example, it would specify 'fr' for the neutral French culture, but not 'fr-FR' for the French culture in France. Returned by default. Read only.
        Args:
            value: Value to set for the untranslatedLanguages property.
        """
        self._untranslated_languages = value
    

