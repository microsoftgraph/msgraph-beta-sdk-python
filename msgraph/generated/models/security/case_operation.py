from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import case_action, case_operation_status, ediscovery_add_to_review_set_operation, ediscovery_estimate_operation, ediscovery_export_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_purge_data_operation, ediscovery_tag_operation
    from .. import entity, identity_set, result_info

from .. import entity

class CaseOperation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new caseOperation and sets the default values.
        """
        super().__init__()
        # The type of action the operation represents. Possible values are: addToReviewSet,applyTags,contentExport,convertToPdf,estimateStatistics, purgeData
        self._action: Optional[case_action.CaseAction] = None
        # The date and time the operation was completed.
        self._completed_date_time: Optional[datetime] = None
        # The user that created the operation.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The date and time the operation was created.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The progress of the operation.
        self._percent_progress: Optional[int] = None
        # Contains success and failure-specific result information.
        self._result_info: Optional[result_info.ResultInfo] = None
        # The status of the case operation. Possible values are: notStarted, submissionFailed, running, succeeded, partiallySucceeded, failed.
        self._status: Optional[case_operation_status.CaseOperationStatus] = None
    
    @property
    def action(self,) -> Optional[case_action.CaseAction]:
        """
        Gets the action property value. The type of action the operation represents. Possible values are: addToReviewSet,applyTags,contentExport,convertToPdf,estimateStatistics, purgeData
        Returns: Optional[case_action.CaseAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[case_action.CaseAction] = None) -> None:
        """
        Sets the action property value. The type of action the operation represents. Possible values are: addToReviewSet,applyTags,contentExport,convertToPdf,estimateStatistics, purgeData
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The date and time the operation was completed.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The date and time the operation was completed.
        Args:
            value: Value to set for the completed_date_time property.
        """
        self._completed_date_time = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user that created the operation.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user that created the operation.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the operation was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the operation was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
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
            if mapping_value == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation":
                from . import ediscovery_add_to_review_set_operation

                return ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryEstimateOperation":
                from . import ediscovery_estimate_operation

                return ediscovery_estimate_operation.EdiscoveryEstimateOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryExportOperation":
                from . import ediscovery_export_operation

                return ediscovery_export_operation.EdiscoveryExportOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryHoldOperation":
                from . import ediscovery_hold_operation

                return ediscovery_hold_operation.EdiscoveryHoldOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryIndexOperation":
                from . import ediscovery_index_operation

                return ediscovery_index_operation.EdiscoveryIndexOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryPurgeDataOperation":
                from . import ediscovery_purge_data_operation

                return ediscovery_purge_data_operation.EdiscoveryPurgeDataOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryTagOperation":
                from . import ediscovery_tag_operation

                return ediscovery_tag_operation.EdiscoveryTagOperation()
        return CaseOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import case_action, case_operation_status, ediscovery_add_to_review_set_operation, ediscovery_estimate_operation, ediscovery_export_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_purge_data_operation, ediscovery_tag_operation
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
    
    @property
    def percent_progress(self,) -> Optional[int]:
        """
        Gets the percentProgress property value. The progress of the operation.
        Returns: Optional[int]
        """
        return self._percent_progress
    
    @percent_progress.setter
    def percent_progress(self,value: Optional[int] = None) -> None:
        """
        Sets the percentProgress property value. The progress of the operation.
        Args:
            value: Value to set for the percent_progress property.
        """
        self._percent_progress = value
    
    @property
    def result_info(self,) -> Optional[result_info.ResultInfo]:
        """
        Gets the resultInfo property value. Contains success and failure-specific result information.
        Returns: Optional[result_info.ResultInfo]
        """
        return self._result_info
    
    @result_info.setter
    def result_info(self,value: Optional[result_info.ResultInfo] = None) -> None:
        """
        Sets the resultInfo property value. Contains success and failure-specific result information.
        Args:
            value: Value to set for the result_info property.
        """
        self._result_info = value
    
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
    
    @property
    def status(self,) -> Optional[case_operation_status.CaseOperationStatus]:
        """
        Gets the status property value. The status of the case operation. Possible values are: notStarted, submissionFailed, running, succeeded, partiallySucceeded, failed.
        Returns: Optional[case_operation_status.CaseOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[case_operation_status.CaseOperationStatus] = None) -> None:
        """
        Sets the status property value. The status of the case operation. Possible values are: notStarted, submissionFailed, running, succeeded, partiallySucceeded, failed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

