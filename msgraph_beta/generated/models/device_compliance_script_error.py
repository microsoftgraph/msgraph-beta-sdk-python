from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .code import Code
    from .device_compliance_script_rules_validation_error import DeviceComplianceScriptRulesValidationError
    from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError

@dataclass
class DeviceComplianceScriptError(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Error code for rule validation.
    code: Optional[Code] = None
    # Error code for rule validation.
    device_compliance_script_rules_validation_error: Optional[DeviceComplianceScriptRulesValidationError] = None
    # Error message.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceScriptError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScriptRuleError".casefold():
            from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError

            return DeviceComplianceScriptRuleError()
        return DeviceComplianceScriptError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .code import Code
        from .device_compliance_script_rules_validation_error import DeviceComplianceScriptRulesValidationError
        from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError

        from .code import Code
        from .device_compliance_script_rules_validation_error import DeviceComplianceScriptRulesValidationError
        from .device_compliance_script_rule_error import DeviceComplianceScriptRuleError

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(Code)),
            "deviceComplianceScriptRulesValidationError": lambda n : setattr(self, 'device_compliance_script_rules_validation_error', n.get_enum_value(DeviceComplianceScriptRulesValidationError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("code", self.code)
        writer.write_enum_value("deviceComplianceScriptRulesValidationError", self.device_compliance_script_rules_validation_error)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

