from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_transform_constant = lazy_import('msgraph.generated.models.authentication_transform_constant')
diffie_hellman_group = lazy_import('msgraph.generated.models.diffie_hellman_group')
perfect_forward_secrecy_group = lazy_import('msgraph.generated.models.perfect_forward_secrecy_group')
vpn_encryption_algorithm_type = lazy_import('msgraph.generated.models.vpn_encryption_algorithm_type')
vpn_integrity_algorithm_type = lazy_import('msgraph.generated.models.vpn_integrity_algorithm_type')

class CryptographySuite(AdditionalDataHolder, Parsable):
    """
    VPN Security Association Parameters
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def authentication_transform_constants(self,) -> Optional[authentication_transform_constant.AuthenticationTransformConstant]:
        """
        Gets the authenticationTransformConstants property value. Authentication Transform Constants. Possible values are: md5_96, sha1_96, sha_256_128, aes128Gcm, aes192Gcm, aes256Gcm.
        Returns: Optional[authentication_transform_constant.AuthenticationTransformConstant]
        """
        return self._authentication_transform_constants
    
    @authentication_transform_constants.setter
    def authentication_transform_constants(self,value: Optional[authentication_transform_constant.AuthenticationTransformConstant] = None) -> None:
        """
        Sets the authenticationTransformConstants property value. Authentication Transform Constants. Possible values are: md5_96, sha1_96, sha_256_128, aes128Gcm, aes192Gcm, aes256Gcm.
        Args:
            value: Value to set for the authenticationTransformConstants property.
        """
        self._authentication_transform_constants = value
    
    @property
    def cipher_transform_constants(self,) -> Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType]:
        """
        Gets the cipherTransformConstants property value. Cipher Transform Constants. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        Returns: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType]
        """
        return self._cipher_transform_constants
    
    @cipher_transform_constants.setter
    def cipher_transform_constants(self,value: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None) -> None:
        """
        Sets the cipherTransformConstants property value. Cipher Transform Constants. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        Args:
            value: Value to set for the cipherTransformConstants property.
        """
        self._cipher_transform_constants = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cryptographySuite and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Authentication Transform Constants. Possible values are: md5_96, sha1_96, sha_256_128, aes128Gcm, aes192Gcm, aes256Gcm.
        self._authentication_transform_constants: Optional[authentication_transform_constant.AuthenticationTransformConstant] = None
        # Cipher Transform Constants. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        self._cipher_transform_constants: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None
        # Diffie Hellman Group. Possible values are: group1, group2, group14, ecp256, ecp384, group24.
        self._dh_group: Optional[diffie_hellman_group.DiffieHellmanGroup] = None
        # Encryption Method. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        self._encryption_method: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None
        # Integrity Check Method. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
        self._integrity_check_method: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Perfect Forward Secrecy Group. Possible values are: pfs1, pfs2, pfs2048, ecp256, ecp384, pfsMM, pfs24.
        self._pfs_group: Optional[perfect_forward_secrecy_group.PerfectForwardSecrecyGroup] = None
    
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
    
    @property
    def dh_group(self,) -> Optional[diffie_hellman_group.DiffieHellmanGroup]:
        """
        Gets the dhGroup property value. Diffie Hellman Group. Possible values are: group1, group2, group14, ecp256, ecp384, group24.
        Returns: Optional[diffie_hellman_group.DiffieHellmanGroup]
        """
        return self._dh_group
    
    @dh_group.setter
    def dh_group(self,value: Optional[diffie_hellman_group.DiffieHellmanGroup] = None) -> None:
        """
        Sets the dhGroup property value. Diffie Hellman Group. Possible values are: group1, group2, group14, ecp256, ecp384, group24.
        Args:
            value: Value to set for the dhGroup property.
        """
        self._dh_group = value
    
    @property
    def encryption_method(self,) -> Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType]:
        """
        Gets the encryptionMethod property value. Encryption Method. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        Returns: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType]
        """
        return self._encryption_method
    
    @encryption_method.setter
    def encryption_method(self,value: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None) -> None:
        """
        Sets the encryptionMethod property value. Encryption Method. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        Args:
            value: Value to set for the encryptionMethod property.
        """
        self._encryption_method = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_transform_constants": lambda n : setattr(self, 'authentication_transform_constants', n.get_enum_value(authentication_transform_constant.AuthenticationTransformConstant)),
            "cipher_transform_constants": lambda n : setattr(self, 'cipher_transform_constants', n.get_enum_value(vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType)),
            "dh_group": lambda n : setattr(self, 'dh_group', n.get_enum_value(diffie_hellman_group.DiffieHellmanGroup)),
            "encryption_method": lambda n : setattr(self, 'encryption_method', n.get_enum_value(vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType)),
            "integrity_check_method": lambda n : setattr(self, 'integrity_check_method', n.get_enum_value(vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pfs_group": lambda n : setattr(self, 'pfs_group', n.get_enum_value(perfect_forward_secrecy_group.PerfectForwardSecrecyGroup)),
        }
        return fields
    
    @property
    def integrity_check_method(self,) -> Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType]:
        """
        Gets the integrityCheckMethod property value. Integrity Check Method. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
        Returns: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType]
        """
        return self._integrity_check_method
    
    @integrity_check_method.setter
    def integrity_check_method(self,value: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType] = None) -> None:
        """
        Sets the integrityCheckMethod property value. Integrity Check Method. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
        Args:
            value: Value to set for the integrityCheckMethod property.
        """
        self._integrity_check_method = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def pfs_group(self,) -> Optional[perfect_forward_secrecy_group.PerfectForwardSecrecyGroup]:
        """
        Gets the pfsGroup property value. Perfect Forward Secrecy Group. Possible values are: pfs1, pfs2, pfs2048, ecp256, ecp384, pfsMM, pfs24.
        Returns: Optional[perfect_forward_secrecy_group.PerfectForwardSecrecyGroup]
        """
        return self._pfs_group
    
    @pfs_group.setter
    def pfs_group(self,value: Optional[perfect_forward_secrecy_group.PerfectForwardSecrecyGroup] = None) -> None:
        """
        Sets the pfsGroup property value. Perfect Forward Secrecy Group. Possible values are: pfs1, pfs2, pfs2048, ecp256, ecp384, pfsMM, pfs24.
        Args:
            value: Value to set for the pfsGroup property.
        """
        self._pfs_group = value
    
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
    

