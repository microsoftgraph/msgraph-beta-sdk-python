from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_authority_as_entity, certificate_based_application_configuration, directory_object

from . import directory_object

@dataclass
class TrustedCertificateAuthorityAsEntityBase(directory_object.DirectoryObject):
    odata_type = "#microsoft.graph.trustedCertificateAuthorityAsEntityBase"
    # The trustedCertificateAuthorities property
    trusted_certificate_authorities: Optional[List[certificate_authority_as_entity.CertificateAuthorityAsEntity]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrustedCertificateAuthorityAsEntityBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TrustedCertificateAuthorityAsEntityBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedApplicationConfiguration".casefold():
            from . import certificate_based_application_configuration

            return certificate_based_application_configuration.CertificateBasedApplicationConfiguration()
        return TrustedCertificateAuthorityAsEntityBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_authority_as_entity, certificate_based_application_configuration, directory_object

        from . import certificate_authority_as_entity, certificate_based_application_configuration, directory_object

        fields: Dict[str, Callable[[Any], None]] = {
            "trustedCertificateAuthorities": lambda n : setattr(self, 'trusted_certificate_authorities', n.get_collection_of_object_values(certificate_authority_as_entity.CertificateAuthorityAsEntity)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("trustedCertificateAuthorities", self.trusted_certificate_authorities)
    

