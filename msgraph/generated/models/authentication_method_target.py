from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target, voice_authentication_method_target

from . import entity

@dataclass
class AuthenticationMethodTarget(entity.Entity):
    # Determines if the user is enforced to register the authentication method.
    is_registration_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The targetType property
    target_type: Optional[authentication_method_target_type.AuthenticationMethodTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget".casefold():
            from . import microsoft_authenticator_authentication_method_target

            return microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodTarget".casefold():
            from . import sms_authentication_method_target

            return sms_authentication_method_target.SmsAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodTarget".casefold():
            from . import voice_authentication_method_target

            return voice_authentication_method_target.VoiceAuthenticationMethodTarget()
        return AuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target, voice_authentication_method_target

        from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target, voice_authentication_method_target

        fields: Dict[str, Callable[[Any], None]] = {
            "isRegistrationRequired": lambda n : setattr(self, 'is_registration_required', n.get_bool_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(authentication_method_target_type.AuthenticationMethodTargetType)),
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
        writer.write_bool_value("isRegistrationRequired", self.is_registration_required)
        writer.write_enum_value("targetType", self.target_type)
    

