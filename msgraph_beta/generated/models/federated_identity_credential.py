from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .federated_identity_expression import FederatedIdentityExpression

from .entity import Entity

@dataclass
class FederatedIdentityCredential(Entity, Parsable):
    # The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Microsoft Entra ID. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Microsoft Entra ID in your external identity provider and has no fixed value across identity providers - you may need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.
    audiences: Optional[list[str]] = None
    # Nullable.  Defaults to null if not set. Enables the use of claims matching expressions against specified claims. If claimsMatchingExpression is defined, subject must be null. For the list of supported expression syntax and claims, visit the Flexible FIC reference.
    claims_matching_expression: Optional[FederatedIdentityExpression] = None
    # The un-validated, user-provided description of the federated identity credential. It has a limit of 600 characters. Optional.
    description: Optional[str] = None
    # The URL of the external identity provider and must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique on the app. It has a limit of 600 characters. Required.
    issuer: Optional[str] = None
    # The unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. It is immutable once created. Alternate key. Required. Not nullable. Supports $filter (eq).
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Nullable.  Defaults to null if not set. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format, as each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Microsoft Entra ID. The combination of issuer and subject must be unique on the app. It has a limit of 600 characters. If subject is defined, claimsMatchingExpression must be null. Supports $filter (eq).
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FederatedIdentityCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FederatedIdentityCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FederatedIdentityCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .federated_identity_expression import FederatedIdentityExpression

        from .entity import Entity
        from .federated_identity_expression import FederatedIdentityExpression

        fields: dict[str, Callable[[Any], None]] = {
            "audiences": lambda n : setattr(self, 'audiences', n.get_collection_of_primitive_values(str)),
            "claimsMatchingExpression": lambda n : setattr(self, 'claims_matching_expression', n.get_object_value(FederatedIdentityExpression)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("audiences", self.audiences)
        writer.write_object_value("claimsMatchingExpression", self.claims_matching_expression)
        writer.write_str_value("description", self.description)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("name", self.name)
        writer.write_str_value("subject", self.subject)
    

