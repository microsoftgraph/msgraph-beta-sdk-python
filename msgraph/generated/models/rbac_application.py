from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval, entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

from . import entity

@dataclass
class RbacApplication(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceNamespaces property
    resource_namespaces: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None
    # The roleAssignmentApprovals property
    role_assignment_approvals: Optional[List[approval.Approval]] = None
    # The roleAssignmentScheduleInstances property
    role_assignment_schedule_instances: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None
    # The roleAssignmentScheduleRequests property
    role_assignment_schedule_requests: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None
    # The roleAssignmentSchedules property
    role_assignment_schedules: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None
    # The roleAssignments property
    role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
    # The roleDefinitions property
    role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
    # The roleEligibilityScheduleInstances property
    role_eligibility_schedule_instances: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None
    # The roleEligibilityScheduleRequests property
    role_eligibility_schedule_requests: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None
    # The roleEligibilitySchedules property
    role_eligibility_schedules: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None
    # The transitiveRoleAssignments property
    transitive_role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RbacApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RbacApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval, entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(unified_rbac_resource_namespace.UnifiedRbacResourceNamespace)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
            "roleAssignmentApprovals": lambda n : setattr(self, 'role_assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "roleAssignmentSchedules": lambda n : setattr(self, 'role_assignment_schedules', n.get_collection_of_object_values(unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule)),
            "roleAssignmentScheduleInstances": lambda n : setattr(self, 'role_assignment_schedule_instances', n.get_collection_of_object_values(unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance)),
            "roleAssignmentScheduleRequests": lambda n : setattr(self, 'role_assignment_schedule_requests', n.get_collection_of_object_values(unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
            "roleEligibilitySchedules": lambda n : setattr(self, 'role_eligibility_schedules', n.get_collection_of_object_values(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
            "roleEligibilityScheduleInstances": lambda n : setattr(self, 'role_eligibility_schedule_instances', n.get_collection_of_object_values(unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance)),
            "roleEligibilityScheduleRequests": lambda n : setattr(self, 'role_eligibility_schedule_requests', n.get_collection_of_object_values(unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest)),
            "transitiveRoleAssignments": lambda n : setattr(self, 'transitive_role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
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
        writer.write_collection_of_object_values("resourceNamespaces", self.resource_namespaces)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleAssignmentApprovals", self.role_assignment_approvals)
        writer.write_collection_of_object_values("roleAssignmentSchedules", self.role_assignment_schedules)
        writer.write_collection_of_object_values("roleAssignmentScheduleInstances", self.role_assignment_schedule_instances)
        writer.write_collection_of_object_values("roleAssignmentScheduleRequests", self.role_assignment_schedule_requests)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleEligibilitySchedules", self.role_eligibility_schedules)
        writer.write_collection_of_object_values("roleEligibilityScheduleInstances", self.role_eligibility_schedule_instances)
        writer.write_collection_of_object_values("roleEligibilityScheduleRequests", self.role_eligibility_schedule_requests)
        writer.write_collection_of_object_values("transitiveRoleAssignments", self.transitive_role_assignments)
    

