from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserExperienceAnalyticsWindows10DevicesSummary(AdditionalDataHolder, Parsable):
    """
    The user experience analytics work from anywhere Windows 10 devices summary.
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
        Instantiates a new userExperienceAnalyticsWindows10DevicesSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The count of Windows 10 devices that have unsupported OS versions.
        self._unsupported_o_sversion_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWindows10DevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWindows10DevicesSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsWindows10DevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unsupported_o_sversion_device_count": lambda n : setattr(self, 'unsupported_o_sversion_device_count', n.get_int_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("unsupportedOSversionDeviceCount", self.unsupported_o_sversion_device_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def unsupported_o_sversion_device_count(self,) -> Optional[int]:
        """
        Gets the unsupportedOSversionDeviceCount property value. The count of Windows 10 devices that have unsupported OS versions.
        Returns: Optional[int]
        """
        return self._unsupported_o_sversion_device_count
    
    @unsupported_o_sversion_device_count.setter
    def unsupported_o_sversion_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unsupportedOSversionDeviceCount property value. The count of Windows 10 devices that have unsupported OS versions.
        Args:
            value: Value to set for the unsupportedOSversionDeviceCount property.
        """
        self._unsupported_o_sversion_device_count = value
    

