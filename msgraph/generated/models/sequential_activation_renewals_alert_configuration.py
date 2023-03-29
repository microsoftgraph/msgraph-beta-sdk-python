from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_configuration

from . import unified_role_management_alert_configuration

class SequentialActivationRenewalsAlertConfiguration(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new SequentialActivationRenewalsAlertConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration"
        # The sequentialActivationCounterThreshold property
        self._sequential_activation_counter_threshold: Optional[int] = None
        # The timeIntervalBetweenActivations property
        self._time_interval_between_activations: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SequentialActivationRenewalsAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SequentialActivationRenewalsAlertConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SequentialActivationRenewalsAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "sequentialActivationCounterThreshold": lambda n : setattr(self, 'sequential_activation_counter_threshold', n.get_int_value()),
            "timeIntervalBetweenActivations": lambda n : setattr(self, 'time_interval_between_activations', n.get_timedelta_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def sequential_activation_counter_threshold(self,) -> Optional[int]:
        """
        Gets the sequentialActivationCounterThreshold property value. The sequentialActivationCounterThreshold property
        Returns: Optional[int]
        """
        return self._sequential_activation_counter_threshold
    
    @sequential_activation_counter_threshold.setter
    def sequential_activation_counter_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the sequentialActivationCounterThreshold property value. The sequentialActivationCounterThreshold property
        Args:
            value: Value to set for the sequential_activation_counter_threshold property.
        """
        self._sequential_activation_counter_threshold = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("sequentialActivationCounterThreshold", self.sequential_activation_counter_threshold)
        writer.write_timedelta_value("timeIntervalBetweenActivations", self.time_interval_between_activations)
    
    @property
    def time_interval_between_activations(self,) -> Optional[timedelta]:
        """
        Gets the timeIntervalBetweenActivations property value. The timeIntervalBetweenActivations property
        Returns: Optional[timedelta]
        """
        return self._time_interval_between_activations
    
    @time_interval_between_activations.setter
    def time_interval_between_activations(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the timeIntervalBetweenActivations property value. The timeIntervalBetweenActivations property
        Args:
            value: Value to set for the time_interval_between_activations property.
        """
        self._time_interval_between_activations = value
    

