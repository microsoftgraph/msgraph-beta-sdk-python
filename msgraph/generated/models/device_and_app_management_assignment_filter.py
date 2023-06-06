from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assignment_filter_management_type, device_platform_type, entity, payload_by_filter, payload_compatible_assignment_filter

from . import entity

@dataclass
class DeviceAndAppManagementAssignmentFilter(entity.Entity):
    """
    A class containing the properties used for Assignment Filter.
    """
    # Supported filter management types whether its devices or apps.
    assignment_filter_management_type: Optional[assignment_filter_management_type.AssignmentFilterManagementType] = None
    # The creation time of the assignment filter. The value cannot be modified and is automatically populated during new assignment filter process. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
    created_date_time: Optional[datetime] = None
    # Optional description of the Assignment Filter.
    description: Optional[str] = None
    # The name of the Assignment Filter.
    display_name: Optional[str] = None
    # Last modified time of the Assignment Filter. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates associated assignments for a specific filter.
    payloads: Optional[List[payload_by_filter.PayloadByFilter]] = None
    # Supported platform types.
    platform: Optional[device_platform_type.DevicePlatformType] = None
    # Indicates role scope tags assigned for the assignment filter.
    role_scope_tags: Optional[List[str]] = None
    # Rule definition of the assignment filter.
    rule: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignmentFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignmentFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.payloadCompatibleAssignmentFilter":
                from . import payload_compatible_assignment_filter

                return payload_compatible_assignment_filter.PayloadCompatibleAssignmentFilter()
        return DeviceAndAppManagementAssignmentFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assignment_filter_management_type, device_platform_type, entity, payload_by_filter, payload_compatible_assignment_filter

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentFilterManagementType": lambda n : setattr(self, 'assignment_filter_management_type', n.get_enum_value(assignment_filter_management_type.AssignmentFilterManagementType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloads": lambda n : setattr(self, 'payloads', n.get_collection_of_object_values(payload_by_filter.PayloadByFilter)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_primitive_values(str)),
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
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
        writer.write_enum_value("assignmentFilterManagementType", self.assignment_filter_management_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("payloads", self.payloads)
        writer.write_enum_value("platform", self.platform)
        writer.write_collection_of_primitive_values("roleScopeTags", self.role_scope_tags)
        writer.write_str_value("rule", self.rule)
    

