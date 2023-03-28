from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration

from . import device_configuration

class WindowsPhone81TrustedRootCertificate(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new windowsPhone81TrustedRootCertificate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81TrustedRootCertificate"
        # File name to display in UI.
        self._cert_file_name: Optional[str] = None
        # Trusted Root Certificate
        self._trusted_root_certificate: Optional[bytes] = None
    
    @property
    def cert_file_name(self,) -> Optional[str]:
        """
        Gets the certFileName property value. File name to display in UI.
        Returns: Optional[str]
        """
        return self._cert_file_name
    
    @cert_file_name.setter
    def cert_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certFileName property value. File name to display in UI.
        Args:
            value: Value to set for the cert_file_name property.
        """
        self._cert_file_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81TrustedRootCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81TrustedRootCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81TrustedRootCertificate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "certFileName": lambda n : setattr(self, 'cert_file_name', n.get_str_value()),
            "trustedRootCertificate": lambda n : setattr(self, 'trusted_root_certificate', n.get_bytes_value()),
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
        writer.write_str_value("certFileName", self.cert_file_name)
        writer.write_object_value("trustedRootCertificate", self.trusted_root_certificate)
    
    @property
    def trusted_root_certificate(self,) -> Optional[bytes]:
        """
        Gets the trustedRootCertificate property value. Trusted Root Certificate
        Returns: Optional[bytes]
        """
        return self._trusted_root_certificate
    
    @trusted_root_certificate.setter
    def trusted_root_certificate(self,value: Optional[bytes] = None) -> None:
        """
        Sets the trustedRootCertificate property value. Trusted Root Certificate
        Args:
            value: Value to set for the trusted_root_certificate property.
        """
        self._trusted_root_certificate = value
    

