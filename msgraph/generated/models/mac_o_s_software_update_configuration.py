from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_update_time_window = lazy_import('msgraph.generated.models.custom_update_time_window')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
mac_o_s_software_update_behavior = lazy_import('msgraph.generated.models.mac_o_s_software_update_behavior')
mac_o_s_software_update_schedule_type = lazy_import('msgraph.generated.models.mac_o_s_software_update_schedule_type')

class MacOSSoftwareUpdateConfiguration(device_configuration.DeviceConfiguration):
    @property
    def all_other_update_behavior(self,) -> Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]:
        """
        Gets the allOtherUpdateBehavior property value. Update behavior options for macOS software updates.
        Returns: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]
        """
        return self._all_other_update_behavior
    
    @all_other_update_behavior.setter
    def all_other_update_behavior(self,value: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None) -> None:
        """
        Sets the allOtherUpdateBehavior property value. Update behavior options for macOS software updates.
        Args:
            value: Value to set for the allOtherUpdateBehavior property.
        """
        self._all_other_update_behavior = value
    
    @property
    def config_data_update_behavior(self,) -> Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]:
        """
        Gets the configDataUpdateBehavior property value. Update behavior options for macOS software updates.
        Returns: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]
        """
        return self._config_data_update_behavior
    
    @config_data_update_behavior.setter
    def config_data_update_behavior(self,value: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None) -> None:
        """
        Sets the configDataUpdateBehavior property value. Update behavior options for macOS software updates.
        Args:
            value: Value to set for the configDataUpdateBehavior property.
        """
        self._config_data_update_behavior = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSSoftwareUpdateConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSSoftwareUpdateConfiguration"
        # Update behavior options for macOS software updates.
        self._all_other_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
        # Update behavior options for macOS software updates.
        self._config_data_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
        # Update behavior options for macOS software updates.
        self._critical_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
        # Custom Time windows when updates will be allowed or blocked. This collection can contain a maximum of 20 elements.
        self._custom_update_time_windows: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]] = None
        # Update behavior options for macOS software updates.
        self._firmware_update_behavior: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None
        # Update schedule type for macOS software updates.
        self._update_schedule_type: Optional[mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType] = None
        # Minutes indicating UTC offset for each update time window
        self._update_time_window_utc_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSoftwareUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSSoftwareUpdateConfiguration()
    
    @property
    def critical_update_behavior(self,) -> Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]:
        """
        Gets the criticalUpdateBehavior property value. Update behavior options for macOS software updates.
        Returns: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]
        """
        return self._critical_update_behavior
    
    @critical_update_behavior.setter
    def critical_update_behavior(self,value: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None) -> None:
        """
        Sets the criticalUpdateBehavior property value. Update behavior options for macOS software updates.
        Args:
            value: Value to set for the criticalUpdateBehavior property.
        """
        self._critical_update_behavior = value
    
    @property
    def custom_update_time_windows(self,) -> Optional[List[custom_update_time_window.CustomUpdateTimeWindow]]:
        """
        Gets the customUpdateTimeWindows property value. Custom Time windows when updates will be allowed or blocked. This collection can contain a maximum of 20 elements.
        Returns: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]]
        """
        return self._custom_update_time_windows
    
    @custom_update_time_windows.setter
    def custom_update_time_windows(self,value: Optional[List[custom_update_time_window.CustomUpdateTimeWindow]] = None) -> None:
        """
        Sets the customUpdateTimeWindows property value. Custom Time windows when updates will be allowed or blocked. This collection can contain a maximum of 20 elements.
        Args:
            value: Value to set for the customUpdateTimeWindows property.
        """
        self._custom_update_time_windows = value
    
    @property
    def firmware_update_behavior(self,) -> Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]:
        """
        Gets the firmwareUpdateBehavior property value. Update behavior options for macOS software updates.
        Returns: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior]
        """
        return self._firmware_update_behavior
    
    @firmware_update_behavior.setter
    def firmware_update_behavior(self,value: Optional[mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior] = None) -> None:
        """
        Sets the firmwareUpdateBehavior property value. Update behavior options for macOS software updates.
        Args:
            value: Value to set for the firmwareUpdateBehavior property.
        """
        self._firmware_update_behavior = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "all_other_update_behavior": lambda n : setattr(self, 'all_other_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "config_data_update_behavior": lambda n : setattr(self, 'config_data_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "critical_update_behavior": lambda n : setattr(self, 'critical_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "custom_update_time_windows": lambda n : setattr(self, 'custom_update_time_windows', n.get_collection_of_object_values(custom_update_time_window.CustomUpdateTimeWindow)),
            "firmware_update_behavior": lambda n : setattr(self, 'firmware_update_behavior', n.get_enum_value(mac_o_s_software_update_behavior.MacOSSoftwareUpdateBehavior)),
            "update_schedule_type": lambda n : setattr(self, 'update_schedule_type', n.get_enum_value(mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType)),
            "update_time_window_utc_offset_in_minutes": lambda n : setattr(self, 'update_time_window_utc_offset_in_minutes', n.get_int_value()),
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
        writer.write_enum_value("allOtherUpdateBehavior", self.all_other_update_behavior)
        writer.write_enum_value("configDataUpdateBehavior", self.config_data_update_behavior)
        writer.write_enum_value("criticalUpdateBehavior", self.critical_update_behavior)
        writer.write_collection_of_object_values("customUpdateTimeWindows", self.custom_update_time_windows)
        writer.write_enum_value("firmwareUpdateBehavior", self.firmware_update_behavior)
        writer.write_enum_value("updateScheduleType", self.update_schedule_type)
        writer.write_int_value("updateTimeWindowUtcOffsetInMinutes", self.update_time_window_utc_offset_in_minutes)
    
    @property
    def update_schedule_type(self,) -> Optional[mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType]:
        """
        Gets the updateScheduleType property value. Update schedule type for macOS software updates.
        Returns: Optional[mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType]
        """
        return self._update_schedule_type
    
    @update_schedule_type.setter
    def update_schedule_type(self,value: Optional[mac_o_s_software_update_schedule_type.MacOSSoftwareUpdateScheduleType] = None) -> None:
        """
        Sets the updateScheduleType property value. Update schedule type for macOS software updates.
        Args:
            value: Value to set for the updateScheduleType property.
        """
        self._update_schedule_type = value
    
    @property
    def update_time_window_utc_offset_in_minutes(self,) -> Optional[int]:
        """
        Gets the updateTimeWindowUtcOffsetInMinutes property value. Minutes indicating UTC offset for each update time window
        Returns: Optional[int]
        """
        return self._update_time_window_utc_offset_in_minutes
    
    @update_time_window_utc_offset_in_minutes.setter
    def update_time_window_utc_offset_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the updateTimeWindowUtcOffsetInMinutes property value. Minutes indicating UTC offset for each update time window
        Args:
            value: Value to set for the updateTimeWindowUtcOffsetInMinutes property.
        """
        self._update_time_window_utc_offset_in_minutes = value
    

