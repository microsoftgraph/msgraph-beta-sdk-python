from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_applicability_rule_type, windows10_device_mode_type

@dataclass
class DeviceManagementApplicabilityRuleDeviceMode(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Windows 10 Device Mode type.
    device_mode: Optional[windows10_device_mode_type.Windows10DeviceModeType] = None
    # Name for object.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported Applicability rule types for Device Configuration
    rule_type: Optional[device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementApplicabilityRuleDeviceMode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementApplicabilityRuleDeviceMode
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementApplicabilityRuleDeviceMode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_applicability_rule_type, windows10_device_mode_type

        from . import device_management_applicability_rule_type, windows10_device_mode_type

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceMode": lambda n : setattr(self, 'device_mode', n.get_enum_value(windows10_device_mode_type.Windows10DeviceModeType)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(device_management_applicability_rule_type.DeviceManagementApplicabilityRuleType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("deviceMode", self.device_mode)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleType", self.rule_type)
        writer.write_additional_data_value(self.additional_data)
    

