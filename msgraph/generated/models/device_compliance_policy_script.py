from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceCompliancePolicyScript(AdditionalDataHolder, Parsable):
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
        Instantiates a new deviceCompliancePolicyScript and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Device compliance script Id.
        self._device_compliance_script_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Json of the rules.
        self._rules_content: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyScript
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyScript()
    
    @property
    def device_compliance_script_id(self,) -> Optional[str]:
        """
        Gets the deviceComplianceScriptId property value. Device compliance script Id.
        Returns: Optional[str]
        """
        return self._device_compliance_script_id
    
    @device_compliance_script_id.setter
    def device_compliance_script_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceComplianceScriptId property value. Device compliance script Id.
        Args:
            value: Value to set for the deviceComplianceScriptId property.
        """
        self._device_compliance_script_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_compliance_script_id": lambda n : setattr(self, 'device_compliance_script_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rules_content": lambda n : setattr(self, 'rules_content', n.get_bytes_value()),
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
    def rules_content(self,) -> Optional[bytes]:
        """
        Gets the rulesContent property value. Json of the rules.
        Returns: Optional[bytes]
        """
        return self._rules_content
    
    @rules_content.setter
    def rules_content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the rulesContent property value. Json of the rules.
        Args:
            value: Value to set for the rulesContent property.
        """
        self._rules_content = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("deviceComplianceScriptId", self.device_compliance_script_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("rulesContent", self.rules_content)
        writer.write_additional_data_value(self.additional_data)
    

