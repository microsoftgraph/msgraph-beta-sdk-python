from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bit_locker_encryption_method = lazy_import('msgraph.generated.models.bit_locker_encryption_method')
bit_locker_recovery_options = lazy_import('msgraph.generated.models.bit_locker_recovery_options')

class BitLockerFixedDrivePolicy(AdditionalDataHolder, Parsable):
    """
    BitLocker Fixed Drive Policies.
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
        Instantiates a new bitLockerFixedDrivePolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Select the encryption method for fixed drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
        self._encryption_method: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # This policy setting allows you to control how BitLocker-protected fixed data drives are recovered in the absence of the required credentials. This policy setting is applied when you turn on BitLocker.
        self._recovery_options: Optional[bit_locker_recovery_options.BitLockerRecoveryOptions] = None
        # This policy setting determines whether BitLocker protection is required for fixed data drives to be writable on a computer.
        self._require_encryption_for_write_access: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitLockerFixedDrivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerFixedDrivePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitLockerFixedDrivePolicy()
    
    @property
    def encryption_method(self,) -> Optional[bit_locker_encryption_method.BitLockerEncryptionMethod]:
        """
        Gets the encryptionMethod property value. Select the encryption method for fixed drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
        Returns: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod]
        """
        return self._encryption_method
    
    @encryption_method.setter
    def encryption_method(self,value: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod] = None) -> None:
        """
        Sets the encryptionMethod property value. Select the encryption method for fixed drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
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
            "encryption_method": lambda n : setattr(self, 'encryption_method', n.get_enum_value(bit_locker_encryption_method.BitLockerEncryptionMethod)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recovery_options": lambda n : setattr(self, 'recovery_options', n.get_object_value(bit_locker_recovery_options.BitLockerRecoveryOptions)),
            "require_encryption_for_write_access": lambda n : setattr(self, 'require_encryption_for_write_access', n.get_bool_value()),
        }
        return fields
    
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
    def recovery_options(self,) -> Optional[bit_locker_recovery_options.BitLockerRecoveryOptions]:
        """
        Gets the recoveryOptions property value. This policy setting allows you to control how BitLocker-protected fixed data drives are recovered in the absence of the required credentials. This policy setting is applied when you turn on BitLocker.
        Returns: Optional[bit_locker_recovery_options.BitLockerRecoveryOptions]
        """
        return self._recovery_options
    
    @recovery_options.setter
    def recovery_options(self,value: Optional[bit_locker_recovery_options.BitLockerRecoveryOptions] = None) -> None:
        """
        Sets the recoveryOptions property value. This policy setting allows you to control how BitLocker-protected fixed data drives are recovered in the absence of the required credentials. This policy setting is applied when you turn on BitLocker.
        Args:
            value: Value to set for the recoveryOptions property.
        """
        self._recovery_options = value
    
    @property
    def require_encryption_for_write_access(self,) -> Optional[bool]:
        """
        Gets the requireEncryptionForWriteAccess property value. This policy setting determines whether BitLocker protection is required for fixed data drives to be writable on a computer.
        Returns: Optional[bool]
        """
        return self._require_encryption_for_write_access
    
    @require_encryption_for_write_access.setter
    def require_encryption_for_write_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireEncryptionForWriteAccess property value. This policy setting determines whether BitLocker protection is required for fixed data drives to be writable on a computer.
        Args:
            value: Value to set for the requireEncryptionForWriteAccess property.
        """
        self._require_encryption_for_write_access = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recoveryOptions", self.recovery_options)
        writer.write_bool_value("requireEncryptionForWriteAccess", self.require_encryption_for_write_access)
        writer.write_additional_data_value(self.additional_data)
    

