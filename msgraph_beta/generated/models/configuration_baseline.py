from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .baseline_parameter import BaselineParameter
    from .baseline_resource import BaselineResource
    from .entity import Entity

from .entity import Entity

@dataclass
class ConfigurationBaseline(Entity, Parsable):
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parameters property
    parameters: Optional[list[BaselineParameter]] = None
    # The resources property
    resources: Optional[list[BaselineResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationBaseline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationBaseline
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationBaseline()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .baseline_parameter import BaselineParameter
        from .baseline_resource import BaselineResource
        from .entity import Entity

        from .baseline_parameter import BaselineParameter
        from .baseline_resource import BaselineResource
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(BaselineParameter)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(BaselineResource)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_collection_of_object_values("resources", self.resources)
    

