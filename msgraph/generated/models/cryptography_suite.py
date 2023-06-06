from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_transform_constant, diffie_hellman_group, perfect_forward_secrecy_group, vpn_encryption_algorithm_type, vpn_integrity_algorithm_type

@dataclass
class CryptographySuite(AdditionalDataHolder, Parsable):
    """
    VPN Security Association Parameters
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Authentication Transform Constants. Possible values are: md5_96, sha1_96, sha_256_128, aes128Gcm, aes192Gcm, aes256Gcm.
    authentication_transform_constants: Optional[authentication_transform_constant.AuthenticationTransformConstant] = None
    # Cipher Transform Constants. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
    cipher_transform_constants: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None
    # Diffie Hellman Group. Possible values are: group1, group2, group14, ecp256, ecp384, group24.
    dh_group: Optional[diffie_hellman_group.DiffieHellmanGroup] = None
    # Encryption Method. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
    encryption_method: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None
    # Integrity Check Method. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
    integrity_check_method: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Perfect Forward Secrecy Group. Possible values are: pfs1, pfs2, pfs2048, ecp256, ecp384, pfsMM, pfs24.
    pfs_group: Optional[perfect_forward_secrecy_group.PerfectForwardSecrecyGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CryptographySuite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CryptographySuite
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CryptographySuite()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_transform_constant, diffie_hellman_group, perfect_forward_secrecy_group, vpn_encryption_algorithm_type, vpn_integrity_algorithm_type

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationTransformConstants": lambda n : setattr(self, 'authentication_transform_constants', n.get_enum_value(authentication_transform_constant.AuthenticationTransformConstant)),
            "cipherTransformConstants": lambda n : setattr(self, 'cipher_transform_constants', n.get_enum_value(vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType)),
            "dhGroup": lambda n : setattr(self, 'dh_group', n.get_enum_value(diffie_hellman_group.DiffieHellmanGroup)),
            "encryptionMethod": lambda n : setattr(self, 'encryption_method', n.get_enum_value(vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType)),
            "integrityCheckMethod": lambda n : setattr(self, 'integrity_check_method', n.get_enum_value(vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pfsGroup": lambda n : setattr(self, 'pfs_group', n.get_enum_value(perfect_forward_secrecy_group.PerfectForwardSecrecyGroup)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("authenticationTransformConstants", self.authentication_transform_constants)
        writer.write_enum_value("cipherTransformConstants", self.cipher_transform_constants)
        writer.write_enum_value("dhGroup", self.dh_group)
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_enum_value("integrityCheckMethod", self.integrity_check_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("pfsGroup", self.pfs_group)
        writer.write_additional_data_value(self.additional_data)
    

