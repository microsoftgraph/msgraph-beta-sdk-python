from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .related_resource import RelatedResource

from .related_resource import RelatedResource

@dataclass
class RelatedFile(RelatedResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.relatedFile"
    # The directory property
    directory: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The sizeInBytes property
    size_in_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelatedFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .related_resource import RelatedResource

        from .related_resource import RelatedResource

        fields: Dict[str, Callable[[Any], None]] = {
            "directory": lambda n : setattr(self, 'directory', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "sizeInBytes": lambda n : setattr(self, 'size_in_bytes', n.get_int_value()),
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
        from .related_resource import RelatedResource

        writer.write_str_value("directory", self.directory)
        writer.write_str_value("name", self.name)
        writer.write_int_value("sizeInBytes", self.size_in_bytes)
    

