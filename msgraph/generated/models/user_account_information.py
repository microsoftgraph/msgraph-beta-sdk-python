from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')
locale_info = lazy_import('msgraph.generated.models.locale_info')

class UserAccountInformation(item_facet.ItemFacet):
    @property
    def age_group(self,) -> Optional[str]:
        """
        Gets the ageGroup property value. Shows the age group of user. Allowed values null, minor, notAdult and adult are generated by the directory and cannot be changed.
        Returns: Optional[str]
        """
        return self._age_group
    
    @age_group.setter
    def age_group(self,value: Optional[str] = None) -> None:
        """
        Sets the ageGroup property value. Shows the age group of user. Allowed values null, minor, notAdult and adult are generated by the directory and cannot be changed.
        Args:
            value: Value to set for the ageGroup property.
        """
        self._age_group = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new UserAccountInformation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.userAccountInformation"
        # Shows the age group of user. Allowed values null, minor, notAdult and adult are generated by the directory and cannot be changed.
        self._age_group: Optional[str] = None
        # Contains the two-character country code associated with the users account.
        self._country_code: Optional[str] = None
        # The preferredLanguageTag property
        self._preferred_language_tag: Optional[locale_info.LocaleInfo] = None
        # The user principal name (UPN) of the user associated with the account.
        self._user_principal_name: Optional[str] = None
    
    @property
    def country_code(self,) -> Optional[str]:
        """
        Gets the countryCode property value. Contains the two-character country code associated with the users account.
        Returns: Optional[str]
        """
        return self._country_code
    
    @country_code.setter
    def country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryCode property value. Contains the two-character country code associated with the users account.
        Args:
            value: Value to set for the countryCode property.
        """
        self._country_code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAccountInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAccountInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserAccountInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "age_group": lambda n : setattr(self, 'age_group', n.get_str_value()),
            "country_code": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "preferred_language_tag": lambda n : setattr(self, 'preferred_language_tag', n.get_object_value(locale_info.LocaleInfo)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def preferred_language_tag(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the preferredLanguageTag property value. The preferredLanguageTag property
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._preferred_language_tag
    
    @preferred_language_tag.setter
    def preferred_language_tag(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the preferredLanguageTag property value. The preferredLanguageTag property
        Args:
            value: Value to set for the preferredLanguageTag property.
        """
        self._preferred_language_tag = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("ageGroup", self.age_group)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_object_value("preferredLanguageTag", self.preferred_language_tag)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user associated with the account.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user associated with the account.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

