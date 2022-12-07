from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsBatteryHealthAppImpact(entity.Entity):
    """
    The user experience analytics battery health app impact entity contains battery usage related information at an app level for the tenant.
    """
    @property
    def active_devices(self,) -> Optional[int]:
        """
        Gets the activeDevices property value. Number of active devices for using that app over a 14-day period. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_devices
    
    @active_devices.setter
    def active_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDevices property value. Number of active devices for using that app over a 14-day period. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the activeDevices property.
        """
        self._active_devices = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. User friendly display name for the app. Eg: Outlook
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. User friendly display name for the app. Eg: Outlook
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_name(self,) -> Optional[str]:
        """
        Gets the appName property value. App name. Eg: oltk.exe
        Returns: Optional[str]
        """
        return self._app_name
    
    @app_name.setter
    def app_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appName property value. App name. Eg: oltk.exe
        Args:
            value: Value to set for the appName property.
        """
        self._app_name = value
    
    @property
    def app_publisher(self,) -> Optional[str]:
        """
        Gets the appPublisher property value. App publisher. Eg: Microsoft Corporation
        Returns: Optional[str]
        """
        return self._app_publisher
    
    @app_publisher.setter
    def app_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the appPublisher property value. App publisher. Eg: Microsoft Corporation
        Args:
            value: Value to set for the appPublisher property.
        """
        self._app_publisher = value
    
    @property
    def battery_usage_percentage(self,) -> Optional[float]:
        """
        Gets the batteryUsagePercentage property value. The percent of total battery power used by this application when the device was not plugged into AC power, over 14 days computed across all devices in the tenant. Unit in percentage. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._battery_usage_percentage
    
    @battery_usage_percentage.setter
    def battery_usage_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the batteryUsagePercentage property value. The percent of total battery power used by this application when the device was not plugged into AC power, over 14 days computed across all devices in the tenant. Unit in percentage. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the batteryUsagePercentage property.
        """
        self._battery_usage_percentage = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthAppImpact and sets the default values.
        """
        super().__init__()
        # Number of active devices for using that app over a 14-day period. Valid values -2147483648 to 2147483647
        self._active_devices: Optional[int] = None
        # User friendly display name for the app. Eg: Outlook
        self._app_display_name: Optional[str] = None
        # App name. Eg: oltk.exe
        self._app_name: Optional[str] = None
        # App publisher. Eg: Microsoft Corporation
        self._app_publisher: Optional[str] = None
        # The percent of total battery power used by this application when the device was not plugged into AC power, over 14 days computed across all devices in the tenant. Unit in percentage. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._battery_usage_percentage: Optional[float] = None
        # true if the user had active interaction with the app.
        self._is_foreground_app: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthAppImpact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthAppImpact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthAppImpact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_devices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_name": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "app_publisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "battery_usage_percentage": lambda n : setattr(self, 'battery_usage_percentage', n.get_float_value()),
            "is_foreground_app": lambda n : setattr(self, 'is_foreground_app', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_foreground_app(self,) -> Optional[bool]:
        """
        Gets the isForegroundApp property value. true if the user had active interaction with the app.
        Returns: Optional[bool]
        """
        return self._is_foreground_app
    
    @is_foreground_app.setter
    def is_foreground_app(self,value: Optional[bool] = None) -> None:
        """
        Sets the isForegroundApp property value. true if the user had active interaction with the app.
        Args:
            value: Value to set for the isForegroundApp property.
        """
        self._is_foreground_app = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_float_value("batteryUsagePercentage", self.battery_usage_percentage)
        writer.write_bool_value("isForegroundApp", self.is_foreground_app)
    

