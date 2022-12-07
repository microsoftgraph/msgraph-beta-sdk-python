from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_segment = lazy_import('msgraph.generated.models.application_segment')

class IpApplicationSegment(application_segment.ApplicationSegment):
    def __init__(self,) -> None:
        """
        Instantiates a new IpApplicationSegment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.ipApplicationSegment"
        # The destinationHost property
        self._destination_host: Optional[str] = None
        # The port property
        self._port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpApplicationSegment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpApplicationSegment()
    
    @property
    def destination_host(self,) -> Optional[str]:
        """
        Gets the destinationHost property value. The destinationHost property
        Returns: Optional[str]
        """
        return self._destination_host
    
    @destination_host.setter
    def destination_host(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationHost property value. The destinationHost property
        Args:
            value: Value to set for the destinationHost property.
        """
        self._destination_host = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "destination_host": lambda n : setattr(self, 'destination_host', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def port(self,) -> Optional[int]:
        """
        Gets the port property value. The port property
        Returns: Optional[int]
        """
        return self._port
    
    @port.setter
    def port(self,value: Optional[int] = None) -> None:
        """
        Sets the port property value. The port property
        Args:
            value: Value to set for the port property.
        """
        self._port = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("destinationHost", self.destination_host)
        writer.write_int_value("port", self.port)
    

