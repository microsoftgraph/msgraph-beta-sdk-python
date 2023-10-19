from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .property_to_evaluate import PropertyToEvaluate

@dataclass
class ExpressionEvaluationDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents expression which has been evaluated.
    expression: Optional[str] = None
    # Represents the details of the evaluation of the expression.
    expression_evaluation_details: Optional[List[ExpressionEvaluationDetails]] = None
    # Represents the value of the result of the current expression.
    expression_result: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the name of the property and the value of that property.
    property_to_evaluate: Optional[PropertyToEvaluate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpressionEvaluationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExpressionEvaluationDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExpressionEvaluationDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .property_to_evaluate import PropertyToEvaluate

        from .property_to_evaluate import PropertyToEvaluate

        fields: Dict[str, Callable[[Any], None]] = {
            "expression": lambda n : setattr(self, 'expression', n.get_str_value()),
            "expressionEvaluationDetails": lambda n : setattr(self, 'expression_evaluation_details', n.get_collection_of_object_values(ExpressionEvaluationDetails)),
            "expressionResult": lambda n : setattr(self, 'expression_result', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propertyToEvaluate": lambda n : setattr(self, 'property_to_evaluate', n.get_object_value(PropertyToEvaluate)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("expression", self.expression)
        writer.write_collection_of_object_values("expressionEvaluationDetails", self.expression_evaluation_details)
        writer.write_bool_value("expressionResult", self.expression_result)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("propertyToEvaluate", self.property_to_evaluate)
        writer.write_additional_data_value(self.additional_data)
    

