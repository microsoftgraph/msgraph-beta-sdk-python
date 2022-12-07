from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceHealthScriptRemediationSummary(AdditionalDataHolder, Parsable):
    """
    The number of device health scripts deployed and the number of devices the scripts remediated.
    """
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
        Instantiates a new deviceHealthScriptRemediationSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of devices remediated by device health scripts.
        self._remediated_device_count: Optional[int] = None
        # The number of device health scripts deployed.
        self._script_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptRemediationSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRemediationSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptRemediationSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediated_device_count": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "script_count": lambda n : setattr(self, 'script_count', n.get_int_value()),
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
    def remediated_device_count(self,) -> Optional[int]:
        """
        Gets the remediatedDeviceCount property value. The number of devices remediated by device health scripts.
        Returns: Optional[int]
        """
        return self._remediated_device_count
    
    @remediated_device_count.setter
    def remediated_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedDeviceCount property value. The number of devices remediated by device health scripts.
        Args:
            value: Value to set for the remediatedDeviceCount property.
        """
        self._remediated_device_count = value
    
    @property
    def script_count(self,) -> Optional[int]:
        """
        Gets the scriptCount property value. The number of device health scripts deployed.
        Returns: Optional[int]
        """
        return self._script_count
    
    @script_count.setter
    def script_count(self,value: Optional[int] = None) -> None:
        """
        Sets the scriptCount property value. The number of device health scripts deployed.
        Args:
            value: Value to set for the scriptCount property.
        """
        self._script_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_int_value("scriptCount", self.script_count)
        writer.write_additional_data_value(self.additional_data)
    

