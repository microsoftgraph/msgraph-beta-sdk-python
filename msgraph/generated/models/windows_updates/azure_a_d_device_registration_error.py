from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

azure_a_d_device_registration_error_reason = lazy_import('msgraph.generated.models.windows_updates.azure_a_d_device_registration_error_reason')
updatable_asset_error = lazy_import('msgraph.generated.models.windows_updates.updatable_asset_error')

class AzureADDeviceRegistrationError(updatable_asset_error.UpdatableAssetError):
    def __init__(self,) -> None:
        """
        Instantiates a new AzureADDeviceRegistrationError and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.azureADDeviceRegistrationError"
        # The reason property
        self._reason: Optional[azure_a_d_device_registration_error_reason.AzureADDeviceRegistrationErrorReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureADDeviceRegistrationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AzureADDeviceRegistrationError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AzureADDeviceRegistrationError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(azure_a_d_device_registration_error_reason.AzureADDeviceRegistrationErrorReason)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reason(self,) -> Optional[azure_a_d_device_registration_error_reason.AzureADDeviceRegistrationErrorReason]:
        """
        Gets the reason property value. The reason property
        Returns: Optional[azure_a_d_device_registration_error_reason.AzureADDeviceRegistrationErrorReason]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[azure_a_d_device_registration_error_reason.AzureADDeviceRegistrationErrorReason] = None) -> None:
        """
        Sets the reason property value. The reason property
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("reason", self.reason)
    

