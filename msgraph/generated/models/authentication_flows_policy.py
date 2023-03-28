from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, self_service_sign_up_authentication_flow_configuration

from . import entity

class AuthenticationFlowsPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationFlowsPolicy and sets the default values.
        """
        super().__init__()
        # Inherited property. A description of the policy. This property is not a key. Optional. Read-only.
        self._description: Optional[str] = None
        # Inherited property. The human-readable name of the policy. This property is not a key. Optional. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Contains selfServiceSignUpAuthenticationFlowConfiguration settings that convey whether self-service sign-up is enabled or disabled. This property is not a key. Optional. Read-only.
        self._self_service_sign_up: Optional[self_service_sign_up_authentication_flow_configuration.SelfServiceSignUpAuthenticationFlowConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationFlowsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationFlowsPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationFlowsPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Inherited property. A description of the policy. This property is not a key. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Inherited property. A description of the policy. This property is not a key. Optional. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Inherited property. The human-readable name of the policy. This property is not a key. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Inherited property. The human-readable name of the policy. This property is not a key. Optional. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, self_service_sign_up_authentication_flow_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "selfServiceSignUp": lambda n : setattr(self, 'self_service_sign_up', n.get_object_value(self_service_sign_up_authentication_flow_configuration.SelfServiceSignUpAuthenticationFlowConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def self_service_sign_up(self,) -> Optional[self_service_sign_up_authentication_flow_configuration.SelfServiceSignUpAuthenticationFlowConfiguration]:
        """
        Gets the selfServiceSignUp property value. Contains selfServiceSignUpAuthenticationFlowConfiguration settings that convey whether self-service sign-up is enabled or disabled. This property is not a key. Optional. Read-only.
        Returns: Optional[self_service_sign_up_authentication_flow_configuration.SelfServiceSignUpAuthenticationFlowConfiguration]
        """
        return self._self_service_sign_up
    
    @self_service_sign_up.setter
    def self_service_sign_up(self,value: Optional[self_service_sign_up_authentication_flow_configuration.SelfServiceSignUpAuthenticationFlowConfiguration] = None) -> None:
        """
        Sets the selfServiceSignUp property value. Contains selfServiceSignUpAuthenticationFlowConfiguration settings that convey whether self-service sign-up is enabled or disabled. This property is not a key. Optional. Read-only.
        Args:
            value: Value to set for the self_service_sign_up property.
        """
        self._self_service_sign_up = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("selfServiceSignUp", self.self_service_sign_up)
    

