from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion(entity.Entity):
    """
    The user experience analytics application performance entity contains app performance details by app version.
    """
    @property
    def app_crash_count(self,) -> Optional[int]:
        """
        Gets the appCrashCount property value. The number of crashes for the app. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_crash_count
    
    @app_crash_count.setter
    def app_crash_count(self,value: Optional[int] = None) -> None:
        """
        Sets the appCrashCount property value. The number of crashes for the app. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appCrashCount property.
        """
        self._app_crash_count = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The friendly name of the application.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The friendly name of the application.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_name(self,) -> Optional[str]:
        """
        Gets the appName property value. The name of the application.
        Returns: Optional[str]
        """
        return self._app_name
    
    @app_name.setter
    def app_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appName property value. The name of the application.
        Args:
            value: Value to set for the appName property.
        """
        self._app_name = value
    
    @property
    def app_publisher(self,) -> Optional[str]:
        """
        Gets the appPublisher property value. The publisher of the application.
        Returns: Optional[str]
        """
        return self._app_publisher
    
    @app_publisher.setter
    def app_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the appPublisher property value. The publisher of the application.
        Args:
            value: Value to set for the appPublisher property.
        """
        self._app_publisher = value
    
    @property
    def app_usage_duration(self,) -> Optional[int]:
        """
        Gets the appUsageDuration property value. The total usage time of the application in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._app_usage_duration
    
    @app_usage_duration.setter
    def app_usage_duration(self,value: Optional[int] = None) -> None:
        """
        Sets the appUsageDuration property value. The total usage time of the application in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the appUsageDuration property.
        """
        self._app_usage_duration = value
    
    @property
    def app_version(self,) -> Optional[str]:
        """
        Gets the appVersion property value. The version of the application.
        Returns: Optional[str]
        """
        return self._app_version
    
    @app_version.setter
    def app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the appVersion property value. The version of the application.
        Args:
            value: Value to set for the appVersion property.
        """
        self._app_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAppHealthAppPerformanceByAppVersion and sets the default values.
        """
        super().__init__()
        # The number of crashes for the app. Valid values -2147483648 to 2147483647
        self._app_crash_count: Optional[int] = None
        # The friendly name of the application.
        self._app_display_name: Optional[str] = None
        # The name of the application.
        self._app_name: Optional[str] = None
        # The publisher of the application.
        self._app_publisher: Optional[str] = None
        # The total usage time of the application in minutes. Valid values -2147483648 to 2147483647
        self._app_usage_duration: Optional[int] = None
        # The version of the application.
        self._app_version: Optional[str] = None
        # The mean time to failure for the app in minutes. Valid values -2147483648 to 2147483647
        self._mean_time_to_failure_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_crash_count": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_name": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "app_publisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "app_usage_duration": lambda n : setattr(self, 'app_usage_duration', n.get_int_value()),
            "app_version": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "mean_time_to_failure_in_minutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mean_time_to_failure_in_minutes(self,) -> Optional[int]:
        """
        Gets the meanTimeToFailureInMinutes property value. The mean time to failure for the app in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._mean_time_to_failure_in_minutes
    
    @mean_time_to_failure_in_minutes.setter
    def mean_time_to_failure_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the meanTimeToFailureInMinutes property value. The mean time to failure for the app in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the meanTimeToFailureInMinutes property.
        """
        self._mean_time_to_failure_in_minutes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("appCrashCount", self.app_crash_count)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_int_value("appUsageDuration", self.app_usage_duration)
        writer.write_str_value("appVersion", self.app_version)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
    

