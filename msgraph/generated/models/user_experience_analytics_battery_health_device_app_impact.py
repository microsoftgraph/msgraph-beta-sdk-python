from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class UserExperienceAnalyticsBatteryHealthDeviceAppImpact(entity.Entity):
    """
    The user experience analytics battery health device app impact entity contains battery usage related information at an app level for a given device.
    """
    # User friendly display name for the app. Eg: Outlook
    app_display_name: Optional[str] = None
    # App name. Eg: oltk.exe
    app_name: Optional[str] = None
    # App publisher. Eg: Microsoft Corporation
    app_publisher: Optional[str] = None
    # The percent of total battery power used by this application when the device was not plugged into AC power, over 14 days. Unit in percentage. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    battery_usage_percentage: Optional[float] = None
    # The unique identifier of the device, Intune DeviceID or SCCM device id.
    device_id: Optional[str] = None
    # true if the user had active interaction with the app.
    is_foreground_app: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthDeviceAppImpact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthDeviceAppImpact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthDeviceAppImpact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appPublisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "batteryUsagePercentage": lambda n : setattr(self, 'battery_usage_percentage', n.get_float_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "isForegroundApp": lambda n : setattr(self, 'is_foreground_app', n.get_bool_value()),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_float_value("batteryUsagePercentage", self.battery_usage_percentage)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_bool_value("isForegroundApp", self.is_foreground_app)
    

