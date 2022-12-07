from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bit_locker_recovery_information_type = lazy_import('msgraph.generated.models.bit_locker_recovery_information_type')
configuration_usage = lazy_import('msgraph.generated.models.configuration_usage')

class BitLockerRecoveryOptions(AdditionalDataHolder, Parsable):
    """
    BitLocker Recovery Options.
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
    def block_data_recovery_agent(self,) -> Optional[bool]:
        """
        Gets the blockDataRecoveryAgent property value. Indicates whether to block certificate-based data recovery agent.
        Returns: Optional[bool]
        """
        return self._block_data_recovery_agent
    
    @block_data_recovery_agent.setter
    def block_data_recovery_agent(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockDataRecoveryAgent property value. Indicates whether to block certificate-based data recovery agent.
        Args:
            value: Value to set for the blockDataRecoveryAgent property.
        """
        self._block_data_recovery_agent = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bitLockerRecoveryOptions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether to block certificate-based data recovery agent.
        self._block_data_recovery_agent: Optional[bool] = None
        # Indicates whether or not to enable BitLocker until recovery information is stored in AD DS.
        self._enable_bit_locker_after_recovery_information_to_store: Optional[bool] = None
        # Indicates whether or not to allow BitLocker recovery information to store in AD DS.
        self._enable_recovery_information_save_to_store: Optional[bool] = None
        # Indicates whether or not to allow showing recovery options in BitLocker Setup Wizard for fixed or system disk.
        self._hide_recovery_options: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # BitLockerRecoveryInformationType types
        self._recovery_information_to_store: Optional[bit_locker_recovery_information_type.BitLockerRecoveryInformationType] = None
        # Possible values of the ConfigurationUsage list.
        self._recovery_key_usage: Optional[configuration_usage.ConfigurationUsage] = None
        # Possible values of the ConfigurationUsage list.
        self._recovery_password_usage: Optional[configuration_usage.ConfigurationUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitLockerRecoveryOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerRecoveryOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitLockerRecoveryOptions()
    
    @property
    def enable_bit_locker_after_recovery_information_to_store(self,) -> Optional[bool]:
        """
        Gets the enableBitLockerAfterRecoveryInformationToStore property value. Indicates whether or not to enable BitLocker until recovery information is stored in AD DS.
        Returns: Optional[bool]
        """
        return self._enable_bit_locker_after_recovery_information_to_store
    
    @enable_bit_locker_after_recovery_information_to_store.setter
    def enable_bit_locker_after_recovery_information_to_store(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableBitLockerAfterRecoveryInformationToStore property value. Indicates whether or not to enable BitLocker until recovery information is stored in AD DS.
        Args:
            value: Value to set for the enableBitLockerAfterRecoveryInformationToStore property.
        """
        self._enable_bit_locker_after_recovery_information_to_store = value
    
    @property
    def enable_recovery_information_save_to_store(self,) -> Optional[bool]:
        """
        Gets the enableRecoveryInformationSaveToStore property value. Indicates whether or not to allow BitLocker recovery information to store in AD DS.
        Returns: Optional[bool]
        """
        return self._enable_recovery_information_save_to_store
    
    @enable_recovery_information_save_to_store.setter
    def enable_recovery_information_save_to_store(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableRecoveryInformationSaveToStore property value. Indicates whether or not to allow BitLocker recovery information to store in AD DS.
        Args:
            value: Value to set for the enableRecoveryInformationSaveToStore property.
        """
        self._enable_recovery_information_save_to_store = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "block_data_recovery_agent": lambda n : setattr(self, 'block_data_recovery_agent', n.get_bool_value()),
            "enable_bit_locker_after_recovery_information_to_store": lambda n : setattr(self, 'enable_bit_locker_after_recovery_information_to_store', n.get_bool_value()),
            "enable_recovery_information_save_to_store": lambda n : setattr(self, 'enable_recovery_information_save_to_store', n.get_bool_value()),
            "hide_recovery_options": lambda n : setattr(self, 'hide_recovery_options', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recovery_information_to_store": lambda n : setattr(self, 'recovery_information_to_store', n.get_enum_value(bit_locker_recovery_information_type.BitLockerRecoveryInformationType)),
            "recovery_key_usage": lambda n : setattr(self, 'recovery_key_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
            "recovery_password_usage": lambda n : setattr(self, 'recovery_password_usage', n.get_enum_value(configuration_usage.ConfigurationUsage)),
        }
        return fields
    
    @property
    def hide_recovery_options(self,) -> Optional[bool]:
        """
        Gets the hideRecoveryOptions property value. Indicates whether or not to allow showing recovery options in BitLocker Setup Wizard for fixed or system disk.
        Returns: Optional[bool]
        """
        return self._hide_recovery_options
    
    @hide_recovery_options.setter
    def hide_recovery_options(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideRecoveryOptions property value. Indicates whether or not to allow showing recovery options in BitLocker Setup Wizard for fixed or system disk.
        Args:
            value: Value to set for the hideRecoveryOptions property.
        """
        self._hide_recovery_options = value
    
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
    def recovery_information_to_store(self,) -> Optional[bit_locker_recovery_information_type.BitLockerRecoveryInformationType]:
        """
        Gets the recoveryInformationToStore property value. BitLockerRecoveryInformationType types
        Returns: Optional[bit_locker_recovery_information_type.BitLockerRecoveryInformationType]
        """
        return self._recovery_information_to_store
    
    @recovery_information_to_store.setter
    def recovery_information_to_store(self,value: Optional[bit_locker_recovery_information_type.BitLockerRecoveryInformationType] = None) -> None:
        """
        Sets the recoveryInformationToStore property value. BitLockerRecoveryInformationType types
        Args:
            value: Value to set for the recoveryInformationToStore property.
        """
        self._recovery_information_to_store = value
    
    @property
    def recovery_key_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the recoveryKeyUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._recovery_key_usage
    
    @recovery_key_usage.setter
    def recovery_key_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the recoveryKeyUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the recoveryKeyUsage property.
        """
        self._recovery_key_usage = value
    
    @property
    def recovery_password_usage(self,) -> Optional[configuration_usage.ConfigurationUsage]:
        """
        Gets the recoveryPasswordUsage property value. Possible values of the ConfigurationUsage list.
        Returns: Optional[configuration_usage.ConfigurationUsage]
        """
        return self._recovery_password_usage
    
    @recovery_password_usage.setter
    def recovery_password_usage(self,value: Optional[configuration_usage.ConfigurationUsage] = None) -> None:
        """
        Sets the recoveryPasswordUsage property value. Possible values of the ConfigurationUsage list.
        Args:
            value: Value to set for the recoveryPasswordUsage property.
        """
        self._recovery_password_usage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("blockDataRecoveryAgent", self.block_data_recovery_agent)
        writer.write_bool_value("enableBitLockerAfterRecoveryInformationToStore", self.enable_bit_locker_after_recovery_information_to_store)
        writer.write_bool_value("enableRecoveryInformationSaveToStore", self.enable_recovery_information_save_to_store)
        writer.write_bool_value("hideRecoveryOptions", self.hide_recovery_options)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recoveryInformationToStore", self.recovery_information_to_store)
        writer.write_enum_value("recoveryKeyUsage", self.recovery_key_usage)
        writer.write_enum_value("recoveryPasswordUsage", self.recovery_password_usage)
        writer.write_additional_data_value(self.additional_data)
    

