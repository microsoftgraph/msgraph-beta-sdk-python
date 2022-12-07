from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

string_key_long_value_pair = lazy_import('msgraph.generated.models.string_key_long_value_pair')
synchronization_progress = lazy_import('msgraph.generated.models.synchronization_progress')
synchronization_quarantine = lazy_import('msgraph.generated.models.synchronization_quarantine')
synchronization_status_code = lazy_import('msgraph.generated.models.synchronization_status_code')
synchronization_task_execution = lazy_import('msgraph.generated.models.synchronization_task_execution')

class SynchronizationStatus(AdditionalDataHolder, Parsable):
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
    def code(self,) -> Optional[synchronization_status_code.SynchronizationStatusCode]:
        """
        Gets the code property value. The code property
        Returns: Optional[synchronization_status_code.SynchronizationStatusCode]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[synchronization_status_code.SynchronizationStatusCode] = None) -> None:
        """
        Sets the code property value. The code property
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The code property
        self._code: Optional[synchronization_status_code.SynchronizationStatusCode] = None
        # Number of consecutive times this job failed.
        self._count_successive_complete_failures: Optional[int] = None
        # true if the job's escrows (object-level errors) were pruned during initial synchronization. Escrows can be pruned if during the initial synchronization, you reach the threshold of errors that would normally put the job in quarantine. Instead of going into quarantine, the synchronization process clears the job's errors and continues until the initial synchronization is completed. When the initial synchronization is completed, the job will pause and wait for the customer to clean up the errors.
        self._escrows_pruned: Optional[bool] = None
        # Details of the last execution of the job.
        self._last_execution: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None
        # Details of the last execution of this job, which didn't have any errors.
        self._last_successful_execution: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None
        # Details of the last execution of the job, which exported objects into the target directory.
        self._last_successful_execution_with_exports: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Details of the progress of a job toward completion.
        self._progress: Optional[List[synchronization_progress.SynchronizationProgress]] = None
        # If job is in quarantine, quarantine details.
        self._quarantine: Optional[synchronization_quarantine.SynchronizationQuarantine] = None
        # The time when steady state (no more changes to the process) was first achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._steady_state_first_achieved_time: Optional[datetime] = None
        # The time when steady state (no more changes to the process) was last achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._steady_state_last_achieved_time: Optional[datetime] = None
        # Count of synchronized objects, listed by object type.
        self._synchronized_entry_count_by_type: Optional[List[string_key_long_value_pair.StringKeyLongValuePair]] = None
        # In the event of an error, the URL with the troubleshooting steps for the issue.
        self._troubleshooting_url: Optional[str] = None
    
    @property
    def count_successive_complete_failures(self,) -> Optional[int]:
        """
        Gets the countSuccessiveCompleteFailures property value. Number of consecutive times this job failed.
        Returns: Optional[int]
        """
        return self._count_successive_complete_failures
    
    @count_successive_complete_failures.setter
    def count_successive_complete_failures(self,value: Optional[int] = None) -> None:
        """
        Sets the countSuccessiveCompleteFailures property value. Number of consecutive times this job failed.
        Args:
            value: Value to set for the countSuccessiveCompleteFailures property.
        """
        self._count_successive_complete_failures = value
    
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
    
    @property
    def escrows_pruned(self,) -> Optional[bool]:
        """
        Gets the escrowsPruned property value. true if the job's escrows (object-level errors) were pruned during initial synchronization. Escrows can be pruned if during the initial synchronization, you reach the threshold of errors that would normally put the job in quarantine. Instead of going into quarantine, the synchronization process clears the job's errors and continues until the initial synchronization is completed. When the initial synchronization is completed, the job will pause and wait for the customer to clean up the errors.
        Returns: Optional[bool]
        """
        return self._escrows_pruned
    
    @escrows_pruned.setter
    def escrows_pruned(self,value: Optional[bool] = None) -> None:
        """
        Sets the escrowsPruned property value. true if the job's escrows (object-level errors) were pruned during initial synchronization. Escrows can be pruned if during the initial synchronization, you reach the threshold of errors that would normally put the job in quarantine. Instead of going into quarantine, the synchronization process clears the job's errors and continues until the initial synchronization is completed. When the initial synchronization is completed, the job will pause and wait for the customer to clean up the errors.
        Args:
            value: Value to set for the escrowsPruned property.
        """
        self._escrows_pruned = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(synchronization_status_code.SynchronizationStatusCode)),
            "count_successive_complete_failures": lambda n : setattr(self, 'count_successive_complete_failures', n.get_int_value()),
            "escrows_pruned": lambda n : setattr(self, 'escrows_pruned', n.get_bool_value()),
            "last_execution": lambda n : setattr(self, 'last_execution', n.get_object_value(synchronization_task_execution.SynchronizationTaskExecution)),
            "last_successful_execution": lambda n : setattr(self, 'last_successful_execution', n.get_object_value(synchronization_task_execution.SynchronizationTaskExecution)),
            "last_successful_execution_with_exports": lambda n : setattr(self, 'last_successful_execution_with_exports', n.get_object_value(synchronization_task_execution.SynchronizationTaskExecution)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_collection_of_object_values(synchronization_progress.SynchronizationProgress)),
            "quarantine": lambda n : setattr(self, 'quarantine', n.get_object_value(synchronization_quarantine.SynchronizationQuarantine)),
            "steady_state_first_achieved_time": lambda n : setattr(self, 'steady_state_first_achieved_time', n.get_datetime_value()),
            "steady_state_last_achieved_time": lambda n : setattr(self, 'steady_state_last_achieved_time', n.get_datetime_value()),
            "synchronized_entry_count_by_type": lambda n : setattr(self, 'synchronized_entry_count_by_type', n.get_collection_of_object_values(string_key_long_value_pair.StringKeyLongValuePair)),
            "troubleshooting_url": lambda n : setattr(self, 'troubleshooting_url', n.get_str_value()),
        }
        return fields
    
    @property
    def last_execution(self,) -> Optional[synchronization_task_execution.SynchronizationTaskExecution]:
        """
        Gets the lastExecution property value. Details of the last execution of the job.
        Returns: Optional[synchronization_task_execution.SynchronizationTaskExecution]
        """
        return self._last_execution
    
    @last_execution.setter
    def last_execution(self,value: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None) -> None:
        """
        Sets the lastExecution property value. Details of the last execution of the job.
        Args:
            value: Value to set for the lastExecution property.
        """
        self._last_execution = value
    
    @property
    def last_successful_execution(self,) -> Optional[synchronization_task_execution.SynchronizationTaskExecution]:
        """
        Gets the lastSuccessfulExecution property value. Details of the last execution of this job, which didn't have any errors.
        Returns: Optional[synchronization_task_execution.SynchronizationTaskExecution]
        """
        return self._last_successful_execution
    
    @last_successful_execution.setter
    def last_successful_execution(self,value: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None) -> None:
        """
        Sets the lastSuccessfulExecution property value. Details of the last execution of this job, which didn't have any errors.
        Args:
            value: Value to set for the lastSuccessfulExecution property.
        """
        self._last_successful_execution = value
    
    @property
    def last_successful_execution_with_exports(self,) -> Optional[synchronization_task_execution.SynchronizationTaskExecution]:
        """
        Gets the lastSuccessfulExecutionWithExports property value. Details of the last execution of the job, which exported objects into the target directory.
        Returns: Optional[synchronization_task_execution.SynchronizationTaskExecution]
        """
        return self._last_successful_execution_with_exports
    
    @last_successful_execution_with_exports.setter
    def last_successful_execution_with_exports(self,value: Optional[synchronization_task_execution.SynchronizationTaskExecution] = None) -> None:
        """
        Sets the lastSuccessfulExecutionWithExports property value. Details of the last execution of the job, which exported objects into the target directory.
        Args:
            value: Value to set for the lastSuccessfulExecutionWithExports property.
        """
        self._last_successful_execution_with_exports = value
    
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
    def progress(self,) -> Optional[List[synchronization_progress.SynchronizationProgress]]:
        """
        Gets the progress property value. Details of the progress of a job toward completion.
        Returns: Optional[List[synchronization_progress.SynchronizationProgress]]
        """
        return self._progress
    
    @progress.setter
    def progress(self,value: Optional[List[synchronization_progress.SynchronizationProgress]] = None) -> None:
        """
        Sets the progress property value. Details of the progress of a job toward completion.
        Args:
            value: Value to set for the progress property.
        """
        self._progress = value
    
    @property
    def quarantine(self,) -> Optional[synchronization_quarantine.SynchronizationQuarantine]:
        """
        Gets the quarantine property value. If job is in quarantine, quarantine details.
        Returns: Optional[synchronization_quarantine.SynchronizationQuarantine]
        """
        return self._quarantine
    
    @quarantine.setter
    def quarantine(self,value: Optional[synchronization_quarantine.SynchronizationQuarantine] = None) -> None:
        """
        Sets the quarantine property value. If job is in quarantine, quarantine details.
        Args:
            value: Value to set for the quarantine property.
        """
        self._quarantine = value
    
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
    
    @property
    def steady_state_first_achieved_time(self,) -> Optional[datetime]:
        """
        Gets the steadyStateFirstAchievedTime property value. The time when steady state (no more changes to the process) was first achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._steady_state_first_achieved_time
    
    @steady_state_first_achieved_time.setter
    def steady_state_first_achieved_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the steadyStateFirstAchievedTime property value. The time when steady state (no more changes to the process) was first achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the steadyStateFirstAchievedTime property.
        """
        self._steady_state_first_achieved_time = value
    
    @property
    def steady_state_last_achieved_time(self,) -> Optional[datetime]:
        """
        Gets the steadyStateLastAchievedTime property value. The time when steady state (no more changes to the process) was last achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._steady_state_last_achieved_time
    
    @steady_state_last_achieved_time.setter
    def steady_state_last_achieved_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the steadyStateLastAchievedTime property value. The time when steady state (no more changes to the process) was last achieved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the steadyStateLastAchievedTime property.
        """
        self._steady_state_last_achieved_time = value
    
    @property
    def synchronized_entry_count_by_type(self,) -> Optional[List[string_key_long_value_pair.StringKeyLongValuePair]]:
        """
        Gets the synchronizedEntryCountByType property value. Count of synchronized objects, listed by object type.
        Returns: Optional[List[string_key_long_value_pair.StringKeyLongValuePair]]
        """
        return self._synchronized_entry_count_by_type
    
    @synchronized_entry_count_by_type.setter
    def synchronized_entry_count_by_type(self,value: Optional[List[string_key_long_value_pair.StringKeyLongValuePair]] = None) -> None:
        """
        Sets the synchronizedEntryCountByType property value. Count of synchronized objects, listed by object type.
        Args:
            value: Value to set for the synchronizedEntryCountByType property.
        """
        self._synchronized_entry_count_by_type = value
    
    @property
    def troubleshooting_url(self,) -> Optional[str]:
        """
        Gets the troubleshootingUrl property value. In the event of an error, the URL with the troubleshooting steps for the issue.
        Returns: Optional[str]
        """
        return self._troubleshooting_url
    
    @troubleshooting_url.setter
    def troubleshooting_url(self,value: Optional[str] = None) -> None:
        """
        Sets the troubleshootingUrl property value. In the event of an error, the URL with the troubleshooting steps for the issue.
        Args:
            value: Value to set for the troubleshootingUrl property.
        """
        self._troubleshooting_url = value
    

