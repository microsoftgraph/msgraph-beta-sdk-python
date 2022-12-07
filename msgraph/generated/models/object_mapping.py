from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attribute_mapping = lazy_import('msgraph.generated.models.attribute_mapping')
filter = lazy_import('msgraph.generated.models.filter')
metadata_entry = lazy_import('msgraph.generated.models.metadata_entry')
object_flow_types = lazy_import('msgraph.generated.models.object_flow_types')

class ObjectMapping(AdditionalDataHolder, Parsable):
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
    
    @property
    def attribute_mappings(self,) -> Optional[List[attribute_mapping.AttributeMapping]]:
        """
        Gets the attributeMappings property value. Attribute mappings define which attributes to map from the source object into the target object and how they should flow. A number of functions are available to support the transformation of the original source values.
        Returns: Optional[List[attribute_mapping.AttributeMapping]]
        """
        return self._attribute_mappings
    
    @attribute_mappings.setter
    def attribute_mappings(self,value: Optional[List[attribute_mapping.AttributeMapping]] = None) -> None:
        """
        Sets the attributeMappings property value. Attribute mappings define which attributes to map from the source object into the target object and how they should flow. A number of functions are available to support the transformation of the original source values.
        Args:
            value: Value to set for the attributeMappings property.
        """
        self._attribute_mappings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new objectMapping and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Attribute mappings define which attributes to map from the source object into the target object and how they should flow. A number of functions are available to support the transformation of the original source values.
        self._attribute_mappings: Optional[List[attribute_mapping.AttributeMapping]] = None
        # When true, this object mapping will be processed during synchronization. When false, this object mapping will be skipped.
        self._enabled: Optional[bool] = None
        # The flowTypes property
        self._flow_types: Optional[object_flow_types.ObjectFlowTypes] = None
        # Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
        self._metadata: Optional[List[metadata_entry.MetadataEntry]] = None
        # Human-friendly name of the object mapping.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines a filter to be used when deciding whether a given object should be provisioned. For example, you might want to only provision users that are located in the US.
        self._scope: Optional[filter.Filter] = None
        # Name of the object in the source directory. Must match the object name from the source directory definition.
        self._source_object_name: Optional[str] = None
        # Name of the object in target directory. Must match the object name from the target directory definition.
        self._target_object_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ObjectMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ObjectMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ObjectMapping()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. When true, this object mapping will be processed during synchronization. When false, this object mapping will be skipped.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. When true, this object mapping will be processed during synchronization. When false, this object mapping will be skipped.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    @property
    def flow_types(self,) -> Optional[object_flow_types.ObjectFlowTypes]:
        """
        Gets the flowTypes property value. The flowTypes property
        Returns: Optional[object_flow_types.ObjectFlowTypes]
        """
        return self._flow_types
    
    @flow_types.setter
    def flow_types(self,value: Optional[object_flow_types.ObjectFlowTypes] = None) -> None:
        """
        Sets the flowTypes property value. The flowTypes property
        Args:
            value: Value to set for the flowTypes property.
        """
        self._flow_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attribute_mappings": lambda n : setattr(self, 'attribute_mappings', n.get_collection_of_object_values(attribute_mapping.AttributeMapping)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "flow_types": lambda n : setattr(self, 'flow_types', n.get_enum_value(object_flow_types.ObjectFlowTypes)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(metadata_entry.MetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(filter.Filter)),
            "source_object_name": lambda n : setattr(self, 'source_object_name', n.get_str_value()),
            "target_object_name": lambda n : setattr(self, 'target_object_name', n.get_str_value()),
        }
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
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Human-friendly name of the object mapping.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Human-friendly name of the object mapping.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    def scope(self,) -> Optional[filter.Filter]:
        """
        Gets the scope property value. Defines a filter to be used when deciding whether a given object should be provisioned. For example, you might want to only provision users that are located in the US.
        Returns: Optional[filter.Filter]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[filter.Filter] = None) -> None:
        """
        Sets the scope property value. Defines a filter to be used when deciding whether a given object should be provisioned. For example, you might want to only provision users that are located in the US.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attributeMappings", self.attribute_mappings)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_enum_value("flowTypes", self.flow_types)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scope", self.scope)
        writer.write_str_value("sourceObjectName", self.source_object_name)
        writer.write_str_value("targetObjectName", self.target_object_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_object_name(self,) -> Optional[str]:
        """
        Gets the sourceObjectName property value. Name of the object in the source directory. Must match the object name from the source directory definition.
        Returns: Optional[str]
        """
        return self._source_object_name
    
    @source_object_name.setter
    def source_object_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceObjectName property value. Name of the object in the source directory. Must match the object name from the source directory definition.
        Args:
            value: Value to set for the sourceObjectName property.
        """
        self._source_object_name = value
    
    @property
    def target_object_name(self,) -> Optional[str]:
        """
        Gets the targetObjectName property value. Name of the object in target directory. Must match the object name from the target directory definition.
        Returns: Optional[str]
        """
        return self._target_object_name
    
    @target_object_name.setter
    def target_object_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetObjectName property value. Name of the object in target directory. Must match the object name from the target directory definition.
        Args:
            value: Value to set for the targetObjectName property.
        """
        self._target_object_name = value
    

