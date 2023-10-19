from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_conditions import AuthenticationConditions
    from .entity import Entity
    from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

from .entity import Entity

@dataclass
class AuthenticationEventsFlow(Entity):
    # The conditions representing the context of the authentication request that will be used to decide whether the events policy will be invoked.
    conditions: Optional[AuthenticationConditions] = None
    # The description of the events policy.
    description: Optional[str] = None
    # Required. The display name for the events policy.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority to use for each individual event of the events policy. If multiple competing listeners for an event have the same priority, one is chosen and an error is silently logged. Defaults to 500.
    priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationEventsFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationEventsFlow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow".casefold():
            from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

            return ExternalUsersSelfServiceSignUpEventsFlow()
        return AuthenticationEventsFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_conditions import AuthenticationConditions
        from .entity import Entity
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

        from .authentication_conditions import AuthenticationConditions
        from .entity import Entity
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

        fields: Dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(AuthenticationConditions)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("conditions", self.conditions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("priority", self.priority)
    

