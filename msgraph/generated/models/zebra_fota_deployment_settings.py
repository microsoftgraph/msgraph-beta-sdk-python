from __future__ import annotations
from datetime import datetime, time
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

zebra_fota_network_type = lazy_import('msgraph.generated.models.zebra_fota_network_type')
zebra_fota_schedule_mode = lazy_import('msgraph.generated.models.zebra_fota_schedule_mode')
zebra_fota_update_type = lazy_import('msgraph.generated.models.zebra_fota_update_type')

class ZebraFotaDeploymentSettings(AdditionalDataHolder, Parsable):
    """
    The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
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
    
    @property
    def battery_rule_minimum_battery_level_percentage(self,) -> Optional[int]:
        """
        Gets the batteryRuleMinimumBatteryLevelPercentage property value. Minimum battery level (%) required for both download and installation. Default: -1 (System defaults). Maximum is 100.
        Returns: Optional[int]
        """
        return self._battery_rule_minimum_battery_level_percentage
    
    @battery_rule_minimum_battery_level_percentage.setter
    def battery_rule_minimum_battery_level_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the batteryRuleMinimumBatteryLevelPercentage property value. Minimum battery level (%) required for both download and installation. Default: -1 (System defaults). Maximum is 100.
        Args:
            value: Value to set for the batteryRuleMinimumBatteryLevelPercentage property.
        """
        self._battery_rule_minimum_battery_level_percentage = value
    
    @property
    def battery_rule_require_charger(self,) -> Optional[bool]:
        """
        Gets the batteryRuleRequireCharger property value. Flag indicating if charger is required. When set to false, the client can install updates whether the device is in or out of the charger. Applied only for installation. Defaults to false.
        Returns: Optional[bool]
        """
        return self._battery_rule_require_charger
    
    @battery_rule_require_charger.setter
    def battery_rule_require_charger(self,value: Optional[bool] = None) -> None:
        """
        Sets the batteryRuleRequireCharger property value. Flag indicating if charger is required. When set to false, the client can install updates whether the device is in or out of the charger. Applied only for installation. Defaults to false.
        Args:
            value: Value to set for the batteryRuleRequireCharger property.
        """
        self._battery_rule_require_charger = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new zebraFotaDeploymentSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Minimum battery level (%) required for both download and installation. Default: -1 (System defaults). Maximum is 100.
        self._battery_rule_minimum_battery_level_percentage: Optional[int] = None
        # Flag indicating if charger is required. When set to false, the client can install updates whether the device is in or out of the charger. Applied only for installation. Defaults to false.
        self._battery_rule_require_charger: Optional[bool] = None
        # Deploy update for devices with this model only.
        self._device_model: Optional[str] = None
        # Represents various network types for Zebra FOTA deployment.
        self._download_rule_network_type: Optional[zebra_fota_network_type.ZebraFotaNetworkType] = None
        # Date and time in the device time zone when the download will start (e.g., 2018-07-25T10:20:32). The default value is UTC now and the maximum is 10 days from deployment creation.
        self._download_rule_start_date_time: Optional[datetime] = None
        # A description provided by Zebra for the the firmware artifact to update the device to (e.g.: LifeGuard Update 120 (released 29-June-2022).
        self._firmware_target_artifact_description: Optional[str] = None
        # Deployment's Board Support Package (BSP. E.g.: '01.18.02.00'). Required only for custom update type.
        self._firmware_target_board_support_package_version: Optional[str] = None
        # Target OS Version (e.g.: '8.1.0'). Required only for custom update type.
        self._firmware_target_os_version: Optional[str] = None
        # Target patch name (e.g.: 'U06'). Required only for custom update type.
        self._firmware_target_patch: Optional[str] = None
        # Date and time in device time zone when the install will start. Default - download startDate if configured, otherwise defaults to NOW. Ignored when deployment update type was set to auto.
        self._install_rule_start_date_time: Optional[datetime] = None
        # Time of day after which the install cannot start. Possible range is 00:30:00 to 23:59:59. Should be greater than 'installRuleWindowStartTime' by 30 mins. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 23:59:59. Respected for all values of update type, including AUTO.
        self._install_rule_window_end_time: Optional[Time] = None
        # Time of day (00:00:00 - 23:30:00) when installation should begin. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 00:00:00. Respected for all values of update type, including AUTO.
        self._install_rule_window_start_time: Optional[Time] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Maximum 28 days. Default is 28 days. Sequence of dates are: 1) Download start date. 2) Install start date. 3) Schedule end date. If any of the values are not provided, the date provided in the preceding step of the sequence is used. If no values are provided, the string value of the current UTC is used.
        self._schedule_duration_in_days: Optional[int] = None
        # Represents various schedule modes for Zebra FOTA deployment.
        self._schedule_mode: Optional[zebra_fota_schedule_mode.ZebraFotaScheduleMode] = None
        # This attribute indicates the deployment time offset (e.g.180 represents an offset of +03:00, and -270 represents an offset of -04:30). The time offset is the time timezone where the devices are located. The deployment start and end data uses this timezone
        self._time_zone_offset_in_minutes: Optional[int] = None
        # Represents various update types for Zebra FOTA deployment.
        self._update_type: Optional[zebra_fota_update_type.ZebraFotaUpdateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ZebraFotaDeploymentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeploymentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ZebraFotaDeploymentSettings()
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. Deploy update for devices with this model only.
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. Deploy update for devices with this model only.
        Args:
            value: Value to set for the deviceModel property.
        """
        self._device_model = value
    
    @property
    def download_rule_network_type(self,) -> Optional[zebra_fota_network_type.ZebraFotaNetworkType]:
        """
        Gets the downloadRuleNetworkType property value. Represents various network types for Zebra FOTA deployment.
        Returns: Optional[zebra_fota_network_type.ZebraFotaNetworkType]
        """
        return self._download_rule_network_type
    
    @download_rule_network_type.setter
    def download_rule_network_type(self,value: Optional[zebra_fota_network_type.ZebraFotaNetworkType] = None) -> None:
        """
        Sets the downloadRuleNetworkType property value. Represents various network types for Zebra FOTA deployment.
        Args:
            value: Value to set for the downloadRuleNetworkType property.
        """
        self._download_rule_network_type = value
    
    @property
    def download_rule_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the downloadRuleStartDateTime property value. Date and time in the device time zone when the download will start (e.g., 2018-07-25T10:20:32). The default value is UTC now and the maximum is 10 days from deployment creation.
        Returns: Optional[datetime]
        """
        return self._download_rule_start_date_time
    
    @download_rule_start_date_time.setter
    def download_rule_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the downloadRuleStartDateTime property value. Date and time in the device time zone when the download will start (e.g., 2018-07-25T10:20:32). The default value is UTC now and the maximum is 10 days from deployment creation.
        Args:
            value: Value to set for the downloadRuleStartDateTime property.
        """
        self._download_rule_start_date_time = value
    
    @property
    def firmware_target_artifact_description(self,) -> Optional[str]:
        """
        Gets the firmwareTargetArtifactDescription property value. A description provided by Zebra for the the firmware artifact to update the device to (e.g.: LifeGuard Update 120 (released 29-June-2022).
        Returns: Optional[str]
        """
        return self._firmware_target_artifact_description
    
    @firmware_target_artifact_description.setter
    def firmware_target_artifact_description(self,value: Optional[str] = None) -> None:
        """
        Sets the firmwareTargetArtifactDescription property value. A description provided by Zebra for the the firmware artifact to update the device to (e.g.: LifeGuard Update 120 (released 29-June-2022).
        Args:
            value: Value to set for the firmwareTargetArtifactDescription property.
        """
        self._firmware_target_artifact_description = value
    
    @property
    def firmware_target_board_support_package_version(self,) -> Optional[str]:
        """
        Gets the firmwareTargetBoardSupportPackageVersion property value. Deployment's Board Support Package (BSP. E.g.: '01.18.02.00'). Required only for custom update type.
        Returns: Optional[str]
        """
        return self._firmware_target_board_support_package_version
    
    @firmware_target_board_support_package_version.setter
    def firmware_target_board_support_package_version(self,value: Optional[str] = None) -> None:
        """
        Sets the firmwareTargetBoardSupportPackageVersion property value. Deployment's Board Support Package (BSP. E.g.: '01.18.02.00'). Required only for custom update type.
        Args:
            value: Value to set for the firmwareTargetBoardSupportPackageVersion property.
        """
        self._firmware_target_board_support_package_version = value
    
    @property
    def firmware_target_os_version(self,) -> Optional[str]:
        """
        Gets the firmwareTargetOsVersion property value. Target OS Version (e.g.: '8.1.0'). Required only for custom update type.
        Returns: Optional[str]
        """
        return self._firmware_target_os_version
    
    @firmware_target_os_version.setter
    def firmware_target_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the firmwareTargetOsVersion property value. Target OS Version (e.g.: '8.1.0'). Required only for custom update type.
        Args:
            value: Value to set for the firmwareTargetOsVersion property.
        """
        self._firmware_target_os_version = value
    
    @property
    def firmware_target_patch(self,) -> Optional[str]:
        """
        Gets the firmwareTargetPatch property value. Target patch name (e.g.: 'U06'). Required only for custom update type.
        Returns: Optional[str]
        """
        return self._firmware_target_patch
    
    @firmware_target_patch.setter
    def firmware_target_patch(self,value: Optional[str] = None) -> None:
        """
        Sets the firmwareTargetPatch property value. Target patch name (e.g.: 'U06'). Required only for custom update type.
        Args:
            value: Value to set for the firmwareTargetPatch property.
        """
        self._firmware_target_patch = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "battery_rule_minimum_battery_level_percentage": lambda n : setattr(self, 'battery_rule_minimum_battery_level_percentage', n.get_int_value()),
            "battery_rule_require_charger": lambda n : setattr(self, 'battery_rule_require_charger', n.get_bool_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "download_rule_network_type": lambda n : setattr(self, 'download_rule_network_type', n.get_enum_value(zebra_fota_network_type.ZebraFotaNetworkType)),
            "download_rule_start_date_time": lambda n : setattr(self, 'download_rule_start_date_time', n.get_datetime_value()),
            "firmware_target_artifact_description": lambda n : setattr(self, 'firmware_target_artifact_description', n.get_str_value()),
            "firmware_target_board_support_package_version": lambda n : setattr(self, 'firmware_target_board_support_package_version', n.get_str_value()),
            "firmware_target_os_version": lambda n : setattr(self, 'firmware_target_os_version', n.get_str_value()),
            "firmware_target_patch": lambda n : setattr(self, 'firmware_target_patch', n.get_str_value()),
            "install_rule_start_date_time": lambda n : setattr(self, 'install_rule_start_date_time', n.get_datetime_value()),
            "install_rule_window_end_time": lambda n : setattr(self, 'install_rule_window_end_time', n.get_object_value(Time)),
            "install_rule_window_start_time": lambda n : setattr(self, 'install_rule_window_start_time', n.get_object_value(Time)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "schedule_duration_in_days": lambda n : setattr(self, 'schedule_duration_in_days', n.get_int_value()),
            "schedule_mode": lambda n : setattr(self, 'schedule_mode', n.get_enum_value(zebra_fota_schedule_mode.ZebraFotaScheduleMode)),
            "time_zone_offset_in_minutes": lambda n : setattr(self, 'time_zone_offset_in_minutes', n.get_int_value()),
            "update_type": lambda n : setattr(self, 'update_type', n.get_enum_value(zebra_fota_update_type.ZebraFotaUpdateType)),
        }
        return fields
    
    @property
    def install_rule_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the installRuleStartDateTime property value. Date and time in device time zone when the install will start. Default - download startDate if configured, otherwise defaults to NOW. Ignored when deployment update type was set to auto.
        Returns: Optional[datetime]
        """
        return self._install_rule_start_date_time
    
    @install_rule_start_date_time.setter
    def install_rule_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the installRuleStartDateTime property value. Date and time in device time zone when the install will start. Default - download startDate if configured, otherwise defaults to NOW. Ignored when deployment update type was set to auto.
        Args:
            value: Value to set for the installRuleStartDateTime property.
        """
        self._install_rule_start_date_time = value
    
    @property
    def install_rule_window_end_time(self,) -> Optional[Time]:
        """
        Gets the installRuleWindowEndTime property value. Time of day after which the install cannot start. Possible range is 00:30:00 to 23:59:59. Should be greater than 'installRuleWindowStartTime' by 30 mins. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 23:59:59. Respected for all values of update type, including AUTO.
        Returns: Optional[Time]
        """
        return self._install_rule_window_end_time
    
    @install_rule_window_end_time.setter
    def install_rule_window_end_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the installRuleWindowEndTime property value. Time of day after which the install cannot start. Possible range is 00:30:00 to 23:59:59. Should be greater than 'installRuleWindowStartTime' by 30 mins. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 23:59:59. Respected for all values of update type, including AUTO.
        Args:
            value: Value to set for the installRuleWindowEndTime property.
        """
        self._install_rule_window_end_time = value
    
    @property
    def install_rule_window_start_time(self,) -> Optional[Time]:
        """
        Gets the installRuleWindowStartTime property value. Time of day (00:00:00 - 23:30:00) when installation should begin. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 00:00:00. Respected for all values of update type, including AUTO.
        Returns: Optional[Time]
        """
        return self._install_rule_window_start_time
    
    @install_rule_window_start_time.setter
    def install_rule_window_start_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the installRuleWindowStartTime property value. Time of day (00:00:00 - 23:30:00) when installation should begin. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 00:00:00. Respected for all values of update type, including AUTO.
        Args:
            value: Value to set for the installRuleWindowStartTime property.
        """
        self._install_rule_window_start_time = value
    
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
    def schedule_duration_in_days(self,) -> Optional[int]:
        """
        Gets the scheduleDurationInDays property value. Maximum 28 days. Default is 28 days. Sequence of dates are: 1) Download start date. 2) Install start date. 3) Schedule end date. If any of the values are not provided, the date provided in the preceding step of the sequence is used. If no values are provided, the string value of the current UTC is used.
        Returns: Optional[int]
        """
        return self._schedule_duration_in_days
    
    @schedule_duration_in_days.setter
    def schedule_duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the scheduleDurationInDays property value. Maximum 28 days. Default is 28 days. Sequence of dates are: 1) Download start date. 2) Install start date. 3) Schedule end date. If any of the values are not provided, the date provided in the preceding step of the sequence is used. If no values are provided, the string value of the current UTC is used.
        Args:
            value: Value to set for the scheduleDurationInDays property.
        """
        self._schedule_duration_in_days = value
    
    @property
    def schedule_mode(self,) -> Optional[zebra_fota_schedule_mode.ZebraFotaScheduleMode]:
        """
        Gets the scheduleMode property value. Represents various schedule modes for Zebra FOTA deployment.
        Returns: Optional[zebra_fota_schedule_mode.ZebraFotaScheduleMode]
        """
        return self._schedule_mode
    
    @schedule_mode.setter
    def schedule_mode(self,value: Optional[zebra_fota_schedule_mode.ZebraFotaScheduleMode] = None) -> None:
        """
        Sets the scheduleMode property value. Represents various schedule modes for Zebra FOTA deployment.
        Args:
            value: Value to set for the scheduleMode property.
        """
        self._schedule_mode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("batteryRuleMinimumBatteryLevelPercentage", self.battery_rule_minimum_battery_level_percentage)
        writer.write_bool_value("batteryRuleRequireCharger", self.battery_rule_require_charger)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_enum_value("downloadRuleNetworkType", self.download_rule_network_type)
        writer.write_datetime_value("downloadRuleStartDateTime", self.download_rule_start_date_time)
        writer.write_str_value("firmwareTargetArtifactDescription", self.firmware_target_artifact_description)
        writer.write_str_value("firmwareTargetBoardSupportPackageVersion", self.firmware_target_board_support_package_version)
        writer.write_str_value("firmwareTargetOsVersion", self.firmware_target_os_version)
        writer.write_str_value("firmwareTargetPatch", self.firmware_target_patch)
        writer.write_datetime_value("installRuleStartDateTime", self.install_rule_start_date_time)
        writer.write_object_value("installRuleWindowEndTime", self.install_rule_window_end_time)
        writer.write_object_value("installRuleWindowStartTime", self.install_rule_window_start_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("scheduleDurationInDays", self.schedule_duration_in_days)
        writer.write_enum_value("scheduleMode", self.schedule_mode)
        writer.write_int_value("timeZoneOffsetInMinutes", self.time_zone_offset_in_minutes)
        writer.write_enum_value("updateType", self.update_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_zone_offset_in_minutes(self,) -> Optional[int]:
        """
        Gets the timeZoneOffsetInMinutes property value. This attribute indicates the deployment time offset (e.g.180 represents an offset of +03:00, and -270 represents an offset of -04:30). The time offset is the time timezone where the devices are located. The deployment start and end data uses this timezone
        Returns: Optional[int]
        """
        return self._time_zone_offset_in_minutes
    
    @time_zone_offset_in_minutes.setter
    def time_zone_offset_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the timeZoneOffsetInMinutes property value. This attribute indicates the deployment time offset (e.g.180 represents an offset of +03:00, and -270 represents an offset of -04:30). The time offset is the time timezone where the devices are located. The deployment start and end data uses this timezone
        Args:
            value: Value to set for the timeZoneOffsetInMinutes property.
        """
        self._time_zone_offset_in_minutes = value
    
    @property
    def update_type(self,) -> Optional[zebra_fota_update_type.ZebraFotaUpdateType]:
        """
        Gets the updateType property value. Represents various update types for Zebra FOTA deployment.
        Returns: Optional[zebra_fota_update_type.ZebraFotaUpdateType]
        """
        return self._update_type
    
    @update_type.setter
    def update_type(self,value: Optional[zebra_fota_update_type.ZebraFotaUpdateType] = None) -> None:
        """
        Sets the updateType property value. Represents various update types for Zebra FOTA deployment.
        Args:
            value: Value to set for the updateType property.
        """
        self._update_type = value
    

