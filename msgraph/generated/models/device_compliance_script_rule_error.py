from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_script_error = lazy_import('msgraph.generated.models.device_compliance_script_error')

class DeviceComplianceScriptRuleError(device_compliance_script_error.DeviceComplianceScriptError):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceComplianceScriptRuleError and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Setting name for the rule with error.
        self._setting_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptRuleError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptRuleError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScriptRuleError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("settingName", self.setting_name)
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. Setting name for the rule with error.
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. Setting name for the rule with error.
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    

