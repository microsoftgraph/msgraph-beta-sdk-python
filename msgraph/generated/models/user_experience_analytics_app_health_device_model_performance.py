from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsAppHealthDeviceModelPerformance(entity.Entity):
    """
    The user experience analytics device model performance entity contains device model performance details.
    """
    @property
    def active_device_count(self,) -> Optional[int]:
        """
        Gets the activeDeviceCount property value. The number of active devices for the model. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._active_device_count
    
    @active_device_count.setter
    def active_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activeDeviceCount property value. The number of active devices for the model. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the activeDeviceCount property.
        """
        self._active_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAppHealthDeviceModelPerformance and sets the default values.
        """
        super().__init__()
        # The number of active devices for the model. Valid values -2147483648 to 2147483647
        self._active_device_count: Optional[int] = None
        # The manufacturer name of the device.
        self._device_manufacturer: Optional[str] = None
        # The model name of the device.
        self._device_model: Optional[str] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The mean time to failure for the model device in minutes. Valid values -2147483648 to 2147483647
        self._mean_time_to_failure_in_minutes: Optional[int] = None
        # The app health score of the device model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._model_app_health_score: Optional[float] = None
        # The overall app health status of the device model.
        self._model_app_health_status: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthDeviceModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthDeviceModelPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAppHealthDeviceModelPerformance()
    
    @property
    def device_manufacturer(self,) -> Optional[str]:
        """
        Gets the deviceManufacturer property value. The manufacturer name of the device.
        Returns: Optional[str]
        """
        return self._device_manufacturer
    
    @device_manufacturer.setter
    def device_manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceManufacturer property value. The manufacturer name of the device.
        Args:
            value: Value to set for the deviceManufacturer property.
        """
        self._device_manufacturer = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. The model name of the device.
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. The model name of the device.
        Args:
            value: Value to set for the deviceModel property.
        """
        self._device_model = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_device_count": lambda n : setattr(self, 'active_device_count', n.get_int_value()),
            "device_manufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "mean_time_to_failure_in_minutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "model_app_health_score": lambda n : setattr(self, 'model_app_health_score', n.get_float_value()),
            "model_app_health_status": lambda n : setattr(self, 'model_app_health_status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_status(self,) -> Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]:
        """
        Gets the healthStatus property value. The healthStatus property
        Returns: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None) -> None:
        """
        Sets the healthStatus property value. The healthStatus property
        Args:
            value: Value to set for the healthStatus property.
        """
        self._health_status = value
    
    @property
    def mean_time_to_failure_in_minutes(self,) -> Optional[int]:
        """
        Gets the meanTimeToFailureInMinutes property value. The mean time to failure for the model device in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._mean_time_to_failure_in_minutes
    
    @mean_time_to_failure_in_minutes.setter
    def mean_time_to_failure_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the meanTimeToFailureInMinutes property value. The mean time to failure for the model device in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the meanTimeToFailureInMinutes property.
        """
        self._mean_time_to_failure_in_minutes = value
    
    @property
    def model_app_health_score(self,) -> Optional[float]:
        """
        Gets the modelAppHealthScore property value. The app health score of the device model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._model_app_health_score
    
    @model_app_health_score.setter
    def model_app_health_score(self,value: Optional[float] = None) -> None:
        """
        Sets the modelAppHealthScore property value. The app health score of the device model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the modelAppHealthScore property.
        """
        self._model_app_health_score = value
    
    @property
    def model_app_health_status(self,) -> Optional[str]:
        """
        Gets the modelAppHealthStatus property value. The overall app health status of the device model.
        Returns: Optional[str]
        """
        return self._model_app_health_status
    
    @model_app_health_status.setter
    def model_app_health_status(self,value: Optional[str] = None) -> None:
        """
        Sets the modelAppHealthStatus property value. The overall app health status of the device model.
        Args:
            value: Value to set for the modelAppHealthStatus property.
        """
        self._model_app_health_status = value
    
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
        writer.write_str_value("deviceManufacturer", self.device_manufacturer)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_float_value("modelAppHealthScore", self.model_app_health_score)
        writer.write_str_value("modelAppHealthStatus", self.model_app_health_status)
    

