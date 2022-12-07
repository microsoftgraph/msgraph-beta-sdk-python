from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attribute_flow_behavior = lazy_import('msgraph.generated.models.attribute_flow_behavior')
attribute_flow_type = lazy_import('msgraph.generated.models.attribute_flow_type')
attribute_mapping_source = lazy_import('msgraph.generated.models.attribute_mapping_source')

class AttributeMapping(AdditionalDataHolder, Parsable):
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
        Instantiates a new attributeMapping and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Default value to be used in case the source property was evaluated to null. Optional.
        self._default_value: Optional[str] = None
        # For internal use only.
        self._export_missing_references: Optional[bool] = None
        # The flowBehavior property
        self._flow_behavior: Optional[attribute_flow_behavior.AttributeFlowBehavior] = None
        # The flowType property
        self._flow_type: Optional[attribute_flow_type.AttributeFlowType] = None
        # If higher than 0, this attribute will be used to perform an initial match of the objects between source and target directories. The synchronization engine will try to find the matching object using attribute with lowest value of matching priority first. If not found, the attribute with the next matching priority will be used, and so on a until match is found or no more matching attributes are left. Only attributes that are expected to have unique values, such as email, should be used as matching attributes.
        self._matching_priority: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines how a value should be extracted (or transformed) from the source object.
        self._source: Optional[attribute_mapping_source.AttributeMappingSource] = None
        # Name of the attribute on the target object.
        self._target_attribute_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeMapping()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. Default value to be used in case the source property was evaluated to null. Optional.
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. Default value to be used in case the source property was evaluated to null. Optional.
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    @property
    def export_missing_references(self,) -> Optional[bool]:
        """
        Gets the exportMissingReferences property value. For internal use only.
        Returns: Optional[bool]
        """
        return self._export_missing_references
    
    @export_missing_references.setter
    def export_missing_references(self,value: Optional[bool] = None) -> None:
        """
        Sets the exportMissingReferences property value. For internal use only.
        Args:
            value: Value to set for the exportMissingReferences property.
        """
        self._export_missing_references = value
    
    @property
    def flow_behavior(self,) -> Optional[attribute_flow_behavior.AttributeFlowBehavior]:
        """
        Gets the flowBehavior property value. The flowBehavior property
        Returns: Optional[attribute_flow_behavior.AttributeFlowBehavior]
        """
        return self._flow_behavior
    
    @flow_behavior.setter
    def flow_behavior(self,value: Optional[attribute_flow_behavior.AttributeFlowBehavior] = None) -> None:
        """
        Sets the flowBehavior property value. The flowBehavior property
        Args:
            value: Value to set for the flowBehavior property.
        """
        self._flow_behavior = value
    
    @property
    def flow_type(self,) -> Optional[attribute_flow_type.AttributeFlowType]:
        """
        Gets the flowType property value. The flowType property
        Returns: Optional[attribute_flow_type.AttributeFlowType]
        """
        return self._flow_type
    
    @flow_type.setter
    def flow_type(self,value: Optional[attribute_flow_type.AttributeFlowType] = None) -> None:
        """
        Sets the flowType property value. The flowType property
        Args:
            value: Value to set for the flowType property.
        """
        self._flow_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_value": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "export_missing_references": lambda n : setattr(self, 'export_missing_references', n.get_bool_value()),
            "flow_behavior": lambda n : setattr(self, 'flow_behavior', n.get_enum_value(attribute_flow_behavior.AttributeFlowBehavior)),
            "flow_type": lambda n : setattr(self, 'flow_type', n.get_enum_value(attribute_flow_type.AttributeFlowType)),
            "matching_priority": lambda n : setattr(self, 'matching_priority', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(attribute_mapping_source.AttributeMappingSource)),
            "target_attribute_name": lambda n : setattr(self, 'target_attribute_name', n.get_str_value()),
        }
        return fields
    
    @property
    def matching_priority(self,) -> Optional[int]:
        """
        Gets the matchingPriority property value. If higher than 0, this attribute will be used to perform an initial match of the objects between source and target directories. The synchronization engine will try to find the matching object using attribute with lowest value of matching priority first. If not found, the attribute with the next matching priority will be used, and so on a until match is found or no more matching attributes are left. Only attributes that are expected to have unique values, such as email, should be used as matching attributes.
        Returns: Optional[int]
        """
        return self._matching_priority
    
    @matching_priority.setter
    def matching_priority(self,value: Optional[int] = None) -> None:
        """
        Sets the matchingPriority property value. If higher than 0, this attribute will be used to perform an initial match of the objects between source and target directories. The synchronization engine will try to find the matching object using attribute with lowest value of matching priority first. If not found, the attribute with the next matching priority will be used, and so on a until match is found or no more matching attributes are left. Only attributes that are expected to have unique values, such as email, should be used as matching attributes.
        Args:
            value: Value to set for the matchingPriority property.
        """
        self._matching_priority = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("exportMissingReferences", self.export_missing_references)
        writer.write_enum_value("flowBehavior", self.flow_behavior)
        writer.write_enum_value("flowType", self.flow_type)
        writer.write_int_value("matchingPriority", self.matching_priority)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("source", self.source)
        writer.write_str_value("targetAttributeName", self.target_attribute_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source(self,) -> Optional[attribute_mapping_source.AttributeMappingSource]:
        """
        Gets the source property value. Defines how a value should be extracted (or transformed) from the source object.
        Returns: Optional[attribute_mapping_source.AttributeMappingSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[attribute_mapping_source.AttributeMappingSource] = None) -> None:
        """
        Sets the source property value. Defines how a value should be extracted (or transformed) from the source object.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def target_attribute_name(self,) -> Optional[str]:
        """
        Gets the targetAttributeName property value. Name of the attribute on the target object.
        Returns: Optional[str]
        """
        return self._target_attribute_name
    
    @target_attribute_name.setter
    def target_attribute_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetAttributeName property value. Name of the attribute on the target object.
        Args:
            value: Value to set for the targetAttributeName property.
        """
        self._target_attribute_name = value
    

