from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_resize_validation_code

class CloudPcResizeValidationResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcResizeValidationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cloudPcId property
        self._cloud_pc_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The validationResult property
        self._validation_result: Optional[cloud_pc_resize_validation_code.CloudPcResizeValidationCode] = None
    
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
    def cloud_pc_id(self,) -> Optional[str]:
        """
        Gets the cloudPcId property value. The cloudPcId property
        Returns: Optional[str]
        """
        return self._cloud_pc_id
    
    @cloud_pc_id.setter
    def cloud_pc_id(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcId property value. The cloudPcId property
        Args:
            value: Value to set for the cloud_pc_id property.
        """
        self._cloud_pc_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcResizeValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcResizeValidationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcResizeValidationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_resize_validation_code

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "validationResult": lambda n : setattr(self, 'validation_result', n.get_enum_value(cloud_pc_resize_validation_code.CloudPcResizeValidationCode)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("validationResult", self.validation_result)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def validation_result(self,) -> Optional[cloud_pc_resize_validation_code.CloudPcResizeValidationCode]:
        """
        Gets the validationResult property value. The validationResult property
        Returns: Optional[cloud_pc_resize_validation_code.CloudPcResizeValidationCode]
        """
        return self._validation_result
    
    @validation_result.setter
    def validation_result(self,value: Optional[cloud_pc_resize_validation_code.CloudPcResizeValidationCode] = None) -> None:
        """
        Sets the validationResult property value. The validationResult property
        Args:
            value: Value to set for the validation_result property.
        """
        self._validation_result = value
    

