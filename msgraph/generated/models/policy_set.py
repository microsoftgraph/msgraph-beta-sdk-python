from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, error_code, policy_set_assignment, policy_set_item, policy_set_status

from . import entity

@dataclass
class PolicySet(entity.Entity):
    """
    A class containing the properties used for PolicySet.
    """
    # Assignments of the PolicySet.
    assignments: Optional[List[policy_set_assignment.PolicySetAssignment]] = None
    # Creation time of the PolicySet.
    created_date_time: Optional[datetime] = None
    # Description of the PolicySet.
    description: Optional[str] = None
    # DisplayName of the PolicySet.
    display_name: Optional[str] = None
    # The errorCode property
    error_code: Optional[error_code.ErrorCode] = None
    # Tags of the guided deployment
    guided_deployment_tags: Optional[List[str]] = None
    # Items of the PolicySet with maximum count 100.
    items: Optional[List[policy_set_item.PolicySetItem]] = None
    # Last modified time of the PolicySet.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # RoleScopeTags of the PolicySet
    role_scope_tags: Optional[List[str]] = None
    # The enum to specify the status of PolicySet.
    status: Optional[policy_set_status.PolicySetStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PolicySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, error_code, policy_set_assignment, policy_set_item, policy_set_status

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(policy_set_assignment.PolicySetAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(error_code.ErrorCode)),
            "guidedDeploymentTags": lambda n : setattr(self, 'guided_deployment_tags', n.get_collection_of_primitive_values(str)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(policy_set_item.PolicySetItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(policy_set_status.PolicySetStatus)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_collection_of_primitive_values("guidedDeploymentTags", self.guided_deployment_tags)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTags", self.role_scope_tags)
        writer.write_enum_value("status", self.status)
    

