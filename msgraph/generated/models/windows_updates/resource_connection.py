from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import operational_insights_connection, resource_connection_state
    from .. import entity

from .. import entity

class ResourceConnection(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new resourceConnection and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The state of the connection. The possible values are: connected, notAuthorized, notFound, unknownFutureValue.
        self._state: Optional[resource_connection_state.ResourceConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsUpdates.operationalInsightsConnection":
                from . import operational_insights_connection

                return operational_insights_connection.OperationalInsightsConnection()
        return ResourceConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import operational_insights_connection, resource_connection_state
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "state": lambda n : setattr(self, 'state', n.get_enum_value(resource_connection_state.ResourceConnectionState)),
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
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[resource_connection_state.ResourceConnectionState]:
        """
        Gets the state property value. The state of the connection. The possible values are: connected, notAuthorized, notFound, unknownFutureValue.
        Returns: Optional[resource_connection_state.ResourceConnectionState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[resource_connection_state.ResourceConnectionState] = None) -> None:
        """
        Sets the state property value. The state of the connection. The possible values are: connected, notAuthorized, notFound, unknownFutureValue.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

