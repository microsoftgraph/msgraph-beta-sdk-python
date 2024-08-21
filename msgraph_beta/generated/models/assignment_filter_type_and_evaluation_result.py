from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_filter_evaluation_result import AssignmentFilterEvaluationResult
    from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

@dataclass
class AssignmentFilterTypeAndEvaluationResult(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents the filter type and evalaution result of the filter.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents type of the assignment filter.
    assignment_filter_type: Optional[DeviceAndAppManagementAssignmentFilterType] = None
    # Supported evaluation results for filter.
    evaluation_result: Optional[AssignmentFilterEvaluationResult] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentFilterTypeAndEvaluationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterTypeAndEvaluationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentFilterTypeAndEvaluationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_filter_evaluation_result import AssignmentFilterEvaluationResult
        from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

        from .assignment_filter_evaluation_result import AssignmentFilterEvaluationResult
        from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentFilterType": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(DeviceAndAppManagementAssignmentFilterType)),
            "evaluationResult": lambda n : setattr(self, 'evaluation_result', n.get_enum_value(AssignmentFilterEvaluationResult)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("assignmentFilterType", self.assignment_filter_type)
        writer.write_enum_value("evaluationResult", self.evaluation_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

