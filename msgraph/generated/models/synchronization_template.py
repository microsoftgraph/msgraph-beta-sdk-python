from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, synchronization_metadata_entry, synchronization_schema

from . import entity

@dataclass
class SynchronizationTemplate(entity.Entity):
    # Identifier of the application this template belongs to.
    application_id: Optional[UUID] = None
    # true if this template is recommended to be the default for the application.
    default: Optional[bool] = None
    # Description of the template.
    description: Optional[str] = None
    # true if this template should appear in the collection of templates available for the application instance (service principal).
    discoverable: Optional[bool] = None
    # One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.
    factory_tag: Optional[str] = None
    # Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
    metadata: Optional[List[synchronization_metadata_entry.SynchronizationMetadataEntry]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Default synchronization schema for the jobs based on this template.
    schema: Optional[synchronization_schema.SynchronizationSchema] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, synchronization_metadata_entry, synchronization_schema

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationId": lambda n : setattr(self, 'application_id', n.get_uuid_value()),
            "default": lambda n : setattr(self, 'default', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoverable": lambda n : setattr(self, 'discoverable', n.get_bool_value()),
            "factoryTag": lambda n : setattr(self, 'factory_tag', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(synchronization_metadata_entry.SynchronizationMetadataEntry)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(synchronization_schema.SynchronizationSchema)),
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
        writer.write_uuid_value("applicationId", self.application_id)
        writer.write_bool_value("default", self.default)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("discoverable", self.discoverable)
        writer.write_str_value("factoryTag", self.factory_tag)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_object_value("schema", self.schema)
    

