from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsNotAutopilotReadyDevice(entity.Entity):
    """
    The user experience analytics Device not windows autopilot ready.
    """
    @property
    def auto_pilot_profile_assigned(self,) -> Optional[bool]:
        """
        Gets the autoPilotProfileAssigned property value. The intune device's autopilotProfileAssigned.
        Returns: Optional[bool]
        """
        return self._auto_pilot_profile_assigned
    
    @auto_pilot_profile_assigned.setter
    def auto_pilot_profile_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoPilotProfileAssigned property value. The intune device's autopilotProfileAssigned.
        Args:
            value: Value to set for the autoPilotProfileAssigned property.
        """
        self._auto_pilot_profile_assigned = value
    
    @property
    def auto_pilot_registered(self,) -> Optional[bool]:
        """
        Gets the autoPilotRegistered property value. The intune device's autopilotRegistered.
        Returns: Optional[bool]
        """
        return self._auto_pilot_registered
    
    @auto_pilot_registered.setter
    def auto_pilot_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoPilotRegistered property value. The intune device's autopilotRegistered.
        Args:
            value: Value to set for the autoPilotRegistered property.
        """
        self._auto_pilot_registered = value
    
    @property
    def azure_ad_join_type(self,) -> Optional[str]:
        """
        Gets the azureAdJoinType property value. The intune device's azure Ad joinType.
        Returns: Optional[str]
        """
        return self._azure_ad_join_type
    
    @azure_ad_join_type.setter
    def azure_ad_join_type(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdJoinType property value. The intune device's azure Ad joinType.
        Args:
            value: Value to set for the azureAdJoinType property.
        """
        self._azure_ad_join_type = value
    
    @property
    def azure_ad_registered(self,) -> Optional[bool]:
        """
        Gets the azureAdRegistered property value. The intune device's azureAdRegistered.
        Returns: Optional[bool]
        """
        return self._azure_ad_registered
    
    @azure_ad_registered.setter
    def azure_ad_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the azureAdRegistered property value. The intune device's azureAdRegistered.
        Args:
            value: Value to set for the azureAdRegistered property.
        """
        self._azure_ad_registered = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsNotAutopilotReadyDevice and sets the default values.
        """
        super().__init__()
        # The intune device's autopilotProfileAssigned.
        self._auto_pilot_profile_assigned: Optional[bool] = None
        # The intune device's autopilotRegistered.
        self._auto_pilot_registered: Optional[bool] = None
        # The intune device's azure Ad joinType.
        self._azure_ad_join_type: Optional[str] = None
        # The intune device's azureAdRegistered.
        self._azure_ad_registered: Optional[bool] = None
        # The intune device's name.
        self._device_name: Optional[str] = None
        # The intune device's managed by.
        self._managed_by: Optional[str] = None
        # The intune device's manufacturer.
        self._manufacturer: Optional[str] = None
        # The intune device's model.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The intune device's serial number.
        self._serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsNotAutopilotReadyDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsNotAutopilotReadyDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsNotAutopilotReadyDevice()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The intune device's name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The intune device's name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auto_pilot_profile_assigned": lambda n : setattr(self, 'auto_pilot_profile_assigned', n.get_bool_value()),
            "auto_pilot_registered": lambda n : setattr(self, 'auto_pilot_registered', n.get_bool_value()),
            "azure_ad_join_type": lambda n : setattr(self, 'azure_ad_join_type', n.get_str_value()),
            "azure_ad_registered": lambda n : setattr(self, 'azure_ad_registered', n.get_bool_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managed_by": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_by(self,) -> Optional[str]:
        """
        Gets the managedBy property value. The intune device's managed by.
        Returns: Optional[str]
        """
        return self._managed_by
    
    @managed_by.setter
    def managed_by(self,value: Optional[str] = None) -> None:
        """
        Sets the managedBy property value. The intune device's managed by.
        Args:
            value: Value to set for the managedBy property.
        """
        self._managed_by = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The intune device's manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The intune device's manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The intune device's model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The intune device's model.
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
        writer.write_bool_value("autoPilotProfileAssigned", self.auto_pilot_profile_assigned)
        writer.write_bool_value("autoPilotRegistered", self.auto_pilot_registered)
        writer.write_str_value("azureAdJoinType", self.azure_ad_join_type)
        writer.write_bool_value("azureAdRegistered", self.azure_ad_registered)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("serialNumber", self.serial_number)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. The intune device's serial number.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. The intune device's serial number.
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    

