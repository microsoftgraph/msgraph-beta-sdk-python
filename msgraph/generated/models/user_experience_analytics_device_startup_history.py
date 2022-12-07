from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_operating_system_restart_category = lazy_import('msgraph.generated.models.user_experience_analytics_operating_system_restart_category')

class UserExperienceAnalyticsDeviceStartupHistory(entity.Entity):
    """
    The user experience analytics device startup history entity contains device boot performance history details.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsDeviceStartupHistory and sets the default values.
        """
        super().__init__()
        # The user experience analytics device core boot time in milliseconds.
        self._core_boot_time_in_ms: Optional[int] = None
        # The user experience analytics device core login time in milliseconds.
        self._core_login_time_in_ms: Optional[int] = None
        # The user experience analytics device id.
        self._device_id: Optional[str] = None
        # The user experience analytics device feature update time in milliseconds.
        self._feature_update_boot_time_in_ms: Optional[int] = None
        # The User experience analytics Device group policy boot time in milliseconds.
        self._group_policy_boot_time_in_ms: Optional[int] = None
        # The User experience analytics Device group policy login time in milliseconds.
        self._group_policy_login_time_in_ms: Optional[int] = None
        # The user experience analytics device boot record is a feature update.
        self._is_feature_update: Optional[bool] = None
        # The user experience analytics device first login.
        self._is_first_login: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience analytics device boot record's operating system version.
        self._operating_system_version: Optional[str] = None
        # The user experience analytics responsive desktop time in milliseconds.
        self._responsive_desktop_time_in_ms: Optional[int] = None
        # Operating System restart category
        self._restart_category: Optional[user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory] = None
        # OS restart fault bucket. The fault bucket is used to find additional information about a system crash.
        self._restart_fault_bucket: Optional[str] = None
        # OS restart stop code. This shows the bug check code which can be used to look up the blue screen reason.
        self._restart_stop_code: Optional[str] = None
        # The user experience analytics device boot start time.
        self._start_time: Optional[datetime] = None
        # The user experience analytics device total boot time in milliseconds.
        self._total_boot_time_in_ms: Optional[int] = None
        # The user experience analytics device total login time in milliseconds.
        self._total_login_time_in_ms: Optional[int] = None
    
    @property
    def core_boot_time_in_ms(self,) -> Optional[int]:
        """
        Gets the coreBootTimeInMs property value. The user experience analytics device core boot time in milliseconds.
        Returns: Optional[int]
        """
        return self._core_boot_time_in_ms
    
    @core_boot_time_in_ms.setter
    def core_boot_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the coreBootTimeInMs property value. The user experience analytics device core boot time in milliseconds.
        Args:
            value: Value to set for the coreBootTimeInMs property.
        """
        self._core_boot_time_in_ms = value
    
    @property
    def core_login_time_in_ms(self,) -> Optional[int]:
        """
        Gets the coreLoginTimeInMs property value. The user experience analytics device core login time in milliseconds.
        Returns: Optional[int]
        """
        return self._core_login_time_in_ms
    
    @core_login_time_in_ms.setter
    def core_login_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the coreLoginTimeInMs property value. The user experience analytics device core login time in milliseconds.
        Args:
            value: Value to set for the coreLoginTimeInMs property.
        """
        self._core_login_time_in_ms = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceStartupHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceStartupHistory()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The user experience analytics device id.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The user experience analytics device id.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def feature_update_boot_time_in_ms(self,) -> Optional[int]:
        """
        Gets the featureUpdateBootTimeInMs property value. The user experience analytics device feature update time in milliseconds.
        Returns: Optional[int]
        """
        return self._feature_update_boot_time_in_ms
    
    @feature_update_boot_time_in_ms.setter
    def feature_update_boot_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the featureUpdateBootTimeInMs property value. The user experience analytics device feature update time in milliseconds.
        Args:
            value: Value to set for the featureUpdateBootTimeInMs property.
        """
        self._feature_update_boot_time_in_ms = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "core_boot_time_in_ms": lambda n : setattr(self, 'core_boot_time_in_ms', n.get_int_value()),
            "core_login_time_in_ms": lambda n : setattr(self, 'core_login_time_in_ms', n.get_int_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "feature_update_boot_time_in_ms": lambda n : setattr(self, 'feature_update_boot_time_in_ms', n.get_int_value()),
            "group_policy_boot_time_in_ms": lambda n : setattr(self, 'group_policy_boot_time_in_ms', n.get_int_value()),
            "group_policy_login_time_in_ms": lambda n : setattr(self, 'group_policy_login_time_in_ms', n.get_int_value()),
            "is_feature_update": lambda n : setattr(self, 'is_feature_update', n.get_bool_value()),
            "is_first_login": lambda n : setattr(self, 'is_first_login', n.get_bool_value()),
            "operating_system_version": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "responsive_desktop_time_in_ms": lambda n : setattr(self, 'responsive_desktop_time_in_ms', n.get_int_value()),
            "restart_category": lambda n : setattr(self, 'restart_category', n.get_enum_value(user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory)),
            "restart_fault_bucket": lambda n : setattr(self, 'restart_fault_bucket', n.get_str_value()),
            "restart_stop_code": lambda n : setattr(self, 'restart_stop_code', n.get_str_value()),
            "start_time": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
            "total_boot_time_in_ms": lambda n : setattr(self, 'total_boot_time_in_ms', n.get_int_value()),
            "total_login_time_in_ms": lambda n : setattr(self, 'total_login_time_in_ms', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_boot_time_in_ms(self,) -> Optional[int]:
        """
        Gets the groupPolicyBootTimeInMs property value. The User experience analytics Device group policy boot time in milliseconds.
        Returns: Optional[int]
        """
        return self._group_policy_boot_time_in_ms
    
    @group_policy_boot_time_in_ms.setter
    def group_policy_boot_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the groupPolicyBootTimeInMs property value. The User experience analytics Device group policy boot time in milliseconds.
        Args:
            value: Value to set for the groupPolicyBootTimeInMs property.
        """
        self._group_policy_boot_time_in_ms = value
    
    @property
    def group_policy_login_time_in_ms(self,) -> Optional[int]:
        """
        Gets the groupPolicyLoginTimeInMs property value. The User experience analytics Device group policy login time in milliseconds.
        Returns: Optional[int]
        """
        return self._group_policy_login_time_in_ms
    
    @group_policy_login_time_in_ms.setter
    def group_policy_login_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the groupPolicyLoginTimeInMs property value. The User experience analytics Device group policy login time in milliseconds.
        Args:
            value: Value to set for the groupPolicyLoginTimeInMs property.
        """
        self._group_policy_login_time_in_ms = value
    
    @property
    def is_feature_update(self,) -> Optional[bool]:
        """
        Gets the isFeatureUpdate property value. The user experience analytics device boot record is a feature update.
        Returns: Optional[bool]
        """
        return self._is_feature_update
    
    @is_feature_update.setter
    def is_feature_update(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFeatureUpdate property value. The user experience analytics device boot record is a feature update.
        Args:
            value: Value to set for the isFeatureUpdate property.
        """
        self._is_feature_update = value
    
    @property
    def is_first_login(self,) -> Optional[bool]:
        """
        Gets the isFirstLogin property value. The user experience analytics device first login.
        Returns: Optional[bool]
        """
        return self._is_first_login
    
    @is_first_login.setter
    def is_first_login(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFirstLogin property value. The user experience analytics device first login.
        Args:
            value: Value to set for the isFirstLogin property.
        """
        self._is_first_login = value
    
    @property
    def operating_system_version(self,) -> Optional[str]:
        """
        Gets the operatingSystemVersion property value. The user experience analytics device boot record's operating system version.
        Returns: Optional[str]
        """
        return self._operating_system_version
    
    @operating_system_version.setter
    def operating_system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemVersion property value. The user experience analytics device boot record's operating system version.
        Args:
            value: Value to set for the operatingSystemVersion property.
        """
        self._operating_system_version = value
    
    @property
    def responsive_desktop_time_in_ms(self,) -> Optional[int]:
        """
        Gets the responsiveDesktopTimeInMs property value. The user experience analytics responsive desktop time in milliseconds.
        Returns: Optional[int]
        """
        return self._responsive_desktop_time_in_ms
    
    @responsive_desktop_time_in_ms.setter
    def responsive_desktop_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the responsiveDesktopTimeInMs property value. The user experience analytics responsive desktop time in milliseconds.
        Args:
            value: Value to set for the responsiveDesktopTimeInMs property.
        """
        self._responsive_desktop_time_in_ms = value
    
    @property
    def restart_category(self,) -> Optional[user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory]:
        """
        Gets the restartCategory property value. Operating System restart category
        Returns: Optional[user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory]
        """
        return self._restart_category
    
    @restart_category.setter
    def restart_category(self,value: Optional[user_experience_analytics_operating_system_restart_category.UserExperienceAnalyticsOperatingSystemRestartCategory] = None) -> None:
        """
        Sets the restartCategory property value. Operating System restart category
        Args:
            value: Value to set for the restartCategory property.
        """
        self._restart_category = value
    
    @property
    def restart_fault_bucket(self,) -> Optional[str]:
        """
        Gets the restartFaultBucket property value. OS restart fault bucket. The fault bucket is used to find additional information about a system crash.
        Returns: Optional[str]
        """
        return self._restart_fault_bucket
    
    @restart_fault_bucket.setter
    def restart_fault_bucket(self,value: Optional[str] = None) -> None:
        """
        Sets the restartFaultBucket property value. OS restart fault bucket. The fault bucket is used to find additional information about a system crash.
        Args:
            value: Value to set for the restartFaultBucket property.
        """
        self._restart_fault_bucket = value
    
    @property
    def restart_stop_code(self,) -> Optional[str]:
        """
        Gets the restartStopCode property value. OS restart stop code. This shows the bug check code which can be used to look up the blue screen reason.
        Returns: Optional[str]
        """
        return self._restart_stop_code
    
    @restart_stop_code.setter
    def restart_stop_code(self,value: Optional[str] = None) -> None:
        """
        Sets the restartStopCode property value. OS restart stop code. This shows the bug check code which can be used to look up the blue screen reason.
        Args:
            value: Value to set for the restartStopCode property.
        """
        self._restart_stop_code = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def start_time(self,) -> Optional[datetime]:
        """
        Gets the startTime property value. The user experience analytics device boot start time.
        Returns: Optional[datetime]
        """
        return self._start_time
    
    @start_time.setter
    def start_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startTime property value. The user experience analytics device boot start time.
        Args:
            value: Value to set for the startTime property.
        """
        self._start_time = value
    
    @property
    def total_boot_time_in_ms(self,) -> Optional[int]:
        """
        Gets the totalBootTimeInMs property value. The user experience analytics device total boot time in milliseconds.
        Returns: Optional[int]
        """
        return self._total_boot_time_in_ms
    
    @total_boot_time_in_ms.setter
    def total_boot_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the totalBootTimeInMs property value. The user experience analytics device total boot time in milliseconds.
        Args:
            value: Value to set for the totalBootTimeInMs property.
        """
        self._total_boot_time_in_ms = value
    
    @property
    def total_login_time_in_ms(self,) -> Optional[int]:
        """
        Gets the totalLoginTimeInMs property value. The user experience analytics device total login time in milliseconds.
        Returns: Optional[int]
        """
        return self._total_login_time_in_ms
    
    @total_login_time_in_ms.setter
    def total_login_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the totalLoginTimeInMs property value. The user experience analytics device total login time in milliseconds.
        Args:
            value: Value to set for the totalLoginTimeInMs property.
        """
        self._total_login_time_in_ms = value
    

