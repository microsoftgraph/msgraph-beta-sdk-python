from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')
language_proficiency_level = lazy_import('msgraph.generated.models.language_proficiency_level')

class LanguageProficiency(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new LanguageProficiency and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.languageProficiency"
        # Contains the long-form name for the language.
        self._display_name: Optional[str] = None
        # The proficiency property
        self._proficiency: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
        # Represents the users reading comprehension for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        self._reading: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
        # Represents the users spoken proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        self._spoken: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
        # Contains the four-character BCP47 name for the language (en-US, no-NB, en-AU).
        self._tag: Optional[str] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
        # Represents the users written proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        self._written: Optional[language_proficiency_level.LanguageProficiencyLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LanguageProficiency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LanguageProficiency
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LanguageProficiency()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Contains the long-form name for the language.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Contains the long-form name for the language.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "proficiency": lambda n : setattr(self, 'proficiency', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
            "reading": lambda n : setattr(self, 'reading', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
            "spoken": lambda n : setattr(self, 'spoken', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
            "tag": lambda n : setattr(self, 'tag', n.get_str_value()),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "written": lambda n : setattr(self, 'written', n.get_enum_value(language_proficiency_level.LanguageProficiencyLevel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def proficiency(self,) -> Optional[language_proficiency_level.LanguageProficiencyLevel]:
        """
        Gets the proficiency property value. The proficiency property
        Returns: Optional[language_proficiency_level.LanguageProficiencyLevel]
        """
        return self._proficiency
    
    @proficiency.setter
    def proficiency(self,value: Optional[language_proficiency_level.LanguageProficiencyLevel] = None) -> None:
        """
        Sets the proficiency property value. The proficiency property
        Args:
            value: Value to set for the proficiency property.
        """
        self._proficiency = value
    
    @property
    def reading(self,) -> Optional[language_proficiency_level.LanguageProficiencyLevel]:
        """
        Gets the reading property value. Represents the users reading comprehension for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        Returns: Optional[language_proficiency_level.LanguageProficiencyLevel]
        """
        return self._reading
    
    @reading.setter
    def reading(self,value: Optional[language_proficiency_level.LanguageProficiencyLevel] = None) -> None:
        """
        Sets the reading property value. Represents the users reading comprehension for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        Args:
            value: Value to set for the reading property.
        """
        self._reading = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("proficiency", self.proficiency)
        writer.write_enum_value("reading", self.reading)
        writer.write_enum_value("spoken", self.spoken)
        writer.write_str_value("tag", self.tag)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_enum_value("written", self.written)
    
    @property
    def spoken(self,) -> Optional[language_proficiency_level.LanguageProficiencyLevel]:
        """
        Gets the spoken property value. Represents the users spoken proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        Returns: Optional[language_proficiency_level.LanguageProficiencyLevel]
        """
        return self._spoken
    
    @spoken.setter
    def spoken(self,value: Optional[language_proficiency_level.LanguageProficiencyLevel] = None) -> None:
        """
        Sets the spoken property value. Represents the users spoken proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        Args:
            value: Value to set for the spoken property.
        """
        self._spoken = value
    
    @property
    def tag(self,) -> Optional[str]:
        """
        Gets the tag property value. Contains the four-character BCP47 name for the language (en-US, no-NB, en-AU).
        Returns: Optional[str]
        """
        return self._tag
    
    @tag.setter
    def tag(self,value: Optional[str] = None) -> None:
        """
        Sets the tag property value. Contains the four-character BCP47 name for the language (en-US, no-NB, en-AU).
        Args:
            value: Value to set for the tag property.
        """
        self._tag = value
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. The thumbnailUrl property
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. The thumbnailUrl property
        Args:
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    
    @property
    def written(self,) -> Optional[language_proficiency_level.LanguageProficiencyLevel]:
        """
        Gets the written property value. Represents the users written proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        Returns: Optional[language_proficiency_level.LanguageProficiencyLevel]
        """
        return self._written
    
    @written.setter
    def written(self,value: Optional[language_proficiency_level.LanguageProficiencyLevel] = None) -> None:
        """
        Sets the written property value. Represents the users written proficiency for the language represented by the object. Possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
        Args:
            value: Value to set for the written property.
        """
        self._written = value
    

