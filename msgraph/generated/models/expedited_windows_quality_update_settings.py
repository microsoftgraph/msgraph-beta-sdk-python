from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ExpeditedWindowsQualityUpdateSettings(AdditionalDataHolder, Parsable):
    """
    A complex type to store the expedited quality update settings such as release date and days until forced reboot.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new expeditedWindowsQualityUpdateSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of days after installation that forced reboot will happen.
        self._days_until_forced_reboot: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The release date to identify a quality update.
        self._quality_update_release: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpeditedWindowsQualityUpdateSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExpeditedWindowsQualityUpdateSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExpeditedWindowsQualityUpdateSettings()
    
    @property
    def days_until_forced_reboot(self,) -> Optional[int]:
        """
        Gets the daysUntilForcedReboot property value. The number of days after installation that forced reboot will happen.
        Returns: Optional[int]
        """
        return self._days_until_forced_reboot
    
    @days_until_forced_reboot.setter
    def days_until_forced_reboot(self,value: Optional[int] = None) -> None:
        """
        Sets the daysUntilForcedReboot property value. The number of days after installation that forced reboot will happen.
        Args:
            value: Value to set for the daysUntilForcedReboot property.
        """
        self._days_until_forced_reboot = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "days_until_forced_reboot": lambda n : setattr(self, 'days_until_forced_reboot', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quality_update_release": lambda n : setattr(self, 'quality_update_release', n.get_str_value()),
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def quality_update_release(self,) -> Optional[str]:
        """
        Gets the qualityUpdateRelease property value. The release date to identify a quality update.
        Returns: Optional[str]
        """
        return self._quality_update_release
    
    @quality_update_release.setter
    def quality_update_release(self,value: Optional[str] = None) -> None:
        """
        Sets the qualityUpdateRelease property value. The release date to identify a quality update.
        Args:
            value: Value to set for the qualityUpdateRelease property.
        """
        self._quality_update_release = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("daysUntilForcedReboot", self.days_until_forced_reboot)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityUpdateRelease", self.quality_update_release)
        writer.write_additional_data_value(self.additional_data)
    

