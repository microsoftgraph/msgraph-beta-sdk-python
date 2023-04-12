from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_conditions, entity, on_token_issuance_start_listener

from . import entity

class AuthenticationEventListener(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationEventListener and sets the default values.
        """
        super().__init__()
        # The authenticationEventsFlowId property
        self._authentication_events_flow_id: Optional[str] = None
        # The conditions property
        self._conditions: Optional[authentication_conditions.AuthenticationConditions] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The priority property
        self._priority: Optional[int] = None
    
    @property
    def authentication_events_flow_id(self,) -> Optional[str]:
        """
        Gets the authenticationEventsFlowId property value. The authenticationEventsFlowId property
        Returns: Optional[str]
        """
        return self._authentication_events_flow_id
    
    @authentication_events_flow_id.setter
    def authentication_events_flow_id(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationEventsFlowId property value. The authenticationEventsFlowId property
        Args:
            value: Value to set for the authentication_events_flow_id property.
        """
        self._authentication_events_flow_id = value
    
    @property
    def conditions(self,) -> Optional[authentication_conditions.AuthenticationConditions]:
        """
        Gets the conditions property value. The conditions property
        Returns: Optional[authentication_conditions.AuthenticationConditions]
        """
        return self._conditions
    
    @conditions.setter
    def conditions(self,value: Optional[authentication_conditions.AuthenticationConditions] = None) -> None:
        """
        Sets the conditions property value. The conditions property
        Args:
            value: Value to set for the conditions property.
        """
        self._conditions = value
    
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
            if mapping_value == "#microsoft.graph.onTokenIssuanceStartListener":
                from . import on_token_issuance_start_listener

                return on_token_issuance_start_listener.OnTokenIssuanceStartListener()
        return AuthenticationEventListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_conditions, entity, on_token_issuance_start_listener

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationEventsFlowId": lambda n : setattr(self, 'authentication_events_flow_id', n.get_str_value()),
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(authentication_conditions.AuthenticationConditions)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority property
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
        writer.write_str_value("authenticationEventsFlowId", self.authentication_events_flow_id)
        writer.write_object_value("conditions", self.conditions)
        writer.write_int_value("priority", self.priority)
    

