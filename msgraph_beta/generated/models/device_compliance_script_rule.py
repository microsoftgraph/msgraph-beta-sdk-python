from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_type import DataType
    from .device_compliance_script_rule_data_type import DeviceComplianceScriptRuleDataType
    from .device_compliance_script_rul_operator import DeviceComplianceScriptRulOperator
    from .operator import Operator

@dataclass
class DeviceComplianceScriptRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Data types for rules.
    data_type: Optional[DataType] = None
    # Operator for rules.
    device_compliance_script_rul_operator: Optional[DeviceComplianceScriptRulOperator] = None
    # Data types for rules.
    device_compliance_script_rule_data_type: Optional[DeviceComplianceScriptRuleDataType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operand specified in the rule.
    operand: Optional[str] = None
    # Operator for rules.
    operator: Optional[Operator] = None
    # Setting name specified in the rule.
    setting_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceScriptRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScriptRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .data_type import DataType
        from .device_compliance_script_rule_data_type import DeviceComplianceScriptRuleDataType
        from .device_compliance_script_rul_operator import DeviceComplianceScriptRulOperator
        from .operator import Operator

        from .data_type import DataType
        from .device_compliance_script_rule_data_type import DeviceComplianceScriptRuleDataType
        from .device_compliance_script_rul_operator import DeviceComplianceScriptRulOperator
        from .operator import Operator

        fields: Dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(DataType)),
            "deviceComplianceScriptRulOperator": lambda n : setattr(self, 'device_compliance_script_rul_operator', n.get_enum_value(DeviceComplianceScriptRulOperator)),
            "deviceComplianceScriptRuleDataType": lambda n : setattr(self, 'device_compliance_script_rule_data_type', n.get_enum_value(DeviceComplianceScriptRuleDataType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operand": lambda n : setattr(self, 'operand', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(Operator)),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
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
        writer.write_enum_value("dataType", self.data_type)
        writer.write_enum_value("deviceComplianceScriptRulOperator", self.device_compliance_script_rul_operator)
        writer.write_enum_value("deviceComplianceScriptRuleDataType", self.device_compliance_script_rule_data_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operand", self.operand)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_additional_data_value(self.additional_data)
    

