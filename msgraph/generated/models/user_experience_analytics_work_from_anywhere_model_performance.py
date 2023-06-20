from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_experience_analytics_health_state

from . import entity

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereModelPerformance(entity.Entity):
    """
    The user experience analytics work from anywhere model performance.
    """
    # The user experience work from anywhere's cloud identity score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_identity_score: Optional[float] = None
    # The user experience work from anywhere's cloud management score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_management_score: Optional[float] = None
    # The user experience work from anywhere's cloud provisioning score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_provisioning_score: Optional[float] = None
    # The healthStatus property
    health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
    # The user experience work from anywhere's manufacturer name of the devices.
    manufacturer: Optional[str] = None
    # The user experience work from anywhere's model name of the devices.
    model: Optional[str] = None
    # The user experience work from anywhere's devices count for the model. Valid values -2147483648 to 2147483647
    model_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience work from anywhere windows score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    windows_score: Optional[float] = None
    # The user experience work from anywhere overall score for the model. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    work_from_anywhere_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsWorkFromAnywhereModelPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_experience_analytics_health_state

        from . import entity, user_experience_analytics_health_state

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudIdentityScore": lambda n : setattr(self, 'cloud_identity_score', n.get_float_value()),
            "cloudManagementScore": lambda n : setattr(self, 'cloud_management_score', n.get_float_value()),
            "cloudProvisioningScore": lambda n : setattr(self, 'cloud_provisioning_score', n.get_float_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "modelDeviceCount": lambda n : setattr(self, 'model_device_count', n.get_int_value()),
            "windowsScore": lambda n : setattr(self, 'windows_score', n.get_float_value()),
            "workFromAnywhereScore": lambda n : setattr(self, 'work_from_anywhere_score', n.get_float_value()),
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
        writer.write_float_value("cloudIdentityScore", self.cloud_identity_score)
        writer.write_float_value("cloudManagementScore", self.cloud_management_score)
        writer.write_float_value("cloudProvisioningScore", self.cloud_provisioning_score)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_int_value("modelDeviceCount", self.model_device_count)
        writer.write_float_value("windowsScore", self.windows_score)
        writer.write_float_value("workFromAnywhereScore", self.work_from_anywhere_score)
    

