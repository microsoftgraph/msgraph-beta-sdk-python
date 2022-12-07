from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')
person_name_pronounciation = lazy_import('msgraph.generated.models.person_name_pronounciation')

class PersonName(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new PersonName and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personName"
        # Provides an ordered rendering of firstName and lastName depending on the locale of the user or their device.
        self._display_name: Optional[str] = None
        # First name of the user.
        self._first: Optional[str] = None
        # Initials of the user.
        self._initials: Optional[str] = None
        # Contains the name for the language (en-US, no-NB, en-AU) following IETF BCP47 format.
        self._language_tag: Optional[str] = None
        # Last name of the user.
        self._last: Optional[str] = None
        # Maiden name of the user.
        self._maiden: Optional[str] = None
        # Middle name of the user.
        self._middle: Optional[str] = None
        # Nickname of the user.
        self._nickname: Optional[str] = None
        # Guidance on how to pronounce the users name.
        self._pronunciation: Optional[person_name_pronounciation.PersonNamePronounciation] = None
        # Designators used after the users name (eg: PhD.)
        self._suffix: Optional[str] = None
        # Honorifics used to prefix a users name (eg: Dr, Sir, Madam, Mrs.)
        self._title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonName:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonName
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonName()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Provides an ordered rendering of firstName and lastName depending on the locale of the user or their device.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Provides an ordered rendering of firstName and lastName depending on the locale of the user or their device.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def first(self,) -> Optional[str]:
        """
        Gets the first property value. First name of the user.
        Returns: Optional[str]
        """
        return self._first
    
    @first.setter
    def first(self,value: Optional[str] = None) -> None:
        """
        Sets the first property value. First name of the user.
        Args:
            value: Value to set for the first property.
        """
        self._first = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "first": lambda n : setattr(self, 'first', n.get_str_value()),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "language_tag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "last": lambda n : setattr(self, 'last', n.get_str_value()),
            "maiden": lambda n : setattr(self, 'maiden', n.get_str_value()),
            "middle": lambda n : setattr(self, 'middle', n.get_str_value()),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
            "pronunciation": lambda n : setattr(self, 'pronunciation', n.get_object_value(person_name_pronounciation.PersonNamePronounciation)),
            "suffix": lambda n : setattr(self, 'suffix', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initials(self,) -> Optional[str]:
        """
        Gets the initials property value. Initials of the user.
        Returns: Optional[str]
        """
        return self._initials
    
    @initials.setter
    def initials(self,value: Optional[str] = None) -> None:
        """
        Sets the initials property value. Initials of the user.
        Args:
            value: Value to set for the initials property.
        """
        self._initials = value
    
    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. Contains the name for the language (en-US, no-NB, en-AU) following IETF BCP47 format.
        Returns: Optional[str]
        """
        return self._language_tag
    
    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. Contains the name for the language (en-US, no-NB, en-AU) following IETF BCP47 format.
        Args:
            value: Value to set for the languageTag property.
        """
        self._language_tag = value
    
    @property
    def last(self,) -> Optional[str]:
        """
        Gets the last property value. Last name of the user.
        Returns: Optional[str]
        """
        return self._last
    
    @last.setter
    def last(self,value: Optional[str] = None) -> None:
        """
        Sets the last property value. Last name of the user.
        Args:
            value: Value to set for the last property.
        """
        self._last = value
    
    @property
    def maiden(self,) -> Optional[str]:
        """
        Gets the maiden property value. Maiden name of the user.
        Returns: Optional[str]
        """
        return self._maiden
    
    @maiden.setter
    def maiden(self,value: Optional[str] = None) -> None:
        """
        Sets the maiden property value. Maiden name of the user.
        Args:
            value: Value to set for the maiden property.
        """
        self._maiden = value
    
    @property
    def middle(self,) -> Optional[str]:
        """
        Gets the middle property value. Middle name of the user.
        Returns: Optional[str]
        """
        return self._middle
    
    @middle.setter
    def middle(self,value: Optional[str] = None) -> None:
        """
        Sets the middle property value. Middle name of the user.
        Args:
            value: Value to set for the middle property.
        """
        self._middle = value
    
    @property
    def nickname(self,) -> Optional[str]:
        """
        Gets the nickname property value. Nickname of the user.
        Returns: Optional[str]
        """
        return self._nickname
    
    @nickname.setter
    def nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the nickname property value. Nickname of the user.
        Args:
            value: Value to set for the nickname property.
        """
        self._nickname = value
    
    @property
    def pronunciation(self,) -> Optional[person_name_pronounciation.PersonNamePronounciation]:
        """
        Gets the pronunciation property value. Guidance on how to pronounce the users name.
        Returns: Optional[person_name_pronounciation.PersonNamePronounciation]
        """
        return self._pronunciation
    
    @pronunciation.setter
    def pronunciation(self,value: Optional[person_name_pronounciation.PersonNamePronounciation] = None) -> None:
        """
        Sets the pronunciation property value. Guidance on how to pronounce the users name.
        Args:
            value: Value to set for the pronunciation property.
        """
        self._pronunciation = value
    
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
        writer.write_str_value("first", self.first)
        writer.write_str_value("initials", self.initials)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("last", self.last)
        writer.write_str_value("maiden", self.maiden)
        writer.write_str_value("middle", self.middle)
        writer.write_str_value("nickname", self.nickname)
        writer.write_object_value("pronunciation", self.pronunciation)
        writer.write_str_value("suffix", self.suffix)
        writer.write_str_value("title", self.title)
    
    @property
    def suffix(self,) -> Optional[str]:
        """
        Gets the suffix property value. Designators used after the users name (eg: PhD.)
        Returns: Optional[str]
        """
        return self._suffix
    
    @suffix.setter
    def suffix(self,value: Optional[str] = None) -> None:
        """
        Sets the suffix property value. Designators used after the users name (eg: PhD.)
        Args:
            value: Value to set for the suffix property.
        """
        self._suffix = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Honorifics used to prefix a users name (eg: Dr, Sir, Madam, Mrs.)
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Honorifics used to prefix a users name (eg: Dr, Sir, Madam, Mrs.)
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

