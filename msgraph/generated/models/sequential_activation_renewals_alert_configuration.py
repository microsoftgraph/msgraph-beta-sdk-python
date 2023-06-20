from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_configuration

from . import unified_role_management_alert_configuration

@dataclass
class SequentialActivationRenewalsAlertConfiguration(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration):
    odata_type = "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration"
    # The sequentialActivationCounterThreshold property
    sequential_activation_counter_threshold: Optional[int] = None
    # The timeIntervalBetweenActivations property
    time_interval_between_activations: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SequentialActivationRenewalsAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SequentialActivationRenewalsAlertConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SequentialActivationRenewalsAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_configuration

        from . import unified_role_management_alert_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "sequentialActivationCounterThreshold": lambda n : setattr(self, 'sequential_activation_counter_threshold', n.get_int_value()),
            "timeIntervalBetweenActivations": lambda n : setattr(self, 'time_interval_between_activations', n.get_timedelta_value()),
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
        writer.write_int_value("sequentialActivationCounterThreshold", self.sequential_activation_counter_threshold)
        writer.write_timedelta_value("timeIntervalBetweenActivations", self.time_interval_between_activations)
    

