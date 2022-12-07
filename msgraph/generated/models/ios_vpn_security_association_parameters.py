from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

vpn_encryption_algorithm_type = lazy_import('msgraph.generated.models.vpn_encryption_algorithm_type')
vpn_integrity_algorithm_type = lazy_import('msgraph.generated.models.vpn_integrity_algorithm_type')

class IosVpnSecurityAssociationParameters(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosVpnSecurityAssociationParameters and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Lifetime (minutes)
        self._lifetime_in_minutes: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Diffie-Hellman Group
        self._security_diffie_hellman_group: Optional[int] = None
        # Encryption algorithm. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        self._security_encryption_algorithm: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None
        # Integrity algorithm. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
        self._security_integrity_algorithm: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVpnSecurityAssociationParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVpnSecurityAssociationParameters
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosVpnSecurityAssociationParameters()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "lifetime_in_minutes": lambda n : setattr(self, 'lifetime_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "security_diffie_hellman_group": lambda n : setattr(self, 'security_diffie_hellman_group', n.get_int_value()),
            "security_encryption_algorithm": lambda n : setattr(self, 'security_encryption_algorithm', n.get_enum_value(vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType)),
            "security_integrity_algorithm": lambda n : setattr(self, 'security_integrity_algorithm', n.get_enum_value(vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType)),
        }
        return fields
    
    @property
    def lifetime_in_minutes(self,) -> Optional[int]:
        """
        Gets the lifetimeInMinutes property value. Lifetime (minutes)
        Returns: Optional[int]
        """
        return self._lifetime_in_minutes
    
    @lifetime_in_minutes.setter
    def lifetime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the lifetimeInMinutes property value. Lifetime (minutes)
        Args:
            value: Value to set for the lifetimeInMinutes property.
        """
        self._lifetime_in_minutes = value
    
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
    def security_diffie_hellman_group(self,) -> Optional[int]:
        """
        Gets the securityDiffieHellmanGroup property value. Diffie-Hellman Group
        Returns: Optional[int]
        """
        return self._security_diffie_hellman_group
    
    @security_diffie_hellman_group.setter
    def security_diffie_hellman_group(self,value: Optional[int] = None) -> None:
        """
        Sets the securityDiffieHellmanGroup property value. Diffie-Hellman Group
        Args:
            value: Value to set for the securityDiffieHellmanGroup property.
        """
        self._security_diffie_hellman_group = value
    
    @property
    def security_encryption_algorithm(self,) -> Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType]:
        """
        Gets the securityEncryptionAlgorithm property value. Encryption algorithm. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        Returns: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType]
        """
        return self._security_encryption_algorithm
    
    @security_encryption_algorithm.setter
    def security_encryption_algorithm(self,value: Optional[vpn_encryption_algorithm_type.VpnEncryptionAlgorithmType] = None) -> None:
        """
        Sets the securityEncryptionAlgorithm property value. Encryption algorithm. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
        Args:
            value: Value to set for the securityEncryptionAlgorithm property.
        """
        self._security_encryption_algorithm = value
    
    @property
    def security_integrity_algorithm(self,) -> Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType]:
        """
        Gets the securityIntegrityAlgorithm property value. Integrity algorithm. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
        Returns: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType]
        """
        return self._security_integrity_algorithm
    
    @security_integrity_algorithm.setter
    def security_integrity_algorithm(self,value: Optional[vpn_integrity_algorithm_type.VpnIntegrityAlgorithmType] = None) -> None:
        """
        Sets the securityIntegrityAlgorithm property value. Integrity algorithm. Possible values are: sha2_256, sha1_96, sha1_160, sha2_384, sha2_512, md5.
        Args:
            value: Value to set for the securityIntegrityAlgorithm property.
        """
        self._security_integrity_algorithm = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("lifetimeInMinutes", self.lifetime_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("securityDiffieHellmanGroup", self.security_diffie_hellman_group)
        writer.write_enum_value("securityEncryptionAlgorithm", self.security_encryption_algorithm)
        writer.write_enum_value("securityIntegrityAlgorithm", self.security_integrity_algorithm)
        writer.write_additional_data_value(self.additional_data)
    

