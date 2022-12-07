from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_filter_evaluate_request = lazy_import('msgraph.generated.models.assignment_filter_evaluate_request')

class EvaluateAssignmentFilterPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the evaluateAssignmentFilter method.
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
        Instantiates a new evaluateAssignmentFilterPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The data property
        self._data: Optional[assignment_filter_evaluate_request.AssignmentFilterEvaluateRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateAssignmentFilterPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateAssignmentFilterPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateAssignmentFilterPostRequestBody()
    
    @property
    def data(self,) -> Optional[assignment_filter_evaluate_request.AssignmentFilterEvaluateRequest]:
        """
        Gets the data property value. The data property
        Returns: Optional[assignment_filter_evaluate_request.AssignmentFilterEvaluateRequest]
        """
        return self._data
    
    @data.setter
    def data(self,value: Optional[assignment_filter_evaluate_request.AssignmentFilterEvaluateRequest] = None) -> None:
        """
        Sets the data property value. The data property
        Args:
            value: Value to set for the data property.
        """
        self._data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(assignment_filter_evaluate_request.AssignmentFilterEvaluateRequest)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("data", self.data)
        writer.write_additional_data_value(self.additional_data)
    

