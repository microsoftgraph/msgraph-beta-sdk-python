from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import on_interactive_auth_flow_start_handler

from . import on_interactive_auth_flow_start_handler

class OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp(on_interactive_auth_flow_start_handler.OnInteractiveAuthFlowStartHandler):
    def __init__(self,) -> None:
        """
        Instantiates a new OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onInteractiveAuthFlowStartExternalUsersSelfServiceSignUp"
        # Optional. Specifes whether the authentication flow includes an option to sign up (create account) as well as sign in. Default value is false meaning only sign in is enabled.
        self._is_sign_up_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import on_interactive_auth_flow_start_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "isSignUpAllowed": lambda n : setattr(self, 'is_sign_up_allowed', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_sign_up_allowed(self,) -> Optional[bool]:
        """
        Gets the isSignUpAllowed property value. Optional. Specifes whether the authentication flow includes an option to sign up (create account) as well as sign in. Default value is false meaning only sign in is enabled.
        Returns: Optional[bool]
        """
        return self._is_sign_up_allowed
    
    @is_sign_up_allowed.setter
    def is_sign_up_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSignUpAllowed property value. Optional. Specifes whether the authentication flow includes an option to sign up (create account) as well as sign in. Default value is false meaning only sign in is enabled.
        Args:
            value: Value to set for the is_sign_up_allowed property.
        """
        self._is_sign_up_allowed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isSignUpAllowed", self.is_sign_up_allowed)
    

