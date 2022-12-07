from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
resource_connection_state = lazy_import('msgraph.generated.models.windows_updates.resource_connection_state')

class ResourceConnection(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
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
        return ResourceConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
    

