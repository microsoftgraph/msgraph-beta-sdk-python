from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

synchronization_error = lazy_import('msgraph.generated.models.synchronization_error')
synchronization_task_execution_result = lazy_import('msgraph.generated.models.synchronization_task_execution_result')

class SynchronizationTaskExecution(AdditionalDataHolder, Parsable):
    @property
    def activity_identifier(self,) -> Optional[str]:
        """
        Gets the activityIdentifier property value. Identifier of the job run.
        Returns: Optional[str]
        """
        return self._activity_identifier
    
    @activity_identifier.setter
    def activity_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the activityIdentifier property value. Identifier of the job run.
        Args:
            value: Value to set for the activityIdentifier property.
        """
        self._activity_identifier = value
    
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
        Instantiates a new synchronizationTaskExecution and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifier of the job run.
        self._activity_identifier: Optional[str] = None
        # Count of processed entries that were assigned for this application.
        self._count_entitled: Optional[int] = None
        # Count of processed entries that were assigned for provisioning.
        self._count_entitled_for_provisioning: Optional[int] = None
        # Count of entries that were escrowed (errors).
        self._count_escrowed: Optional[int] = None
        # Count of entries that were escrowed, including system-generated escrows.
        self._count_escrowed_raw: Optional[int] = None
        # Count of exported entries.
        self._count_exported: Optional[int] = None
        # Count of entries that were expected to be exported.
        self._count_exports: Optional[int] = None
        # Count of imported entries.
        self._count_imported: Optional[int] = None
        # Count of imported delta-changes.
        self._count_imported_deltas: Optional[int] = None
        # Count of imported delta-changes pertaining to reference changes.
        self._count_imported_reference_deltas: Optional[int] = None
        # If an error was encountered, contains a synchronizationError object with details.
        self._error: Optional[synchronization_error.SynchronizationError] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The state property
        self._state: Optional[synchronization_task_execution_result.SynchronizationTaskExecutionResult] = None
        # Time when this job run began. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._time_began: Optional[datetime] = None
        # Time when this job run ended. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._time_ended: Optional[datetime] = None
    
    @property
    def count_entitled(self,) -> Optional[int]:
        """
        Gets the countEntitled property value. Count of processed entries that were assigned for this application.
        Returns: Optional[int]
        """
        return self._count_entitled
    
    @count_entitled.setter
    def count_entitled(self,value: Optional[int] = None) -> None:
        """
        Sets the countEntitled property value. Count of processed entries that were assigned for this application.
        Args:
            value: Value to set for the countEntitled property.
        """
        self._count_entitled = value
    
    @property
    def count_entitled_for_provisioning(self,) -> Optional[int]:
        """
        Gets the countEntitledForProvisioning property value. Count of processed entries that were assigned for provisioning.
        Returns: Optional[int]
        """
        return self._count_entitled_for_provisioning
    
    @count_entitled_for_provisioning.setter
    def count_entitled_for_provisioning(self,value: Optional[int] = None) -> None:
        """
        Sets the countEntitledForProvisioning property value. Count of processed entries that were assigned for provisioning.
        Args:
            value: Value to set for the countEntitledForProvisioning property.
        """
        self._count_entitled_for_provisioning = value
    
    @property
    def count_escrowed(self,) -> Optional[int]:
        """
        Gets the countEscrowed property value. Count of entries that were escrowed (errors).
        Returns: Optional[int]
        """
        return self._count_escrowed
    
    @count_escrowed.setter
    def count_escrowed(self,value: Optional[int] = None) -> None:
        """
        Sets the countEscrowed property value. Count of entries that were escrowed (errors).
        Args:
            value: Value to set for the countEscrowed property.
        """
        self._count_escrowed = value
    
    @property
    def count_escrowed_raw(self,) -> Optional[int]:
        """
        Gets the countEscrowedRaw property value. Count of entries that were escrowed, including system-generated escrows.
        Returns: Optional[int]
        """
        return self._count_escrowed_raw
    
    @count_escrowed_raw.setter
    def count_escrowed_raw(self,value: Optional[int] = None) -> None:
        """
        Sets the countEscrowedRaw property value. Count of entries that were escrowed, including system-generated escrows.
        Args:
            value: Value to set for the countEscrowedRaw property.
        """
        self._count_escrowed_raw = value
    
    @property
    def count_exported(self,) -> Optional[int]:
        """
        Gets the countExported property value. Count of exported entries.
        Returns: Optional[int]
        """
        return self._count_exported
    
    @count_exported.setter
    def count_exported(self,value: Optional[int] = None) -> None:
        """
        Sets the countExported property value. Count of exported entries.
        Args:
            value: Value to set for the countExported property.
        """
        self._count_exported = value
    
    @property
    def count_exports(self,) -> Optional[int]:
        """
        Gets the countExports property value. Count of entries that were expected to be exported.
        Returns: Optional[int]
        """
        return self._count_exports
    
    @count_exports.setter
    def count_exports(self,value: Optional[int] = None) -> None:
        """
        Sets the countExports property value. Count of entries that were expected to be exported.
        Args:
            value: Value to set for the countExports property.
        """
        self._count_exports = value
    
    @property
    def count_imported(self,) -> Optional[int]:
        """
        Gets the countImported property value. Count of imported entries.
        Returns: Optional[int]
        """
        return self._count_imported
    
    @count_imported.setter
    def count_imported(self,value: Optional[int] = None) -> None:
        """
        Sets the countImported property value. Count of imported entries.
        Args:
            value: Value to set for the countImported property.
        """
        self._count_imported = value
    
    @property
    def count_imported_deltas(self,) -> Optional[int]:
        """
        Gets the countImportedDeltas property value. Count of imported delta-changes.
        Returns: Optional[int]
        """
        return self._count_imported_deltas
    
    @count_imported_deltas.setter
    def count_imported_deltas(self,value: Optional[int] = None) -> None:
        """
        Sets the countImportedDeltas property value. Count of imported delta-changes.
        Args:
            value: Value to set for the countImportedDeltas property.
        """
        self._count_imported_deltas = value
    
    @property
    def count_imported_reference_deltas(self,) -> Optional[int]:
        """
        Gets the countImportedReferenceDeltas property value. Count of imported delta-changes pertaining to reference changes.
        Returns: Optional[int]
        """
        return self._count_imported_reference_deltas
    
    @count_imported_reference_deltas.setter
    def count_imported_reference_deltas(self,value: Optional[int] = None) -> None:
        """
        Sets the countImportedReferenceDeltas property value. Count of imported delta-changes pertaining to reference changes.
        Args:
            value: Value to set for the countImportedReferenceDeltas property.
        """
        self._count_imported_reference_deltas = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationTaskExecution:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationTaskExecution
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationTaskExecution()
    
    @property
    def error(self,) -> Optional[synchronization_error.SynchronizationError]:
        """
        Gets the error property value. If an error was encountered, contains a synchronizationError object with details.
        Returns: Optional[synchronization_error.SynchronizationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[synchronization_error.SynchronizationError] = None) -> None:
        """
        Sets the error property value. If an error was encountered, contains a synchronizationError object with details.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_identifier": lambda n : setattr(self, 'activity_identifier', n.get_str_value()),
            "count_entitled": lambda n : setattr(self, 'count_entitled', n.get_int_value()),
            "count_entitled_for_provisioning": lambda n : setattr(self, 'count_entitled_for_provisioning', n.get_int_value()),
            "count_escrowed": lambda n : setattr(self, 'count_escrowed', n.get_int_value()),
            "count_escrowed_raw": lambda n : setattr(self, 'count_escrowed_raw', n.get_int_value()),
            "count_exported": lambda n : setattr(self, 'count_exported', n.get_int_value()),
            "count_exports": lambda n : setattr(self, 'count_exports', n.get_int_value()),
            "count_imported": lambda n : setattr(self, 'count_imported', n.get_int_value()),
            "count_imported_deltas": lambda n : setattr(self, 'count_imported_deltas', n.get_int_value()),
            "count_imported_reference_deltas": lambda n : setattr(self, 'count_imported_reference_deltas', n.get_int_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(synchronization_error.SynchronizationError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(synchronization_task_execution_result.SynchronizationTaskExecutionResult)),
            "time_began": lambda n : setattr(self, 'time_began', n.get_datetime_value()),
            "time_ended": lambda n : setattr(self, 'time_ended', n.get_datetime_value()),
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
        writer.write_str_value("activityIdentifier", self.activity_identifier)
        writer.write_int_value("countEntitled", self.count_entitled)
        writer.write_int_value("countEntitledForProvisioning", self.count_entitled_for_provisioning)
        writer.write_int_value("countEscrowed", self.count_escrowed)
        writer.write_int_value("countEscrowedRaw", self.count_escrowed_raw)
        writer.write_int_value("countExported", self.count_exported)
        writer.write_int_value("countExports", self.count_exports)
        writer.write_int_value("countImported", self.count_imported)
        writer.write_int_value("countImportedDeltas", self.count_imported_deltas)
        writer.write_int_value("countImportedReferenceDeltas", self.count_imported_reference_deltas)
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_datetime_value("timeBegan", self.time_began)
        writer.write_datetime_value("timeEnded", self.time_ended)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[synchronization_task_execution_result.SynchronizationTaskExecutionResult]:
        """
        Gets the state property value. The state property
        Returns: Optional[synchronization_task_execution_result.SynchronizationTaskExecutionResult]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[synchronization_task_execution_result.SynchronizationTaskExecutionResult] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def time_began(self,) -> Optional[datetime]:
        """
        Gets the timeBegan property value. Time when this job run began. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._time_began
    
    @time_began.setter
    def time_began(self,value: Optional[datetime] = None) -> None:
        """
        Sets the timeBegan property value. Time when this job run began. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the timeBegan property.
        """
        self._time_began = value
    
    @property
    def time_ended(self,) -> Optional[datetime]:
        """
        Gets the timeEnded property value. Time when this job run ended. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._time_ended
    
    @time_ended.setter
    def time_ended(self,value: Optional[datetime] = None) -> None:
        """
        Sets the timeEnded property value. Time when this job run ended. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the timeEnded property.
        """
        self._time_ended = value
    

