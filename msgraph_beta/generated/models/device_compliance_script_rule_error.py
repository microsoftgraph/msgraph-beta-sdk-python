from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_script_error import DeviceComplianceScriptError

from .device_compliance_script_error import DeviceComplianceScriptError

@dataclass
class DeviceComplianceScriptRuleError(DeviceComplianceScriptError):
    # The OdataType property
    odata_type: Optional[str] = None
    # Setting name for the rule with error.
    setting_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceScriptRuleError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptRuleError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScriptRuleError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_script_error import DeviceComplianceScriptError

        from .device_compliance_script_error import DeviceComplianceScriptError

        fields: Dict[str, Callable[[Any], None]] = {
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("settingName", self.setting_name)
    

