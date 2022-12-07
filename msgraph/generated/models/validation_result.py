from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ValidationResult(AdditionalDataHolder, Parsable):
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
        Instantiates a new validationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The string containing the reason for why the rule passed or not. Read-only. Not nullable.
        self._message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The string containing the name of the password validation rule that the action was validated against. Read-only. Not nullable.
        self._rule_name: Optional[str] = None
        # Whether the password passed or failed the validation rule. Read-only. Not nullable.
        self._validation_passed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rule_name": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "validation_passed": lambda n : setattr(self, 'validation_passed', n.get_bool_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The string containing the reason for why the rule passed or not. Read-only. Not nullable.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The string containing the reason for why the rule passed or not. Read-only. Not nullable.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
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
    def rule_name(self,) -> Optional[str]:
        """
        Gets the ruleName property value. The string containing the name of the password validation rule that the action was validated against. Read-only. Not nullable.
        Returns: Optional[str]
        """
        return self._rule_name
    
    @rule_name.setter
    def rule_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleName property value. The string containing the name of the password validation rule that the action was validated against. Read-only. Not nullable.
        Args:
            value: Value to set for the ruleName property.
        """
        self._rule_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_bool_value("validationPassed", self.validation_passed)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def validation_passed(self,) -> Optional[bool]:
        """
        Gets the validationPassed property value. Whether the password passed or failed the validation rule. Read-only. Not nullable.
        Returns: Optional[bool]
        """
        return self._validation_passed
    
    @validation_passed.setter
    def validation_passed(self,value: Optional[bool] = None) -> None:
        """
        Sets the validationPassed property value. Whether the password passed or failed the validation rule. Read-only. Not nullable.
        Args:
            value: Value to set for the validationPassed property.
        """
        self._validation_passed = value
    

