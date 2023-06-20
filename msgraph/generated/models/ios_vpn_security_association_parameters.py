from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import vpn_encryption_algorithm_type, vpn_integrity_algorithm_type

@dataclass
class IosVpnSecurityAssociationParameters(AdditionalDataHolder, Parsable):
    """
    VPN Security Association Parameters
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Lifetime (minutes)
    lifetime_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Diffie-Hellman Group
    security_diffie_hellman_group: Optional[int] = None
    # Encryption algorithm. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
    security_encryption_algorithm: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None
    # Integrity algorithm. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
    security_integrity_algorithm: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVpnSecurityAssociationParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVpnSecurityAssociationParameters
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosVpnSecurityAssociationParameters()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import vpn_encryption_algorithm_type, vpn_integrity_algorithm_type

        from . import vpn_encryption_algorithm_type, vpn_integrity_algorithm_type

        fields: Dict[str, Callable[[Any], None]] = {
            "lifetimeInMinutes": lambda n : setattr(self, 'lifetime_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "securityDiffieHellmanGroup": lambda n : setattr(self, 'security_diffie_hellman_group', n.get_int_value()),
            "securityEncryptionAlgorithm": lambda n : setattr(self, 'security_encryption_algorithm', n.get_enum_value(vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType)),
            "securityIntegrityAlgorithm": lambda n : setattr(self, 'security_integrity_algorithm', n.get_enum_value(vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType)),
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
        writer.write_int_value("lifetimeInMinutes", self.lifetime_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("securityDiffieHellmanGroup", self.security_diffie_hellman_group)
        writer.write_enum_value("securityEncryptionAlgorithm", self.security_encryption_algorithm)
        writer.write_enum_value("securityIntegrityAlgorithm", self.security_integrity_algorithm)
        writer.write_additional_data_value(self.additional_data)
    

