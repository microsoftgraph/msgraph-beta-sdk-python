from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class TeamworkDisplayScreenConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDisplayScreenConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The brightness level on the device (0-100). Not applicable for Microsoft Teams Rooms devices.
        self._backlight_brightness: Optional[int] = None
        # Timeout for backlight (30-3600 secs). Not applicable for Teams Rooms devices.
        self._backlight_timeout: Optional[timedelta] = None
        # True if high contrast mode is enabled. Not applicable for Teams Rooms devices.
        self._is_high_contrast_enabled: Optional[bool] = None
        # True if screensaver is enabled. Not applicable for Teams Rooms devices.
        self._is_screensaver_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Screensaver timeout from 30 to 3600 secs. Not applicable for Teams Rooms devices.
        self._screensaver_timeout: Optional[timedelta] = None
    
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
    
    @property
    def backlight_brightness(self,) -> Optional[int]:
        """
        Gets the backlightBrightness property value. The brightness level on the device (0-100). Not applicable for Microsoft Teams Rooms devices.
        Returns: Optional[int]
        """
        return self._backlight_brightness
    
    @backlight_brightness.setter
    def backlight_brightness(self,value: Optional[int] = None) -> None:
        """
        Sets the backlightBrightness property value. The brightness level on the device (0-100). Not applicable for Microsoft Teams Rooms devices.
        Args:
            value: Value to set for the backlight_brightness property.
        """
        self._backlight_brightness = value
    
    @property
    def backlight_timeout(self,) -> Optional[timedelta]:
        """
        Gets the backlightTimeout property value. Timeout for backlight (30-3600 secs). Not applicable for Teams Rooms devices.
        Returns: Optional[timedelta]
        """
        return self._backlight_timeout
    
    @backlight_timeout.setter
    def backlight_timeout(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the backlightTimeout property value. Timeout for backlight (30-3600 secs). Not applicable for Teams Rooms devices.
        Args:
            value: Value to set for the backlight_timeout property.
        """
        self._backlight_timeout = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDisplayScreenConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDisplayScreenConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
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
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "screensaverTimeout": lambda n : setattr(self, 'screensaver_timeout', n.get_timedelta_value()),
        }
        return fields
    
    @property
    def is_high_contrast_enabled(self,) -> Optional[bool]:
        """
        Gets the isHighContrastEnabled property value. True if high contrast mode is enabled. Not applicable for Teams Rooms devices.
        Returns: Optional[bool]
        """
        return self._is_high_contrast_enabled
    
    @is_high_contrast_enabled.setter
    def is_high_contrast_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHighContrastEnabled property value. True if high contrast mode is enabled. Not applicable for Teams Rooms devices.
        Args:
            value: Value to set for the is_high_contrast_enabled property.
        """
        self._is_high_contrast_enabled = value
    
    @property
    def is_screensaver_enabled(self,) -> Optional[bool]:
        """
        Gets the isScreensaverEnabled property value. True if screensaver is enabled. Not applicable for Teams Rooms devices.
        Returns: Optional[bool]
        """
        return self._is_screensaver_enabled
    
    @is_screensaver_enabled.setter
    def is_screensaver_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isScreensaverEnabled property value. True if screensaver is enabled. Not applicable for Teams Rooms devices.
        Args:
            value: Value to set for the is_screensaver_enabled property.
        """
        self._is_screensaver_enabled = value
    
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
    
    @property
    def screensaver_timeout(self,) -> Optional[timedelta]:
        """
        Gets the screensaverTimeout property value. Screensaver timeout from 30 to 3600 secs. Not applicable for Teams Rooms devices.
        Returns: Optional[timedelta]
        """
        return self._screensaver_timeout
    
    @screensaver_timeout.setter
    def screensaver_timeout(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the screensaverTimeout property value. Screensaver timeout from 30 to 3600 secs. Not applicable for Teams Rooms devices.
        Args:
            value: Value to set for the screensaver_timeout property.
        """
        self._screensaver_timeout = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("backlightBrightness", self.backlight_brightness)
        writer.write_timedelta_value("backlightTimeout", self.backlight_timeout)
        writer.write_bool_value("isHighContrastEnabled", self.is_high_contrast_enabled)
        writer.write_bool_value("isScreensaverEnabled", self.is_screensaver_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_timedelta_value("screensaverTimeout", self.screensaver_timeout)
        writer.write_additional_data_value(self.additional_data)
    

