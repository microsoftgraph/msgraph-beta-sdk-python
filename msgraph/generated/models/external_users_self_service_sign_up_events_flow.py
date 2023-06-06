from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_events_flow, on_attribute_collection_handler, on_authentication_method_load_start_handler, on_interactive_auth_flow_start_handler, on_user_create_start_handler

from . import authentication_events_flow

@dataclass
class ExternalUsersSelfServiceSignUpEventsFlow(authentication_events_flow.AuthenticationEventsFlow):
    odata_type = "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow"
    # The configuration for what to invoke when attributes are ready to be collected from the user.
    on_attribute_collection: Optional[on_attribute_collection_handler.OnAttributeCollectionHandler] = None
    # Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.
    on_authentication_method_load_start: Optional[on_authentication_method_load_start_handler.OnAuthenticationMethodLoadStartHandler] = None
    # Required. The configuration for what to invoke when an authentication flow is ready to be initiated.
    on_interactive_auth_flow_start: Optional[on_interactive_auth_flow_start_handler.OnInteractiveAuthFlowStartHandler] = None
    # The configuration for what to invoke during user creation.
    on_user_create_start: Optional[on_user_create_start_handler.OnUserCreateStartHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalUsersSelfServiceSignUpEventsFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalUsersSelfServiceSignUpEventsFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalUsersSelfServiceSignUpEventsFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_events_flow, on_attribute_collection_handler, on_authentication_method_load_start_handler, on_interactive_auth_flow_start_handler, on_user_create_start_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "onAttributeCollection": lambda n : setattr(self, 'on_attribute_collection', n.get_object_value(on_attribute_collection_handler.OnAttributeCollectionHandler)),
            "onAuthenticationMethodLoadStart": lambda n : setattr(self, 'on_authentication_method_load_start', n.get_object_value(on_authentication_method_load_start_handler.OnAuthenticationMethodLoadStartHandler)),
            "onInteractiveAuthFlowStart": lambda n : setattr(self, 'on_interactive_auth_flow_start', n.get_object_value(on_interactive_auth_flow_start_handler.OnInteractiveAuthFlowStartHandler)),
            "onUserCreateStart": lambda n : setattr(self, 'on_user_create_start', n.get_object_value(on_user_create_start_handler.OnUserCreateStartHandler)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("onAttributeCollection", self.on_attribute_collection)
        writer.write_object_value("onAuthenticationMethodLoadStart", self.on_authentication_method_load_start)
        writer.write_object_value("onInteractiveAuthFlowStart", self.on_interactive_auth_flow_start)
        writer.write_object_value("onUserCreateStart", self.on_user_create_start)
    

