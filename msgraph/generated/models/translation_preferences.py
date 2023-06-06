from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import translation_behavior, translation_language_override

@dataclass
class TranslationPreferences(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Translation override behavior for languages, if any.Returned by default.
    language_overrides: Optional[List[translation_language_override.TranslationLanguageOverride]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user's preferred translation behavior.Returned by default. Not nullable.
    translation_behavior: Optional[translation_behavior.TranslationBehavior] = None
    # The list of languages the user does not need translated. This is computed from the authoringLanguages collection in regionalAndLanguageSettings, and the languageOverrides collection in translationPreferences. The list specifies neutral culture values that include the language code without any country or region association. For example, it would specify 'fr' for the neutral French culture, but not 'fr-FR' for the French culture in France. Returned by default. Read only.
    untranslated_languages: Optional[List[str]] = None
    
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
        from . import translation_behavior, translation_language_override

        fields: Dict[str, Callable[[Any], None]] = {
            "languageOverrides": lambda n : setattr(self, 'language_overrides', n.get_collection_of_object_values(translation_language_override.TranslationLanguageOverride)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "translationBehavior": lambda n : setattr(self, 'translation_behavior', n.get_enum_value(translation_behavior.TranslationBehavior)),
            "untranslatedLanguages": lambda n : setattr(self, 'untranslated_languages', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
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
    

