from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.trust_chain_certificate import TrustChainCertificate

@dataclass
class UploadExternallySignedCertificationAuthorityCertificatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The certificationAuthorityVersion property
    certification_authority_version: Optional[int] = None
    # The signedCertificate property
    signed_certificate: Optional[str] = None
    # The trustChainCertificates property
    trust_chain_certificates: Optional[List[TrustChainCertificate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UploadExternallySignedCertificationAuthorityCertificatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UploadExternallySignedCertificationAuthorityCertificatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UploadExternallySignedCertificationAuthorityCertificatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.trust_chain_certificate import TrustChainCertificate

        from .....models.trust_chain_certificate import TrustChainCertificate

        fields: Dict[str, Callable[[Any], None]] = {
            "certificationAuthorityVersion": lambda n : setattr(self, 'certification_authority_version', n.get_int_value()),
            "signedCertificate": lambda n : setattr(self, 'signed_certificate', n.get_str_value()),
            "trustChainCertificates": lambda n : setattr(self, 'trust_chain_certificates', n.get_collection_of_object_values(TrustChainCertificate)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .....models.trust_chain_certificate import TrustChainCertificate

        writer.write_int_value("certificationAuthorityVersion", self.certification_authority_version)
        writer.write_str_value("signedCertificate", self.signed_certificate)
        writer.write_collection_of_object_values("trustChainCertificates", self.trust_chain_certificates)
        writer.write_additional_data_value(self.additional_data)
    

