from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .operational_insights_connection import OperationalInsightsConnection
    from .resource_connection_state import ResourceConnectionState

from ..entity import Entity

@dataclass
class ResourceConnection(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of the connection. The possible values are: connected, notAuthorized, notFound, unknownFutureValue.
    state: Optional[ResourceConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourceConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.operationalInsightsConnection".casefold():
            from .operational_insights_connection import OperationalInsightsConnection

            return OperationalInsightsConnection()
        return ResourceConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .operational_insights_connection import OperationalInsightsConnection
        from .resource_connection_state import ResourceConnectionState

        from ..entity import Entity
        from .operational_insights_connection import OperationalInsightsConnection
        from .resource_connection_state import ResourceConnectionState

        fields: Dict[str, Callable[[Any], None]] = {
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ResourceConnectionState)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("state", self.state)
    

