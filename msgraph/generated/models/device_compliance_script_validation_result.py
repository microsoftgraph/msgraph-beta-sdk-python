from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_script_error, device_compliance_script_rule, device_compliance_script_rule_error

class DeviceComplianceScriptValidationResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceScriptValidationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Errors in json for the script for rules.
        self._rule_errors: Optional[List[device_compliance_script_rule_error.DeviceComplianceScriptRuleError]] = None
        # Parsed rules from json.
        self._rules: Optional[List[device_compliance_script_rule.DeviceComplianceScriptRule]] = None
        # Errors in json for the script.
        self._script_errors: Optional[List[device_compliance_script_error.DeviceComplianceScriptError]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptValidationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScriptValidationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_script_error, device_compliance_script_rule, device_compliance_script_rule_error

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(device_compliance_script_rule.DeviceComplianceScriptRule)),
            "ruleErrors": lambda n : setattr(self, 'rule_errors', n.get_collection_of_object_values(device_compliance_script_rule_error.DeviceComplianceScriptRuleError)),
            "scriptErrors": lambda n : setattr(self, 'script_errors', n.get_collection_of_object_values(device_compliance_script_error.DeviceComplianceScriptError)),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def rule_errors(self,) -> Optional[List[device_compliance_script_rule_error.DeviceComplianceScriptRuleError]]:
        """
        Gets the ruleErrors property value. Errors in json for the script for rules.
        Returns: Optional[List[device_compliance_script_rule_error.DeviceComplianceScriptRuleError]]
        """
        return self._rule_errors
    
    @rule_errors.setter
    def rule_errors(self,value: Optional[List[device_compliance_script_rule_error.DeviceComplianceScriptRuleError]] = None) -> None:
        """
        Sets the ruleErrors property value. Errors in json for the script for rules.
        Args:
            value: Value to set for the rule_errors property.
        """
        self._rule_errors = value
    
    @property
    def rules(self,) -> Optional[List[device_compliance_script_rule.DeviceComplianceScriptRule]]:
        """
        Gets the rules property value. Parsed rules from json.
        Returns: Optional[List[device_compliance_script_rule.DeviceComplianceScriptRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[device_compliance_script_rule.DeviceComplianceScriptRule]] = None) -> None:
        """
        Sets the rules property value. Parsed rules from json.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    @property
    def script_errors(self,) -> Optional[List[device_compliance_script_error.DeviceComplianceScriptError]]:
        """
        Gets the scriptErrors property value. Errors in json for the script.
        Returns: Optional[List[device_compliance_script_error.DeviceComplianceScriptError]]
        """
        return self._script_errors
    
    @script_errors.setter
    def script_errors(self,value: Optional[List[device_compliance_script_error.DeviceComplianceScriptError]] = None) -> None:
        """
        Sets the scriptErrors property value. Errors in json for the script.
        Args:
            value: Value to set for the script_errors property.
        """
        self._script_errors = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_collection_of_object_values("ruleErrors", self.rule_errors)
        writer.write_collection_of_object_values("scriptErrors", self.script_errors)
        writer.write_additional_data_value(self.additional_data)
    

