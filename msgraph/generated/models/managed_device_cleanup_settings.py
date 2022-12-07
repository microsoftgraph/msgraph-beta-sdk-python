from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ManagedDeviceCleanupSettings(AdditionalDataHolder, Parsable):
    """
    Define the rule when the admin wants the devices to be cleaned up.
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
        Instantiates a new managedDeviceCleanupSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of days when the device has not contacted Intune.
        self._device_inactivity_before_retirement_in_days: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceCleanupSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceCleanupSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceCleanupSettings()
    
    @property
    def device_inactivity_before_retirement_in_days(self,) -> Optional[str]:
        """
        Gets the deviceInactivityBeforeRetirementInDays property value. Number of days when the device has not contacted Intune.
        Returns: Optional[str]
        """
        return self._device_inactivity_before_retirement_in_days
    
    @device_inactivity_before_retirement_in_days.setter
    def device_inactivity_before_retirement_in_days(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceInactivityBeforeRetirementInDays property value. Number of days when the device has not contacted Intune.
        Args:
            value: Value to set for the deviceInactivityBeforeRetirementInDays property.
        """
        self._device_inactivity_before_retirement_in_days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_inactivity_before_retirement_in_days": lambda n : setattr(self, 'device_inactivity_before_retirement_in_days', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("deviceInactivityBeforeRetirementInDays", self.device_inactivity_before_retirement_in_days)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

