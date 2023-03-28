from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_for_work_app_configuration_schema_item, entity

from . import entity

class AndroidForWorkAppConfigurationSchema(entity.Entity):
    """
    Schema describing an Android for Work application's custom configurations.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new androidForWorkAppConfigurationSchema and sets the default values.
        """
        super().__init__()
        # UTF8 encoded byte array containing example JSON string conforming to this schema that demonstrates how to set the configuration for this app
        self._example_json: Optional[bytes] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of items each representing a named configuration option in the schema
        self._schema_items: Optional[List[android_for_work_app_configuration_schema_item.AndroidForWorkAppConfigurationSchemaItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkAppConfigurationSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkAppConfigurationSchema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidForWorkAppConfigurationSchema()
    
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
            value: Value to set for the example_json property.
        """
        self._example_json = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_for_work_app_configuration_schema_item, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "exampleJson": lambda n : setattr(self, 'example_json', n.get_bytes_value()),
            "schemaItems": lambda n : setattr(self, 'schema_items', n.get_collection_of_object_values(android_for_work_app_configuration_schema_item.AndroidForWorkAppConfigurationSchemaItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def schema_items(self,) -> Optional[List[android_for_work_app_configuration_schema_item.AndroidForWorkAppConfigurationSchemaItem]]:
        """
        Gets the schemaItems property value. Collection of items each representing a named configuration option in the schema
        Returns: Optional[List[android_for_work_app_configuration_schema_item.AndroidForWorkAppConfigurationSchemaItem]]
        """
        return self._schema_items
    
    @schema_items.setter
    def schema_items(self,value: Optional[List[android_for_work_app_configuration_schema_item.AndroidForWorkAppConfigurationSchemaItem]] = None) -> None:
        """
        Sets the schemaItems property value. Collection of items each representing a named configuration option in the schema
        Args:
            value: Value to set for the schema_items property.
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
        writer.write_collection_of_object_values("schemaItems", self.schema_items)
    

