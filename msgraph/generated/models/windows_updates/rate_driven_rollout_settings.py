from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gradual_rollout_settings import GradualRolloutSettings

from .gradual_rollout_settings import GradualRolloutSettings

@dataclass
class RateDrivenRolloutSettings(GradualRolloutSettings):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.rateDrivenRolloutSettings"
    # Specifies the number of devices that are offered at the same time. When not set, all devices in the deployment are offered content at the same time.
    devices_per_offer: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RateDrivenRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RateDrivenRolloutSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RateDrivenRolloutSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .gradual_rollout_settings import GradualRolloutSettings

        from .gradual_rollout_settings import GradualRolloutSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "devicesPerOffer": lambda n : setattr(self, 'devices_per_offer', n.get_int_value()),
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
        writer.write_int_value("devicesPerOffer", self.devices_per_offer)
    

