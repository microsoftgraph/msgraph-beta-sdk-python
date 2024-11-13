from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_deployment_channel import AppleDeploymentChannel
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSTrustedRootCertificate(DeviceConfiguration, Parsable):
    """
    OS X Trusted Root Certificate configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSTrustedRootCertificate"
    # File name to display in UI.
    cert_file_name: Optional[str] = None
    # Indicates the deployment channel type used to deploy the configuration profile. Possible values are deviceChannel, userChannel. Possible values are: deviceChannel, userChannel, unknownFutureValue.
    deployment_channel: Optional[AppleDeploymentChannel] = None
    # Trusted Root Certificate.
    trusted_root_certificate: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSTrustedRootCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSTrustedRootCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSTrustedRootCertificate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration

        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "certFileName": lambda n : setattr(self, 'cert_file_name', n.get_str_value()),
            "deploymentChannel": lambda n : setattr(self, 'deployment_channel', n.get_enum_value(AppleDeploymentChannel)),
            "trustedRootCertificate": lambda n : setattr(self, 'trusted_root_certificate', n.get_bytes_value()),
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
        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration

        writer.write_str_value("certFileName", self.cert_file_name)
        writer.write_enum_value("deploymentChannel", self.deployment_channel)
        writer.write_bytes_value("trustedRootCertificate", self.trusted_root_certificate)
    

