from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBatteryHealthAppImpact(Entity):
    """
    The user experience analytics battery health app impact entity contains battery usage related information at an app level for the tenant.
    """
    # Number of active devices for using that app over a 14-day period. Valid values 0 to 2147483647
    active_devices: Optional[int] = None
    # User friendly display name for the app. Eg: Outlook
    app_display_name: Optional[str] = None
    # App name. Eg: oltk.exe
    app_name: Optional[str] = None
    # App publisher. Eg: Microsoft Corporation
    app_publisher: Optional[str] = None
    # The percent of total battery power used by this application when the device was not plugged into AC power, over 14 days computed across all devices in the tenant. Unit in percentage. Valid values 0 to 1.79769313486232E+308
    battery_usage_percentage: Optional[float] = None
    # true if the user had active interaction with the app.
    is_foreground_app: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthAppImpact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthAppImpact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthAppImpact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appPublisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "batteryUsagePercentage": lambda n : setattr(self, 'battery_usage_percentage', n.get_float_value()),
            "isForegroundApp": lambda n : setattr(self, 'is_foreground_app', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_float_value("batteryUsagePercentage", self.battery_usage_percentage)
        writer.write_bool_value("isForegroundApp", self.is_foreground_app)
    

