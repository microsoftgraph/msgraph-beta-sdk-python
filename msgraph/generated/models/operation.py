from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, onenote_operation, operation_status

from . import entity

class Operation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new operation and sets the default values.
        """
        super().__init__()
        # The start time of the operation.
        self._created_date_time: Optional[datetime] = None
        # The time of the last action of the operation.
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Possible values are: notStarted, running, completed, failed. Read-only.
        self._status: Optional[operation_status.OperationStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The start time of the operation.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The start time of the operation.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Operation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Operation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.onenoteOperation":
                from . import onenote_operation

                return onenote_operation.OnenoteOperation()
        return Operation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, onenote_operation, operation_status

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(operation_status.OperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The time of the last action of the operation.
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The time of the last action of the operation.
        Args:
            value: Value to set for the last_action_date_time property.
        """
        self._last_action_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[operation_status.OperationStatus]:
        """
        Gets the status property value. Possible values are: notStarted, running, completed, failed. Read-only.
        Returns: Optional[operation_status.OperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[operation_status.OperationStatus] = None) -> None:
        """
        Sets the status property value. Possible values are: notStarted, running, completed, failed. Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

