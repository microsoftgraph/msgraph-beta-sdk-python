from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import string_key_long_value_pair, synchronization_progress, synchronization_quarantine, synchronization_status_code, synchronization_task_execution

@dataclass
class SynchronizationStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The code property
    code: Optional[synchronization_status_code.SynchronizationStatusCode] = None
    # Number of consecutive times this job failed.
    count_successive_complete_failures: Optional[int] = None
    # true if the job's escrows (object-level errors) were pruned during initial synchronization. Escrows can be pruned if during the initial synchronization, you reach the threshold of errors that would normally put the job in quarantine. Instead of going into quarantine, the synchronization process clears the job's errors and continues until the initial synchronization is completed. When the initial synchronization is completed, the job will pause and wait for the customer to clean up the errors.
    escrows_pruned: Optional[bool] = None
    # Details of the last execution of the job.
    last_execution: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None
    # Details of the last execution of this job, which didn't have any errors.
    last_successful_execution: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None
    # Details of the last execution of the job, which exported objects into the target directory.
    last_successful_execution_with_exports: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Details of the progress of a job toward completion.
    progress: Optional[List[synchronization_progress.SynchronizationProgress]] = None
    # If job is in quarantine, quarantine details.
    quarantine: Optional[synchronization_quarantine.SynchronizationQuarantine] = None
    # The time when steady state (no more changes to the process) was first achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    steady_state_first_achieved_time: Optional[datetime] = None
    # The time when steady state (no more changes to the process) was last achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    steady_state_last_achieved_time: Optional[datetime] = None
    # Count of synchronized objects, listed by object type.
    synchronized_entry_count_by_type: Optional[List[string_key_long_value_pair.StringKeyLongValuePair]] = None
    # In the event of an error, the URL with the troubleshooting steps for the issue.
    troubleshooting_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import string_key_long_value_pair, synchronization_progress, synchronization_quarantine, synchronization_status_code, synchronization_task_execution

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(synchronization_status_code.SynchronizationStatusCode)),
            "countSuccessiveCompleteFailures": lambda n : setattr(self, 'count_successive_complete_failures', n.get_int_value()),
            "escrowsPruned": lambda n : setattr(self, 'escrows_pruned', n.get_bool_value()),
            "lastExecution": lambda n : setattr(self, 'last_execution', n.get_object_value(synchronization_task_execution.SynchronizationTaskExecution)),
            "lastSuccessfulExecution": lambda n : setattr(self, 'last_successful_execution', n.get_object_value(synchronization_task_execution.SynchronizationTaskExecution)),
            "lastSuccessfulExecutionWithExports": lambda n : setattr(self, 'last_successful_execution_with_exports', n.get_object_value(synchronization_task_execution.SynchronizationTaskExecution)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_collection_of_object_values(synchronization_progress.SynchronizationProgress)),
            "quarantine": lambda n : setattr(self, 'quarantine', n.get_object_value(synchronization_quarantine.SynchronizationQuarantine)),
            "steadyStateFirstAchievedTime": lambda n : setattr(self, 'steady_state_first_achieved_time', n.get_datetime_value()),
            "steadyStateLastAchievedTime": lambda n : setattr(self, 'steady_state_last_achieved_time', n.get_datetime_value()),
            "synchronizedEntryCountByType": lambda n : setattr(self, 'synchronized_entry_count_by_type', n.get_collection_of_object_values(string_key_long_value_pair.StringKeyLongValuePair)),
            "troubleshootingUrl": lambda n : setattr(self, 'troubleshooting_url', n.get_str_value()),
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
        writer.write_enum_value("code", self.code)
        writer.write_int_value("countSuccessiveCompleteFailures", self.count_successive_complete_failures)
        writer.write_bool_value("escrowsPruned", self.escrows_pruned)
        writer.write_object_value("lastExecution", self.last_execution)
        writer.write_object_value("lastSuccessfulExecution", self.last_successful_execution)
        writer.write_object_value("lastSuccessfulExecutionWithExports", self.last_successful_execution_with_exports)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("progress", self.progress)
        writer.write_object_value("quarantine", self.quarantine)
        writer.write_datetime_value("steadyStateFirstAchievedTime", self.steady_state_first_achieved_time)
        writer.write_datetime_value("steadyStateLastAchievedTime", self.steady_state_last_achieved_time)
        writer.write_collection_of_object_values("synchronizedEntryCountByType", self.synchronized_entry_count_by_type)
        writer.write_str_value("troubleshootingUrl", self.troubleshooting_url)
        writer.write_additional_data_value(self.additional_data)
    

