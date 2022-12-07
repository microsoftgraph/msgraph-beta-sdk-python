from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_work_from_anywhere_device = lazy_import('msgraph.generated.models.user_experience_analytics_work_from_anywhere_device')

class UserExperienceAnalyticsWorkFromAnywhereMetric(entity.Entity):
    """
    The user experience analytics metric for work from anywhere report
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsWorkFromAnywhereMetric and sets the default values.
        """
        super().__init__()
        # The work from anywhere metric devices.
        self._metric_devices: Optional[List[user_experience_analytics_work_from_anywhere_device.UserExperienceAnalyticsWorkFromAnywhereDevice]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereMetric
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsWorkFromAnywhereMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "metric_devices": lambda n : setattr(self, 'metric_devices', n.get_collection_of_object_values(user_experience_analytics_work_from_anywhere_device.UserExperienceAnalyticsWorkFromAnywhereDevice)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def metric_devices(self,) -> Optional[List[user_experience_analytics_work_from_anywhere_device.UserExperienceAnalyticsWorkFromAnywhereDevice]]:
        """
        Gets the metricDevices property value. The work from anywhere metric devices.
        Returns: Optional[List[user_experience_analytics_work_from_anywhere_device.UserExperienceAnalyticsWorkFromAnywhereDevice]]
        """
        return self._metric_devices
    
    @metric_devices.setter
    def metric_devices(self,value: Optional[List[user_experience_analytics_work_from_anywhere_device.UserExperienceAnalyticsWorkFromAnywhereDevice]] = None) -> None:
        """
        Sets the metricDevices property value. The work from anywhere metric devices.
        Args:
            value: Value to set for the metricDevices property.
        """
        self._metric_devices = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("metricDevices", self.metric_devices)
    

