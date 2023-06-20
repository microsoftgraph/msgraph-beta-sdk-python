from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import translation_behavior

@dataclass
class TranslationLanguageOverride(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The language to apply the override.Returned by default. Not nullable.
    language_tag: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The translation override behavior for the language, if any.Returned by default. Not nullable.
    translation_behavior: Optional[translation_behavior.TranslationBehavior] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TranslationLanguageOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TranslationLanguageOverride
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TranslationLanguageOverride()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import translation_behavior

        from . import translation_behavior

        fields: Dict[str, Callable[[Any], None]] = {
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "translationBehavior": lambda n : setattr(self, 'translation_behavior', n.get_enum_value(translation_behavior.TranslationBehavior)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("translationBehavior", self.translation_behavior)
        writer.write_additional_data_value(self.additional_data)
    

