from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_default_authentication_method_type import UserDefaultAuthenticationMethodType

@dataclass
class SignInPreferences(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether the credential preferences of the system are enabled.
    is_system_preferred_authentication_method_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The default second-factor method used by the user when signing in. If a user is enabled for system-preferred authentication, then this value is ignored except for a few scenarios where a user is authenticating via NPS extension or ADFS adapter. Possible values are push, oath, voiceMobile, voiceAlternateMobile, voiceOffice, sms, and unknownFutureValue
    user_preferred_method_for_secondary_authentication: Optional[UserDefaultAuthenticationMethodType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInPreferences
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SignInPreferences()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .user_default_authentication_method_type import UserDefaultAuthenticationMethodType

        from .user_default_authentication_method_type import UserDefaultAuthenticationMethodType

        fields: Dict[str, Callable[[Any], None]] = {
            "isSystemPreferredAuthenticationMethodEnabled": lambda n : setattr(self, 'is_system_preferred_authentication_method_enabled', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userPreferredMethodForSecondaryAuthentication": lambda n : setattr(self, 'user_preferred_method_for_secondary_authentication', n.get_enum_value(UserDefaultAuthenticationMethodType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isSystemPreferredAuthenticationMethodEnabled", self.is_system_preferred_authentication_method_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("userPreferredMethodForSecondaryAuthentication", self.user_preferred_method_for_secondary_authentication)
        writer.write_additional_data_value(self.additional_data)
    

