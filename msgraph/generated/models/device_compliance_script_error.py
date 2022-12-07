from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

code = lazy_import('msgraph.generated.models.code')
device_compliance_script_rules_validation_error = lazy_import('msgraph.generated.models.device_compliance_script_rules_validation_error')

class DeviceComplianceScriptError(AdditionalDataHolder, Parsable):
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
    
    @property
    def code(self,) -> Optional[code.Code]:
        """
        Gets the code property value. Error code for rule validation.
        Returns: Optional[code.Code]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[code.Code] = None) -> None:
        """
        Sets the code property value. Error code for rule validation.
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceScriptError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Error code for rule validation.
        self._code: Optional[code.Code] = None
        # Error code for rule validation.
        self._device_compliance_script_rules_validation_error: Optional[device_compliance_script_rules_validation_error.DeviceComplianceScriptRulesValidationError] = None
        # Error message.
        self._message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScriptError()
    
    @property
    def device_compliance_script_rules_validation_error(self,) -> Optional[device_compliance_script_rules_validation_error.DeviceComplianceScriptRulesValidationError]:
        """
        Gets the deviceComplianceScriptRulesValidationError property value. Error code for rule validation.
        Returns: Optional[device_compliance_script_rules_validation_error.DeviceComplianceScriptRulesValidationError]
        """
        return self._device_compliance_script_rules_validation_error
    
    @device_compliance_script_rules_validation_error.setter
    def device_compliance_script_rules_validation_error(self,value: Optional[device_compliance_script_rules_validation_error.DeviceComplianceScriptRulesValidationError] = None) -> None:
        """
        Sets the deviceComplianceScriptRulesValidationError property value. Error code for rule validation.
        Args:
            value: Value to set for the deviceComplianceScriptRulesValidationError property.
        """
        self._device_compliance_script_rules_validation_error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(code.Code)),
            "device_compliance_script_rules_validation_error": lambda n : setattr(self, 'device_compliance_script_rules_validation_error', n.get_enum_value(device_compliance_script_rules_validation_error.DeviceComplianceScriptRulesValidationError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. Error message.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. Error message.
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("code", self.code)
        writer.write_enum_value("deviceComplianceScriptRulesValidationError", self.device_compliance_script_rules_validation_error)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

