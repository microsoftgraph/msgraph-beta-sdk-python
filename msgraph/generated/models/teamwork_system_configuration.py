from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_date_time_configuration, teamwork_network_configuration

@dataclass
class TeamworkSystemConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date and time configurations for a device.
    date_time_configuration: Optional[teamwork_date_time_configuration.TeamworkDateTimeConfiguration] = None
    # The default password for the device. Write-Only.
    default_password: Optional[str] = None
    # The device lock timeout in seconds.
    device_lock_timeout: Optional[timedelta] = None
    # True if the device lock is enabled.
    is_device_lock_enabled: Optional[bool] = None
    # True if logging is enabled.
    is_logging_enabled: Optional[bool] = None
    # True if power saving is enabled.
    is_power_saving_enabled: Optional[bool] = None
    # True if screen capture is enabled.
    is_screen_capture_enabled: Optional[bool] = None
    # True if silent mode is enabled.
    is_silent_mode_enabled: Optional[bool] = None
    # The language option for the device.
    language: Optional[str] = None
    # The pin that unlocks the device. Write-Only.
    lock_pin: Optional[str] = None
    # The logging level for the device.
    logging_level: Optional[str] = None
    # The network configuration for the device.
    network_configuration: Optional[teamwork_network_configuration.TeamworkNetworkConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSystemConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSystemConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkSystemConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_date_time_configuration, teamwork_network_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "dateTimeConfiguration": lambda n : setattr(self, 'date_time_configuration', n.get_object_value(teamwork_date_time_configuration.TeamworkDateTimeConfiguration)),
            "defaultPassword": lambda n : setattr(self, 'default_password', n.get_str_value()),
            "deviceLockTimeout": lambda n : setattr(self, 'device_lock_timeout', n.get_timedelta_value()),
            "isDeviceLockEnabled": lambda n : setattr(self, 'is_device_lock_enabled', n.get_bool_value()),
            "isLoggingEnabled": lambda n : setattr(self, 'is_logging_enabled', n.get_bool_value()),
            "isPowerSavingEnabled": lambda n : setattr(self, 'is_power_saving_enabled', n.get_bool_value()),
            "isScreenCaptureEnabled": lambda n : setattr(self, 'is_screen_capture_enabled', n.get_bool_value()),
            "isSilentModeEnabled": lambda n : setattr(self, 'is_silent_mode_enabled', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lockPin": lambda n : setattr(self, 'lock_pin', n.get_str_value()),
            "loggingLevel": lambda n : setattr(self, 'logging_level', n.get_str_value()),
            "networkConfiguration": lambda n : setattr(self, 'network_configuration', n.get_object_value(teamwork_network_configuration.TeamworkNetworkConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("dateTimeConfiguration", self.date_time_configuration)
        writer.write_str_value("defaultPassword", self.default_password)
        writer.write_timedelta_value("deviceLockTimeout", self.device_lock_timeout)
        writer.write_bool_value("isDeviceLockEnabled", self.is_device_lock_enabled)
        writer.write_bool_value("isLoggingEnabled", self.is_logging_enabled)
        writer.write_bool_value("isPowerSavingEnabled", self.is_power_saving_enabled)
        writer.write_bool_value("isScreenCaptureEnabled", self.is_screen_capture_enabled)
        writer.write_bool_value("isSilentModeEnabled", self.is_silent_mode_enabled)
        writer.write_str_value("language", self.language)
        writer.write_str_value("lockPin", self.lock_pin)
        writer.write_str_value("loggingLevel", self.logging_level)
        writer.write_object_value("networkConfiguration", self.network_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

