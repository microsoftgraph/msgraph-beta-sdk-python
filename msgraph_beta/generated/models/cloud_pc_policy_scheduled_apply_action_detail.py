from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcPolicyScheduledApplyActionDetail(Entity, Parsable):
    # An expression that specifies the cron schedule. (For example, '0 0 0 20  ' means schedules a job to run at midnight on the 20th of every month) Administrators can set a cron expression to define the scheduling rules for automatic regular application. When auto-provision is disabled, cronScheduleExpression is set to null, stopping the automatic task scheduling. Read-Only.
    cron_schedule_expression: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The percentage of Cloud PCs to keep available. Administrators can set this property to a value from 0 to 99. Cloud PCs are reprovisioned only when there are no active and connected Cloud PC users. Frontline shared only.
    reserve_percentage: Optional[int] = None
    
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
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "cronScheduleExpression": lambda n : setattr(self, 'cron_schedule_expression', n.get_str_value()),
            "reservePercentage": lambda n : setattr(self, 'reserve_percentage', n.get_int_value()),
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
        writer.write_int_value("reservePercentage", self.reserve_percentage)
    

