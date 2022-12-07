from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_store_app_configuration_schema_item = lazy_import('msgraph.generated.models.android_managed_store_app_configuration_schema_item')
entity = lazy_import('msgraph.generated.models.entity')

class AndroidManagedStoreAppConfigurationSchema(entity.Entity):
    """
    Schema describing an Android application's custom configurations.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new androidManagedStoreAppConfigurationSchema and sets the default values.
        """
        super().__init__()
        # UTF8 encoded byte array containing example JSON string conforming to this schema that demonstrates how to set the configuration for this app
        self._example_json: Optional[bytes] = None
        # Collection of items each representing a named configuration option in the schema. It contains a flat list of all configuration.
        self._nested_schema_items: Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of items each representing a named configuration option in the schema. It only contains the root-level configuration.
        self._schema_items: Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAppConfigurationSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfigurationSchema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreAppConfigurationSchema()
    
    @property
    def example_json(self,) -> Optional[bytes]:
        """
        Gets the exampleJson property value. UTF8 encoded byte array containing example JSON string conforming to this schema that demonstrates how to set the configuration for this app
        Returns: Optional[bytes]
        """
        return self._example_json
    
    @example_json.setter
    def example_json(self,value: Optional[bytes] = None) -> None:
        """
        Sets the exampleJson property value. UTF8 encoded byte array containing example JSON string conforming to this schema that demonstrates how to set the configuration for this app
        Args:
            value: Value to set for the exampleJson property.
        """
        self._example_json = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "example_json": lambda n : setattr(self, 'example_json', n.get_bytes_value()),
            "nested_schema_items": lambda n : setattr(self, 'nested_schema_items', n.get_collection_of_object_values(android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem)),
            "schema_items": lambda n : setattr(self, 'schema_items', n.get_collection_of_object_values(android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def nested_schema_items(self,) -> Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]]:
        """
        Gets the nestedSchemaItems property value. Collection of items each representing a named configuration option in the schema. It contains a flat list of all configuration.
        Returns: Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]]
        """
        return self._nested_schema_items
    
    @nested_schema_items.setter
    def nested_schema_items(self,value: Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]] = None) -> None:
        """
        Sets the nestedSchemaItems property value. Collection of items each representing a named configuration option in the schema. It contains a flat list of all configuration.
        Args:
            value: Value to set for the nestedSchemaItems property.
        """
        self._nested_schema_items = value
    
    @property
    def schema_items(self,) -> Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]]:
        """
        Gets the schemaItems property value. Collection of items each representing a named configuration option in the schema. It only contains the root-level configuration.
        Returns: Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]]
        """
        return self._schema_items
    
    @schema_items.setter
    def schema_items(self,value: Optional[List[android_managed_store_app_configuration_schema_item.AndroidManagedStoreAppConfigurationSchemaItem]] = None) -> None:
        """
        Sets the schemaItems property value. Collection of items each representing a named configuration option in the schema. It only contains the root-level configuration.
        Args:
            value: Value to set for the schemaItems property.
        """
        self._schema_items = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("exampleJson", self.example_json)
        writer.write_collection_of_object_values("nestedSchemaItems", self.nested_schema_items)
        writer.write_collection_of_object_values("schemaItems", self.schema_items)
    

