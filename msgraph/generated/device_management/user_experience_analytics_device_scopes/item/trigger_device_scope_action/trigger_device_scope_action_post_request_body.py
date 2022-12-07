from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TriggerDeviceScopeActionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the triggerDeviceScopeAction method.
    """
    @property
    def action_name(self,) -> Optional[str]:
        """
        Gets the actionName property value. Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        Returns: Optional[str]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[str] = None) -> None:
        """
        Sets the actionName property value. Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
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
        Instantiates a new triggerDeviceScopeActionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        self._action_name: Optional[str] = None
        # The deviceScopeId property
        self._device_scope_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TriggerDeviceScopeActionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TriggerDeviceScopeActionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TriggerDeviceScopeActionPostRequestBody()
    
    @property
    def device_scope_id(self,) -> Optional[str]:
        """
        Gets the deviceScopeId property value. The deviceScopeId property
        Returns: Optional[str]
        """
        return self._device_scope_id
    
    @device_scope_id.setter
    def device_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceScopeId property value. The deviceScopeId property
        Args:
            value: Value to set for the deviceScopeId property.
        """
        self._device_scope_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_name": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "device_scope_id": lambda n : setattr(self, 'device_scope_id', n.get_str_value()),
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_str_value("deviceScopeId", self.device_scope_id)
        writer.write_additional_data_value(self.additional_data)
    

