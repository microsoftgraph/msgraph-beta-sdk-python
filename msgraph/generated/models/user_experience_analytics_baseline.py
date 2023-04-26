from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_category

from . import entity

class UserExperienceAnalyticsBaseline(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new UserExperienceAnalyticsBaseline and sets the default values.
        """
        super().__init__()
        # The user experience analytics app health metrics.
        self._app_health_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # The user experience analytics battery health metrics.
        self._battery_health_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # The user experience analytics best practices metrics.
        self._best_practices_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # The date the custom baseline was created.
        self._created_date_time: Optional[datetime] = None
        # The user experience analytics device boot performance metrics.
        self._device_boot_performance_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # The name of the user experience analytics baseline.
        self._display_name: Optional[str] = None
        # Signifies if the current baseline is the commercial median baseline or a custom baseline.
        self._is_built_in: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience analytics reboot analytics metrics.
        self._reboot_analytics_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # The user experience analytics resource performance metrics.
        self._resource_performance_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
        # The user experience analytics work from anywhere metrics.
        self._work_from_anywhere_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    
    @property
    def app_health_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the appHealthMetrics property value. The user experience analytics app health metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._app_health_metrics
    
    @app_health_metrics.setter
    def app_health_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the appHealthMetrics property value. The user experience analytics app health metrics.
        Args:
            value: Value to set for the app_health_metrics property.
        """
        self._app_health_metrics = value
    
    @property
    def battery_health_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the batteryHealthMetrics property value. The user experience analytics battery health metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._battery_health_metrics
    
    @battery_health_metrics.setter
    def battery_health_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the batteryHealthMetrics property value. The user experience analytics battery health metrics.
        Args:
            value: Value to set for the battery_health_metrics property.
        """
        self._battery_health_metrics = value
    
    @property
    def best_practices_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the bestPracticesMetrics property value. The user experience analytics best practices metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._best_practices_metrics
    
    @best_practices_metrics.setter
    def best_practices_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the bestPracticesMetrics property value. The user experience analytics best practices metrics.
        Args:
            value: Value to set for the best_practices_metrics property.
        """
        self._best_practices_metrics = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date the custom baseline was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date the custom baseline was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBaseline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBaseline
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBaseline()
    
    @property
    def device_boot_performance_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the deviceBootPerformanceMetrics property value. The user experience analytics device boot performance metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._device_boot_performance_metrics
    
    @device_boot_performance_metrics.setter
    def device_boot_performance_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the deviceBootPerformanceMetrics property value. The user experience analytics device boot performance metrics.
        Args:
            value: Value to set for the device_boot_performance_metrics property.
        """
        self._device_boot_performance_metrics = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the user experience analytics baseline.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the user experience analytics baseline.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_category

        fields: Dict[str, Callable[[Any], None]] = {
            "appHealthMetrics": lambda n : setattr(self, 'app_health_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "batteryHealthMetrics": lambda n : setattr(self, 'battery_health_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "bestPracticesMetrics": lambda n : setattr(self, 'best_practices_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceBootPerformanceMetrics": lambda n : setattr(self, 'device_boot_performance_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "rebootAnalyticsMetrics": lambda n : setattr(self, 'reboot_analytics_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "resourcePerformanceMetrics": lambda n : setattr(self, 'resource_performance_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
            "workFromAnywhereMetrics": lambda n : setattr(self, 'work_from_anywhere_metrics', n.get_object_value(user_experience_analytics_category.UserExperienceAnalyticsCategory)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. Signifies if the current baseline is the commercial median baseline or a custom baseline.
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. Signifies if the current baseline is the commercial median baseline or a custom baseline.
        Args:
            value: Value to set for the is_built_in property.
        """
        self._is_built_in = value
    
    @property
    def reboot_analytics_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the rebootAnalyticsMetrics property value. The user experience analytics reboot analytics metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._reboot_analytics_metrics
    
    @reboot_analytics_metrics.setter
    def reboot_analytics_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the rebootAnalyticsMetrics property value. The user experience analytics reboot analytics metrics.
        Args:
            value: Value to set for the reboot_analytics_metrics property.
        """
        self._reboot_analytics_metrics = value
    
    @property
    def resource_performance_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the resourcePerformanceMetrics property value. The user experience analytics resource performance metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._resource_performance_metrics
    
    @resource_performance_metrics.setter
    def resource_performance_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the resourcePerformanceMetrics property value. The user experience analytics resource performance metrics.
        Args:
            value: Value to set for the resource_performance_metrics property.
        """
        self._resource_performance_metrics = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("appHealthMetrics", self.app_health_metrics)
        writer.write_object_value("batteryHealthMetrics", self.battery_health_metrics)
        writer.write_object_value("bestPracticesMetrics", self.best_practices_metrics)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("deviceBootPerformanceMetrics", self.device_boot_performance_metrics)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_object_value("rebootAnalyticsMetrics", self.reboot_analytics_metrics)
        writer.write_object_value("resourcePerformanceMetrics", self.resource_performance_metrics)
        writer.write_object_value("workFromAnywhereMetrics", self.work_from_anywhere_metrics)
    
    @property
    def work_from_anywhere_metrics(self,) -> Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]:
        """
        Gets the workFromAnywhereMetrics property value. The user experience analytics work from anywhere metrics.
        Returns: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory]
        """
        return self._work_from_anywhere_metrics
    
    @work_from_anywhere_metrics.setter
    def work_from_anywhere_metrics(self,value: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None) -> None:
        """
        Sets the workFromAnywhereMetrics property value. The user experience analytics work from anywhere metrics.
        Args:
            value: Value to set for the work_from_anywhere_metrics property.
        """
        self._work_from_anywhere_metrics = value
    

