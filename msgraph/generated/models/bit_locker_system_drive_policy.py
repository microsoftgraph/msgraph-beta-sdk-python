from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bit_locker_encryption_method = lazy_import('msgraph.generated.models.bit_locker_encryption_method')
bit_locker_recovery_options = lazy_import('msgraph.generated.models.bit_locker_recovery_options')
configuration_usage = lazy_import('msgraph.generated.models.configuration_usage')

class BitLockerSystemDrivePolicy(AdditionalDataHolder, Parsable):
    """
    BitLocker Encryption Base Policies.
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
        Instantiates a new bitLockerSystemDrivePolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Select the encryption method for operating system drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
        self._encryption_method: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod] = None
        # Indicates the minimum length of startup pin. Valid values 4 to 20
        self._minimum_pin_length: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Enable pre-boot recovery message and Url. If requireStartupAuthentication is false, this value does not affect.
        self._preboot_recovery_enable_message_and_url: Optional[bool] = None
        # Defines a custom recovery message.
        self._preboot_recovery_message: Optional[str] = None
        # Defines a custom recovery URL.
        self._preboot_recovery_url: Optional[str] = None
        # Allows to recover BitLocker encrypted operating system drives in the absence of the required startup key information. This policy setting is applied when you turn on BitLocker.
        self._recovery_options: Optional[bit_locker_recovery_options.BitLockerRecoveryOptions] = None
        # Indicates whether to allow BitLocker without a compatible TPM (requires a password or a startup key on a USB flash drive).
        self._startup_authentication_block_without_tpm_chip: Optional[bool] = None
        # Require additional authentication at startup.
        self._startup_authentication_required: Optional[bool] = None
        # Possible values of the ConfigurationUsage list.
        self._startup_authentication_tpm_key_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Possible values of the ConfigurationUsage list.
        self._startup_authentication_tpm_pin_and_key_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Possible values of the ConfigurationUsage list.
        self._startup_authentication_tpm_pin_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Possible values of the ConfigurationUsage list.
        self._startup_authentication_tpm_usage: Optional[configuration_usage.ConfigurationUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitLockerSystemDrivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerSystemDrivePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitLockerSystemDrivePolicy()
    
    @property
    def encryption_method(self,) -> Optional[bit_locker_encryption_method.BitLockerEncryptionMethod]:
        """
        Gets the encryptionMethod property value. Select the encryption method for operating system drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
        Returns: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod]
        """
        return self._encryption_method
    
    @encryption_method.setter
    def encryption_method(self,value: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod] = None) -> None:
        """
        Sets the encryptionMethod property value. Select the encryption method for operating system drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
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
            "minimum_pin_length": lambda n : setattr(self, 'minimum_pin_length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preboot_recovery_enable_message_and_url": lambda n : setattr(self, 'preboot_recovery_enable_message_and_url', n.get_bool_value()),
            "preboot_recovery_message": lambda n : setattr(self, 'preboot_recovery_message', n.get_str_value()),
            "preboot_recovery_url": lambda n : setattr(self, 'preboot_recovery_url', n.get_str_value()),
            "recovery_options": lambda n : setattr(self, 'recovery_options', n.get_object_value(bit_locker_recovery_options.BitLockerRecoveryOptions)),
            "startup_authentication_block_without_tpm_chip": lambda n : setattr(self, 'startup_authentication_block_without_tpm_chip', n.get_bool_value()),
            "startup_authentication_required": lambda n : setattr(self, 'startup_authentication_required', n.get_bool_value()),
            "startup_authentication_tpm_key_usage": lambda n : setattr(self, 'startup_authentication_tpm_key_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "startup_authentication_tpm_pin_and_key_usage": lambda n : setattr(self, 'startup_authentication_tpm_pin_and_key_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "startup_authentication_tpm_pin_usage": lambda n : setattr(self, 'startup_authentication_tpm_pin_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "startup_authentication_tpm_usage": lambda n : setattr(self, 'startup_authentication_tpm_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
        }
        return fields
    
    @property
    def minimum_pin_length(self,) -> Optional[int]:
        """
        Gets the minimumPinLength property value. Indicates the minimum length of startup pin. Valid values 4 to 20
        Returns: Optional[int]
        """
        return self._minimum_pin_length
    
    @minimum_pin_length.setter
    def minimum_pin_length(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumPinLength property value. Indicates the minimum length of startup pin. Valid values 4 to 20
        Args:
            value: Value to set for the minimumPinLength property.
        """
        self._minimum_pin_length = value
    
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
    def preboot_recovery_enable_message_and_url(self,) -> Optional[bool]:
        """
        Gets the prebootRecoveryEnableMessageAndUrl property value. Enable pre-boot recovery message and Url. If requireStartupAuthentication is false, this value does not affect.
        Returns: Optional[bool]
        """
        return self._preboot_recovery_enable_message_and_url
    
    @preboot_recovery_enable_message_and_url.setter
    def preboot_recovery_enable_message_and_url(self,value: Optional[bool] = None) -> None:
        """
        Sets the prebootRecoveryEnableMessageAndUrl property value. Enable pre-boot recovery message and Url. If requireStartupAuthentication is false, this value does not affect.
        Args:
            value: Value to set for the prebootRecoveryEnableMessageAndUrl property.
        """
        self._preboot_recovery_enable_message_and_url = value
    
    @property
    def preboot_recovery_message(self,) -> Optional[str]:
        """
        Gets the prebootRecoveryMessage property value. Defines a custom recovery message.
        Returns: Optional[str]
        """
        return self._preboot_recovery_message
    
    @preboot_recovery_message.setter
    def preboot_recovery_message(self,value: Optional[str] = None) -> None:
        """
        Sets the prebootRecoveryMessage property value. Defines a custom recovery message.
        Args:
            value: Value to set for the prebootRecoveryMessage property.
        """
        self._preboot_recovery_message = value
    
    @property
    def preboot_recovery_url(self,) -> Optional[str]:
        """
        Gets the prebootRecoveryUrl property value. Defines a custom recovery URL.
        Returns: Optional[str]
        """
        return self._preboot_recovery_url
    
    @preboot_recovery_url.setter
    def preboot_recovery_url(self,value: Optional[str] = None) -> None:
        """
        Sets the prebootRecoveryUrl property value. Defines a custom recovery URL.
        Args:
            value: Value to set for the prebootRecoveryUrl property.
        """
        self._preboot_recovery_url = value
    
    @property
    def recovery_options(self,) -> Optional[bit_locker_recovery_options.BitLockerRecoveryOptions]:
        """
        Gets the recoveryOptions property value. Allows to recover BitLocker encrypted operating system drives in the absence of the required startup key information. This policy setting is applied when you turn on BitLocker.
        Returns: Optional[bit_locker_recovery_options.BitLockerRecoveryOptions]
        """
        return self._recovery_options
    
    @recovery_options.setter
    def recovery_options(self,value: Optional[bit_locker_recovery_options.BitLockerRecoveryOptions] = None) -> None:
        """
        Sets the recoveryOptions property value. Allows to recover BitLocker encrypted operating system drives in the absence of the required startup key information. This policy setting is applied when you turn on BitLocker.
        Args:
            value: Value to set for the recoveryOptions property.
        """
        self._recovery_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_int_value("minimumPinLength", self.minimum_pin_length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("prebootRecoveryEnableMessageAndUrl", self.preboot_recovery_enable_message_and_url)
        writer.write_str_value("prebootRecoveryMessage", self.preboot_recovery_message)
        writer.write_str_value("prebootRecoveryUrl", self.preboot_recovery_url)
        writer.write_object_value("recoveryOptions", self.recovery_options)
        writer.write_bool_value("startupAuthenticationBlockWithoutTpmChip", self.startup_authentication_block_without_tpm_chip)
        writer.write_bool_value("startupAuthenticationRequired", self.startup_authentication_required)
        writer.write_enum_value("startupAuthenticationTpmKeyUsage", self.startup_authentication_tpm_key_usage)
        writer.write_enum_value("startupAuthenticationTpmPinAndKeyUsage", self.startup_authentication_tpm_pin_and_key_usage)
        writer.write_enum_value("startupAuthenticationTpmPinUsage", self.startup_authentication_tpm_pin_usage)
        writer.write_enum_value("startupAuthenticationTpmUsage", self.startup_authentication_tpm_usage)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def startup_authentication_block_without_tpm_chip(self,) -> Optional[bool]:
        """
        Gets the startupAuthenticationBlockWithoutTpmChip property value. Indicates whether to allow BitLocker without a compatible TPM (requires a password or a startup key on a USB flash drive).
        Returns: Optional[bool]
        """
        return self._startup_authentication_block_without_tpm_chip
    
    @startup_authentication_block_without_tpm_chip.setter
    def startup_authentication_block_without_tpm_chip(self,value: Optional[bool] = None) -> None:
        """
        Sets the startupAuthenticationBlockWithoutTpmChip property value. Indicates whether to allow BitLocker without a compatible TPM (requires a password or a startup key on a USB flash drive).
        Args:
            value: Value to set for the startupAuthenticationBlockWithoutTpmChip property.
        """
        self._startup_authentication_block_without_tpm_chip = value
    
    @property
    def startup_authentication_required(self,) -> Optional[bool]:
        """
        Gets the startupAuthenticationRequired property value. Require additional authentication at startup.
        Returns: Optional[bool]
        """
        return self._startup_authentication_required
    
    @startup_authentication_required.setter
    def startup_authentication_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the startupAuthenticationRequired property value. Require additional authentication at startup.
        Args:
            value: Value to set for the startupAuthenticationRequired property.
        """
        self._startup_authentication_required = value
    
    @property
    def startup_authentication_tpm_key_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the startupAuthenticationTpmKeyUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._startup_authentication_tpm_key_usage
    
    @startup_authentication_tpm_key_usage.setter
    def startup_authentication_tpm_key_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the startupAuthenticationTpmKeyUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the startupAuthenticationTpmKeyUsage property.
        """
        self._startup_authentication_tpm_key_usage = value
    
    @property
    def startup_authentication_tpm_pin_and_key_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the startupAuthenticationTpmPinAndKeyUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._startup_authentication_tpm_pin_and_key_usage
    
    @startup_authentication_tpm_pin_and_key_usage.setter
    def startup_authentication_tpm_pin_and_key_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the startupAuthenticationTpmPinAndKeyUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the startupAuthenticationTpmPinAndKeyUsage property.
        """
        self._startup_authentication_tpm_pin_and_key_usage = value
    
    @property
    def startup_authentication_tpm_pin_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the startupAuthenticationTpmPinUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._startup_authentication_tpm_pin_usage
    
    @startup_authentication_tpm_pin_usage.setter
    def startup_authentication_tpm_pin_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the startupAuthenticationTpmPinUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the startupAuthenticationTpmPinUsage property.
        """
        self._startup_authentication_tpm_pin_usage = value
    
    @property
    def startup_authentication_tpm_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the startupAuthenticationTpmUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._startup_authentication_tpm_usage
    
    @startup_authentication_tpm_usage.setter
    def startup_authentication_tpm_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the startupAuthenticationTpmUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the startupAuthenticationTpmUsage property.
        """
        self._startup_authentication_tpm_usage = value
    

