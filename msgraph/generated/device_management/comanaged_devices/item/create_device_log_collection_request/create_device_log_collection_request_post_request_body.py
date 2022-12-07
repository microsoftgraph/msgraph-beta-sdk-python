from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_log_collection_request = lazy_import('msgraph.generated.models.device_log_collection_request')

class CreateDeviceLogCollectionRequestPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the createDeviceLogCollectionRequest method.
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
        Instantiates a new createDeviceLogCollectionRequestPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The templateType property
        self._template_type: Optional[device_log_collection_request.DeviceLogCollectionRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateDeviceLogCollectionRequestPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreateDeviceLogCollectionRequestPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreateDeviceLogCollectionRequestPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "template_type": lambda n : setattr(self, 'template_type', n.get_object_value(device_log_collection_request.DeviceLogCollectionRequest)),
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
        writer.write_object_value("templateType", self.template_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def template_type(self,) -> Optional[device_log_collection_request.DeviceLogCollectionRequest]:
        """
        Gets the templateType property value. The templateType property
        Returns: Optional[device_log_collection_request.DeviceLogCollectionRequest]
        """
        return self._template_type
    
    @template_type.setter
    def template_type(self,value: Optional[device_log_collection_request.DeviceLogCollectionRequest] = None) -> None:
        """
        Sets the templateType property value. The templateType property
        Args:
            value: Value to set for the templateType property.
        """
        self._template_type = value
    

