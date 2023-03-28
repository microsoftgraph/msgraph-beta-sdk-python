from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target, voice_authentication_method_target

from . import entity

class AuthenticationMethodTarget(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationMethodTarget and sets the default values.
        """
        super().__init__()
        # Determines if the user is enforced to register the authentication method.
        self._is_registration_required: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The targetType property
        self._target_type: Optional[authentication_method_target_type.AuthenticationMethodTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget":
                from . import microsoft_authenticator_authentication_method_target

                return microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget()
            if mapping_value == "#microsoft.graph.smsAuthenticationMethodTarget":
                from . import sms_authentication_method_target

                return sms_authentication_method_target.SmsAuthenticationMethodTarget()
            if mapping_value == "#microsoft.graph.voiceAuthenticationMethodTarget":
                from . import voice_authentication_method_target

                return voice_authentication_method_target.VoiceAuthenticationMethodTarget()
        return AuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target, voice_authentication_method_target

        fields: Dict[str, Callable[[Any], None]] = {
            "isRegistrationRequired": lambda n : setattr(self, 'is_registration_required', n.get_bool_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(authentication_method_target_type.AuthenticationMethodTargetType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_registration_required(self,) -> Optional[bool]:
        """
        Gets the isRegistrationRequired property value. Determines if the user is enforced to register the authentication method.
        Returns: Optional[bool]
        """
        return self._is_registration_required
    
    @is_registration_required.setter
    def is_registration_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRegistrationRequired property value. Determines if the user is enforced to register the authentication method.
        Args:
            value: Value to set for the is_registration_required property.
        """
        self._is_registration_required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isRegistrationRequired", self.is_registration_required)
        writer.write_enum_value("targetType", self.target_type)
    
    @property
    def target_type(self,) -> Optional[authentication_method_target_type.AuthenticationMethodTargetType]:
        """
        Gets the targetType property value. The targetType property
        Returns: Optional[authentication_method_target_type.AuthenticationMethodTargetType]
        """
        return self._target_type
    
    @target_type.setter
    def target_type(self,value: Optional[authentication_method_target_type.AuthenticationMethodTargetType] = None) -> None:
        """
        Sets the targetType property value. The targetType property
        Args:
            value: Value to set for the target_type property.
        """
        self._target_type = value
    

