from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import device_compliance_policy_script

class ValidateComplianceScriptPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new validateComplianceScriptPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceCompliancePolicyScript property
        self._device_compliance_policy_script: Optional[device_compliance_policy_script.DeviceCompliancePolicyScript] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateComplianceScriptPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateComplianceScriptPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidateComplianceScriptPostRequestBody()
    
    @property
    def device_compliance_policy_script(self,) -> Optional[device_compliance_policy_script.DeviceCompliancePolicyScript]:
        """
        Gets the deviceCompliancePolicyScript property value. The deviceCompliancePolicyScript property
        Returns: Optional[device_compliance_policy_script.DeviceCompliancePolicyScript]
        """
        return self._device_compliance_policy_script
    
    @device_compliance_policy_script.setter
    def device_compliance_policy_script(self,value: Optional[device_compliance_policy_script.DeviceCompliancePolicyScript] = None) -> None:
        """
        Sets the deviceCompliancePolicyScript property value. The deviceCompliancePolicyScript property
        Args:
            value: Value to set for the device_compliance_policy_script property.
        """
        self._device_compliance_policy_script = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import device_compliance_policy_script

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCompliancePolicyScript": lambda n : setattr(self, 'device_compliance_policy_script', n.get_object_value(device_compliance_policy_script.DeviceCompliancePolicyScript)),
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
        writer.write_object_value("deviceCompliancePolicyScript", self.device_compliance_policy_script)
        writer.write_additional_data_value(self.additional_data)
    

