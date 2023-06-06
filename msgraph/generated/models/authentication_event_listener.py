from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_conditions, entity, on_attribute_collection_listener, on_authentication_method_load_start_listener, on_interactive_auth_flow_start_listener, on_token_issuance_start_listener, on_user_create_start_listener

from . import entity

@dataclass
class AuthenticationEventListener(entity.Entity):
    # The identifier of the authenticationEventsFlow object.
    authentication_events_flow_id: Optional[str] = None
    # The conditions on which this authenticationEventListener should trigger.
    conditions: Optional[authentication_conditions.AuthenticationConditions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority of this handler. Between 0 (lower priority) and 1000 (higher priority).
    priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationEventListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationEventListener
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.onAttributeCollectionListener":
                from . import on_attribute_collection_listener

                return on_attribute_collection_listener.OnAttributeCollectionListener()
            if mapping_value == "#microsoft.graph.onAuthenticationMethodLoadStartListener":
                from . import on_authentication_method_load_start_listener

                return on_authentication_method_load_start_listener.OnAuthenticationMethodLoadStartListener()
            if mapping_value == "#microsoft.graph.onInteractiveAuthFlowStartListener":
                from . import on_interactive_auth_flow_start_listener

                return on_interactive_auth_flow_start_listener.OnInteractiveAuthFlowStartListener()
            if mapping_value == "#microsoft.graph.onTokenIssuanceStartListener":
                from . import on_token_issuance_start_listener

                return on_token_issuance_start_listener.OnTokenIssuanceStartListener()
            if mapping_value == "#microsoft.graph.onUserCreateStartListener":
                from . import on_user_create_start_listener

                return on_user_create_start_listener.OnUserCreateStartListener()
        return AuthenticationEventListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_conditions, entity, on_attribute_collection_listener, on_authentication_method_load_start_listener, on_interactive_auth_flow_start_listener, on_token_issuance_start_listener, on_user_create_start_listener

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationEventsFlowId": lambda n : setattr(self, 'authentication_events_flow_id', n.get_str_value()),
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(authentication_conditions.AuthenticationConditions)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        writer.write_str_value("authenticationEventsFlowId", self.authentication_events_flow_id)
        writer.write_object_value("conditions", self.conditions)
        writer.write_int_value("priority", self.priority)
    

