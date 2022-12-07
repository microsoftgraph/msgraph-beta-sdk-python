from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserExperienceAnalyticsAutopilotDevicesSummary(AdditionalDataHolder, Parsable):
    """
    The user experience analytics summary of Devices not windows autopilot ready.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAutopilotDevicesSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The count of intune devices that are not autopilot registerd.
        self._devices_not_autopilot_registered: Optional[int] = None
        # The count of intune devices not autopilot profile assigned.
        self._devices_without_autopilot_profile_assigned: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The count of windows 10 devices that are Intune and Comanaged.
        self._total_windows10_devices_without_tenant_attached: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAutopilotDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAutopilotDevicesSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAutopilotDevicesSummary()
    
    @property
    def devices_not_autopilot_registered(self,) -> Optional[int]:
        """
        Gets the devicesNotAutopilotRegistered property value. The count of intune devices that are not autopilot registerd.
        Returns: Optional[int]
        """
        return self._devices_not_autopilot_registered
    
    @devices_not_autopilot_registered.setter
    def devices_not_autopilot_registered(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesNotAutopilotRegistered property value. The count of intune devices that are not autopilot registerd.
        Args:
            value: Value to set for the devicesNotAutopilotRegistered property.
        """
        self._devices_not_autopilot_registered = value
    
    @property
    def devices_without_autopilot_profile_assigned(self,) -> Optional[int]:
        """
        Gets the devicesWithoutAutopilotProfileAssigned property value. The count of intune devices not autopilot profile assigned.
        Returns: Optional[int]
        """
        return self._devices_without_autopilot_profile_assigned
    
    @devices_without_autopilot_profile_assigned.setter
    def devices_without_autopilot_profile_assigned(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesWithoutAutopilotProfileAssigned property value. The count of intune devices not autopilot profile assigned.
        Args:
            value: Value to set for the devicesWithoutAutopilotProfileAssigned property.
        """
        self._devices_without_autopilot_profile_assigned = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "devices_not_autopilot_registered": lambda n : setattr(self, 'devices_not_autopilot_registered', n.get_int_value()),
            "devices_without_autopilot_profile_assigned": lambda n : setattr(self, 'devices_without_autopilot_profile_assigned', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total_windows10_devices_without_tenant_attached": lambda n : setattr(self, 'total_windows10_devices_without_tenant_attached', n.get_int_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("devicesNotAutopilotRegistered", self.devices_not_autopilot_registered)
        writer.write_int_value("devicesWithoutAutopilotProfileAssigned", self.devices_without_autopilot_profile_assigned)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalWindows10DevicesWithoutTenantAttached", self.total_windows10_devices_without_tenant_attached)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_windows10_devices_without_tenant_attached(self,) -> Optional[int]:
        """
        Gets the totalWindows10DevicesWithoutTenantAttached property value. The count of windows 10 devices that are Intune and Comanaged.
        Returns: Optional[int]
        """
        return self._total_windows10_devices_without_tenant_attached
    
    @total_windows10_devices_without_tenant_attached.setter
    def total_windows10_devices_without_tenant_attached(self,value: Optional[int] = None) -> None:
        """
        Sets the totalWindows10DevicesWithoutTenantAttached property value. The count of windows 10 devices that are Intune and Comanaged.
        Args:
            value: Value to set for the totalWindows10DevicesWithoutTenantAttached property.
        """
        self._total_windows10_devices_without_tenant_attached = value
    

