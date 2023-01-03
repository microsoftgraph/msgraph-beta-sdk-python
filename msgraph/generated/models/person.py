from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
location = lazy_import('msgraph.generated.models.location')
person_data_source = lazy_import('msgraph.generated.models.person_data_source')
phone = lazy_import('msgraph.generated.models.phone')
ranked_email_address = lazy_import('msgraph.generated.models.ranked_email_address')
website = lazy_import('msgraph.generated.models.website')

class Person(entity.Entity):
    """
    Provides operations to manage the collection of activityStatistics entities.
    """
    @property
    def birthday(self,) -> Optional[str]:
        """
        Gets the birthday property value. The person's birthday.
        Returns: Optional[str]
        """
        return self._birthday
    
    @birthday.setter
    def birthday(self,value: Optional[str] = None) -> None:
        """
        Sets the birthday property value. The person's birthday.
        Args:
            value: Value to set for the birthday property.
        """
        self._birthday = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The name of the person's company.
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The name of the person's company.
        Args:
            value: Value to set for the companyName property.
        """
        self._company_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new person and sets the default values.
        """
        super().__init__()
        # The person's birthday.
        self._birthday: Optional[str] = None
        # The name of the person's company.
        self._company_name: Optional[str] = None
        # The person's department.
        self._department: Optional[str] = None
        # The person's display name.
        self._display_name: Optional[str] = None
        # The person's email addresses.
        self._email_addresses: Optional[List[ranked_email_address.RankedEmailAddress]] = None
        # The person's given name.
        self._given_name: Optional[str] = None
        # true if the user has flagged this person as a favorite.
        self._is_favorite: Optional[bool] = None
        # The type of mailbox that is represented by the person's email address.
        self._mailbox_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The location of the person's office.
        self._office_location: Optional[str] = None
        # Free-form notes that the user has taken about this person.
        self._person_notes: Optional[str] = None
        # The type of person, for example distribution list.
        self._person_type: Optional[str] = None
        # The person's phone numbers.
        self._phones: Optional[List[phone.Phone]] = None
        # The person's addresses.
        self._postal_addresses: Optional[List[location.Location]] = None
        # The person's profession.
        self._profession: Optional[str] = None
        # The sources the user data comes from, for example Directory or Outlook Contacts.
        self._sources: Optional[List[person_data_source.PersonDataSource]] = None
        # The person's surname.
        self._surname: Optional[str] = None
        # The person's title.
        self._title: Optional[str] = None
        # The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
        self._user_principal_name: Optional[str] = None
        # The person's websites.
        self._websites: Optional[List[website.Website]] = None
        # The phonetic Japanese name of the person's company.
        self._yomi_company: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Person:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Person
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Person()
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. The person's department.
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. The person's department.
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The person's display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The person's display name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email_addresses(self,) -> Optional[List[ranked_email_address.RankedEmailAddress]]:
        """
        Gets the emailAddresses property value. The person's email addresses.
        Returns: Optional[List[ranked_email_address.RankedEmailAddress]]
        """
        return self._email_addresses
    
    @email_addresses.setter
    def email_addresses(self,value: Optional[List[ranked_email_address.RankedEmailAddress]] = None) -> None:
        """
        Sets the emailAddresses property value. The person's email addresses.
        Args:
            value: Value to set for the emailAddresses property.
        """
        self._email_addresses = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "birthday": lambda n : setattr(self, 'birthday', n.get_str_value()),
            "company_name": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email_addresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_object_values(ranked_email_address.RankedEmailAddress)),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "is_favorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "mailbox_type": lambda n : setattr(self, 'mailbox_type', n.get_str_value()),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "person_notes": lambda n : setattr(self, 'person_notes', n.get_str_value()),
            "person_type": lambda n : setattr(self, 'person_type', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(phone.Phone)),
            "postal_addresses": lambda n : setattr(self, 'postal_addresses', n.get_collection_of_object_values(location.Location)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_object_values(person_data_source.PersonDataSource)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(website.Website)),
            "yomi_company": lambda n : setattr(self, 'yomi_company', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The person's given name.
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The person's given name.
        Args:
            value: Value to set for the givenName property.
        """
        self._given_name = value
    
    @property
    def is_favorite(self,) -> Optional[bool]:
        """
        Gets the isFavorite property value. true if the user has flagged this person as a favorite.
        Returns: Optional[bool]
        """
        return self._is_favorite
    
    @is_favorite.setter
    def is_favorite(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFavorite property value. true if the user has flagged this person as a favorite.
        Args:
            value: Value to set for the isFavorite property.
        """
        self._is_favorite = value
    
    @property
    def mailbox_type(self,) -> Optional[str]:
        """
        Gets the mailboxType property value. The type of mailbox that is represented by the person's email address.
        Returns: Optional[str]
        """
        return self._mailbox_type
    
    @mailbox_type.setter
    def mailbox_type(self,value: Optional[str] = None) -> None:
        """
        Sets the mailboxType property value. The type of mailbox that is represented by the person's email address.
        Args:
            value: Value to set for the mailboxType property.
        """
        self._mailbox_type = value
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. The location of the person's office.
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. The location of the person's office.
        Args:
            value: Value to set for the officeLocation property.
        """
        self._office_location = value
    
    @property
    def person_notes(self,) -> Optional[str]:
        """
        Gets the personNotes property value. Free-form notes that the user has taken about this person.
        Returns: Optional[str]
        """
        return self._person_notes
    
    @person_notes.setter
    def person_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the personNotes property value. Free-form notes that the user has taken about this person.
        Args:
            value: Value to set for the personNotes property.
        """
        self._person_notes = value
    
    @property
    def person_type(self,) -> Optional[str]:
        """
        Gets the personType property value. The type of person, for example distribution list.
        Returns: Optional[str]
        """
        return self._person_type
    
    @person_type.setter
    def person_type(self,value: Optional[str] = None) -> None:
        """
        Sets the personType property value. The type of person, for example distribution list.
        Args:
            value: Value to set for the personType property.
        """
        self._person_type = value
    
    @property
    def phones(self,) -> Optional[List[phone.Phone]]:
        """
        Gets the phones property value. The person's phone numbers.
        Returns: Optional[List[phone.Phone]]
        """
        return self._phones
    
    @phones.setter
    def phones(self,value: Optional[List[phone.Phone]] = None) -> None:
        """
        Sets the phones property value. The person's phone numbers.
        Args:
            value: Value to set for the phones property.
        """
        self._phones = value
    
    @property
    def postal_addresses(self,) -> Optional[List[location.Location]]:
        """
        Gets the postalAddresses property value. The person's addresses.
        Returns: Optional[List[location.Location]]
        """
        return self._postal_addresses
    
    @postal_addresses.setter
    def postal_addresses(self,value: Optional[List[location.Location]] = None) -> None:
        """
        Sets the postalAddresses property value. The person's addresses.
        Args:
            value: Value to set for the postalAddresses property.
        """
        self._postal_addresses = value
    
    @property
    def profession(self,) -> Optional[str]:
        """
        Gets the profession property value. The person's profession.
        Returns: Optional[str]
        """
        return self._profession
    
    @profession.setter
    def profession(self,value: Optional[str] = None) -> None:
        """
        Sets the profession property value. The person's profession.
        Args:
            value: Value to set for the profession property.
        """
        self._profession = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("birthday", self.birthday)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("emailAddresses", self.email_addresses)
        writer.write_str_value("givenName", self.given_name)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_str_value("mailboxType", self.mailbox_type)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("personNotes", self.person_notes)
        writer.write_str_value("personType", self.person_type)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_collection_of_object_values("postalAddresses", self.postal_addresses)
        writer.write_str_value("profession", self.profession)
        writer.write_collection_of_object_values("sources", self.sources)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("title", self.title)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_collection_of_object_values("websites", self.websites)
        writer.write_str_value("yomiCompany", self.yomi_company)
    
    @property
    def sources(self,) -> Optional[List[person_data_source.PersonDataSource]]:
        """
        Gets the sources property value. The sources the user data comes from, for example Directory or Outlook Contacts.
        Returns: Optional[List[person_data_source.PersonDataSource]]
        """
        return self._sources
    
    @sources.setter
    def sources(self,value: Optional[List[person_data_source.PersonDataSource]] = None) -> None:
        """
        Sets the sources property value. The sources the user data comes from, for example Directory or Outlook Contacts.
        Args:
            value: Value to set for the sources property.
        """
        self._sources = value
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The person's surname.
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The person's surname.
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The person's title.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The person's title.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def websites(self,) -> Optional[List[website.Website]]:
        """
        Gets the websites property value. The person's websites.
        Returns: Optional[List[website.Website]]
        """
        return self._websites
    
    @websites.setter
    def websites(self,value: Optional[List[website.Website]] = None) -> None:
        """
        Sets the websites property value. The person's websites.
        Args:
            value: Value to set for the websites property.
        """
        self._websites = value
    
    @property
    def yomi_company(self,) -> Optional[str]:
        """
        Gets the yomiCompany property value. The phonetic Japanese name of the person's company.
        Returns: Optional[str]
        """
        return self._yomi_company
    
    @yomi_company.setter
    def yomi_company(self,value: Optional[str] = None) -> None:
        """
        Sets the yomiCompany property value. The phonetic Japanese name of the person's company.
        Args:
            value: Value to set for the yomiCompany property.
        """
        self._yomi_company = value
    

