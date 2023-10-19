from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkDisplayScreenConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The brightness level on the device (0-100). Not applicable for Microsoft Teams Rooms devices.
    backlight_brightness: Optional[int] = None
    # Timeout for backlight (30-3600 secs). Not applicable for Teams Rooms devices.
    backlight_timeout: Optional[datetime.timedelta] = None
    # True if high contrast mode is enabled. Not applicable for Teams Rooms devices.
    is_high_contrast_enabled: Optional[bool] = None
    # True if screensaver is enabled. Not applicable for Teams Rooms devices.
    is_screensaver_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Screensaver timeout from 30 to 3600 secs. Not applicable for Teams Rooms devices.
    screensaver_timeout: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDisplayScreenConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDisplayScreenConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDisplayScreenConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "backlightBrightness": lambda n : setattr(self, 'backlight_brightness', n.get_int_value()),
            "backlightTimeout": lambda n : setattr(self, 'backlight_timeout', n.get_timedelta_value()),
            "isHighContrastEnabled": lambda n : setattr(self, 'is_high_contrast_enabled', n.get_bool_value()),
            "isScreensaverEnabled": lambda n : setattr(self, 'is_screensaver_enabled', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "screensaverTimeout": lambda n : setattr(self, 'screensaver_timeout', n.get_timedelta_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("backlightBrightness", self.backlight_brightness)
        writer.write_timedelta_value("backlightTimeout", self.backlight_timeout)
        writer.write_bool_value("isHighContrastEnabled", self.is_high_contrast_enabled)
        writer.write_bool_value("isScreensaverEnabled", self.is_screensaver_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_timedelta_value("screensaverTimeout", self.screensaver_timeout)
        writer.write_additional_data_value(self.additional_data)
    

