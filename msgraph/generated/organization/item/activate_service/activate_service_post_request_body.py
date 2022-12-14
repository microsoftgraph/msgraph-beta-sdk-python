from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ActivateServicePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the activateService method.
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
        Instantiates a new activateServicePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The service property
        self._service: Optional[str] = None
        # The servicePlanId property
        self._service_plan_id: Optional[Guid] = None
        # The skuId property
        self._sku_id: Optional[Guid] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivateServicePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivateServicePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivateServicePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "service_plan_id": lambda n : setattr(self, 'service_plan_id', n.get_object_value(Guid)),
            "sku_id": lambda n : setattr(self, 'sku_id', n.get_object_value(Guid)),
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
        writer.write_str_value("service", self.service)
        writer.write_object_value("servicePlanId", self.service_plan_id)
        writer.write_object_value("skuId", self.sku_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. The service property
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. The service property
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def service_plan_id(self,) -> Optional[Guid]:
        """
        Gets the servicePlanId property value. The servicePlanId property
        Returns: Optional[Guid]
        """
        return self._service_plan_id
    
    @service_plan_id.setter
    def service_plan_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the servicePlanId property value. The servicePlanId property
        Args:
            value: Value to set for the servicePlanId property.
        """
        self._service_plan_id = value
    
    @property
    def sku_id(self,) -> Optional[Guid]:
        """
        Gets the skuId property value. The skuId property
        Returns: Optional[Guid]
        """
        return self._sku_id
    
    @sku_id.setter
    def sku_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the skuId property value. The skuId property
        Args:
            value: Value to set for the skuId property.
        """
        self._sku_id = value
    

