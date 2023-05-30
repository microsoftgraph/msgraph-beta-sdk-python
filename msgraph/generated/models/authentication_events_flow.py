from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_conditions, entity, external_users_self_service_sign_up_events_flow

from . import entity

class AuthenticationEventsFlow(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationEventsFlow and sets the default values.
        """
        super().__init__()
        # The conditions representing the context of the authentication request which will be used to decide whether the events policy will be invoked.
        self._conditions: Optional[authentication_conditions.AuthenticationConditions] = None
        # The description of the events policy.
        self._description: Optional[str] = None
        # Required. The display name for the events policy.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The priority to use for each individual event of the events policy. If multiple competing listeners for an event have the same priority, one is chosen and an error is silently logged. Defaults to 500.
        self._priority: Optional[int] = None
    
    @property
    def conditions(self,) -> Optional[authentication_conditions.AuthenticationConditions]:
        """
        Gets the conditions property value. The conditions representing the context of the authentication request which will be used to decide whether the events policy will be invoked.
        Returns: Optional[authentication_conditions.AuthenticationConditions]
        """
        return self._conditions
    
    @conditions.setter
    def conditions(self,value: Optional[authentication_conditions.AuthenticationConditions] = None) -> None:
        """
        Sets the conditions property value. The conditions representing the context of the authentication request which will be used to decide whether the events policy will be invoked.
        Args:
            value: Value to set for the conditions property.
        """
        self._conditions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationEventsFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationEventsFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow":
                from . import external_users_self_service_sign_up_events_flow

                return external_users_self_service_sign_up_events_flow.ExternalUsersSelfServiceSignUpEventsFlow()
        return AuthenticationEventsFlow()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the events policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the events policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Required. The display name for the events policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Required. The display name for the events policy.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_conditions, entity, external_users_self_service_sign_up_events_flow

        fields: Dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(authentication_conditions.AuthenticationConditions)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority to use for each individual event of the events policy. If multiple competing listeners for an event have the same priority, one is chosen and an error is silently logged. Defaults to 500.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority to use for each individual event of the events policy. If multiple competing listeners for an event have the same priority, one is chosen and an error is silently logged. Defaults to 500.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("conditions", self.conditions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("priority", self.priority)
    

