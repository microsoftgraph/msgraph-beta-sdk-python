from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .request_schedule import RequestSchedule
    from .unified_role_schedule_base import UnifiedRoleScheduleBase

from .unified_role_schedule_base import UnifiedRoleScheduleBase

@dataclass
class UnifiedRoleEligibilitySchedule(UnifiedRoleScheduleBase):
    # Membership type of the eligible assignment. It can either be Inherited, Direct, or Group. Supports $filter (eq).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The schedule object of the eligible role assignment request.
    schedule_info: Optional[RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleEligibilitySchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleEligibilitySchedule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleEligibilitySchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .request_schedule import RequestSchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        from .request_schedule import RequestSchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        fields: Dict[str, Callable[[Any], None]] = {
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

