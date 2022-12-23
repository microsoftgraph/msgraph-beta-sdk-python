from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
operation_error = lazy_import('msgraph.generated.models.operation_error')
teamwork_device_operation_type = lazy_import('msgraph.generated.models.teamwork_device_operation_type')

class TeamworkDeviceOperation(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. Time at which the operation reached a final state (for example, Successful, Failed, and Cancelled).
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. Time at which the operation reached a final state (for example, Successful, Failed, and Cancelled).
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDeviceOperation and sets the default values.
        """
        super().__init__()
        # Time at which the operation reached a final state (for example, Successful, Failed, and Cancelled).
        self._completed_date_time: Optional[datetime] = None
        # Identity of the user who created the device operation.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device operation was created.
        self._created_date_time: Optional[datetime] = None
        # Error details are available only in case of a failed status.
        self._error: Optional[operation_error.OperationError] = None
        # Identity of the user who last modified the device operation.
        self._last_action_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device operation was last modified.
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operationType property
        self._operation_type: Optional[teamwork_device_operation_type.TeamworkDeviceOperationType] = None
        # Time at which the operation was started.
        self._started_date_time: Optional[datetime] = None
        # The current status of the async operation, for example, Queued, Scheduled, InProgress,  Successful, Cancelled, and Failed.
        self._status: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user who created the device operation.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the device operation.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The UTC date and time when the device operation was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The UTC date and time when the device operation was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDeviceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDeviceOperation()
    
    @property
    def error(self,) -> Optional[operation_error.OperationError]:
        """
        Gets the error property value. Error details are available only in case of a failed status.
        Returns: Optional[operation_error.OperationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[operation_error.OperationError] = None) -> None:
        """
        Sets the error property value. Error details are available only in case of a failed status.
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
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(operation_error.OperationError)),
            "last_action_by": lambda n : setattr(self, 'last_action_by', n.get_object_value(identity_set.IdentitySet)),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(teamwork_device_operation_type.TeamworkDeviceOperationType)),
            "started_date_time": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastActionBy property value. Identity of the user who last modified the device operation.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_action_by
    
    @last_action_by.setter
    def last_action_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastActionBy property value. Identity of the user who last modified the device operation.
        Args:
            value: Value to set for the lastActionBy property.
        """
        self._last_action_by = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The UTC date and time when the device operation was last modified.
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The UTC date and time when the device operation was last modified.
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def operation_type(self,) -> Optional[teamwork_device_operation_type.TeamworkDeviceOperationType]:
        """
        Gets the operationType property value. The operationType property
        Returns: Optional[teamwork_device_operation_type.TeamworkDeviceOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[teamwork_device_operation_type.TeamworkDeviceOperationType] = None) -> None:
        """
        Sets the operationType property value. The operationType property
        Args:
            value: Value to set for the operationType property.
        """
        self._operation_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastActionBy", self.last_action_by)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_str_value("status", self.status)
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. Time at which the operation was started.
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. Time at which the operation was started.
        Args:
            value: Value to set for the startedDateTime property.
        """
        self._started_date_time = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The current status of the async operation, for example, Queued, Scheduled, InProgress,  Successful, Cancelled, and Failed.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The current status of the async operation, for example, Queued, Scheduled, InProgress,  Successful, Cancelled, and Failed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

