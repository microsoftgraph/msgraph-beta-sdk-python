from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import request_schedule, unified_role_schedule_base

from . import unified_role_schedule_base

@dataclass
class UnifiedRoleEligibilitySchedule(unified_role_schedule_base.UnifiedRoleScheduleBase):
    # Membership type of the eligible assignment. It can either be Inherited, Direct, or Group. Supports $filter (eq).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The schedule object of the eligible role assignment request.
    schedule_info: Optional[request_schedule.RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleEligibilitySchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleEligibilitySchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleEligibilitySchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import request_schedule, unified_role_schedule_base

        fields: Dict[str, Callable[[Any], None]] = {
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
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
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

