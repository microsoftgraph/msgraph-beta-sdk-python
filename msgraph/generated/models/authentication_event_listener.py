from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_conditions = lazy_import('msgraph.generated.models.authentication_conditions')
entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class AuthenticationEventListener(entity.Entity):
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
            value: Value to set for the authenticationEventsFlowId property.
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
        # The tags property
        self._tags: Optional[List[key_value_pair.KeyValuePair]] = None
    
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
        return AuthenticationEventListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_events_flow_id": lambda n : setattr(self, 'authentication_events_flow_id', n.get_str_value()),
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(authentication_conditions.AuthenticationConditions)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
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
        writer.write_collection_of_object_values("tags", self.tags)
    
    @property
    def tags(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the tags property value. The tags property
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the tags property value. The tags property
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    

