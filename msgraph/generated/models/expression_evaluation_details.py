from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

property_to_evaluate = lazy_import('msgraph.generated.models.property_to_evaluate')

class ExpressionEvaluationDetails(AdditionalDataHolder, Parsable):
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
        Instantiates a new expressionEvaluationDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents expression which has been evaluated.
        self._expression: Optional[str] = None
        # Represents the details of the evaluation of the expression.
        self._expression_evaluation_details: Optional[List[ExpressionEvaluationDetails]] = None
        # Represents the value of the result of the current expression.
        self._expression_result: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines the name of the property and the value of that property.
        self._property_to_evaluate: Optional[property_to_evaluate.PropertyToEvaluate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpressionEvaluationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExpressionEvaluationDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExpressionEvaluationDetails()
    
    @property
    def expression(self,) -> Optional[str]:
        """
        Gets the expression property value. Represents expression which has been evaluated.
        Returns: Optional[str]
        """
        return self._expression
    
    @expression.setter
    def expression(self,value: Optional[str] = None) -> None:
        """
        Sets the expression property value. Represents expression which has been evaluated.
        Args:
            value: Value to set for the expression property.
        """
        self._expression = value
    
    @property
    def expression_evaluation_details(self,) -> Optional[List[ExpressionEvaluationDetails]]:
        """
        Gets the expressionEvaluationDetails property value. Represents the details of the evaluation of the expression.
        Returns: Optional[List[ExpressionEvaluationDetails]]
        """
        return self._expression_evaluation_details
    
    @expression_evaluation_details.setter
    def expression_evaluation_details(self,value: Optional[List[ExpressionEvaluationDetails]] = None) -> None:
        """
        Sets the expressionEvaluationDetails property value. Represents the details of the evaluation of the expression.
        Args:
            value: Value to set for the expressionEvaluationDetails property.
        """
        self._expression_evaluation_details = value
    
    @property
    def expression_result(self,) -> Optional[bool]:
        """
        Gets the expressionResult property value. Represents the value of the result of the current expression.
        Returns: Optional[bool]
        """
        return self._expression_result
    
    @expression_result.setter
    def expression_result(self,value: Optional[bool] = None) -> None:
        """
        Sets the expressionResult property value. Represents the value of the result of the current expression.
        Args:
            value: Value to set for the expressionResult property.
        """
        self._expression_result = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expression": lambda n : setattr(self, 'expression', n.get_str_value()),
            "expression_evaluation_details": lambda n : setattr(self, 'expression_evaluation_details', n.get_collection_of_object_values(ExpressionEvaluationDetails)),
            "expression_result": lambda n : setattr(self, 'expression_result', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "property_to_evaluate": lambda n : setattr(self, 'property_to_evaluate', n.get_object_value(property_to_evaluate.PropertyToEvaluate)),
        }
        return fields
    
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
    def property_to_evaluate(self,) -> Optional[property_to_evaluate.PropertyToEvaluate]:
        """
        Gets the propertyToEvaluate property value. Defines the name of the property and the value of that property.
        Returns: Optional[property_to_evaluate.PropertyToEvaluate]
        """
        return self._property_to_evaluate
    
    @property_to_evaluate.setter
    def property_to_evaluate(self,value: Optional[property_to_evaluate.PropertyToEvaluate] = None) -> None:
        """
        Sets the propertyToEvaluate property value. Defines the name of the property and the value of that property.
        Args:
            value: Value to set for the propertyToEvaluate property.
        """
        self._property_to_evaluate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("expression", self.expression)
        writer.write_collection_of_object_values("expressionEvaluationDetails", self.expression_evaluation_details)
        writer.write_bool_value("expressionResult", self.expression_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("propertyToEvaluate", self.property_to_evaluate)
        writer.write_additional_data_value(self.additional_data)
    

