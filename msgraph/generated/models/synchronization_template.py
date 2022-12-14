from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
metadata_entry = lazy_import('msgraph.generated.models.metadata_entry')
synchronization_schema = lazy_import('msgraph.generated.models.synchronization_schema')

class SynchronizationTemplate(entity.Entity):
    """
    Casts the previous resource to application.
    """
    @property
    def application_id(self,) -> Optional[Guid]:
        """
        Gets the applicationId property value. Identifier of the application this template belongs to.
        Returns: Optional[Guid]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the applicationId property value. Identifier of the application this template belongs to.
        Args:
            value: Value to set for the applicationId property.
        """
        self._application_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationTemplate and sets the default values.
        """
        super().__init__()
        # Identifier of the application this template belongs to.
        self._application_id: Optional[Guid] = None
        # true if this template is recommended to be the default for the application.
        self._default: Optional[bool] = None
        # Description of the template.
        self._description: Optional[str] = None
        # true if this template should appear in the collection of templates available for the application instance (service principal).
        self._discoverable: Optional[bool] = None
        # One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.
        self._factory_tag: Optional[str] = None
        # Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
        self._metadata: Optional[List[metadata_entry.MetadataEntry]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Default synchronization schema for the jobs based on this template.
        self._schema: Optional[synchronization_schema.SynchronizationSchema] = None
    
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
    
    @property
    def default(self,) -> Optional[bool]:
        """
        Gets the default property value. true if this template is recommended to be the default for the application.
        Returns: Optional[bool]
        """
        return self._default
    
    @default.setter
    def default(self,value: Optional[bool] = None) -> None:
        """
        Sets the default property value. true if this template is recommended to be the default for the application.
        Args:
            value: Value to set for the default property.
        """
        self._default = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the template.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the template.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def discoverable(self,) -> Optional[bool]:
        """
        Gets the discoverable property value. true if this template should appear in the collection of templates available for the application instance (service principal).
        Returns: Optional[bool]
        """
        return self._discoverable
    
    @discoverable.setter
    def discoverable(self,value: Optional[bool] = None) -> None:
        """
        Sets the discoverable property value. true if this template should appear in the collection of templates available for the application instance (service principal).
        Args:
            value: Value to set for the discoverable property.
        """
        self._discoverable = value
    
    @property
    def factory_tag(self,) -> Optional[str]:
        """
        Gets the factoryTag property value. One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.
        Returns: Optional[str]
        """
        return self._factory_tag
    
    @factory_tag.setter
    def factory_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the factoryTag property value. One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.
        Args:
            value: Value to set for the factoryTag property.
        """
        self._factory_tag = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_id": lambda n : setattr(self, 'application_id', n.get_object_value(Guid)),
            "default": lambda n : setattr(self, 'default', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoverable": lambda n : setattr(self, 'discoverable', n.get_bool_value()),
            "factory_tag": lambda n : setattr(self, 'factory_tag', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(metadata_entry.MetadataEntry)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(synchronization_schema.SynchronizationSchema)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def metadata(self,) -> Optional[List[metadata_entry.MetadataEntry]]:
        """
        Gets the metadata property value. Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
        Returns: Optional[List[metadata_entry.MetadataEntry]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[metadata_entry.MetadataEntry]] = None) -> None:
        """
        Sets the metadata property value. Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def schema(self,) -> Optional[synchronization_schema.SynchronizationSchema]:
        """
        Gets the schema property value. Default synchronization schema for the jobs based on this template.
        Returns: Optional[synchronization_schema.SynchronizationSchema]
        """
        return self._schema
    
    @schema.setter
    def schema(self,value: Optional[synchronization_schema.SynchronizationSchema] = None) -> None:
        """
        Sets the schema property value. Default synchronization schema for the jobs based on this template.
        Args:
            value: Value to set for the schema property.
        """
        self._schema = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("applicationId", self.application_id)
        writer.write_bool_value("default", self.default)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("discoverable", self.discoverable)
        writer.write_str_value("factoryTag", self.factory_tag)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_object_value("schema", self.schema)
    

