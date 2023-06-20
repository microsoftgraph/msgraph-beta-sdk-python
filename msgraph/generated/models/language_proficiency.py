from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet, language_proficiency_level

from . import item_facet

@dataclass
class LanguageProficiency(item_facet.ItemFacet):
    odata_type = "#microsoft.graph.languageProficiency"
    # Contains the long-form name for the language.
    display_name: Optional[str] = None
    # The proficiency property
    proficiency: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
    # Represents the users reading comprehension for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
    reading: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
    # Represents the users spoken proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
    spoken: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
    # Contains the four-character BCP47 name for the language (en-US, no-NB, en-AU).
    tag: Optional[str] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # Represents the users written proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
    written: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LanguageProficiency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LanguageProficiency
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LanguageProficiency()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet, language_proficiency_level

        from . import item_facet, language_proficiency_level

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "proficiency": lambda n : setattr(self, 'proficiency', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
            "reading": lambda n : setattr(self, 'reading', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
            "spoken": lambda n : setattr(self, 'spoken', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
            "tag": lambda n : setattr(self, 'tag', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "written": lambda n : setattr(self, 'written', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("proficiency", self.proficiency)
        writer.write_enum_value("reading", self.reading)
        writer.write_enum_value("spoken", self.spoken)
        writer.write_str_value("tag", self.tag)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_enum_value("written", self.written)
    

