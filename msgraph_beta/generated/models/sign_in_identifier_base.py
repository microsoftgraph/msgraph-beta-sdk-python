from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_username_sign_in_identifier import CustomUsernameSignInIdentifier
    from .email_sign_in_identifier import EmailSignInIdentifier
    from .upn_sign_in_identifier import UpnSignInIdentifier
    from .username_sign_in_identifier import UsernameSignInIdentifier

@dataclass
class SignInIdentifierBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether this sign-in identifier type is enabled for user authentication in the tenant.
    is_enabled: Optional[bool] = None
    # The unique name identifier for this sign-in identifier configuration. Possible values include: Email, UPN, Username, CustomUsername1, CustomUsername2.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignInIdentifierBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInIdentifierBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customUsernameSignInIdentifier".casefold():
            from .custom_username_sign_in_identifier import CustomUsernameSignInIdentifier

            return CustomUsernameSignInIdentifier()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailSignInIdentifier".casefold():
            from .email_sign_in_identifier import EmailSignInIdentifier

            return EmailSignInIdentifier()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.upnSignInIdentifier".casefold():
            from .upn_sign_in_identifier import UpnSignInIdentifier

            return UpnSignInIdentifier()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.usernameSignInIdentifier".casefold():
            from .username_sign_in_identifier import UsernameSignInIdentifier

            return UsernameSignInIdentifier()
        return SignInIdentifierBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_username_sign_in_identifier import CustomUsernameSignInIdentifier
        from .email_sign_in_identifier import EmailSignInIdentifier
        from .upn_sign_in_identifier import UpnSignInIdentifier
        from .username_sign_in_identifier import UsernameSignInIdentifier

        from .custom_username_sign_in_identifier import CustomUsernameSignInIdentifier
        from .email_sign_in_identifier import EmailSignInIdentifier
        from .upn_sign_in_identifier import UpnSignInIdentifier
        from .username_sign_in_identifier import UsernameSignInIdentifier

        fields: dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

