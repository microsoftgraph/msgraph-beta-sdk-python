from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_applicability_rule_type, windows10_device_mode_type

class DeviceManagementApplicabilityRuleDeviceMode(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementApplicabilityRuleDeviceMode and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Windows 10 Device Mode type.
        self._device_mode: Optional[windows10_device_mode_type.Windows10DeviceModeType] = None
        # Name for object.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Supported Applicability rule types for Device Configuration
        self._rule_type: Optional[device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementApplicabilityRuleDeviceMode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementApplicabilityRuleDeviceMode
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementApplicabilityRuleDeviceMode()
    
    @property
    def device_mode(self,) -> Optional[windows10_device_mode_type.Windows10DeviceModeType]:
        """
        Gets the deviceMode property value. Windows 10 Device Mode type.
        Returns: Optional[windows10_device_mode_type.Windows10DeviceModeType]
        """
        return self._device_mode
    
    @device_mode.setter
    def device_mode(self,value: Optional[windows10_device_mode_type.Windows10DeviceModeType] = None) -> None:
        """
        Sets the deviceMode property value. Windows 10 Device Mode type.
        Args:
            value: Value to set for the device_mode property.
        """
        self._device_mode = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_applicability_rule_type, windows10_device_mode_type

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceMode": lambda n : setattr(self, 'device_mode', n.get_enum_value(windows10_device_mode_type.Windows10DeviceModeType)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType)),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name for object.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name for object.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def rule_type(self,) -> Optional[device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType]:
        """
        Gets the ruleType property value. Supported Applicability rule types for Device Configuration
        Returns: Optional[device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType]
        """
        return self._rule_type
    
    @rule_type.setter
    def rule_type(self,value: Optional[device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType] = None) -> None:
        """
        Sets the ruleType property value. Supported Applicability rule types for Device Configuration
        Args:
            value: Value to set for the rule_type property.
        """
        self._rule_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("deviceMode", self.device_mode)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleType", self.rule_type)
        writer.write_additional_data_value(self.additional_data)
    

