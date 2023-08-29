from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .extension import Extension
    from .followup_flag import FollowupFlag
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .phone import Phone
    from .physical_address import PhysicalAddress
    from .profile_photo import ProfilePhoto
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
    from .typed_email_address import TypedEmailAddress
    from .website import Website

from .outlook_item import OutlookItem

@dataclass
class Contact(OutlookItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.contact"
    # The name of the contact's assistant.
    assistant_name: Optional[str] = None
    # The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    birthday: Optional[datetime.datetime] = None
    # The names of the contact's children.
    children: Optional[List[str]] = None
    # The name of the contact's company.
    company_name: Optional[str] = None
    # The contact's department.
    department: Optional[str] = None
    # The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.
    display_name: Optional[str] = None
    # The contact's email addresses.
    email_addresses: Optional[List[TypedEmailAddress]] = None
    # The collection of open extensions defined for the contact. Nullable.
    extensions: Optional[List[Extension]] = None
    # The name the contact is filed under.
    file_as: Optional[str] = None
    # The flag value that indicates the status, start date, due date, or completion date for the contact.
    flag: Optional[FollowupFlag] = None
    # The contact's gender.
    gender: Optional[str] = None
    # The contact's generation.
    generation: Optional[str] = None
    # The contact's given name.
    given_name: Optional[str] = None
    # The imAddresses property
    im_addresses: Optional[List[str]] = None
    # The initials property
    initials: Optional[str] = None
    # The isFavorite property
    is_favorite: Optional[bool] = None
    # The jobTitle property
    job_title: Optional[str] = None
    # The manager property
    manager: Optional[str] = None
    # The middleName property
    middle_name: Optional[str] = None
    # The collection of multi-value extended properties defined for the contact. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The nickName property
    nick_name: Optional[str] = None
    # The officeLocation property
    office_location: Optional[str] = None
    # The parentFolderId property
    parent_folder_id: Optional[str] = None
    # The personalNotes property
    personal_notes: Optional[str] = None
    # The phones property
    phones: Optional[List[Phone]] = None
    # Optional contact picture. You can get or set a photo for a contact.
    photo: Optional[ProfilePhoto] = None
    # The postalAddresses property
    postal_addresses: Optional[List[PhysicalAddress]] = None
    # The profession property
    profession: Optional[str] = None
    # The collection of single-value extended properties defined for the contact. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    # The spouseName property
    spouse_name: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The websites property
    websites: Optional[List[Website]] = None
    # The weddingAnniversary property
    wedding_anniversary: Optional[datetime.date] = None
    # The yomiCompanyName property
    yomi_company_name: Optional[str] = None
    # The yomiGivenName property
    yomi_given_name: Optional[str] = None
    # The yomiSurname property
    yomi_surname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Contact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Contact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Contact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .extension import Extension
        from .followup_flag import FollowupFlag
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .phone import Phone
        from .physical_address import PhysicalAddress
        from .profile_photo import ProfilePhoto
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .typed_email_address import TypedEmailAddress
        from .website import Website

        from .extension import Extension
        from .followup_flag import FollowupFlag
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .phone import Phone
        from .physical_address import PhysicalAddress
        from .profile_photo import ProfilePhoto
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .typed_email_address import TypedEmailAddress
        from .website import Website

        fields: Dict[str, Callable[[Any], None]] = {
            "assistantName": lambda n : setattr(self, 'assistant_name', n.get_str_value()),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_primitive_values(str)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_object_values(TypedEmailAddress)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "fileAs": lambda n : setattr(self, 'file_as', n.get_str_value()),
            "flag": lambda n : setattr(self, 'flag', n.get_object_value(FollowupFlag)),
            "gender": lambda n : setattr(self, 'gender', n.get_str_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "imAddresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "isFavorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_str_value()),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "nickName": lambda n : setattr(self, 'nick_name', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "personalNotes": lambda n : setattr(self, 'personal_notes', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "postalAddresses": lambda n : setattr(self, 'postal_addresses', n.get_collection_of_object_values(PhysicalAddress)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "spouseName": lambda n : setattr(self, 'spouse_name', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(Website)),
            "weddingAnniversary": lambda n : setattr(self, 'wedding_anniversary', n.get_date_value()),
            "yomiCompanyName": lambda n : setattr(self, 'yomi_company_name', n.get_str_value()),
            "yomiGivenName": lambda n : setattr(self, 'yomi_given_name', n.get_str_value()),
            "yomiSurname": lambda n : setattr(self, 'yomi_surname', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("assistantName", self.assistant_name)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_collection_of_primitive_values("children", self.children)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("emailAddresses", self.email_addresses)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("fileAs", self.file_as)
        writer.write_object_value("flag", self.flag)
        writer.write_str_value("gender", self.gender)
        writer.write_str_value("generation", self.generation)
        writer.write_str_value("givenName", self.given_name)
        writer.write_collection_of_primitive_values("imAddresses", self.im_addresses)
        writer.write_str_value("initials", self.initials)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("manager", self.manager)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("nickName", self.nick_name)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_str_value("personalNotes", self.personal_notes)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("postalAddresses", self.postal_addresses)
        writer.write_str_value("profession", self.profession)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_str_value("spouseName", self.spouse_name)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_object_values("websites", self.websites)
        writer.write_date_value("weddingAnniversary", self.wedding_anniversary)
        writer.write_str_value("yomiCompanyName", self.yomi_company_name)
        writer.write_str_value("yomiGivenName", self.yomi_given_name)
        writer.write_str_value("yomiSurname", self.yomi_surname)
    

