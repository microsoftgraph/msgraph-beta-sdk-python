from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_script_error, device_compliance_script_rule, device_compliance_script_rule_error

@dataclass
class DeviceComplianceScriptValidationResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Errors in json for the script for rules.
    rule_errors: Optional[List[device_compliance_script_rule_error.DeviceComplianceScriptRuleError]] = None
    # Parsed rules from json.
    rules: Optional[List[device_compliance_script_rule.DeviceComplianceScriptRule]] = None
    # Errors in json for the script.
    script_errors: Optional[List[device_compliance_script_error.DeviceComplianceScriptError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptValidationResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScriptValidationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_script_error, device_compliance_script_rule, device_compliance_script_rule_error

        from . import device_compliance_script_error, device_compliance_script_rule, device_compliance_script_rule_error

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleErrors": lambda n : setattr(self, 'rule_errors', n.get_collection_of_object_values(device_compliance_script_rule_error.DeviceComplianceScriptRuleError)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(device_compliance_script_rule.DeviceComplianceScriptRule)),
            "scriptErrors": lambda n : setattr(self, 'script_errors', n.get_collection_of_object_values(device_compliance_script_error.DeviceComplianceScriptError)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("ruleErrors", self.rule_errors)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_collection_of_object_values("scriptErrors", self.script_errors)
        writer.write_additional_data_value(self.additional_data)
    

