from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_exchange_access_level = lazy_import('msgraph.generated.models.device_management_exchange_access_level')
device_management_exchange_device_class = lazy_import('msgraph.generated.models.device_management_exchange_device_class')

class DeviceManagementExchangeAccessRule(AdditionalDataHolder, Parsable):
    """
    Device Access Rules in Exchange.
    """
    @property
    def access_level(self,) -> Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel]:
        """
        Gets the accessLevel property value. Access Level in Exchange.
        Returns: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel]
        """
        return self._access_level
    
    @access_level.setter
    def access_level(self,value: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel] = None) -> None:
        """
        Sets the accessLevel property value. Access Level in Exchange.
        Args:
            value: Value to set for the accessLevel property.
        """
        self._access_level = value
    
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
        Instantiates a new deviceManagementExchangeAccessRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Access Level in Exchange.
        self._access_level: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel] = None
        # Device Class which will be impacted by this rule.
        self._device_class: Optional[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExchangeAccessRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeAccessRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementExchangeAccessRule()
    
    @property
    def device_class(self,) -> Optional[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]:
        """
        Gets the deviceClass property value. Device Class which will be impacted by this rule.
        Returns: Optional[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]
        """
        return self._device_class
    
    @device_class.setter
    def device_class(self,value: Optional[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass] = None) -> None:
        """
        Sets the deviceClass property value. Device Class which will be impacted by this rule.
        Args:
            value: Value to set for the deviceClass property.
        """
        self._device_class = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_level": lambda n : setattr(self, 'access_level', n.get_enum_value(device_management_exchange_access_level.DeviceManagementExchangeAccessLevel)),
            "device_class": lambda n : setattr(self, 'device_class', n.get_object_value(device_management_exchange_device_class.DeviceManagementExchangeDeviceClass)),
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
        writer.write_enum_value("accessLevel", self.access_level)
        writer.write_object_value("deviceClass", self.device_class)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

