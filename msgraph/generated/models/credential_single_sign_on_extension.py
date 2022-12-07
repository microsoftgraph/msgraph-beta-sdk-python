from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_typed_value_pair = lazy_import('msgraph.generated.models.key_typed_value_pair')
single_sign_on_extension = lazy_import('msgraph.generated.models.single_sign_on_extension')

class CredentialSingleSignOnExtension(single_sign_on_extension.SingleSignOnExtension):
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
        Instantiates a new CredentialSingleSignOnExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.credentialSingleSignOnExtension"
        # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        self._configurations: Optional[List[key_typed_value_pair.KeyTypedValuePair]] = None
        # Gets or sets a list of hosts or domain names for which the app extension performs SSO.
        self._domains: Optional[List[str]] = None
        # Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
        self._extension_identifier: Optional[str] = None
        # Gets or sets the case-sensitive realm name for this profile.
        self._realm: Optional[str] = None
        # Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
        self._team_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CredentialSingleSignOnExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CredentialSingleSignOnExtension()
    
    @property
    def domains(self,) -> Optional[List[str]]:
        """
        Gets the domains property value. Gets or sets a list of hosts or domain names for which the app extension performs SSO.
        Returns: Optional[List[str]]
        """
        return self._domains
    
    @domains.setter
    def domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the domains property value. Gets or sets a list of hosts or domain names for which the app extension performs SSO.
        Args:
            value: Value to set for the domains property.
        """
        self._domains = value
    
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
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "extension_identifier": lambda n : setattr(self, 'extension_identifier', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "team_identifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def realm(self,) -> Optional[str]:
        """
        Gets the realm property value. Gets or sets the case-sensitive realm name for this profile.
        Returns: Optional[str]
        """
        return self._realm
    
    @realm.setter
    def realm(self,value: Optional[str] = None) -> None:
        """
        Sets the realm property value. Gets or sets the case-sensitive realm name for this profile.
        Args:
            value: Value to set for the realm property.
        """
        self._realm = value
    
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
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_str_value("extensionIdentifier", self.extension_identifier)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("teamIdentifier", self.team_identifier)
    
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
    

