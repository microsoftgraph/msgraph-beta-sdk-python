from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_type = lazy_import('msgraph.generated.models.data_type')
device_compliance_script_rul_operator = lazy_import('msgraph.generated.models.device_compliance_script_rul_operator')
device_compliance_script_rule_data_type = lazy_import('msgraph.generated.models.device_compliance_script_rule_data_type')
operator = lazy_import('msgraph.generated.models.operator')

class DeviceComplianceScriptRule(AdditionalDataHolder, Parsable):
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
        Instantiates a new deviceComplianceScriptRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Data types for rules.
        self._data_type: Optional[data_type.DataType] = None
        # Data types for rules.
        self._device_compliance_script_rule_data_type: Optional[device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType] = None
        # Operator for rules.
        self._device_compliance_script_rul_operator: Optional[device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Operand specified in the rule.
        self._operand: Optional[str] = None
        # Operator for rules.
        self._operator: Optional[operator.Operator] = None
        # Setting name specified in the rule.
        self._setting_name: Optional[str] = None
    
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
    
    @property
    def data_type(self,) -> Optional[data_type.DataType]:
        """
        Gets the dataType property value. Data types for rules.
        Returns: Optional[data_type.DataType]
        """
        return self._data_type
    
    @data_type.setter
    def data_type(self,value: Optional[data_type.DataType] = None) -> None:
        """
        Sets the dataType property value. Data types for rules.
        Args:
            value: Value to set for the dataType property.
        """
        self._data_type = value
    
    @property
    def device_compliance_script_rule_data_type(self,) -> Optional[device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType]:
        """
        Gets the deviceComplianceScriptRuleDataType property value. Data types for rules.
        Returns: Optional[device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType]
        """
        return self._device_compliance_script_rule_data_type
    
    @device_compliance_script_rule_data_type.setter
    def device_compliance_script_rule_data_type(self,value: Optional[device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType] = None) -> None:
        """
        Sets the deviceComplianceScriptRuleDataType property value. Data types for rules.
        Args:
            value: Value to set for the deviceComplianceScriptRuleDataType property.
        """
        self._device_compliance_script_rule_data_type = value
    
    @property
    def device_compliance_script_rul_operator(self,) -> Optional[device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator]:
        """
        Gets the deviceComplianceScriptRulOperator property value. Operator for rules.
        Returns: Optional[device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator]
        """
        return self._device_compliance_script_rul_operator
    
    @device_compliance_script_rul_operator.setter
    def device_compliance_script_rul_operator(self,value: Optional[device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator] = None) -> None:
        """
        Sets the deviceComplianceScriptRulOperator property value. Operator for rules.
        Args:
            value: Value to set for the deviceComplianceScriptRulOperator property.
        """
        self._device_compliance_script_rul_operator = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_type": lambda n : setattr(self, 'data_type', n.get_enum_value(data_type.DataType)),
            "device_compliance_script_rule_data_type": lambda n : setattr(self, 'device_compliance_script_rule_data_type', n.get_enum_value(device_compliance_script_rule_data_type.DeviceComplianceScriptRuleDataType)),
            "device_compliance_script_rul_operator": lambda n : setattr(self, 'device_compliance_script_rul_operator', n.get_enum_value(device_compliance_script_rul_operator.DeviceComplianceScriptRulOperator)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operand": lambda n : setattr(self, 'operand', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(operator.Operator)),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
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
    
    @property
    def operand(self,) -> Optional[str]:
        """
        Gets the operand property value. Operand specified in the rule.
        Returns: Optional[str]
        """
        return self._operand
    
    @operand.setter
    def operand(self,value: Optional[str] = None) -> None:
        """
        Sets the operand property value. Operand specified in the rule.
        Args:
            value: Value to set for the operand property.
        """
        self._operand = value
    
    @property
    def operator(self,) -> Optional[operator.Operator]:
        """
        Gets the operator property value. Operator for rules.
        Returns: Optional[operator.Operator]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[operator.Operator] = None) -> None:
        """
        Sets the operator property value. Operator for rules.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
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
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. Setting name specified in the rule.
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. Setting name specified in the rule.
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    

