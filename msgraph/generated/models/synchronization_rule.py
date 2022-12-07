from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

object_mapping = lazy_import('msgraph.generated.models.object_mapping')
string_key_string_value_pair = lazy_import('msgraph.generated.models.string_key_string_value_pair')

class SynchronizationRule(AdditionalDataHolder, Parsable):
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
        Instantiates a new synchronizationRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # true if the synchronization rule can be customized; false if this rule is read-only and should not be changed.
        self._editable: Optional[bool] = None
        # Synchronization rule identifier. Must be one of the identifiers recognized by the synchronization engine. Supported rule identifiers can be found in the synchronization template returned by the API.
        self._id: Optional[str] = None
        # Additional extension properties. Unless instructed explicitly by the support team, metadata values should not be changed.
        self._metadata: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None
        # Human-readable name of the synchronization rule. Not nullable.
        self._name: Optional[str] = None
        # Collection of object mappings supported by the rule. Tells the synchronization engine which objects should be synchronized.
        self._object_mappings: Optional[List[object_mapping.ObjectMapping]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Priority relative to other rules in the synchronizationSchema. Rules with the lowest priority number will be processed first.
        self._priority: Optional[int] = None
        # Name of the source directory. Must match one of the directory definitions in synchronizationSchema.
        self._source_directory_name: Optional[str] = None
        # Name of the target directory. Must match one of the directory definitions in synchronizationSchema.
        self._target_directory_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationRule()
    
    @property
    def editable(self,) -> Optional[bool]:
        """
        Gets the editable property value. true if the synchronization rule can be customized; false if this rule is read-only and should not be changed.
        Returns: Optional[bool]
        """
        return self._editable
    
    @editable.setter
    def editable(self,value: Optional[bool] = None) -> None:
        """
        Sets the editable property value. true if the synchronization rule can be customized; false if this rule is read-only and should not be changed.
        Args:
            value: Value to set for the editable property.
        """
        self._editable = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(string_key_string_value_pair.StringKeyStringValuePair)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "object_mappings": lambda n : setattr(self, 'object_mappings', n.get_collection_of_object_values(object_mapping.ObjectMapping)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "source_directory_name": lambda n : setattr(self, 'source_directory_name', n.get_str_value()),
            "target_directory_name": lambda n : setattr(self, 'target_directory_name', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Synchronization rule identifier. Must be one of the identifiers recognized by the synchronization engine. Supported rule identifiers can be found in the synchronization template returned by the API.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Synchronization rule identifier. Must be one of the identifiers recognized by the synchronization engine. Supported rule identifiers can be found in the synchronization template returned by the API.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def metadata(self,) -> Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]:
        """
        Gets the metadata property value. Additional extension properties. Unless instructed explicitly by the support team, metadata values should not be changed.
        Returns: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None) -> None:
        """
        Sets the metadata property value. Additional extension properties. Unless instructed explicitly by the support team, metadata values should not be changed.
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Human-readable name of the synchronization rule. Not nullable.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Human-readable name of the synchronization rule. Not nullable.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def object_mappings(self,) -> Optional[List[object_mapping.ObjectMapping]]:
        """
        Gets the objectMappings property value. Collection of object mappings supported by the rule. Tells the synchronization engine which objects should be synchronized.
        Returns: Optional[List[object_mapping.ObjectMapping]]
        """
        return self._object_mappings
    
    @object_mappings.setter
    def object_mappings(self,value: Optional[List[object_mapping.ObjectMapping]] = None) -> None:
        """
        Sets the objectMappings property value. Collection of object mappings supported by the rule. Tells the synchronization engine which objects should be synchronized.
        Args:
            value: Value to set for the objectMappings property.
        """
        self._object_mappings = value
    
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
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Priority relative to other rules in the synchronizationSchema. Rules with the lowest priority number will be processed first.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Priority relative to other rules in the synchronizationSchema. Rules with the lowest priority number will be processed first.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("editable", self.editable)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objectMappings", self.object_mappings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("sourceDirectoryName", self.source_directory_name)
        writer.write_str_value("targetDirectoryName", self.target_directory_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_directory_name(self,) -> Optional[str]:
        """
        Gets the sourceDirectoryName property value. Name of the source directory. Must match one of the directory definitions in synchronizationSchema.
        Returns: Optional[str]
        """
        return self._source_directory_name
    
    @source_directory_name.setter
    def source_directory_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceDirectoryName property value. Name of the source directory. Must match one of the directory definitions in synchronizationSchema.
        Args:
            value: Value to set for the sourceDirectoryName property.
        """
        self._source_directory_name = value
    
    @property
    def target_directory_name(self,) -> Optional[str]:
        """
        Gets the targetDirectoryName property value. Name of the target directory. Must match one of the directory definitions in synchronizationSchema.
        Returns: Optional[str]
        """
        return self._target_directory_name
    
    @target_directory_name.setter
    def target_directory_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetDirectoryName property value. Name of the target directory. Must match one of the directory definitions in synchronizationSchema.
        Args:
            value: Value to set for the targetDirectoryName property.
        """
        self._target_directory_name = value
    

