from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_manager_action_delivery_status import ConfigurationManagerActionDeliveryStatus
    from .device_action_result import DeviceActionResult

from .device_action_result import DeviceActionResult

@dataclass
class ConfigurationManagerActionResult(DeviceActionResult):
    """
    Result of the ConfigurationManager action
    """
    # Delivery state of Configuration Manager device action
    action_delivery_status: Optional[ConfigurationManagerActionDeliveryStatus] = None
    # Error code of Configuration Manager action from client
    error_code: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationManagerActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .configuration_manager_action_delivery_status import ConfigurationManagerActionDeliveryStatus
        from .device_action_result import DeviceActionResult

        from .configuration_manager_action_delivery_status import ConfigurationManagerActionDeliveryStatus
        from .device_action_result import DeviceActionResult

        fields: Dict[str, Callable[[Any], None]] = {
            "actionDeliveryStatus": lambda n : setattr(self, 'action_delivery_status', n.get_enum_value(ConfigurationManagerActionDeliveryStatus)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("actionDeliveryStatus", self.action_delivery_status)
        writer.write_int_value("errorCode", self.error_code)
    

