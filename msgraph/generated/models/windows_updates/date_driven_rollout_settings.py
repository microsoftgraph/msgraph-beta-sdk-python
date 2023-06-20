from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import gradual_rollout_settings

from . import gradual_rollout_settings

@dataclass
class DateDrivenRolloutSettings(gradual_rollout_settings.GradualRolloutSettings):
    odata_type = "#microsoft.graph.windowsUpdates.dateDrivenRolloutSettings"
    # Specifies the date before which all devices currently in the deployment are offered the update. Devices added after this date are offered immediately. When the endDateTime is not set, all devices in the deployment are offered content at the same time.
    end_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DateDrivenRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DateDrivenRolloutSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DateDrivenRolloutSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import gradual_rollout_settings

        from . import gradual_rollout_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("endDateTime", self.end_date_time)
    

