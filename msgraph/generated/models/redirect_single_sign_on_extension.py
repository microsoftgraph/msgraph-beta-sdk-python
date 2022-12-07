from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_typed_value_pair = lazy_import('msgraph.generated.models.key_typed_value_pair')
single_sign_on_extension = lazy_import('msgraph.generated.models.single_sign_on_extension')

class RedirectSingleSignOnExtension(single_sign_on_extension.SingleSignOnExtension):
    @property
    def configurations(self,) -> Optional[List[key_typed_value_pair.KeyTypedValuePair]]:
        """
        Gets the configurations property value. Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[key_typed_value_pair.KeyTypedValuePair]]
        """
        return self._configurations
    
    @configurations.setter
    def configurations(self,value: Optional[List[key_typed_value_pair.KeyTypedValuePair]] = None) -> None:
        """
        Sets the configurations property value. Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the configurations property.
        """
        self._configurations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new RedirectSingleSignOnExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.redirectSingleSignOnExtension"
        # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        self._configurations: Optional[List[key_typed_value_pair.KeyTypedValuePair]] = None
        # Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
        self._extension_identifier: Optional[str] = None
        # Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
        self._team_identifier: Optional[str] = None
        # One or more URL prefixes of identity providers on whose behalf the app extension performs single sign-on. URLs must begin with http:// or https://. All URL prefixes must be unique for all profiles.
        self._url_prefixes: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedirectSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RedirectSingleSignOnExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RedirectSingleSignOnExtension()
    
    @property
    def extension_identifier(self,) -> Optional[str]:
        """
        Gets the extensionIdentifier property value. Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
        Returns: Optional[str]
        """
        return self._extension_identifier
    
    @extension_identifier.setter
    def extension_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionIdentifier property value. Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
        Args:
            value: Value to set for the extensionIdentifier property.
        """
        self._extension_identifier = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configurations": lambda n : setattr(self, 'configurations', n.get_collection_of_object_values(key_typed_value_pair.KeyTypedValuePair)),
            "extension_identifier": lambda n : setattr(self, 'extension_identifier', n.get_str_value()),
            "team_identifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
            "url_prefixes": lambda n : setattr(self, 'url_prefixes', n.get_collection_of_primitive_values(str)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("configurations", self.configurations)
        writer.write_str_value("extensionIdentifier", self.extension_identifier)
        writer.write_str_value("teamIdentifier", self.team_identifier)
        writer.write_collection_of_primitive_values("urlPrefixes", self.url_prefixes)
    
    @property
    def team_identifier(self,) -> Optional[str]:
        """
        Gets the teamIdentifier property value. Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
        Returns: Optional[str]
        """
        return self._team_identifier
    
    @team_identifier.setter
    def team_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the teamIdentifier property value. Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
        Args:
            value: Value to set for the teamIdentifier property.
        """
        self._team_identifier = value
    
    @property
    def url_prefixes(self,) -> Optional[List[str]]:
        """
        Gets the urlPrefixes property value. One or more URL prefixes of identity providers on whose behalf the app extension performs single sign-on. URLs must begin with http:// or https://. All URL prefixes must be unique for all profiles.
        Returns: Optional[List[str]]
        """
        return self._url_prefixes
    
    @url_prefixes.setter
    def url_prefixes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the urlPrefixes property value. One or more URL prefixes of identity providers on whose behalf the app extension performs single sign-on. URLs must begin with http:// or https://. All URL prefixes must be unique for all profiles.
        Args:
            value: Value to set for the urlPrefixes property.
        """
        self._url_prefixes = value
    

