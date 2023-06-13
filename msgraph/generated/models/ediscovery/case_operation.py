from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_to_review_set_operation, case_action, case_export_operation, case_hold_operation, case_index_operation, case_operation_status, estimate_statistics_operation, purge_data_operation, tag_operation
    from .. import entity, identity_set, result_info

from .. import entity

@dataclass
class CaseOperation(entity.Entity):
    # The type of action the operation represents. Possible values are: addToReviewSet,applyTags,contentExport,convertToPdf,estimateStatistics, purgeData
    action: Optional[case_action.CaseAction] = None
    # The date and time the operation was completed.
    completed_date_time: Optional[datetime] = None
    # The user that created the operation.
    created_by: Optional[identity_set.IdentitySet] = None
    # The date and time the operation was created.
    created_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The progress of the operation.
    percent_progress: Optional[int] = None
    # Contains success and failure-specific result information.
    result_info: Optional[result_info.ResultInfo] = None
    # The status of the case operation. Possible values are: notStarted, submissionFailed, running, succeeded, partiallySucceeded, failed.
    status: Optional[case_operation_status.CaseOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CaseOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CaseOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.ediscovery.addToReviewSetOperation":
                from . import add_to_review_set_operation

                return add_to_review_set_operation.AddToReviewSetOperation()
            if mapping_value == "#microsoft.graph.ediscovery.caseExportOperation":
                from . import case_export_operation

                return case_export_operation.CaseExportOperation()
            if mapping_value == "#microsoft.graph.ediscovery.caseHoldOperation":
                from . import case_hold_operation

                return case_hold_operation.CaseHoldOperation()
            if mapping_value == "#microsoft.graph.ediscovery.caseIndexOperation":
                from . import case_index_operation

                return case_index_operation.CaseIndexOperation()
            if mapping_value == "#microsoft.graph.ediscovery.estimateStatisticsOperation":
                from . import estimate_statistics_operation

                return estimate_statistics_operation.EstimateStatisticsOperation()
            if mapping_value == "#microsoft.graph.ediscovery.purgeDataOperation":
                from . import purge_data_operation

                return purge_data_operation.PurgeDataOperation()
            if mapping_value == "#microsoft.graph.ediscovery.tagOperation":
                from . import tag_operation

                return tag_operation.TagOperation()
        return CaseOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_to_review_set_operation, case_action, case_export_operation, case_hold_operation, case_index_operation, case_operation_status, estimate_statistics_operation, purge_data_operation, tag_operation
        from .. import entity, identity_set, result_info

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(case_action.CaseAction)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "percentProgress": lambda n : setattr(self, 'percent_progress', n.get_int_value()),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(result_info.ResultInfo)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(case_operation_status.CaseOperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("percentProgress", self.percent_progress)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_enum_value("status", self.status)
    

