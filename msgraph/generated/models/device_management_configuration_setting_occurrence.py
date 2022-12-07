from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceManagementConfigurationSettingOccurrence(AdditionalDataHolder, Parsable):
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
        Instantiates a new deviceManagementConfigurationSettingOccurrence and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Maximum times setting can be set on device.
        self._max_device_occurrence: Optional[int] = None
        # Minimum times setting can be set on device. A MinDeviceOccurrence of 0 means setting is optional
        self._min_device_occurrence: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingOccurrence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingOccurrence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingOccurrence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "max_device_occurrence": lambda n : setattr(self, 'max_device_occurrence', n.get_int_value()),
            "min_device_occurrence": lambda n : setattr(self, 'min_device_occurrence', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def max_device_occurrence(self,) -> Optional[int]:
        """
        Gets the maxDeviceOccurrence property value. Maximum times setting can be set on device.
        Returns: Optional[int]
        """
        return self._max_device_occurrence
    
    @max_device_occurrence.setter
    def max_device_occurrence(self,value: Optional[int] = None) -> None:
        """
        Sets the maxDeviceOccurrence property value. Maximum times setting can be set on device.
        Args:
            value: Value to set for the maxDeviceOccurrence property.
        """
        self._max_device_occurrence = value
    
    @property
    def min_device_occurrence(self,) -> Optional[int]:
        """
        Gets the minDeviceOccurrence property value. Minimum times setting can be set on device. A MinDeviceOccurrence of 0 means setting is optional
        Returns: Optional[int]
        """
        return self._min_device_occurrence
    
    @min_device_occurrence.setter
    def min_device_occurrence(self,value: Optional[int] = None) -> None:
        """
        Sets the minDeviceOccurrence property value. Minimum times setting can be set on device. A MinDeviceOccurrence of 0 means setting is optional
        Args:
            value: Value to set for the minDeviceOccurrence property.
        """
        self._min_device_occurrence = value
    
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
        writer.write_int_value("maxDeviceOccurrence", self.max_device_occurrence)
        writer.write_int_value("minDeviceOccurrence", self.min_device_occurrence)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

