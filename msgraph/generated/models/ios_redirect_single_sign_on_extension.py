from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_single_sign_on_extension, key_typed_value_pair

from . import ios_single_sign_on_extension

@dataclass
class IosRedirectSingleSignOnExtension(ios_single_sign_on_extension.IosSingleSignOnExtension):
    odata_type = "#microsoft.graph.iosRedirectSingleSignOnExtension"
    # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
    configurations: Optional[List[key_typed_value_pair.KeyTypedValuePair]] = None
    # Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
    extension_identifier: Optional[str] = None
    # Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
    team_identifier: Optional[str] = None
    # One or more URL prefixes of identity providers on whose behalf the app extension performs single sign-on. URLs must begin with http:// or https://. All URL prefixes must be unique for all profiles.
    url_prefixes: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosRedirectSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosRedirectSingleSignOnExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosRedirectSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_single_sign_on_extension, key_typed_value_pair

        from . import ios_single_sign_on_extension, key_typed_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "configurations": lambda n : setattr(self, 'configurations', n.get_collection_of_object_values(key_typed_value_pair.KeyTypedValuePair)),
            "extensionIdentifier": lambda n : setattr(self, 'extension_identifier', n.get_str_value()),
            "teamIdentifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
            "urlPrefixes": lambda n : setattr(self, 'url_prefixes', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("configurations", self.configurations)
        writer.write_str_value("extensionIdentifier", self.extension_identifier)
        writer.write_str_value("teamIdentifier", self.team_identifier)
        writer.write_collection_of_primitive_values("urlPrefixes", self.url_prefixes)
    

