from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import configuration_manager_action_delivery_status, device_action_result

from . import device_action_result

class ConfigurationManagerActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new ConfigurationManagerActionResult and sets the default values.
        """
        super().__init__()
        # Delivery state of Configuration Manager device action
        self._action_delivery_status: Optional[configuration_manager_action_delivery_status.ConfigurationManagerActionDeliveryStatus] = None
        # Error code of Configuration Manager action from client
        self._error_code: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def action_delivery_status(self,) -> Optional[configuration_manager_action_delivery_status.ConfigurationManagerActionDeliveryStatus]:
        """
        Gets the actionDeliveryStatus property value. Delivery state of Configuration Manager device action
        Returns: Optional[configuration_manager_action_delivery_status.ConfigurationManagerActionDeliveryStatus]
        """
        return self._action_delivery_status
    
    @action_delivery_status.setter
    def action_delivery_status(self,value: Optional[configuration_manager_action_delivery_status.ConfigurationManagerActionDeliveryStatus] = None) -> None:
        """
        Sets the actionDeliveryStatus property value. Delivery state of Configuration Manager device action
        Args:
            value: Value to set for the action_delivery_status property.
        """
        self._action_delivery_status = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigurationManagerActionResult()
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. Error code of Configuration Manager action from client
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. Error code of Configuration Manager action from client
        Args:
            value: Value to set for the error_code property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import configuration_manager_action_delivery_status, device_action_result

        fields: Dict[str, Callable[[Any], None]] = {
            "actionDeliveryStatus": lambda n : setattr(self, 'action_delivery_status', n.get_enum_value(configuration_manager_action_delivery_status.ConfigurationManagerActionDeliveryStatus)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("actionDeliveryStatus", self.action_delivery_status)
        writer.write_int_value("errorCode", self.error_code)
    

