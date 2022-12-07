from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

translation_behavior = lazy_import('msgraph.generated.models.translation_behavior')

class TranslationLanguageOverride(AdditionalDataHolder, Parsable):
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
        Instantiates a new translationLanguageOverride and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The language to apply the override.Returned by default. Not nullable.
        self._language_tag: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The translation override behavior for the language, if any.Returned by default. Not nullable.
        self._translation_behavior: Optional[translation_behavior.TranslationBehavior] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TranslationLanguageOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TranslationLanguageOverride
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TranslationLanguageOverride()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "language_tag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "translation_behavior": lambda n : setattr(self, 'translation_behavior', n.get_enum_value(translation_behavior.TranslationBehavior)),
        }
        return fields
    
    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. The language to apply the override.Returned by default. Not nullable.
        Returns: Optional[str]
        """
        return self._language_tag
    
    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. The language to apply the override.Returned by default. Not nullable.
        Args:
            value: Value to set for the languageTag property.
        """
        self._language_tag = value
    
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
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("translationBehavior", self.translation_behavior)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def translation_behavior(self,) -> Optional[translation_behavior.TranslationBehavior]:
        """
        Gets the translationBehavior property value. The translation override behavior for the language, if any.Returned by default. Not nullable.
        Returns: Optional[translation_behavior.TranslationBehavior]
        """
        return self._translation_behavior
    
    @translation_behavior.setter
    def translation_behavior(self,value: Optional[translation_behavior.TranslationBehavior] = None) -> None:
        """
        Sets the translationBehavior property value. The translation override behavior for the language, if any.Returned by default. Not nullable.
        Args:
            value: Value to set for the translationBehavior property.
        """
        self._translation_behavior = value
    

