from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import network_access_traffic
    from .. import entity

from .. import entity

@dataclass
class Logs(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The traffic property
    traffic: Optional[List[network_access_traffic.NetworkAccessTraffic]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Logs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Logs
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Logs()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import network_access_traffic
        from .. import entity

        from . import network_access_traffic
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "traffic": lambda n : setattr(self, 'traffic', n.get_collection_of_object_values(network_access_traffic.NetworkAccessTraffic)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("traffic", self.traffic)
    

