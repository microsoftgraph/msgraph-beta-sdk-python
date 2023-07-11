from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.update_windows_device_account_action_parameter import UpdateWindowsDeviceAccountActionParameter

@dataclass
class UpdateWindowsDeviceAccountPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The updateWindowsDeviceAccountActionParameter property
    update_windows_device_account_action_parameter: Optional[UpdateWindowsDeviceAccountActionParameter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateWindowsDeviceAccountPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateWindowsDeviceAccountPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateWindowsDeviceAccountPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.update_windows_device_account_action_parameter import UpdateWindowsDeviceAccountActionParameter

        from ......models.update_windows_device_account_action_parameter import UpdateWindowsDeviceAccountActionParameter

        fields: Dict[str, Callable[[Any], None]] = {
            "updateWindowsDeviceAccountActionParameter": lambda n : setattr(self, 'update_windows_device_account_action_parameter', n.get_object_value(UpdateWindowsDeviceAccountActionParameter)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("updateWindowsDeviceAccountActionParameter", self.update_windows_device_account_action_parameter)
        writer.write_additional_data_value(self.additional_data)
    

