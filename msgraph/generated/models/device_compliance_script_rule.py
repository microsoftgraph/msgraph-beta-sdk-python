from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_type, device_compliance_script_rule_data_type, device_compliance_script_rul_operator, operator

@dataclass
class DeviceComplianceScriptRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Data types for rules.
    data_type: Optional[data_type.DataType] = None
    # Operator for rules.
    device_compliance_script_rul_operator: Optional[device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator] = None
    # Data types for rules.
    device_compliance_script_rule_data_type: Optional[device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operand specified in the rule.
    operand: Optional[str] = None
    # Operator for rules.
    operator: Optional[operator.Operator] = None
    # Setting name specified in the rule.
    setting_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScriptRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_type, device_compliance_script_rule_data_type, device_compliance_script_rul_operator, operator

        fields: Dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(data_type.DataType)),
            "deviceComplianceScriptRuleDataType": lambda n : setattr(self, 'device_compliance_script_rule_data_type', n.get_enum_value(device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType)),
            "deviceComplianceScriptRulOperator": lambda n : setattr(self, 'device_compliance_script_rul_operator', n.get_enum_value(device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operand": lambda n : setattr(self, 'operand', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(operator.Operator)),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("dataType", self.data_type)
        writer.write_enum_value("deviceComplianceScriptRuleDataType", self.device_compliance_script_rule_data_type)
        writer.write_enum_value("deviceComplianceScriptRulOperator", self.device_compliance_script_rul_operator)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operand", self.operand)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_additional_data_value(self.additional_data)
    

