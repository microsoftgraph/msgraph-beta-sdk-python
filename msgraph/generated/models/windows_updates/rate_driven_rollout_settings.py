from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import gradual_rollout_settings

from . import gradual_rollout_settings

class RateDrivenRolloutSettings(gradual_rollout_settings.GradualRolloutSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new RateDrivenRolloutSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.rateDrivenRolloutSettings"
        # Specifies the number of devices that are offered at the same time. When not set, all devices in the deployment are offered content at the same time.
        self._devices_per_offer: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RateDrivenRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RateDrivenRolloutSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RateDrivenRolloutSettings()
    
    @property
    def devices_per_offer(self,) -> Optional[int]:
        """
        Gets the devicesPerOffer property value. Specifies the number of devices that are offered at the same time. When not set, all devices in the deployment are offered content at the same time.
        Returns: Optional[int]
        """
        return self._devices_per_offer
    
    @devices_per_offer.setter
    def devices_per_offer(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesPerOffer property value. Specifies the number of devices that are offered at the same time. When not set, all devices in the deployment are offered content at the same time.
        Args:
            value: Value to set for the devices_per_offer property.
        """
        self._devices_per_offer = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import gradual_rollout_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "devicesPerOffer": lambda n : setattr(self, 'devices_per_offer', n.get_int_value()),
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
        writer.write_int_value("devicesPerOffer", self.devices_per_offer)
    

