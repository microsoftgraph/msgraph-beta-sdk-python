from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_operating_system_restart_category

from . import entity

@dataclass
class UserExperienceAnalyticsDeviceStartupHistory(entity.Entity):
    """
    The user experience analytics device startup history entity contains device boot performance history details.
    """
    # The user experience analytics device core boot time in milliseconds.
    core_boot_time_in_ms: Optional[int] = None
    # The user experience analytics device core login time in milliseconds.
    core_login_time_in_ms: Optional[int] = None
    # The user experience analytics device id.
    device_id: Optional[str] = None
    # The user experience analytics device feature update time in milliseconds.
    feature_update_boot_time_in_ms: Optional[int] = None
    # The User experience analytics Device group policy boot time in milliseconds.
    group_policy_boot_time_in_ms: Optional[int] = None
    # The User experience analytics Device group policy login time in milliseconds.
    group_policy_login_time_in_ms: Optional[int] = None
    # The user experience analytics device boot record is a feature update.
    is_feature_update: Optional[bool] = None
    # The user experience analytics device first login.
    is_first_login: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience analytics device boot record's operating system version.
    operating_system_version: Optional[str] = None
    # The user experience analytics responsive desktop time in milliseconds.
    responsive_desktop_time_in_ms: Optional[int] = None
    # Operating System restart category.
    restart_category: Optional[user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory] = None
    # OS restart fault bucket. The fault bucket is used to find additional information about a system crash.
    restart_fault_bucket: Optional[str] = None
    # OS restart stop code. This shows the bug check code which can be used to look up the blue screen reason.
    restart_stop_code: Optional[str] = None
    # The user experience analytics device boot start time.
    start_time: Optional[datetime] = None
    # The user experience analytics device total boot time in milliseconds.
    total_boot_time_in_ms: Optional[int] = None
    # The user experience analytics device total login time in milliseconds.
    total_login_time_in_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceStartupHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupHistory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceStartupHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_operating_system_restart_category

        from . import entity, user_experience_analytics_operating_system_restart_category

        fields: Dict[str, Callable[[Any], None]] = {
            "coreBootTimeInMs": lambda n : setattr(self, 'core_boot_time_in_ms', n.get_int_value()),
            "coreLoginTimeInMs": lambda n : setattr(self, 'core_login_time_in_ms', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "featureUpdateBootTimeInMs": lambda n : setattr(self, 'feature_update_boot_time_in_ms', n.get_int_value()),
            "groupPolicyBootTimeInMs": lambda n : setattr(self, 'group_policy_boot_time_in_ms', n.get_int_value()),
            "groupPolicyLoginTimeInMs": lambda n : setattr(self, 'group_policy_login_time_in_ms', n.get_int_value()),
            "isFeatureUpdate": lambda n : setattr(self, 'is_feature_update', n.get_bool_value()),
            "isFirstLogin": lambda n : setattr(self, 'is_first_login', n.get_bool_value()),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "responsiveDesktopTimeInMs": lambda n : setattr(self, 'responsive_desktop_time_in_ms', n.get_int_value()),
            "restartCategory": lambda n : setattr(self, 'restart_category', n.get_enum_value(user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory)),
            "restartFaultBucket": lambda n : setattr(self, 'restart_fault_bucket', n.get_str_value()),
            "restartStopCode": lambda n : setattr(self, 'restart_stop_code', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
            "totalBootTimeInMs": lambda n : setattr(self, 'total_boot_time_in_ms', n.get_int_value()),
            "totalLoginTimeInMs": lambda n : setattr(self, 'total_login_time_in_ms', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("coreBootTimeInMs", self.core_boot_time_in_ms)
        writer.write_int_value("coreLoginTimeInMs", self.core_login_time_in_ms)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_int_value("featureUpdateBootTimeInMs", self.feature_update_boot_time_in_ms)
        writer.write_int_value("groupPolicyBootTimeInMs", self.group_policy_boot_time_in_ms)
        writer.write_int_value("groupPolicyLoginTimeInMs", self.group_policy_login_time_in_ms)
        writer.write_bool_value("isFeatureUpdate", self.is_feature_update)
        writer.write_bool_value("isFirstLogin", self.is_first_login)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_int_value("responsiveDesktopTimeInMs", self.responsive_desktop_time_in_ms)
        writer.write_enum_value("restartCategory", self.restart_category)
        writer.write_str_value("restartFaultBucket", self.restart_fault_bucket)
        writer.write_str_value("restartStopCode", self.restart_stop_code)
        writer.write_datetime_value("startTime", self.start_time)
        writer.write_int_value("totalBootTimeInMs", self.total_boot_time_in_ms)
        writer.write_int_value("totalLoginTimeInMs", self.total_login_time_in_ms)
    

