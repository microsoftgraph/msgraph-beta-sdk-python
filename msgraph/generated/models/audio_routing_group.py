from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, routing_mode

from . import entity

class AudioRoutingGroup(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new audioRoutingGroup and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of receiving participant ids.
        self._receivers: Optional[List[str]] = None
        # The routingMode property
        self._routing_mode: Optional[routing_mode.RoutingMode] = None
        # List of source participant ids.
        self._sources: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AudioRoutingGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AudioRoutingGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AudioRoutingGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, routing_mode

        fields: Dict[str, Callable[[Any], None]] = {
            "receivers": lambda n : setattr(self, 'receivers', n.get_collection_of_primitive_values(str)),
            "routingMode": lambda n : setattr(self, 'routing_mode', n.get_enum_value(routing_mode.RoutingMode)),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def receivers(self,) -> Optional[List[str]]:
        """
        Gets the receivers property value. List of receiving participant ids.
        Returns: Optional[List[str]]
        """
        return self._receivers
    
    @receivers.setter
    def receivers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the receivers property value. List of receiving participant ids.
        Args:
            value: Value to set for the receivers property.
        """
        self._receivers = value
    
    @property
    def routing_mode(self,) -> Optional[routing_mode.RoutingMode]:
        """
        Gets the routingMode property value. The routingMode property
        Returns: Optional[routing_mode.RoutingMode]
        """
        return self._routing_mode
    
    @routing_mode.setter
    def routing_mode(self,value: Optional[routing_mode.RoutingMode] = None) -> None:
        """
        Sets the routingMode property value. The routingMode property
        Args:
            value: Value to set for the routing_mode property.
        """
        self._routing_mode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("receivers", self.receivers)
        writer.write_enum_value("routingMode", self.routing_mode)
        writer.write_collection_of_primitive_values("sources", self.sources)
    
    @property
    def sources(self,) -> Optional[List[str]]:
        """
        Gets the sources property value. List of source participant ids.
        Returns: Optional[List[str]]
        """
        return self._sources
    
    @sources.setter
    def sources(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sources property value. List of source participant ids.
        Args:
            value: Value to set for the sources property.
        """
        self._sources = value
    

