from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
    from .on_otp_send_custom_extension import OnOtpSendCustomExtension
    from .on_otp_send_handler import OnOtpSendHandler

from .on_otp_send_handler import OnOtpSendHandler

@dataclass
class OnOtpSendCustomExtensionHandler(OnOtpSendHandler, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onOtpSendCustomExtensionHandler"
    # Configuration regarding properties of the custom extension that are can be overwritten for the onEmailOtpSendListener event listener.
    configuration: Optional[CustomExtensionOverwriteConfiguration] = None
    # The customExtension property
    custom_extension: Optional[OnOtpSendCustomExtension] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnOtpSendCustomExtensionHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnOtpSendCustomExtensionHandler
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnOtpSendCustomExtensionHandler()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_otp_send_handler import OnOtpSendHandler

        from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_otp_send_handler import OnOtpSendHandler

        fields: dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(CustomExtensionOverwriteConfiguration)),
            "customExtension": lambda n : setattr(self, 'custom_extension', n.get_object_value(OnOtpSendCustomExtension)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("customExtension", self.custom_extension)
    

