from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
    from .entity import Entity
    from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration

from .entity import Entity

@dataclass
class CertificateAuthorityPath(Entity, Parsable):
    # Defines the trusted certificate authorities for certificates that can be added to apps and service principals in the tenant.
    certificate_based_application_configurations: Optional[List[CertificateBasedApplicationConfiguration]] = None
    # Defines the trusted certificate authorities for certificates that can be added to Internet of Things (IoT) devices.
    mutual_tls_oauth_configurations: Optional[List[MutualTlsOauthConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateAuthorityPath:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthorityPath
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateAuthorityPath()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .entity import Entity
        from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration

        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .entity import Entity
        from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateBasedApplicationConfigurations": lambda n : setattr(self, 'certificate_based_application_configurations', n.get_collection_of_object_values(CertificateBasedApplicationConfiguration)),
            "mutualTlsOauthConfigurations": lambda n : setattr(self, 'mutual_tls_oauth_configurations', n.get_collection_of_object_values(MutualTlsOauthConfiguration)),
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
        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .entity import Entity
        from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration

        writer.write_collection_of_object_values("certificateBasedApplicationConfigurations", self.certificate_based_application_configurations)
        writer.write_collection_of_object_values("mutualTlsOauthConfigurations", self.mutual_tls_oauth_configurations)
    

