from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import gradual_rollout_settings

from . import gradual_rollout_settings

class DurationDrivenRolloutSettings(gradual_rollout_settings.GradualRolloutSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new DurationDrivenRolloutSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.durationDrivenRolloutSettings"
        # The target duration of the rollout. Given durationBetweenOffers and durationUntilDeploymentEnd, the system will automatically calculate how many devices are in each offering.
        self._duration_until_deployment_end: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DurationDrivenRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DurationDrivenRolloutSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DurationDrivenRolloutSettings()
    
    @property
    def duration_until_deployment_end(self,) -> Optional[timedelta]:
        """
        Gets the durationUntilDeploymentEnd property value. The target duration of the rollout. Given durationBetweenOffers and durationUntilDeploymentEnd, the system will automatically calculate how many devices are in each offering.
        Returns: Optional[timedelta]
        """
        return self._duration_until_deployment_end
    
    @duration_until_deployment_end.setter
    def duration_until_deployment_end(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the durationUntilDeploymentEnd property value. The target duration of the rollout. Given durationBetweenOffers and durationUntilDeploymentEnd, the system will automatically calculate how many devices are in each offering.
        Args:
            value: Value to set for the duration_until_deployment_end property.
        """
        self._duration_until_deployment_end = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import gradual_rollout_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "durationUntilDeploymentEnd": lambda n : setattr(self, 'duration_until_deployment_end', n.get_timedelta_value()),
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
        writer.write_timedelta_value("durationUntilDeploymentEnd", self.duration_until_deployment_end)
    

