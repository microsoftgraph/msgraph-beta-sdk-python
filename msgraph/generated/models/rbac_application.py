from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

approval = lazy_import('msgraph.generated.models.approval')
entity = lazy_import('msgraph.generated.models.entity')
unified_rbac_resource_namespace = lazy_import('msgraph.generated.models.unified_rbac_resource_namespace')
unified_role_assignment = lazy_import('msgraph.generated.models.unified_role_assignment')
unified_role_assignment_schedule = lazy_import('msgraph.generated.models.unified_role_assignment_schedule')
unified_role_assignment_schedule_instance = lazy_import('msgraph.generated.models.unified_role_assignment_schedule_instance')
unified_role_assignment_schedule_request = lazy_import('msgraph.generated.models.unified_role_assignment_schedule_request')
unified_role_definition = lazy_import('msgraph.generated.models.unified_role_definition')
unified_role_eligibility_schedule = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule')
unified_role_eligibility_schedule_instance = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule_instance')
unified_role_eligibility_schedule_request = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule_request')

class RbacApplication(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RbacApplication and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resourceNamespaces property
        self._resource_namespaces: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None
        # The roleAssignmentApprovals property
        self._role_assignment_approvals: Optional[List[approval.Approval]] = None
        # The roleAssignments property
        self._role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
        # The roleAssignmentScheduleInstances property
        self._role_assignment_schedule_instances: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None
        # The roleAssignmentScheduleRequests property
        self._role_assignment_schedule_requests: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None
        # The roleAssignmentSchedules property
        self._role_assignment_schedules: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None
        # The roleDefinitions property
        self._role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
        # The roleEligibilityScheduleInstances property
        self._role_eligibility_schedule_instances: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None
        # The roleEligibilityScheduleRequests property
        self._role_eligibility_schedule_requests: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None
        # The roleEligibilitySchedules property
        self._role_eligibility_schedules: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None
        # The transitiveRoleAssignments property
        self._transitive_role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
    
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
        fields = {
            "resource_namespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(unified_rbac_resource_namespace.UnifiedRbacResourceNamespace)),
            "role_assignment_approvals": lambda n : setattr(self, 'role_assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
            "role_assignment_schedule_instances": lambda n : setattr(self, 'role_assignment_schedule_instances', n.get_collection_of_object_values(unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance)),
            "role_assignment_schedule_requests": lambda n : setattr(self, 'role_assignment_schedule_requests', n.get_collection_of_object_values(unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest)),
            "role_assignment_schedules": lambda n : setattr(self, 'role_assignment_schedules', n.get_collection_of_object_values(unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
            "role_eligibility_schedule_instances": lambda n : setattr(self, 'role_eligibility_schedule_instances', n.get_collection_of_object_values(unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance)),
            "role_eligibility_schedule_requests": lambda n : setattr(self, 'role_eligibility_schedule_requests', n.get_collection_of_object_values(unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest)),
            "role_eligibility_schedules": lambda n : setattr(self, 'role_eligibility_schedules', n.get_collection_of_object_values(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
            "transitive_role_assignments": lambda n : setattr(self, 'transitive_role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_namespaces(self,) -> Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]:
        """
        Gets the resourceNamespaces property value. The resourceNamespaces property
        Returns: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]
        """
        return self._resource_namespaces
    
    @resource_namespaces.setter
    def resource_namespaces(self,value: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None) -> None:
        """
        Sets the resourceNamespaces property value. The resourceNamespaces property
        Args:
            value: Value to set for the resourceNamespaces property.
        """
        self._resource_namespaces = value
    
    @property
    def role_assignment_approvals(self,) -> Optional[List[approval.Approval]]:
        """
        Gets the roleAssignmentApprovals property value. The roleAssignmentApprovals property
        Returns: Optional[List[approval.Approval]]
        """
        return self._role_assignment_approvals
    
    @role_assignment_approvals.setter
    def role_assignment_approvals(self,value: Optional[List[approval.Approval]] = None) -> None:
        """
        Sets the roleAssignmentApprovals property value. The roleAssignmentApprovals property
        Args:
            value: Value to set for the roleAssignmentApprovals property.
        """
        self._role_assignment_approvals = value
    
    @property
    def role_assignments(self,) -> Optional[List[unified_role_assignment.UnifiedRoleAssignment]]:
        """
        Gets the roleAssignments property value. The roleAssignments property
        Returns: Optional[List[unified_role_assignment.UnifiedRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. The roleAssignments property
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_assignment_schedule_instances(self,) -> Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]]:
        """
        Gets the roleAssignmentScheduleInstances property value. The roleAssignmentScheduleInstances property
        Returns: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]]
        """
        return self._role_assignment_schedule_instances
    
    @role_assignment_schedule_instances.setter
    def role_assignment_schedule_instances(self,value: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None) -> None:
        """
        Sets the roleAssignmentScheduleInstances property value. The roleAssignmentScheduleInstances property
        Args:
            value: Value to set for the roleAssignmentScheduleInstances property.
        """
        self._role_assignment_schedule_instances = value
    
    @property
    def role_assignment_schedule_requests(self,) -> Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]]:
        """
        Gets the roleAssignmentScheduleRequests property value. The roleAssignmentScheduleRequests property
        Returns: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]]
        """
        return self._role_assignment_schedule_requests
    
    @role_assignment_schedule_requests.setter
    def role_assignment_schedule_requests(self,value: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None) -> None:
        """
        Sets the roleAssignmentScheduleRequests property value. The roleAssignmentScheduleRequests property
        Args:
            value: Value to set for the roleAssignmentScheduleRequests property.
        """
        self._role_assignment_schedule_requests = value
    
    @property
    def role_assignment_schedules(self,) -> Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]]:
        """
        Gets the roleAssignmentSchedules property value. The roleAssignmentSchedules property
        Returns: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]]
        """
        return self._role_assignment_schedules
    
    @role_assignment_schedules.setter
    def role_assignment_schedules(self,value: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None) -> None:
        """
        Sets the roleAssignmentSchedules property value. The roleAssignmentSchedules property
        Args:
            value: Value to set for the roleAssignmentSchedules property.
        """
        self._role_assignment_schedules = value
    
    @property
    def role_definitions(self,) -> Optional[List[unified_role_definition.UnifiedRoleDefinition]]:
        """
        Gets the roleDefinitions property value. The roleDefinitions property
        Returns: Optional[List[unified_role_definition.UnifiedRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. The roleDefinitions property
        Args:
            value: Value to set for the roleDefinitions property.
        """
        self._role_definitions = value
    
    @property
    def role_eligibility_schedule_instances(self,) -> Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]]:
        """
        Gets the roleEligibilityScheduleInstances property value. The roleEligibilityScheduleInstances property
        Returns: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]]
        """
        return self._role_eligibility_schedule_instances
    
    @role_eligibility_schedule_instances.setter
    def role_eligibility_schedule_instances(self,value: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None) -> None:
        """
        Sets the roleEligibilityScheduleInstances property value. The roleEligibilityScheduleInstances property
        Args:
            value: Value to set for the roleEligibilityScheduleInstances property.
        """
        self._role_eligibility_schedule_instances = value
    
    @property
    def role_eligibility_schedule_requests(self,) -> Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]]:
        """
        Gets the roleEligibilityScheduleRequests property value. The roleEligibilityScheduleRequests property
        Returns: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]]
        """
        return self._role_eligibility_schedule_requests
    
    @role_eligibility_schedule_requests.setter
    def role_eligibility_schedule_requests(self,value: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None) -> None:
        """
        Sets the roleEligibilityScheduleRequests property value. The roleEligibilityScheduleRequests property
        Args:
            value: Value to set for the roleEligibilityScheduleRequests property.
        """
        self._role_eligibility_schedule_requests = value
    
    @property
    def role_eligibility_schedules(self,) -> Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]]:
        """
        Gets the roleEligibilitySchedules property value. The roleEligibilitySchedules property
        Returns: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]]
        """
        return self._role_eligibility_schedules
    
    @role_eligibility_schedules.setter
    def role_eligibility_schedules(self,value: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None) -> None:
        """
        Sets the roleEligibilitySchedules property value. The roleEligibilitySchedules property
        Args:
            value: Value to set for the roleEligibilitySchedules property.
        """
        self._role_eligibility_schedules = value
    
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
        writer.write_collection_of_object_values("roleAssignmentApprovals", self.role_assignment_approvals)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleAssignmentScheduleInstances", self.role_assignment_schedule_instances)
        writer.write_collection_of_object_values("roleAssignmentScheduleRequests", self.role_assignment_schedule_requests)
        writer.write_collection_of_object_values("roleAssignmentSchedules", self.role_assignment_schedules)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleEligibilityScheduleInstances", self.role_eligibility_schedule_instances)
        writer.write_collection_of_object_values("roleEligibilityScheduleRequests", self.role_eligibility_schedule_requests)
        writer.write_collection_of_object_values("roleEligibilitySchedules", self.role_eligibility_schedules)
        writer.write_collection_of_object_values("transitiveRoleAssignments", self.transitive_role_assignments)
    
    @property
    def transitive_role_assignments(self,) -> Optional[List[unified_role_assignment.UnifiedRoleAssignment]]:
        """
        Gets the transitiveRoleAssignments property value. The transitiveRoleAssignments property
        Returns: Optional[List[unified_role_assignment.UnifiedRoleAssignment]]
        """
        return self._transitive_role_assignments
    
    @transitive_role_assignments.setter
    def transitive_role_assignments(self,value: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None) -> None:
        """
        Sets the transitiveRoleAssignments property value. The transitiveRoleAssignments property
        Args:
            value: Value to set for the transitiveRoleAssignments property.
        """
        self._transitive_role_assignments = value
    

