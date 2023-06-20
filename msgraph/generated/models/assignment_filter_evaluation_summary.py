from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assignment_filter_evaluation_result, assignment_filter_type_and_evaluation_result, device_and_app_management_assignment_filter_type, device_platform_type

@dataclass
class AssignmentFilterEvaluationSummary(AdditionalDataHolder, Parsable):
    """
    Represent result summary for assignment filter evaluation
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The admin defined name for assignment filter.
    assignment_filter_display_name: Optional[str] = None
    # Unique identifier for the assignment filter object
    assignment_filter_id: Optional[str] = None
    # The time the assignment filter was last modified.
    assignment_filter_last_modified_date_time: Optional[datetime] = None
    # Supported platform types.
    assignment_filter_platform: Optional[device_platform_type.DevicePlatformType] = None
    # Represents type of the assignment filter.
    assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
    # A collection of filter types and their corresponding evaluation results.
    assignment_filter_type_and_evaluation_results: Optional[List[assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult]] = None
    # The time assignment filter was evaluated.
    evaluation_date_time: Optional[datetime] = None
    # Supported evaluation results for filter.
    evaluation_result: Optional[assignment_filter_evaluation_result.AssignmentFilterEvaluationResult] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterEvaluationSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterEvaluationSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignmentFilterEvaluationSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assignment_filter_evaluation_result, assignment_filter_type_and_evaluation_result, device_and_app_management_assignment_filter_type, device_platform_type

        from . import assignment_filter_evaluation_result, assignment_filter_type_and_evaluation_result, device_and_app_management_assignment_filter_type, device_platform_type

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentFilterDisplayName": lambda n : setattr(self, 'assignment_filter_display_name', n.get_str_value()),
            "assignmentFilterId": lambda n : setattr(self, 'assignment_filter_id', n.get_str_value()),
            "assignmentFilterLastModifiedDateTime": lambda n : setattr(self, 'assignment_filter_last_modified_date_time', n.get_datetime_value()),
            "assignmentFilterPlatform": lambda n : setattr(self, 'assignment_filter_platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "assignmentFilterType": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "assignmentFilterTypeAndEvaluationResults": lambda n : setattr(self, 'assignment_filter_type_and_evaluation_results', n.get_collection_of_object_values(assignment_filter_type_and_evaluation_result.AssignmentFilterTypeAndEvaluationResult)),
            "evaluationDateTime": lambda n : setattr(self, 'evaluation_date_time', n.get_datetime_value()),
            "evaluationResult": lambda n : setattr(self, 'evaluation_result', n.get_enum_value(assignment_filter_evaluation_result.AssignmentFilterEvaluationResult)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
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
    

