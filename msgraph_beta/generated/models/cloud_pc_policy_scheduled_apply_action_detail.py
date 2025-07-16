from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_policy_timezone import CloudPcPolicyTimezone
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcPolicyScheduledApplyActionDetail(Entity, Parsable):
    # An expression that specifies the cron schedule. (For example, '0 0 0 20  ' means schedules a job to run at midnight on the 20th of every month) Administrators can set a cron expression to define the scheduling rules for automatic regular application. When auto provision is disabled, cronScheduleExpression is set to null, stopping the automatic task scheduling. Read-Only.
    cron_schedule_expression: Optional[str] = None
    # Indicates IT Admins can set an end date to define the last scheduler run before this time. If not set, the scheduler runs continuously. There is no time zone information at this time; it needs to be coordinated with timezone, for example, '2025-02-01 00:00:00' with 'China Standard Time' means the scheduling rule takes effect before Feb 01 2025 00:00:00 GMT+0800 (China Standard Time).
    end_date_time: Optional[str] = None
    # Indicates IT Admins can see when the next automatic regular apply is executed. It needs to be coordinated with timezone, for example, '2025-01-01 00:00:00' with 'China Standard Time' means the next task executes at Jan 01 2025 00:00:00 GMT+0800 (China Standard Time). Read-Only.
    next_run_date_time: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The percentage of Cloud PCs to keep available. Administrators can set this property to a value from 0 to 99. Cloud PCs are reprovisioned only when there are no active and connected Cloud PC users. Frontline shared only.
    reserve_percentage: Optional[int] = None
    # Indicates IT Admins can set a start date to define the first scheduler run after this time. If not set, the default is the current time. There is no time zone information at this time, it needs to be coordinated with timezone, for example, '2025-01-01 00:00:00' with 'China Standard Time' means the scheduling rule takes effect after Jan 01 2025 00:00:00 GMT+0800 (China Standard Time).
    start_date_time: Optional[str] = None
    # The timezone property
    timezone: Optional[CloudPcPolicyTimezone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcPolicyScheduledApplyActionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcPolicyScheduledApplyActionDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcPolicyScheduledApplyActionDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_policy_timezone import CloudPcPolicyTimezone
        from .entity import Entity

        from .cloud_pc_policy_timezone import CloudPcPolicyTimezone
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "cronScheduleExpression": lambda n : setattr(self, 'cron_schedule_expression', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_str_value()),
            "nextRunDateTime": lambda n : setattr(self, 'next_run_date_time', n.get_str_value()),
            "reservePercentage": lambda n : setattr(self, 'reserve_percentage', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_str_value()),
            "timezone": lambda n : setattr(self, 'timezone', n.get_enum_value(CloudPcPolicyTimezone)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("cronScheduleExpression", self.cron_schedule_expression)
        writer.write_str_value("endDateTime", self.end_date_time)
        writer.write_str_value("nextRunDateTime", self.next_run_date_time)
        writer.write_int_value("reservePercentage", self.reserve_percentage)
        writer.write_str_value("startDateTime", self.start_date_time)
        writer.write_enum_value("timezone", self.timezone)
    

