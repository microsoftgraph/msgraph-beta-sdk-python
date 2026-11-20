from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .repository_access_credential import RepositoryAccessCredential

from .repository_access_credential import RepositoryAccessCredential

@dataclass
class RepositoryOAuthCredential(RepositoryAccessCredential, Parsable):
    """
    OAuth authorization-code credential.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.contentManagement.repositoryOAuthCredential"
    # OAuth client id.
    client_id: Optional[str] = None
    # OAuth authorization code.
    code: Optional[str] = None
    # PKCE code verifier.
    code_verifier: Optional[str] = None
    # OAuth redirect URI.
    redirect_uri: Optional[str] = None
    # OAuth state value.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RepositoryOAuthCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RepositoryOAuthCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RepositoryOAuthCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .repository_access_credential import RepositoryAccessCredential

        from .repository_access_credential import RepositoryAccessCredential

        fields: dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "codeVerifier": lambda n : setattr(self, 'code_verifier', n.get_str_value()),
            "redirectUri": lambda n : setattr(self, 'redirect_uri', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("code", self.code)
        writer.write_str_value("codeVerifier", self.code_verifier)
        writer.write_str_value("redirectUri", self.redirect_uri)
        writer.write_str_value("state", self.state)
    

