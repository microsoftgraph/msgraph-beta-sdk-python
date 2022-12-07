from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
external_connection = lazy_import('msgraph.generated.models.external_connection')

class External(entity.Entity):
    @property
    def connections(self,) -> Optional[List[external_connection.ExternalConnection]]:
        """
        Gets the connections property value. The connections property
        Returns: Optional[List[external_connection.ExternalConnection]]
        """
        return self._connections
    
    @connections.setter
    def connections(self,value: Optional[List[external_connection.ExternalConnection]] = None) -> None:
        """
        Sets the connections property value. The connections property
        Args:
            value: Value to set for the connections property.
        """
        self._connections = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new External and sets the default values.
        """
        super().__init__()
        # The connections property
        self._connections: Optional[List[external_connection.ExternalConnection]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> External:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: External
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return External()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connections": lambda n : setattr(self, 'connections', n.get_collection_of_object_values(external_connection.ExternalConnection)),
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
        writer.write_collection_of_object_values("connections", self.connections)
    

