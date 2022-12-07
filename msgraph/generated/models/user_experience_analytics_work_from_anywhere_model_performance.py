from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsWorkFromAnywhereModelPerformance(entity.Entity):
    """
    The user experience analytics work from anywhere model performance.
    """
    @property
    def cloud_identity_score(self,) -> Optional[float]:
        """
        Gets the cloudIdentityScore property value. The user experience work from anywhere's cloud identity score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_identity_score
    
    @cloud_identity_score.setter
    def cloud_identity_score(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudIdentityScore property value. The user experience work from anywhere's cloud identity score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloudIdentityScore property.
        """
        self._cloud_identity_score = value
    
    @property
    def cloud_management_score(self,) -> Optional[float]:
        """
        Gets the cloudManagementScore property value. The user experience work from anywhere's cloud management score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_management_score
    
    @cloud_management_score.setter
    def cloud_management_score(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudManagementScore property value. The user experience work from anywhere's cloud management score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloudManagementScore property.
        """
        self._cloud_management_score = value
    
    @property
    def cloud_provisioning_score(self,) -> Optional[float]:
        """
        Gets the cloudProvisioningScore property value. The user experience work from anywhere's cloud provisioning score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_provisioning_score
    
    @cloud_provisioning_score.setter
    def cloud_provisioning_score(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudProvisioningScore property value. The user experience work from anywhere's cloud provisioning score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloudProvisioningScore property.
        """
        self._cloud_provisioning_score = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsWorkFromAnywhereModelPerformance and sets the default values.
        """
        super().__init__()
        # The user experience work from anywhere's cloud identity score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._cloud_identity_score: Optional[float] = None
        # The user experience work from anywhere's cloud management score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._cloud_management_score: Optional[float] = None
        # The user experience work from anywhere's cloud provisioning score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._cloud_provisioning_score: Optional[float] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The user experience work from anywhere's manufacturer name of the devices.
        self._manufacturer: Optional[str] = None
        # The user experience work from anywhere's model name of the devices.
        self._model: Optional[str] = None
        # The user experience work from anywhere's devices count for the model. Valid values -2147483648 to 2147483647
        self._model_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience work from anywhere windows score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._windows_score: Optional[float] = None
        # The user experience work from anywhere overall score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._work_from_anywhere_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsWorkFromAnywhereModelPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cloud_identity_score": lambda n : setattr(self, 'cloud_identity_score', n.get_float_value()),
            "cloud_management_score": lambda n : setattr(self, 'cloud_management_score', n.get_float_value()),
            "cloud_provisioning_score": lambda n : setattr(self, 'cloud_provisioning_score', n.get_float_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "model_device_count": lambda n : setattr(self, 'model_device_count', n.get_int_value()),
            "windows_score": lambda n : setattr(self, 'windows_score', n.get_float_value()),
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
        Gets the manufacturer property value. The user experience work from anywhere's manufacturer name of the devices.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The user experience work from anywhere's manufacturer name of the devices.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The user experience work from anywhere's model name of the devices.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The user experience work from anywhere's model name of the devices.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def model_device_count(self,) -> Optional[int]:
        """
        Gets the modelDeviceCount property value. The user experience work from anywhere's devices count for the model. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._model_device_count
    
    @model_device_count.setter
    def model_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the modelDeviceCount property value. The user experience work from anywhere's devices count for the model. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the modelDeviceCount property.
        """
        self._model_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("cloudIdentityScore", self.cloud_identity_score)
        writer.write_float_value("cloudManagementScore", self.cloud_management_score)
        writer.write_float_value("cloudProvisioningScore", self.cloud_provisioning_score)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_int_value("modelDeviceCount", self.model_device_count)
        writer.write_float_value("windowsScore", self.windows_score)
        writer.write_float_value("workFromAnywhereScore", self.work_from_anywhere_score)
    
    @property
    def windows_score(self,) -> Optional[float]:
        """
        Gets the windowsScore property value. The user experience work from anywhere windows score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._windows_score
    
    @windows_score.setter
    def windows_score(self,value: Optional[float] = None) -> None:
        """
        Sets the windowsScore property value. The user experience work from anywhere windows score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the windowsScore property.
        """
        self._windows_score = value
    
    @property
    def work_from_anywhere_score(self,) -> Optional[float]:
        """
        Gets the workFromAnywhereScore property value. The user experience work from anywhere overall score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._work_from_anywhere_score
    
    @work_from_anywhere_score.setter
    def work_from_anywhere_score(self,value: Optional[float] = None) -> None:
        """
        Sets the workFromAnywhereScore property value. The user experience work from anywhere overall score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the workFromAnywhereScore property.
        """
        self._work_from_anywhere_score = value
    

