from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_filter_evaluation_result = lazy_import('msgraph.generated.models.assignment_filter_evaluation_result')
device_and_app_management_assignment_filter_type = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter_type')

class AssignmentFilterTypeAndEvaluationResult(AdditionalDataHolder, Parsable):
    """
    Represents the filter type and evalaution result of the filter.
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
    
    @property
    def assignment_filter_type(self,) -> Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]:
        """
        Gets the assignmentFilterType property value. Represents type of the assignment filter.
        Returns: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]
        """
        return self._assignment_filter_type
    
    @assignment_filter_type.setter
    def assignment_filter_type(self,value: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None) -> None:
        """
        Sets the assignmentFilterType property value. Represents type of the assignment filter.
        Args:
            value: Value to set for the assignmentFilterType property.
        """
        self._assignment_filter_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignmentFilterTypeAndEvaluationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents type of the assignment filter.
        self._assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
        # Supported evaluation results for filter.
        self._evaluation_result: Optional[assignment_filter_evaluation_result.AssignmentFilterEvaluationResult] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterTypeAndEvaluationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterTypeAndEvaluationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentFilterTypeAndEvaluationResult()
    
    @property
    def evaluation_result(self,) -> Optional[assignment_filter_evaluation_result.AssignmentFilterEvaluationResult]:
        """
        Gets the evaluationResult property value. Supported evaluation results for filter.
        Returns: Optional[assignment_filter_evaluation_result.AssignmentFilterEvaluationResult]
        """
        return self._evaluation_result
    
    @evaluation_result.setter
    def evaluation_result(self,value: Optional[assignment_filter_evaluation_result.AssignmentFilterEvaluationResult] = None) -> None:
        """
        Sets the evaluationResult property value. Supported evaluation results for filter.
        Args:
            value: Value to set for the evaluationResult property.
        """
        self._evaluation_result = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_filter_type": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "evaluation_result": lambda n : setattr(self, 'evaluation_result', n.get_enum_value(assignment_filter_evaluation_result.AssignmentFilterEvaluationResult)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("assignmentFilterType", self.assignment_filter_type)
        writer.write_enum_value("evaluationResult", self.evaluation_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

