from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attribute_type = lazy_import('msgraph.generated.models.attribute_type')
metadata_entry = lazy_import('msgraph.generated.models.metadata_entry')
mutability = lazy_import('msgraph.generated.models.mutability')
referenced_object = lazy_import('msgraph.generated.models.referenced_object')
string_key_string_value_pair = lazy_import('msgraph.generated.models.string_key_string_value_pair')

class AttributeDefinition(AdditionalDataHolder, Parsable):
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
    def anchor(self,) -> Optional[bool]:
        """
        Gets the anchor property value. true if the attribute should be used as the anchor for the object. Anchor attributes must have a unique value identifying an object, and must be immutable. Default is false. One, and only one, of the object's attributes must be designated as the anchor to support synchronization.
        Returns: Optional[bool]
        """
        return self._anchor
    
    @anchor.setter
    def anchor(self,value: Optional[bool] = None) -> None:
        """
        Sets the anchor property value. true if the attribute should be used as the anchor for the object. Anchor attributes must have a unique value identifying an object, and must be immutable. Default is false. One, and only one, of the object's attributes must be designated as the anchor to support synchronization.
        Args:
            value: Value to set for the anchor property.
        """
        self._anchor = value
    
    @property
    def api_expressions(self,) -> Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]:
        """
        Gets the apiExpressions property value. The apiExpressions property
        Returns: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]
        """
        return self._api_expressions
    
    @api_expressions.setter
    def api_expressions(self,value: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None) -> None:
        """
        Sets the apiExpressions property value. The apiExpressions property
        Args:
            value: Value to set for the apiExpressions property.
        """
        self._api_expressions = value
    
    @property
    def case_exact(self,) -> Optional[bool]:
        """
        Gets the caseExact property value. true if value of this attribute should be treated as case-sensitive. This setting affects how the synchronization engine detects changes for the attribute.
        Returns: Optional[bool]
        """
        return self._case_exact
    
    @case_exact.setter
    def case_exact(self,value: Optional[bool] = None) -> None:
        """
        Sets the caseExact property value. true if value of this attribute should be treated as case-sensitive. This setting affects how the synchronization engine detects changes for the attribute.
        Args:
            value: Value to set for the caseExact property.
        """
        self._case_exact = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new attributeDefinition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # true if the attribute should be used as the anchor for the object. Anchor attributes must have a unique value identifying an object, and must be immutable. Default is false. One, and only one, of the object's attributes must be designated as the anchor to support synchronization.
        self._anchor: Optional[bool] = None
        # The apiExpressions property
        self._api_expressions: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None
        # true if value of this attribute should be treated as case-sensitive. This setting affects how the synchronization engine detects changes for the attribute.
        self._case_exact: Optional[bool] = None
        # The defaultValue property
        self._default_value: Optional[str] = None
        # 'true' to allow null values for attributes.
        self._flow_null_values: Optional[bool] = None
        # Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
        self._metadata: Optional[List[metadata_entry.MetadataEntry]] = None
        # true if an attribute can have multiple values. Default is false.
        self._multivalued: Optional[bool] = None
        # The mutability property
        self._mutability: Optional[mutability.Mutability] = None
        # Name of the attribute. Must be unique within the object definition. Not nullable.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For attributes with reference type, lists referenced objects (for example, the manager attribute would list User as the referenced object).
        self._referenced_objects: Optional[List[referenced_object.ReferencedObject]] = None
        # true if attribute is required. Object can not be created if any of the required attributes are missing. If during synchronization, the required attribute has no value, the default value will be used. If default the value was not set, synchronization will record an error.
        self._required: Optional[bool] = None
        # The type property
        self._type: Optional[attribute_type.AttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeDefinition()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. The defaultValue property
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. The defaultValue property
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    @property
    def flow_null_values(self,) -> Optional[bool]:
        """
        Gets the flowNullValues property value. 'true' to allow null values for attributes.
        Returns: Optional[bool]
        """
        return self._flow_null_values
    
    @flow_null_values.setter
    def flow_null_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the flowNullValues property value. 'true' to allow null values for attributes.
        Args:
            value: Value to set for the flowNullValues property.
        """
        self._flow_null_values = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "anchor": lambda n : setattr(self, 'anchor', n.get_bool_value()),
            "api_expressions": lambda n : setattr(self, 'api_expressions', n.get_collection_of_object_values(string_key_string_value_pair.StringKeyStringValuePair)),
            "case_exact": lambda n : setattr(self, 'case_exact', n.get_bool_value()),
            "default_value": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "flow_null_values": lambda n : setattr(self, 'flow_null_values', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(metadata_entry.MetadataEntry)),
            "multivalued": lambda n : setattr(self, 'multivalued', n.get_bool_value()),
            "mutability": lambda n : setattr(self, 'mutability', n.get_enum_value(mutability.Mutability)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referenced_objects": lambda n : setattr(self, 'referenced_objects', n.get_collection_of_object_values(referenced_object.ReferencedObject)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(attribute_type.AttributeType)),
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
    def multivalued(self,) -> Optional[bool]:
        """
        Gets the multivalued property value. true if an attribute can have multiple values. Default is false.
        Returns: Optional[bool]
        """
        return self._multivalued
    
    @multivalued.setter
    def multivalued(self,value: Optional[bool] = None) -> None:
        """
        Sets the multivalued property value. true if an attribute can have multiple values. Default is false.
        Args:
            value: Value to set for the multivalued property.
        """
        self._multivalued = value
    
    @property
    def mutability(self,) -> Optional[mutability.Mutability]:
        """
        Gets the mutability property value. The mutability property
        Returns: Optional[mutability.Mutability]
        """
        return self._mutability
    
    @mutability.setter
    def mutability(self,value: Optional[mutability.Mutability] = None) -> None:
        """
        Sets the mutability property value. The mutability property
        Args:
            value: Value to set for the mutability property.
        """
        self._mutability = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the attribute. Must be unique within the object definition. Not nullable.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the attribute. Must be unique within the object definition. Not nullable.
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
    def referenced_objects(self,) -> Optional[List[referenced_object.ReferencedObject]]:
        """
        Gets the referencedObjects property value. For attributes with reference type, lists referenced objects (for example, the manager attribute would list User as the referenced object).
        Returns: Optional[List[referenced_object.ReferencedObject]]
        """
        return self._referenced_objects
    
    @referenced_objects.setter
    def referenced_objects(self,value: Optional[List[referenced_object.ReferencedObject]] = None) -> None:
        """
        Sets the referencedObjects property value. For attributes with reference type, lists referenced objects (for example, the manager attribute would list User as the referenced object).
        Args:
            value: Value to set for the referencedObjects property.
        """
        self._referenced_objects = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. true if attribute is required. Object can not be created if any of the required attributes are missing. If during synchronization, the required attribute has no value, the default value will be used. If default the value was not set, synchronization will record an error.
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. true if attribute is required. Object can not be created if any of the required attributes are missing. If during synchronization, the required attribute has no value, the default value will be used. If default the value was not set, synchronization will record an error.
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("anchor", self.anchor)
        writer.write_collection_of_object_values("apiExpressions", self.api_expressions)
        writer.write_bool_value("caseExact", self.case_exact)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("flowNullValues", self.flow_null_values)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_bool_value("multivalued", self.multivalued)
        writer.write_enum_value("mutability", self.mutability)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("referencedObjects", self.referenced_objects)
        writer.write_bool_value("required", self.required)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[attribute_type.AttributeType]:
        """
        Gets the type property value. The type property
        Returns: Optional[attribute_type.AttributeType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[attribute_type.AttributeType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

