from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_date_time_configuration = lazy_import('msgraph.generated.models.teamwork_date_time_configuration')
teamwork_network_configuration = lazy_import('msgraph.generated.models.teamwork_network_configuration')

class TeamworkSystemConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamworkSystemConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date and time configurations for a device.
        self._date_time_configuration: Optional[teamwork_date_time_configuration.TeamworkDateTimeConfiguration] = None
        # The default password for the device. Write-Only.
        self._default_password: Optional[str] = None
        # The device lock timeout in seconds.
        self._device_lock_timeout: Optional[Timedelta] = None
        # True if the device lock is enabled.
        self._is_device_lock_enabled: Optional[bool] = None
        # True if logging is enabled.
        self._is_logging_enabled: Optional[bool] = None
        # True if power saving is enabled.
        self._is_power_saving_enabled: Optional[bool] = None
        # True if screen capture is enabled.
        self._is_screen_capture_enabled: Optional[bool] = None
        # True if silent mode is enabled.
        self._is_silent_mode_enabled: Optional[bool] = None
        # The language option for the device.
        self._language: Optional[str] = None
        # The pin that unlocks the device. Write-Only.
        self._lock_pin: Optional[str] = None
        # The logging level for the device.
        self._logging_level: Optional[str] = None
        # The network configuration for the device.
        self._network_configuration: Optional[teamwork_network_configuration.TeamworkNetworkConfiguration] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @property
    def date_time_configuration(self,) -> Optional[teamwork_date_time_configuration.TeamworkDateTimeConfiguration]:
        """
        Gets the dateTimeConfiguration property value. The date and time configurations for a device.
        Returns: Optional[teamwork_date_time_configuration.TeamworkDateTimeConfiguration]
        """
        return self._date_time_configuration
    
    @date_time_configuration.setter
    def date_time_configuration(self,value: Optional[teamwork_date_time_configuration.TeamworkDateTimeConfiguration] = None) -> None:
        """
        Sets the dateTimeConfiguration property value. The date and time configurations for a device.
        Args:
            value: Value to set for the dateTimeConfiguration property.
        """
        self._date_time_configuration = value
    
    @property
    def default_password(self,) -> Optional[str]:
        """
        Gets the defaultPassword property value. The default password for the device. Write-Only.
        Returns: Optional[str]
        """
        return self._default_password
    
    @default_password.setter
    def default_password(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultPassword property value. The default password for the device. Write-Only.
        Args:
            value: Value to set for the defaultPassword property.
        """
        self._default_password = value
    
    @property
    def device_lock_timeout(self,) -> Optional[Timedelta]:
        """
        Gets the deviceLockTimeout property value. The device lock timeout in seconds.
        Returns: Optional[Timedelta]
        """
        return self._device_lock_timeout
    
    @device_lock_timeout.setter
    def device_lock_timeout(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the deviceLockTimeout property value. The device lock timeout in seconds.
        Args:
            value: Value to set for the deviceLockTimeout property.
        """
        self._device_lock_timeout = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "date_time_configuration": lambda n : setattr(self, 'date_time_configuration', n.get_object_value(teamwork_date_time_configuration.TeamworkDateTimeConfiguration)),
            "default_password": lambda n : setattr(self, 'default_password', n.get_str_value()),
            "device_lock_timeout": lambda n : setattr(self, 'device_lock_timeout', n.get_object_value(Timedelta)),
            "is_device_lock_enabled": lambda n : setattr(self, 'is_device_lock_enabled', n.get_bool_value()),
            "is_logging_enabled": lambda n : setattr(self, 'is_logging_enabled', n.get_bool_value()),
            "is_power_saving_enabled": lambda n : setattr(self, 'is_power_saving_enabled', n.get_bool_value()),
            "is_screen_capture_enabled": lambda n : setattr(self, 'is_screen_capture_enabled', n.get_bool_value()),
            "is_silent_mode_enabled": lambda n : setattr(self, 'is_silent_mode_enabled', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lock_pin": lambda n : setattr(self, 'lock_pin', n.get_str_value()),
            "logging_level": lambda n : setattr(self, 'logging_level', n.get_str_value()),
            "network_configuration": lambda n : setattr(self, 'network_configuration', n.get_object_value(teamwork_network_configuration.TeamworkNetworkConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_device_lock_enabled(self,) -> Optional[bool]:
        """
        Gets the isDeviceLockEnabled property value. True if the device lock is enabled.
        Returns: Optional[bool]
        """
        return self._is_device_lock_enabled
    
    @is_device_lock_enabled.setter
    def is_device_lock_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeviceLockEnabled property value. True if the device lock is enabled.
        Args:
            value: Value to set for the isDeviceLockEnabled property.
        """
        self._is_device_lock_enabled = value
    
    @property
    def is_logging_enabled(self,) -> Optional[bool]:
        """
        Gets the isLoggingEnabled property value. True if logging is enabled.
        Returns: Optional[bool]
        """
        return self._is_logging_enabled
    
    @is_logging_enabled.setter
    def is_logging_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLoggingEnabled property value. True if logging is enabled.
        Args:
            value: Value to set for the isLoggingEnabled property.
        """
        self._is_logging_enabled = value
    
    @property
    def is_power_saving_enabled(self,) -> Optional[bool]:
        """
        Gets the isPowerSavingEnabled property value. True if power saving is enabled.
        Returns: Optional[bool]
        """
        return self._is_power_saving_enabled
    
    @is_power_saving_enabled.setter
    def is_power_saving_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPowerSavingEnabled property value. True if power saving is enabled.
        Args:
            value: Value to set for the isPowerSavingEnabled property.
        """
        self._is_power_saving_enabled = value
    
    @property
    def is_screen_capture_enabled(self,) -> Optional[bool]:
        """
        Gets the isScreenCaptureEnabled property value. True if screen capture is enabled.
        Returns: Optional[bool]
        """
        return self._is_screen_capture_enabled
    
    @is_screen_capture_enabled.setter
    def is_screen_capture_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isScreenCaptureEnabled property value. True if screen capture is enabled.
        Args:
            value: Value to set for the isScreenCaptureEnabled property.
        """
        self._is_screen_capture_enabled = value
    
    @property
    def is_silent_mode_enabled(self,) -> Optional[bool]:
        """
        Gets the isSilentModeEnabled property value. True if silent mode is enabled.
        Returns: Optional[bool]
        """
        return self._is_silent_mode_enabled
    
    @is_silent_mode_enabled.setter
    def is_silent_mode_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSilentModeEnabled property value. True if silent mode is enabled.
        Args:
            value: Value to set for the isSilentModeEnabled property.
        """
        self._is_silent_mode_enabled = value
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. The language option for the device.
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. The language option for the device.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def lock_pin(self,) -> Optional[str]:
        """
        Gets the lockPin property value. The pin that unlocks the device. Write-Only.
        Returns: Optional[str]
        """
        return self._lock_pin
    
    @lock_pin.setter
    def lock_pin(self,value: Optional[str] = None) -> None:
        """
        Sets the lockPin property value. The pin that unlocks the device. Write-Only.
        Args:
            value: Value to set for the lockPin property.
        """
        self._lock_pin = value
    
    @property
    def logging_level(self,) -> Optional[str]:
        """
        Gets the loggingLevel property value. The logging level for the device.
        Returns: Optional[str]
        """
        return self._logging_level
    
    @logging_level.setter
    def logging_level(self,value: Optional[str] = None) -> None:
        """
        Sets the loggingLevel property value. The logging level for the device.
        Args:
            value: Value to set for the loggingLevel property.
        """
        self._logging_level = value
    
    @property
    def network_configuration(self,) -> Optional[teamwork_network_configuration.TeamworkNetworkConfiguration]:
        """
        Gets the networkConfiguration property value. The network configuration for the device.
        Returns: Optional[teamwork_network_configuration.TeamworkNetworkConfiguration]
        """
        return self._network_configuration
    
    @network_configuration.setter
    def network_configuration(self,value: Optional[teamwork_network_configuration.TeamworkNetworkConfiguration] = None) -> None:
        """
        Sets the networkConfiguration property value. The network configuration for the device.
        Args:
            value: Value to set for the networkConfiguration property.
        """
        self._network_configuration = value
    
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
        writer.write_object_value("deviceLockTimeout", self.device_lock_timeout)
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
    

