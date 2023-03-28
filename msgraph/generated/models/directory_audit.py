from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audit_activity_initiator, entity, key_value, operation_result, target_resource

from . import entity

class DirectoryAudit(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DirectoryAudit and sets the default values.
        """
        super().__init__()
        # Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._activity_date_time: Optional[datetime] = None
        # Indicates the activity name or the operation name (E.g. 'Create User', 'Add member to group'). For a list of activities logged, refer to Azure Ad activity list.
        self._activity_display_name: Optional[str] = None
        # Indicates additional details on the activity.
        self._additional_details: Optional[List[key_value.KeyValue]] = None
        # Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
        self._category: Optional[str] = None
        # Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
        self._correlation_id: Optional[str] = None
        # The initiatedBy property
        self._initiated_by: Optional[audit_activity_initiator.AuditActivityInitiator] = None
        # Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
        self._logged_by_service: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
        self._operation_type: Optional[str] = None
        # Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
        self._result: Optional[operation_result.OperationResult] = None
        # Indicates the reason for failure if the result is failure or timeout.
        self._result_reason: Optional[str] = None
        # Information about the resource that changed due to the activity.
        self._target_resources: Optional[List[target_resource.TargetResource]] = None
        # Type of user agent used by a user in the activity.
        self._user_agent: Optional[str] = None
    
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the activity_date_time property.
        """
        self._activity_date_time = value
    
    @property
    def activity_display_name(self,) -> Optional[str]:
        """
        Gets the activityDisplayName property value. Indicates the activity name or the operation name (E.g. 'Create User', 'Add member to group'). For a list of activities logged, refer to Azure Ad activity list.
        Returns: Optional[str]
        """
        return self._activity_display_name
    
    @activity_display_name.setter
    def activity_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the activityDisplayName property value. Indicates the activity name or the operation name (E.g. 'Create User', 'Add member to group'). For a list of activities logged, refer to Azure Ad activity list.
        Args:
            value: Value to set for the activity_display_name property.
        """
        self._activity_display_name = value
    
    @property
    def additional_details(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the additionalDetails property value. Indicates additional details on the activity.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the additionalDetails property value. Indicates additional details on the activity.
        Args:
            value: Value to set for the additional_details property.
        """
        self._additional_details = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
        Args:
            value: Value to set for the correlation_id property.
        """
        self._correlation_id = value
    
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
    
    @property
    def initiated_by(self,) -> Optional[audit_activity_initiator.AuditActivityInitiator]:
        """
        Gets the initiatedBy property value. The initiatedBy property
        Returns: Optional[audit_activity_initiator.AuditActivityInitiator]
        """
        return self._initiated_by
    
    @initiated_by.setter
    def initiated_by(self,value: Optional[audit_activity_initiator.AuditActivityInitiator] = None) -> None:
        """
        Sets the initiatedBy property value. The initiatedBy property
        Args:
            value: Value to set for the initiated_by property.
        """
        self._initiated_by = value
    
    @property
    def logged_by_service(self,) -> Optional[str]:
        """
        Gets the loggedByService property value. Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
        Returns: Optional[str]
        """
        return self._logged_by_service
    
    @logged_by_service.setter
    def logged_by_service(self,value: Optional[str] = None) -> None:
        """
        Sets the loggedByService property value. Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
        Args:
            value: Value to set for the logged_by_service property.
        """
        self._logged_by_service = value
    
    @property
    def operation_type(self,) -> Optional[str]:
        """
        Gets the operationType property value. Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
        Returns: Optional[str]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[str] = None) -> None:
        """
        Sets the operationType property value. Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
        Args:
            value: Value to set for the operation_type property.
        """
        self._operation_type = value
    
    @property
    def result(self,) -> Optional[operation_result.OperationResult]:
        """
        Gets the result property value. Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
        Returns: Optional[operation_result.OperationResult]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[operation_result.OperationResult] = None) -> None:
        """
        Sets the result property value. Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    @property
    def result_reason(self,) -> Optional[str]:
        """
        Gets the resultReason property value. Indicates the reason for failure if the result is failure or timeout.
        Returns: Optional[str]
        """
        return self._result_reason
    
    @result_reason.setter
    def result_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the resultReason property value. Indicates the reason for failure if the result is failure or timeout.
        Args:
            value: Value to set for the result_reason property.
        """
        self._result_reason = value
    
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
    
    @property
    def target_resources(self,) -> Optional[List[target_resource.TargetResource]]:
        """
        Gets the targetResources property value. Information about the resource that changed due to the activity.
        Returns: Optional[List[target_resource.TargetResource]]
        """
        return self._target_resources
    
    @target_resources.setter
    def target_resources(self,value: Optional[List[target_resource.TargetResource]] = None) -> None:
        """
        Sets the targetResources property value. Information about the resource that changed due to the activity.
        Args:
            value: Value to set for the target_resources property.
        """
        self._target_resources = value
    
    @property
    def user_agent(self,) -> Optional[str]:
        """
        Gets the userAgent property value. Type of user agent used by a user in the activity.
        Returns: Optional[str]
        """
        return self._user_agent
    
    @user_agent.setter
    def user_agent(self,value: Optional[str] = None) -> None:
        """
        Sets the userAgent property value. Type of user agent used by a user in the activity.
        Args:
            value: Value to set for the user_agent property.
        """
        self._user_agent = value
    

