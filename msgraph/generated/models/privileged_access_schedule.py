from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, privileged_access_group_assignment_schedule, privileged_access_group_eligibility_schedule, request_schedule

from . import entity

class PrivilegedAccessSchedule(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedAccessSchedule and sets the default values.
        """
        super().__init__()
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The createdUsing property
        self._created_using: Optional[str] = None
        # The modifiedDateTime property
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scheduleInfo property
        self._schedule_info: Optional[request_schedule.RequestSchedule] = None
        # The status property
        self._status: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @property
    def created_using(self,) -> Optional[str]:
        """
        Gets the createdUsing property value. The createdUsing property
        Returns: Optional[str]
        """
        return self._created_using
    
    @created_using.setter
    def created_using(self,value: Optional[str] = None) -> None:
        """
        Sets the createdUsing property value. The createdUsing property
        Args:
            value: Value to set for the created_using property.
        """
        self._created_using = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule":
                from . import privileged_access_group_assignment_schedule

                return privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule()
            if mapping_value == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule":
                from . import privileged_access_group_eligibility_schedule

                return privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule()
        return PrivilegedAccessSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, privileged_access_group_assignment_schedule, privileged_access_group_eligibility_schedule, request_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdUsing": lambda n : setattr(self, 'created_using', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The modifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The modifiedDateTime property
        Args:
            value: Value to set for the modified_date_time property.
        """
        self._modified_date_time = value
    
    @property
    def schedule_info(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the scheduleInfo property value. The scheduleInfo property
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule_info
    
    @schedule_info.setter
    def schedule_info(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the scheduleInfo property value. The scheduleInfo property
        Args:
            value: Value to set for the schedule_info property.
        """
        self._schedule_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("createdUsing", self.created_using)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

