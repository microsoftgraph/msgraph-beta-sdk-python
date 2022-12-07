from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_type = lazy_import('msgraph.generated.models.device_type')

class MobileAppSupportedDeviceType(AdditionalDataHolder, Parsable):
    """
    Device properties
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
        Instantiates a new mobileAppSupportedDeviceType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Maximum OS version
        self._maximum_operating_system_version: Optional[str] = None
        # Minimum OS version
        self._minimum_operating_system_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Device type.
        self._type: Optional[device_type.DeviceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppSupportedDeviceType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppSupportedDeviceType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppSupportedDeviceType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maximum_operating_system_version": lambda n : setattr(self, 'maximum_operating_system_version', n.get_str_value()),
            "minimum_operating_system_version": lambda n : setattr(self, 'minimum_operating_system_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(device_type.DeviceType)),
        }
        return fields
    
    @property
    def maximum_operating_system_version(self,) -> Optional[str]:
        """
        Gets the maximumOperatingSystemVersion property value. Maximum OS version
        Returns: Optional[str]
        """
        return self._maximum_operating_system_version
    
    @maximum_operating_system_version.setter
    def maximum_operating_system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the maximumOperatingSystemVersion property value. Maximum OS version
        Args:
            value: Value to set for the maximumOperatingSystemVersion property.
        """
        self._maximum_operating_system_version = value
    
    @property
    def minimum_operating_system_version(self,) -> Optional[str]:
        """
        Gets the minimumOperatingSystemVersion property value. Minimum OS version
        Returns: Optional[str]
        """
        return self._minimum_operating_system_version
    
    @minimum_operating_system_version.setter
    def minimum_operating_system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumOperatingSystemVersion property value. Minimum OS version
        Args:
            value: Value to set for the minimumOperatingSystemVersion property.
        """
        self._minimum_operating_system_version = value
    
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
        writer.write_str_value("maximumOperatingSystemVersion", self.maximum_operating_system_version)
        writer.write_str_value("minimumOperatingSystemVersion", self.minimum_operating_system_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[device_type.DeviceType]:
        """
        Gets the type property value. Device type.
        Returns: Optional[device_type.DeviceType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[device_type.DeviceType] = None) -> None:
        """
        Sets the type property value. Device type.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

