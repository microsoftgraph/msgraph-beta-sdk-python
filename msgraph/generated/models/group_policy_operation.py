from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_operation_status, group_policy_operation_type

from . import entity

@dataclass
class GroupPolicyOperation(entity.Entity):
    """
    The entity represents an group policy operation.
    """
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of Group Policy operation status.
    operation_status: Optional[group_policy_operation_status.GroupPolicyOperationStatus] = None
    # Type of Group Policy operation.
    operation_type: Optional[group_policy_operation_type.GroupPolicyOperationType] = None
    # The group policy operation status detail.
    status_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_operation_status, group_policy_operation_type

        from . import entity, group_policy_operation_status, group_policy_operation_type

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operationStatus": lambda n : setattr(self, 'operation_status', n.get_enum_value(group_policy_operation_status.GroupPolicyOperationStatus)),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(group_policy_operation_type.GroupPolicyOperationType)),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("operationStatus", self.operation_status)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_str_value("statusDetails", self.status_details)
    

