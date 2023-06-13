from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audit_activity_initiator, entity, key_value, operation_result, target_resource

from . import entity

@dataclass
class DirectoryAudit(entity.Entity):
    # Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    activity_date_time: Optional[datetime] = None
    # Indicates the activity name or the operation name (E.g. 'Create User', 'Add member to group'). For a list of activities logged, refer to Azure Ad activity list.
    activity_display_name: Optional[str] = None
    # Indicates additional details on the activity.
    additional_details: Optional[List[key_value.KeyValue]] = None
    # Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
    category: Optional[str] = None
    # Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
    correlation_id: Optional[str] = None
    # The initiatedBy property
    initiated_by: Optional[audit_activity_initiator.AuditActivityInitiator] = None
    # Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
    logged_by_service: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
    operation_type: Optional[str] = None
    # Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
    result: Optional[operation_result.OperationResult] = None
    # Indicates the reason for failure if the result is failure or timeout.
    result_reason: Optional[str] = None
    # Information about the resource that changed due to the activity.
    target_resources: Optional[List[target_resource.TargetResource]] = None
    # Type of user agent used by a user in the activity.
    user_agent: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryAudit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectoryAudit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audit_activity_initiator, entity, key_value, operation_result, target_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activityDisplayName": lambda n : setattr(self, 'activity_display_name', n.get_str_value()),
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(key_value.KeyValue)),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(audit_activity_initiator.AuditActivityInitiator)),
            "loggedByService": lambda n : setattr(self, 'logged_by_service', n.get_str_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(operation_result.OperationResult)),
            "resultReason": lambda n : setattr(self, 'result_reason', n.get_str_value()),
            "targetResources": lambda n : setattr(self, 'target_resources', n.get_collection_of_object_values(target_resource.TargetResource)),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
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
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityDisplayName", self.activity_display_name)
        writer.write_collection_of_object_values("additionalDetails", self.additional_details)
        writer.write_str_value("category", self.category)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_str_value("loggedByService", self.logged_by_service)
        writer.write_str_value("operationType", self.operation_type)
        writer.write_enum_value("result", self.result)
        writer.write_str_value("resultReason", self.result_reason)
        writer.write_collection_of_object_values("targetResources", self.target_resources)
        writer.write_str_value("userAgent", self.user_agent)
    

