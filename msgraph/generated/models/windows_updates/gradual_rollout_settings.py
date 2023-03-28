from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import date_driven_rollout_settings, duration_driven_rollout_settings, rate_driven_rollout_settings

class GradualRolloutSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new gradualRolloutSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The duration between each set of devices being offered the update. The value is represented in ISO 8601 format for duration. Default value is P1D (1 day).
        self._duration_between_offers: Optional[timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GradualRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GradualRolloutSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsUpdates.dateDrivenRolloutSettings":
                from . import date_driven_rollout_settings

                return date_driven_rollout_settings.DateDrivenRolloutSettings()
            if mapping_value == "#microsoft.graph.windowsUpdates.durationDrivenRolloutSettings":
                from . import duration_driven_rollout_settings

                return duration_driven_rollout_settings.DurationDrivenRolloutSettings()
            if mapping_value == "#microsoft.graph.windowsUpdates.rateDrivenRolloutSettings":
                from . import rate_driven_rollout_settings

                return rate_driven_rollout_settings.RateDrivenRolloutSettings()
        return GradualRolloutSettings()
    
    @property
    def duration_between_offers(self,) -> Optional[timedelta]:
        """
        Gets the durationBetweenOffers property value. The duration between each set of devices being offered the update. The value is represented in ISO 8601 format for duration. Default value is P1D (1 day).
        Returns: Optional[timedelta]
        """
        return self._duration_between_offers
    
    @duration_between_offers.setter
    def duration_between_offers(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the durationBetweenOffers property value. The duration between each set of devices being offered the update. The value is represented in ISO 8601 format for duration. Default value is P1D (1 day).
        Args:
            value: Value to set for the duration_between_offers property.
        """
        self._duration_between_offers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import date_driven_rollout_settings, duration_driven_rollout_settings, rate_driven_rollout_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "durationBetweenOffers": lambda n : setattr(self, 'duration_between_offers', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_timedelta_value("durationBetweenOffers", self.duration_between_offers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

