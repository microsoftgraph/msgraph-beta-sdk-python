from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_store_app_configuration_schema_item_data_type = lazy_import('msgraph.generated.models.android_managed_store_app_configuration_schema_item_data_type')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class AndroidManagedStoreAppConfigurationSchemaItem(AdditionalDataHolder, Parsable):
    """
    Single configuration item inside an Android application's custom configuration schema.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidManagedStoreAppConfigurationSchemaItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Data type for a configuration item inside an Android application's custom configuration schema
        self._data_type: Optional[android_managed_store_app_configuration_schema_item_data_type.AndroidManagedStoreAppConfigurationSchemaItemDataType] = None
        # Default value for boolean type items, if specified by the app developer
        self._default_bool_value: Optional[bool] = None
        # Default value for integer type items, if specified by the app developer
        self._default_int_value: Optional[int] = None
        # Default value for string array type items, if specified by the app developer
        self._default_string_array_value: Optional[List[str]] = None
        # Default value for string type items, if specified by the app developer
        self._default_string_value: Optional[str] = None
        # Description of what the item controls within the application
        self._description: Optional[str] = None
        # Human readable name
        self._display_name: Optional[str] = None
        # Unique index the application uses to maintain nested schema items
        self._index: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Index of parent schema item to track nested schema items
        self._parent_index: Optional[int] = None
        # Unique key the application uses to identify the item
        self._schema_item_key: Optional[str] = None
        # List of human readable name/value pairs for the valid values that can be set for this item (Choice and Multiselect items only)
        self._selections: Optional[List[key_value_pair.KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAppConfigurationSchemaItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfigurationSchemaItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreAppConfigurationSchemaItem()
    
    @property
    def data_type(self,) -> Optional[android_managed_store_app_configuration_schema_item_data_type.AndroidManagedStoreAppConfigurationSchemaItemDataType]:
        """
        Gets the dataType property value. Data type for a configuration item inside an Android application's custom configuration schema
        Returns: Optional[android_managed_store_app_configuration_schema_item_data_type.AndroidManagedStoreAppConfigurationSchemaItemDataType]
        """
        return self._data_type
    
    @data_type.setter
    def data_type(self,value: Optional[android_managed_store_app_configuration_schema_item_data_type.AndroidManagedStoreAppConfigurationSchemaItemDataType] = None) -> None:
        """
        Sets the dataType property value. Data type for a configuration item inside an Android application's custom configuration schema
        Args:
            value: Value to set for the dataType property.
        """
        self._data_type = value
    
    @property
    def default_bool_value(self,) -> Optional[bool]:
        """
        Gets the defaultBoolValue property value. Default value for boolean type items, if specified by the app developer
        Returns: Optional[bool]
        """
        return self._default_bool_value
    
    @default_bool_value.setter
    def default_bool_value(self,value: Optional[bool] = None) -> None:
        """
        Sets the defaultBoolValue property value. Default value for boolean type items, if specified by the app developer
        Args:
            value: Value to set for the defaultBoolValue property.
        """
        self._default_bool_value = value
    
    @property
    def default_int_value(self,) -> Optional[int]:
        """
        Gets the defaultIntValue property value. Default value for integer type items, if specified by the app developer
        Returns: Optional[int]
        """
        return self._default_int_value
    
    @default_int_value.setter
    def default_int_value(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultIntValue property value. Default value for integer type items, if specified by the app developer
        Args:
            value: Value to set for the defaultIntValue property.
        """
        self._default_int_value = value
    
    @property
    def default_string_array_value(self,) -> Optional[List[str]]:
        """
        Gets the defaultStringArrayValue property value. Default value for string array type items, if specified by the app developer
        Returns: Optional[List[str]]
        """
        return self._default_string_array_value
    
    @default_string_array_value.setter
    def default_string_array_value(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defaultStringArrayValue property value. Default value for string array type items, if specified by the app developer
        Args:
            value: Value to set for the defaultStringArrayValue property.
        """
        self._default_string_array_value = value
    
    @property
    def default_string_value(self,) -> Optional[str]:
        """
        Gets the defaultStringValue property value. Default value for string type items, if specified by the app developer
        Returns: Optional[str]
        """
        return self._default_string_value
    
    @default_string_value.setter
    def default_string_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultStringValue property value. Default value for string type items, if specified by the app developer
        Args:
            value: Value to set for the defaultStringValue property.
        """
        self._default_string_value = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of what the item controls within the application
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of what the item controls within the application
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Human readable name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Human readable name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_type": lambda n : setattr(self, 'data_type', n.get_enum_value(android_managed_store_app_configuration_schema_item_data_type.AndroidManagedStoreAppConfigurationSchemaItemDataType)),
            "default_bool_value": lambda n : setattr(self, 'default_bool_value', n.get_bool_value()),
            "default_int_value": lambda n : setattr(self, 'default_int_value', n.get_int_value()),
            "default_string_array_value": lambda n : setattr(self, 'default_string_array_value', n.get_collection_of_primitive_values(str)),
            "default_string_value": lambda n : setattr(self, 'default_string_value', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parent_index": lambda n : setattr(self, 'parent_index', n.get_int_value()),
            "schema_item_key": lambda n : setattr(self, 'schema_item_key', n.get_str_value()),
            "selections": lambda n : setattr(self, 'selections', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
        }
        return fields
    
    @property
    def index(self,) -> Optional[int]:
        """
        Gets the index property value. Unique index the application uses to maintain nested schema items
        Returns: Optional[int]
        """
        return self._index
    
    @index.setter
    def index(self,value: Optional[int] = None) -> None:
        """
        Sets the index property value. Unique index the application uses to maintain nested schema items
        Args:
            value: Value to set for the index property.
        """
        self._index = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def parent_index(self,) -> Optional[int]:
        """
        Gets the parentIndex property value. Index of parent schema item to track nested schema items
        Returns: Optional[int]
        """
        return self._parent_index
    
    @parent_index.setter
    def parent_index(self,value: Optional[int] = None) -> None:
        """
        Sets the parentIndex property value. Index of parent schema item to track nested schema items
        Args:
            value: Value to set for the parentIndex property.
        """
        self._parent_index = value
    
    @property
    def schema_item_key(self,) -> Optional[str]:
        """
        Gets the schemaItemKey property value. Unique key the application uses to identify the item
        Returns: Optional[str]
        """
        return self._schema_item_key
    
    @schema_item_key.setter
    def schema_item_key(self,value: Optional[str] = None) -> None:
        """
        Sets the schemaItemKey property value. Unique key the application uses to identify the item
        Args:
            value: Value to set for the schemaItemKey property.
        """
        self._schema_item_key = value
    
    @property
    def selections(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the selections property value. List of human readable name/value pairs for the valid values that can be set for this item (Choice and Multiselect items only)
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._selections
    
    @selections.setter
    def selections(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the selections property value. List of human readable name/value pairs for the valid values that can be set for this item (Choice and Multiselect items only)
        Args:
            value: Value to set for the selections property.
        """
        self._selections = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("dataType", self.data_type)
        writer.write_bool_value("defaultBoolValue", self.default_bool_value)
        writer.write_int_value("defaultIntValue", self.default_int_value)
        writer.write_collection_of_primitive_values("defaultStringArrayValue", self.default_string_array_value)
        writer.write_str_value("defaultStringValue", self.default_string_value)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("index", self.index)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("parentIndex", self.parent_index)
        writer.write_str_value("schemaItemKey", self.schema_item_key)
        writer.write_collection_of_object_values("selections", self.selections)
        writer.write_additional_data_value(self.additional_data)
    

