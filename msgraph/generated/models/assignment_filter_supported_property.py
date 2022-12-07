from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_filter_operator = lazy_import('msgraph.generated.models.assignment_filter_operator')

class AssignmentFilterSupportedProperty(AdditionalDataHolder, Parsable):
    """
    Represents the information about the property which is supported in crafting the rule of AssignmentFilter.
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
        Instantiates a new assignmentFilterSupportedProperty and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The data type of the property.
        self._data_type: Optional[str] = None
        # Indicates whether the property is a collection type or not.
        self._is_collection: Optional[bool] = None
        # Name of the property.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Regex string to do validation on the property value.
        self._property_regex_constraint: Optional[str] = None
        # List of all supported operators on this property.
        self._supported_operators: Optional[List[assignment_filter_operator.AssignmentFilterOperator]] = None
        # List of all supported values for this propery, empty if everything is supported.
        self._supported_values: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterSupportedProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterSupportedProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentFilterSupportedProperty()
    
    @property
    def data_type(self,) -> Optional[str]:
        """
        Gets the dataType property value. The data type of the property.
        Returns: Optional[str]
        """
        return self._data_type
    
    @data_type.setter
    def data_type(self,value: Optional[str] = None) -> None:
        """
        Sets the dataType property value. The data type of the property.
        Args:
            value: Value to set for the dataType property.
        """
        self._data_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_type": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "is_collection": lambda n : setattr(self, 'is_collection', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "property_regex_constraint": lambda n : setattr(self, 'property_regex_constraint', n.get_str_value()),
            "supported_operators": lambda n : setattr(self, 'supported_operators', n.get_collection_of_enum_values(assignment_filter_operator.AssignmentFilterOperator)),
            "supported_values": lambda n : setattr(self, 'supported_values', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def is_collection(self,) -> Optional[bool]:
        """
        Gets the isCollection property value. Indicates whether the property is a collection type or not.
        Returns: Optional[bool]
        """
        return self._is_collection
    
    @is_collection.setter
    def is_collection(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCollection property value. Indicates whether the property is a collection type or not.
        Args:
            value: Value to set for the isCollection property.
        """
        self._is_collection = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the property.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the property.
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
    def property_regex_constraint(self,) -> Optional[str]:
        """
        Gets the propertyRegexConstraint property value. Regex string to do validation on the property value.
        Returns: Optional[str]
        """
        return self._property_regex_constraint
    
    @property_regex_constraint.setter
    def property_regex_constraint(self,value: Optional[str] = None) -> None:
        """
        Sets the propertyRegexConstraint property value. Regex string to do validation on the property value.
        Args:
            value: Value to set for the propertyRegexConstraint property.
        """
        self._property_regex_constraint = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("dataType", self.data_type)
        writer.write_bool_value("isCollection", self.is_collection)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("propertyRegexConstraint", self.property_regex_constraint)
        writer.write_enum_value("supportedOperators", self.supported_operators)
        writer.write_collection_of_primitive_values("supportedValues", self.supported_values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def supported_operators(self,) -> Optional[List[assignment_filter_operator.AssignmentFilterOperator]]:
        """
        Gets the supportedOperators property value. List of all supported operators on this property.
        Returns: Optional[List[assignment_filter_operator.AssignmentFilterOperator]]
        """
        return self._supported_operators
    
    @supported_operators.setter
    def supported_operators(self,value: Optional[List[assignment_filter_operator.AssignmentFilterOperator]] = None) -> None:
        """
        Sets the supportedOperators property value. List of all supported operators on this property.
        Args:
            value: Value to set for the supportedOperators property.
        """
        self._supported_operators = value
    
    @property
    def supported_values(self,) -> Optional[List[str]]:
        """
        Gets the supportedValues property value. List of all supported values for this propery, empty if everything is supported.
        Returns: Optional[List[str]]
        """
        return self._supported_values
    
    @supported_values.setter
    def supported_values(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedValues property value. List of all supported values for this propery, empty if everything is supported.
        Args:
            value: Value to set for the supportedValues property.
        """
        self._supported_values = value
    

