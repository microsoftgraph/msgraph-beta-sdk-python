from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

certificate_destination_store = lazy_import('msgraph.generated.models.certificate_destination_store')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class Windows81TrustedRootCertificate(device_configuration.DeviceConfiguration):
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
            value: Value to set for the certFileName property.
        """
        self._cert_file_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windows81TrustedRootCertificate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows81TrustedRootCertificate"
        # File name to display in UI.
        self._cert_file_name: Optional[str] = None
        # Possible values for the Certificate Destination Store.
        self._destination_store: Optional[certificate_destination_store.CertificateDestinationStore] = None
        # Trusted Root Certificate
        self._trusted_root_certificate: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81TrustedRootCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows81TrustedRootCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows81TrustedRootCertificate()
    
    @property
    def destination_store(self,) -> Optional[certificate_destination_store.CertificateDestinationStore]:
        """
        Gets the destinationStore property value. Possible values for the Certificate Destination Store.
        Returns: Optional[certificate_destination_store.CertificateDestinationStore]
        """
        return self._destination_store
    
    @destination_store.setter
    def destination_store(self,value: Optional[certificate_destination_store.CertificateDestinationStore] = None) -> None:
        """
        Sets the destinationStore property value. Possible values for the Certificate Destination Store.
        Args:
            value: Value to set for the destinationStore property.
        """
        self._destination_store = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cert_file_name": lambda n : setattr(self, 'cert_file_name', n.get_str_value()),
            "destination_store": lambda n : setattr(self, 'destination_store', n.get_enum_value(certificate_destination_store.CertificateDestinationStore)),
            "trusted_root_certificate": lambda n : setattr(self, 'trusted_root_certificate', n.get_bytes_value()),
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
        writer.write_enum_value("destinationStore", self.destination_store)
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
            value: Value to set for the trustedRootCertificate property.
        """
        self._trusted_root_certificate = value
    

