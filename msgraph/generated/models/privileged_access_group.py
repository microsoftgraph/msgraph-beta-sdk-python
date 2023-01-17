from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
privileged_access_group_assignment_schedule = lazy_import('msgraph.generated.models.privileged_access_group_assignment_schedule')
privileged_access_group_assignment_schedule_instance = lazy_import('msgraph.generated.models.privileged_access_group_assignment_schedule_instance')
privileged_access_group_assignment_schedule_request = lazy_import('msgraph.generated.models.privileged_access_group_assignment_schedule_request')
privileged_access_group_eligibility_schedule = lazy_import('msgraph.generated.models.privileged_access_group_eligibility_schedule')
privileged_access_group_eligibility_schedule_instance = lazy_import('msgraph.generated.models.privileged_access_group_eligibility_schedule_instance')
privileged_access_group_eligibility_schedule_request = lazy_import('msgraph.generated.models.privileged_access_group_eligibility_schedule_request')

class PrivilegedAccessGroup(entity.Entity):
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
            value: Value to set for the assignmentScheduleInstances property.
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
            value: Value to set for the assignmentScheduleRequests property.
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
            value: Value to set for the assignmentSchedules property.
        """
        self._assignment_schedules = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedAccessGroup and sets the default values.
        """
        super().__init__()
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
            value: Value to set for the eligibilityScheduleInstances property.
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
            value: Value to set for the eligibilityScheduleRequests property.
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
            value: Value to set for the eligibilitySchedules property.
        """
        self._eligibility_schedules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_schedule_instances": lambda n : setattr(self, 'assignment_schedule_instances', n.get_collection_of_object_values(privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance)),
            "assignment_schedule_requests": lambda n : setattr(self, 'assignment_schedule_requests', n.get_collection_of_object_values(privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest)),
            "assignment_schedules": lambda n : setattr(self, 'assignment_schedules', n.get_collection_of_object_values(privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule)),
            "eligibility_schedule_instances": lambda n : setattr(self, 'eligibility_schedule_instances', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance)),
            "eligibility_schedule_requests": lambda n : setattr(self, 'eligibility_schedule_requests', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest)),
            "eligibility_schedules": lambda n : setattr(self, 'eligibility_schedules', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
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
        writer.write_collection_of_object_values("assignmentScheduleInstances", self.assignment_schedule_instances)
        writer.write_collection_of_object_values("assignmentScheduleRequests", self.assignment_schedule_requests)
        writer.write_collection_of_object_values("assignmentSchedules", self.assignment_schedules)
        writer.write_collection_of_object_values("eligibilityScheduleInstances", self.eligibility_schedule_instances)
        writer.write_collection_of_object_values("eligibilityScheduleRequests", self.eligibility_schedule_requests)
        writer.write_collection_of_object_values("eligibilitySchedules", self.eligibility_schedules)
    

