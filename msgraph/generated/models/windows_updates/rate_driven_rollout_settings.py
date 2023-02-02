from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

gradual_rollout_settings = lazy_import('msgraph.generated.models.windows_updates.gradual_rollout_settings')

class RateDrivenRolloutSettings(gradual_rollout_settings.GradualRolloutSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new RateDrivenRolloutSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.rateDrivenRolloutSettings"
        # The devicesPerOffer property
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
        Gets the devicesPerOffer property value. The devicesPerOffer property
        Returns: Optional[int]
        """
        return self._devices_per_offer
    
    @devices_per_offer.setter
    def devices_per_offer(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesPerOffer property value. The devicesPerOffer property
        Args:
            value: Value to set for the devices_per_offer property.
        """
        self._devices_per_offer = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
    

