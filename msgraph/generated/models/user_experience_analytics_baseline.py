from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_category

from . import entity

@dataclass
class UserExperienceAnalyticsBaseline(entity.Entity):
    """
    The user experience analytics baseline entity contains baseline values against which to compare the user experience analytics scores.
    """
    # The user experience analytics app health metrics.
    app_health_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # The user experience analytics battery health metrics.
    battery_health_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # The user experience analytics best practices metrics.
    best_practices_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # The date the custom baseline was created.
    created_date_time: Optional[datetime] = None
    # The user experience analytics device boot performance metrics.
    device_boot_performance_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # The name of the user experience analytics baseline.
    display_name: Optional[str] = None
    # Signifies if the current baseline is the commercial median baseline or a custom baseline.
    is_built_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience analytics reboot analytics metrics.
    reboot_analytics_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # The user experience analytics resource performance metrics.
    resource_performance_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    # The user experience analytics work from anywhere metrics.
    work_from_anywhere_metrics: Optional[user_experience_analytics_category.UserExperienceAnalyticsCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBaseline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBaseline
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBaseline()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_category

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
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
    

