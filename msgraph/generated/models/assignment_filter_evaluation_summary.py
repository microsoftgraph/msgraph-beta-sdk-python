from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_filter_evaluation_result = lazy_import('msgraph.generated.models.assignment_filter_evaluation_result')
assignment_filter_type_and_evaluation_result = lazy_import('msgraph.generated.models.assignment_filter_type_and_evaluation_result')
device_and_app_management_assignment_filter_type = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter_type')
device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')

class AssignmentFilterEvaluationSummary(AdditionalDataHolder, Parsable):
    """
    Represent result summary for assignment filter evaluation
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
    def assignment_filter_display_name(self,) -> Optional[str]:
        """
        Gets the assignmentFilterDisplayName property value. The admin defined name for assignment filter.
        Returns: Optional[str]
        """
        return self._assignment_filter_display_name
    
    @assignment_filter_display_name.setter
    def assignment_filter_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentFilterDisplayName property value. The admin defined name for assignment filter.
        Args:
            value: Value to set for the assignmentFilterDisplayName property.
        """
        self._assignment_filter_display_name = value
    
    @property
    def assignment_filter_id(self,) -> Optional[str]:
        """
        Gets the assignmentFilterId property value. Unique identifier for the assignment filter object
        Returns: Optional[str]
        """
        return self._assignment_filter_id
    
    @assignment_filter_id.setter
    def assignment_filter_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentFilterId property value. Unique identifier for the assignment filter object
        Args:
            value: Value to set for the assignmentFilterId property.
        """
        self._assignment_filter_id = value
    
    @property
    def assignment_filter_last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignmentFilterLastModifiedDateTime property value. The time the assignment filter was last modified.
        Returns: Optional[datetime]
        """
        return self._assignment_filter_last_modified_date_time
    
    @assignment_filter_last_modified_date_time.setter
    def assignment_filter_last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignmentFilterLastModifiedDateTime property value. The time the assignment filter was last modified.
        Args:
            value: Value to set for the assignmentFilterLastModifiedDateTime property.
        """
        self._assignment_filter_last_modified_date_time = value
    
    @property
    def assignment_filter_platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the assignmentFilterPlatform property value. Supported platform types.
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._assignment_filter_platform
    
    @assignment_filter_platform.setter
    def assignment_filter_platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the assignmentFilterPlatform property value. Supported platform types.
        Args:
            value: Value to set for the assignmentFilterPlatform property.
        """
        self._assignment_filter_platform = value
    
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
    
    @property
    def assignment_filter_type_and_evaluation_results(self,) -> Optional[List[assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult]]:
        """
        Gets the assignmentFilterTypeAndEvaluationResults property value. A collection of filter types and their corresponding evaluation results.
        Returns: Optional[List[assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult]]
        """
        return self._assignment_filter_type_and_evaluation_results
    
    @assignment_filter_type_and_evaluation_results.setter
    def assignment_filter_type_and_evaluation_results(self,value: Optional[List[assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult]] = None) -> None:
        """
        Sets the assignmentFilterTypeAndEvaluationResults property value. A collection of filter types and their corresponding evaluation results.
        Args:
            value: Value to set for the assignmentFilterTypeAndEvaluationResults property.
        """
        self._assignment_filter_type_and_evaluation_results = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignmentFilterEvaluationSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The admin defined name for assignment filter.
        self._assignment_filter_display_name: Optional[str] = None
        # Unique identifier for the assignment filter object
        self._assignment_filter_id: Optional[str] = None
        # The time the assignment filter was last modified.
        self._assignment_filter_last_modified_date_time: Optional[datetime] = None
        # Supported platform types.
        self._assignment_filter_platform: Optional[device_platform_type.DevicePlatformType] = None
        # Represents type of the assignment filter.
        self._assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
        # A collection of filter types and their corresponding evaluation results.
        self._assignment_filter_type_and_evaluation_results: Optional[List[assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult]] = None
        # The time assignment filter was evaluated.
        self._evaluation_date_time: Optional[datetime] = None
        # Supported evaluation results for filter.
        self._evaluation_result: Optional[assignment_filter_evaluation_result.AssignmentFilterEvaluationResult] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterEvaluationSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterEvaluationSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentFilterEvaluationSummary()
    
    @property
    def evaluation_date_time(self,) -> Optional[datetime]:
        """
        Gets the evaluationDateTime property value. The time assignment filter was evaluated.
        Returns: Optional[datetime]
        """
        return self._evaluation_date_time
    
    @evaluation_date_time.setter
    def evaluation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the evaluationDateTime property value. The time assignment filter was evaluated.
        Args:
            value: Value to set for the evaluationDateTime property.
        """
        self._evaluation_date_time = value
    
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
            "assignment_filter_display_name": lambda n : setattr(self, 'assignment_filter_display_name', n.get_str_value()),
            "assignment_filter_id": lambda n : setattr(self, 'assignment_filter_id', n.get_str_value()),
            "assignment_filter_last_modified_date_time": lambda n : setattr(self, 'assignment_filter_last_modified_date_time', n.get_datetime_value()),
            "assignment_filter_platform": lambda n : setattr(self, 'assignment_filter_platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "assignment_filter_type": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "assignment_filter_type_and_evaluation_results": lambda n : setattr(self, 'assignment_filter_type_and_evaluation_results', n.get_collection_of_object_values(assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult)),
            "evaluation_date_time": lambda n : setattr(self, 'evaluation_date_time', n.get_datetime_value()),
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
        writer.write_str_value("assignmentFilterDisplayName", self.assignment_filter_display_name)
        writer.write_str_value("assignmentFilterId", self.assignment_filter_id)
        writer.write_datetime_value("assignmentFilterLastModifiedDateTime", self.assignment_filter_last_modified_date_time)
        writer.write_enum_value("assignmentFilterPlatform", self.assignment_filter_platform)
        writer.write_enum_value("assignmentFilterType", self.assignment_filter_type)
        writer.write_collection_of_object_values("assignmentFilterTypeAndEvaluationResults", self.assignment_filter_type_and_evaluation_results)
        writer.write_datetime_value("evaluationDateTime", self.evaluation_date_time)
        writer.write_enum_value("evaluationResult", self.evaluation_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

