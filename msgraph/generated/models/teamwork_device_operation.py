from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, operation_error, teamwork_device_operation_type

from . import entity

@dataclass
class TeamworkDeviceOperation(entity.Entity):
    # Time at which the operation reached a final state (for example, Successful, Failed, and Cancelled).
    completed_date_time: Optional[datetime] = None
    # Identity of the user who created the device operation.
    created_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the device operation was created.
    created_date_time: Optional[datetime] = None
    # Error details are available only in case of a failed status.
    error: Optional[operation_error.OperationError] = None
    # Identity of the user who last modified the device operation.
    last_action_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the device operation was last modified.
    last_action_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationType property
    operation_type: Optional[teamwork_device_operation_type.TeamworkDeviceOperationType] = None
    # Time at which the operation was started.
    started_date_time: Optional[datetime] = None
    # The current status of the async operation, for example, Queued, Scheduled, InProgress,  Successful, Cancelled, and Failed.
    status: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, operation_error, teamwork_device_operation_type

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(operation_error.OperationError)),
            "lastActionBy": lambda n : setattr(self, 'last_action_by', n.get_object_value(identity_set.IdentitySet)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(teamwork_device_operation_type.TeamworkDeviceOperationType)),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastActionBy", self.last_action_by)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_str_value("status", self.status)
    

