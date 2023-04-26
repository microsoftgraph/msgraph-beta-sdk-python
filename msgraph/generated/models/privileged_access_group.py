from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval, entity, privileged_access_group_assignment_schedule, privileged_access_group_assignment_schedule_instance, privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule, privileged_access_group_eligibility_schedule_instance, privileged_access_group_eligibility_schedule_request

from . import entity

class PrivilegedAccessGroup(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedAccessGroup and sets the default values.
        """
        super().__init__()
        # The assignmentApprovals property
        self._assignment_approvals: Optional[List[approval.Approval]] = None
        # The assignmentScheduleInstances property
        self._assignment_schedule_instances: Optional[List[privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance]] = None
        # The assignmentScheduleRequests property
        self._assignment_schedule_requests: Optional[List[privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest]] = None
        # The assignmentSchedules property
        self._assignment_schedules: Optional[List[privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule]] = None
        # The eligibilityScheduleInstances property
        self._eligibility_schedule_instances: Optional[List[privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance]] = None
        # The eligibilityScheduleRequests property
        self._eligibility_schedule_requests: Optional[List[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]] = None
        # The eligibilitySchedules property
        self._eligibility_schedules: Optional[List[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def assignment_approvals(self,) -> Optional[List[approval.Approval]]:
        """
        Gets the assignmentApprovals property value. The assignmentApprovals property
        Returns: Optional[List[approval.Approval]]
        """
        return self._assignment_approvals
    
    @assignment_approvals.setter
    def assignment_approvals(self,value: Optional[List[approval.Approval]] = None) -> None:
        """
        Sets the assignmentApprovals property value. The assignmentApprovals property
        Args:
            value: Value to set for the assignment_approvals property.
        """
        self._assignment_approvals = value
    
    @property
    def assignment_schedule_instances(self,) -> Optional[List[privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance]]:
        """
        Gets the assignmentScheduleInstances property value. The assignmentScheduleInstances property
        Returns: Optional[List[privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance]]
        """
        return self._assignment_schedule_instances
    
    @assignment_schedule_instances.setter
    def assignment_schedule_instances(self,value: Optional[List[privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance]] = None) -> None:
        """
        Sets the assignmentScheduleInstances property value. The assignmentScheduleInstances property
        Args:
            value: Value to set for the assignment_schedule_instances property.
        """
        self._assignment_schedule_instances = value
    
    @property
    def assignment_schedule_requests(self,) -> Optional[List[privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest]]:
        """
        Gets the assignmentScheduleRequests property value. The assignmentScheduleRequests property
        Returns: Optional[List[privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest]]
        """
        return self._assignment_schedule_requests
    
    @assignment_schedule_requests.setter
    def assignment_schedule_requests(self,value: Optional[List[privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest]] = None) -> None:
        """
        Sets the assignmentScheduleRequests property value. The assignmentScheduleRequests property
        Args:
            value: Value to set for the assignment_schedule_requests property.
        """
        self._assignment_schedule_requests = value
    
    @property
    def assignment_schedules(self,) -> Optional[List[privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule]]:
        """
        Gets the assignmentSchedules property value. The assignmentSchedules property
        Returns: Optional[List[privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule]]
        """
        return self._assignment_schedules
    
    @assignment_schedules.setter
    def assignment_schedules(self,value: Optional[List[privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule]] = None) -> None:
        """
        Sets the assignmentSchedules property value. The assignmentSchedules property
        Args:
            value: Value to set for the assignment_schedules property.
        """
        self._assignment_schedules = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroup()
    
    @property
    def eligibility_schedule_instances(self,) -> Optional[List[privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance]]:
        """
        Gets the eligibilityScheduleInstances property value. The eligibilityScheduleInstances property
        Returns: Optional[List[privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance]]
        """
        return self._eligibility_schedule_instances
    
    @eligibility_schedule_instances.setter
    def eligibility_schedule_instances(self,value: Optional[List[privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance]] = None) -> None:
        """
        Sets the eligibilityScheduleInstances property value. The eligibilityScheduleInstances property
        Args:
            value: Value to set for the eligibility_schedule_instances property.
        """
        self._eligibility_schedule_instances = value
    
    @property
    def eligibility_schedule_requests(self,) -> Optional[List[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]]:
        """
        Gets the eligibilityScheduleRequests property value. The eligibilityScheduleRequests property
        Returns: Optional[List[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]]
        """
        return self._eligibility_schedule_requests
    
    @eligibility_schedule_requests.setter
    def eligibility_schedule_requests(self,value: Optional[List[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]] = None) -> None:
        """
        Sets the eligibilityScheduleRequests property value. The eligibilityScheduleRequests property
        Args:
            value: Value to set for the eligibility_schedule_requests property.
        """
        self._eligibility_schedule_requests = value
    
    @property
    def eligibility_schedules(self,) -> Optional[List[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]]:
        """
        Gets the eligibilitySchedules property value. The eligibilitySchedules property
        Returns: Optional[List[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]]
        """
        return self._eligibility_schedules
    
    @eligibility_schedules.setter
    def eligibility_schedules(self,value: Optional[List[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]] = None) -> None:
        """
        Sets the eligibilitySchedules property value. The eligibilitySchedules property
        Args:
            value: Value to set for the eligibility_schedules property.
        """
        self._eligibility_schedules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval, entity, privileged_access_group_assignment_schedule, privileged_access_group_assignment_schedule_instance, privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule, privileged_access_group_eligibility_schedule_instance, privileged_access_group_eligibility_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentApprovals": lambda n : setattr(self, 'assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "assignmentSchedules": lambda n : setattr(self, 'assignment_schedules', n.get_collection_of_object_values(privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule)),
            "assignmentScheduleInstances": lambda n : setattr(self, 'assignment_schedule_instances', n.get_collection_of_object_values(privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance)),
            "assignmentScheduleRequests": lambda n : setattr(self, 'assignment_schedule_requests', n.get_collection_of_object_values(privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest)),
            "eligibilitySchedules": lambda n : setattr(self, 'eligibility_schedules', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
            "eligibilityScheduleInstances": lambda n : setattr(self, 'eligibility_schedule_instances', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance)),
            "eligibilityScheduleRequests": lambda n : setattr(self, 'eligibility_schedule_requests', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest)),
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
        writer.write_collection_of_object_values("assignmentApprovals", self.assignment_approvals)
        writer.write_collection_of_object_values("assignmentSchedules", self.assignment_schedules)
        writer.write_collection_of_object_values("assignmentScheduleInstances", self.assignment_schedule_instances)
        writer.write_collection_of_object_values("assignmentScheduleRequests", self.assignment_schedule_requests)
        writer.write_collection_of_object_values("eligibilitySchedules", self.eligibility_schedules)
        writer.write_collection_of_object_values("eligibilityScheduleInstances", self.eligibility_schedule_instances)
        writer.write_collection_of_object_values("eligibilityScheduleRequests", self.eligibility_schedule_requests)
    

