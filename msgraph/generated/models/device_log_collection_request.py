from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_log_collection_template_type = lazy_import('msgraph.generated.models.device_log_collection_template_type')

class DeviceLogCollectionRequest(AdditionalDataHolder, Parsable):
    """
    Windows Log Collection request entity.
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
        Instantiates a new deviceLogCollectionRequest and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Enum for the template type used for collecting logs
        self._template_type: Optional[device_log_collection_template_type.DeviceLogCollectionTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceLogCollectionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLogCollectionRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceLogCollectionRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "template_type": lambda n : setattr(self, 'template_type', n.get_enum_value(device_log_collection_template_type.DeviceLogCollectionTemplateType)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The unique identifier
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The unique identifier
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("templateType", self.template_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def template_type(self,) -> Optional[device_log_collection_template_type.DeviceLogCollectionTemplateType]:
        """
        Gets the templateType property value. Enum for the template type used for collecting logs
        Returns: Optional[device_log_collection_template_type.DeviceLogCollectionTemplateType]
        """
        return self._template_type
    
    @template_type.setter
    def template_type(self,value: Optional[device_log_collection_template_type.DeviceLogCollectionTemplateType] = None) -> None:
        """
        Sets the templateType property value. Enum for the template type used for collecting logs
        Args:
            value: Value to set for the templateType property.
        """
        self._template_type = value
    

