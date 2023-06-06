from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_audit_activity_operation_type, cloud_pc_audit_activity_result, cloud_pc_audit_actor, cloud_pc_audit_category, cloud_pc_audit_resource, entity

from . import entity

@dataclass
class CloudPcAuditEvent(entity.Entity):
    # Friendly name of the activity. Optional.
    activity: Optional[str] = None
    # The date time in UTC when the activity was performed. Read-only.
    activity_date_time: Optional[datetime] = None
    # The activityOperationType property
    activity_operation_type: Optional[cloud_pc_audit_activity_operation_type.CloudPcAuditActivityOperationType] = None
    # The activityResult property
    activity_result: Optional[cloud_pc_audit_activity_result.CloudPcAuditActivityResult] = None
    # The type of activity that was performed. Read-only.
    activity_type: Optional[str] = None
    # The actor property
    actor: Optional[cloud_pc_audit_actor.CloudPcAuditActor] = None
    # The category property
    category: Optional[cloud_pc_audit_category.CloudPcAuditCategory] = None
    # Component name. Read-only.
    component_name: Optional[str] = None
    # The client request identifier, used to correlate activity within the system. Read-only.
    correlation_id: Optional[str] = None
    # Event display name. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of cloudPcAuditResource objects. Read-only.
    resources: Optional[List[cloud_pc_audit_resource.CloudPcAuditResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcAuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAuditEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcAuditEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_audit_activity_operation_type, cloud_pc_audit_activity_result, cloud_pc_audit_actor, cloud_pc_audit_category, cloud_pc_audit_resource, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activityOperationType": lambda n : setattr(self, 'activity_operation_type', n.get_enum_value(cloud_pc_audit_activity_operation_type.CloudPcAuditActivityOperationType)),
            "activityResult": lambda n : setattr(self, 'activity_result', n.get_enum_value(cloud_pc_audit_activity_result.CloudPcAuditActivityResult)),
            "activityType": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(cloud_pc_audit_actor.CloudPcAuditActor)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(cloud_pc_audit_category.CloudPcAuditCategory)),
            "componentName": lambda n : setattr(self, 'component_name', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(cloud_pc_audit_resource.CloudPcAuditResource)),
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
        writer.write_str_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_enum_value("activityOperationType", self.activity_operation_type)
        writer.write_enum_value("activityResult", self.activity_result)
        writer.write_str_value("activityType", self.activity_type)
        writer.write_object_value("actor", self.actor)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("componentName", self.component_name)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
    

