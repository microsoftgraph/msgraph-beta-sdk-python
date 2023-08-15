from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration import Configuration
    from .connection_operation import ConnectionOperation
    from .connection_state import ConnectionState
    from .entity import Entity
    from .external_group import ExternalGroup
    from .external_item import ExternalItem
    from .schema import Schema

from .entity import Entity

@dataclass
class ExternalConnection(Entity):
    # The configuration property
    configuration: Optional[Configuration] = None
    # The description property
    description: Optional[str] = None
    # The groups property
    groups: Optional[List[ExternalGroup]] = None
    # The items property
    items: Optional[List[ExternalItem]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[List[ConnectionOperation]] = None
    # The schema property
    schema: Optional[Schema] = None
    # The state property
    state: Optional[ConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalConnection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExternalConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .configuration import Configuration
        from .connection_operation import ConnectionOperation
        from .connection_state import ConnectionState
        from .entity import Entity
        from .external_group import ExternalGroup
        from .external_item import ExternalItem
        from .schema import Schema

        from .configuration import Configuration
        from .connection_operation import ConnectionOperation
        from .connection_state import ConnectionState
        from .entity import Entity
        from .external_group import ExternalGroup
        from .external_item import ExternalItem
        from .schema import Schema

        fields: Dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(Configuration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(ExternalGroup)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(ExternalItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(ConnectionOperation)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(Schema)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ConnectionState)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("schema", self.schema)
    

