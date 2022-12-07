from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsAppHealthOSVersionPerformance(entity.Entity):
    """
    The user experience analytics device OS version performance entity contains OS version performance details.
    """
    @property
    def active_device_count(self,) -> Optional[int]:
        """
        Gets the activeDeviceCount property value. The number of active devices for the OS version. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_device_count
    
    @active_device_count.setter
    def active_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDeviceCount property value. The number of active devices for the OS version. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the activeDeviceCount property.
        """
        self._active_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAppHealthOSVersionPerformance and sets the default values.
        """
        super().__init__()
        # The number of active devices for the OS version. Valid values -2147483648 to 2147483647
        self._active_device_count: Optional[int] = None
        # The mean time to failure for the OS version in minutes. Valid values -2147483648 to 2147483647
        self._mean_time_to_failure_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The OS build number installed on the device.
        self._os_build_number: Optional[str] = None
        # The OS version installed on the device.
        self._os_version: Optional[str] = None
        # The app health score of the OS version. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._os_version_app_health_score: Optional[float] = None
        # The overall app health status of the OS version.
        self._os_version_app_health_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthOSVersionPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthOSVersionPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAppHealthOSVersionPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_device_count": lambda n : setattr(self, 'active_device_count', n.get_int_value()),
            "mean_time_to_failure_in_minutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "os_build_number": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "os_version_app_health_score": lambda n : setattr(self, 'os_version_app_health_score', n.get_float_value()),
            "os_version_app_health_status": lambda n : setattr(self, 'os_version_app_health_status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mean_time_to_failure_in_minutes(self,) -> Optional[int]:
        """
        Gets the meanTimeToFailureInMinutes property value. The mean time to failure for the OS version in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._mean_time_to_failure_in_minutes
    
    @mean_time_to_failure_in_minutes.setter
    def mean_time_to_failure_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the meanTimeToFailureInMinutes property value. The mean time to failure for the OS version in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the meanTimeToFailureInMinutes property.
        """
        self._mean_time_to_failure_in_minutes = value
    
    @property
    def os_build_number(self,) -> Optional[str]:
        """
        Gets the osBuildNumber property value. The OS build number installed on the device.
        Returns: Optional[str]
        """
        return self._os_build_number
    
    @os_build_number.setter
    def os_build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the osBuildNumber property value. The OS build number installed on the device.
        Args:
            value: Value to set for the osBuildNumber property.
        """
        self._os_build_number = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The OS version installed on the device.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The OS version installed on the device.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def os_version_app_health_score(self,) -> Optional[float]:
        """
        Gets the osVersionAppHealthScore property value. The app health score of the OS version. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._os_version_app_health_score
    
    @os_version_app_health_score.setter
    def os_version_app_health_score(self,value: Optional[float] = None) -> None:
        """
        Sets the osVersionAppHealthScore property value. The app health score of the OS version. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the osVersionAppHealthScore property.
        """
        self._os_version_app_health_score = value
    
    @property
    def os_version_app_health_status(self,) -> Optional[str]:
        """
        Gets the osVersionAppHealthStatus property value. The overall app health status of the OS version.
        Returns: Optional[str]
        """
        return self._os_version_app_health_status
    
    @os_version_app_health_status.setter
    def os_version_app_health_status(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersionAppHealthStatus property value. The overall app health status of the OS version.
        Args:
            value: Value to set for the osVersionAppHealthStatus property.
        """
        self._os_version_app_health_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activeDeviceCount", self.active_device_count)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_float_value("osVersionAppHealthScore", self.os_version_app_health_score)
        writer.write_str_value("osVersionAppHealthStatus", self.os_version_app_health_status)
    

