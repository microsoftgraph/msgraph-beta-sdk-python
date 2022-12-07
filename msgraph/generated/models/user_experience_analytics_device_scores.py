from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsDeviceScores(entity.Entity):
    """
    The user experience analytics device scores entity consolidates the various endpoint analytics scores.
    """
    @property
    def app_reliability_score(self,) -> Optional[float]:
        """
        Gets the appReliabilityScore property value. The user experience analytics device app reliability score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._app_reliability_score
    
    @app_reliability_score.setter
    def app_reliability_score(self,value: Optional[float] = None) -> None:
        """
        Sets the appReliabilityScore property value. The user experience analytics device app reliability score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the appReliabilityScore property.
        """
        self._app_reliability_score = value
    
    @property
    def battery_health_score(self,) -> Optional[float]:
        """
        Gets the batteryHealthScore property value. The user experience analytics device battery health score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._battery_health_score
    
    @battery_health_score.setter
    def battery_health_score(self,value: Optional[float] = None) -> None:
        """
        Sets the batteryHealthScore property value. The user experience analytics device battery health score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the batteryHealthScore property.
        """
        self._battery_health_score = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsDeviceScores and sets the default values.
        """
        super().__init__()
        # The user experience analytics device app reliability score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._app_reliability_score: Optional[float] = None
        # The user experience analytics device battery health score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._battery_health_score: Optional[float] = None
        # The user experience analytics device name.
        self._device_name: Optional[str] = None
        # The user experience analytics device score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._endpoint_analytics_score: Optional[float] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The user experience analytics device manufacturer.
        self._manufacturer: Optional[str] = None
        # The user experience analytics device model.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._startup_performance_score: Optional[float] = None
        # The user experience analytics device work From anywhere score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._work_from_anywhere_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceScores:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceScores
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceScores()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The user experience analytics device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The user experience analytics device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def endpoint_analytics_score(self,) -> Optional[float]:
        """
        Gets the endpointAnalyticsScore property value. The user experience analytics device score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._endpoint_analytics_score
    
    @endpoint_analytics_score.setter
    def endpoint_analytics_score(self,value: Optional[float] = None) -> None:
        """
        Sets the endpointAnalyticsScore property value. The user experience analytics device score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the endpointAnalyticsScore property.
        """
        self._endpoint_analytics_score = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_reliability_score": lambda n : setattr(self, 'app_reliability_score', n.get_float_value()),
            "battery_health_score": lambda n : setattr(self, 'battery_health_score', n.get_float_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "endpoint_analytics_score": lambda n : setattr(self, 'endpoint_analytics_score', n.get_float_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "startup_performance_score": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
            "work_from_anywhere_score": lambda n : setattr(self, 'work_from_anywhere_score', n.get_float_value()),
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
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The user experience analytics device manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The user experience analytics device manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The user experience analytics device model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The user experience analytics device model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("appReliabilityScore", self.app_reliability_score)
        writer.write_float_value("batteryHealthScore", self.battery_health_score)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_float_value("endpointAnalyticsScore", self.endpoint_analytics_score)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("startupPerformanceScore", self.startup_performance_score)
        writer.write_float_value("workFromAnywhereScore", self.work_from_anywhere_score)
    
    @property
    def startup_performance_score(self,) -> Optional[float]:
        """
        Gets the startupPerformanceScore property value. The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._startup_performance_score
    
    @startup_performance_score.setter
    def startup_performance_score(self,value: Optional[float] = None) -> None:
        """
        Sets the startupPerformanceScore property value. The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the startupPerformanceScore property.
        """
        self._startup_performance_score = value
    
    @property
    def work_from_anywhere_score(self,) -> Optional[float]:
        """
        Gets the workFromAnywhereScore property value. The user experience analytics device work From anywhere score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._work_from_anywhere_score
    
    @work_from_anywhere_score.setter
    def work_from_anywhere_score(self,value: Optional[float] = None) -> None:
        """
        Sets the workFromAnywhereScore property value. The user experience analytics device work From anywhere score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the workFromAnywhereScore property.
        """
        self._work_from_anywhere_score = value
    

