from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import advanced_bit_locker_state, compliance_status, device_types, encryption_readiness_state, encryption_report_policy_details, encryption_state, entity, file_vault_state

from . import entity

class ManagedDeviceEncryptionState(entity.Entity):
    """
    Encryption report per device
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceEncryptionState and sets the default values.
        """
        super().__init__()
        # Advanced BitLocker State. Possible values are: success, noUserConsent, osVolumeUnprotected, osVolumeTpmRequired, osVolumeTpmOnlyRequired, osVolumeTpmPinRequired, osVolumeTpmStartupKeyRequired, osVolumeTpmPinStartupKeyRequired, osVolumeEncryptionMethodMismatch, recoveryKeyBackupFailed, fixedDriveNotEncrypted, fixedDriveEncryptionMethodMismatch, loggedOnUserNonAdmin, windowsRecoveryEnvironmentNotConfigured, tpmNotAvailable, tpmNotReady, networkError.
        self._advanced_bit_locker_states: Optional[advanced_bit_locker_state.AdvancedBitLockerState] = None
        # Device name
        self._device_name: Optional[str] = None
        # Device type.
        self._device_type: Optional[device_types.DeviceTypes] = None
        # The encryptionPolicySettingState property
        self._encryption_policy_setting_state: Optional[compliance_status.ComplianceStatus] = None
        # Encryption readiness state
        self._encryption_readiness_state: Optional[encryption_readiness_state.EncryptionReadinessState] = None
        # Encryption state
        self._encryption_state: Optional[encryption_state.EncryptionState] = None
        # FileVault State. Possible values are: success, driveEncryptedByUser, userDeferredEncryption, escrowNotEnabled.
        self._file_vault_states: Optional[file_vault_state.FileVaultState] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Operating system version of the device
        self._os_version: Optional[str] = None
        # Policy Details
        self._policy_details: Optional[List[encryption_report_policy_details.EncryptionReportPolicyDetails]] = None
        # Device TPM Version
        self._tpm_specification_version: Optional[str] = None
        # User name
        self._user_principal_name: Optional[str] = None
    
    @property
    def advanced_bit_locker_states(self,) -> Optional[advanced_bit_locker_state.AdvancedBitLockerState]:
        """
        Gets the advancedBitLockerStates property value. Advanced BitLocker State. Possible values are: success, noUserConsent, osVolumeUnprotected, osVolumeTpmRequired, osVolumeTpmOnlyRequired, osVolumeTpmPinRequired, osVolumeTpmStartupKeyRequired, osVolumeTpmPinStartupKeyRequired, osVolumeEncryptionMethodMismatch, recoveryKeyBackupFailed, fixedDriveNotEncrypted, fixedDriveEncryptionMethodMismatch, loggedOnUserNonAdmin, windowsRecoveryEnvironmentNotConfigured, tpmNotAvailable, tpmNotReady, networkError.
        Returns: Optional[advanced_bit_locker_state.AdvancedBitLockerState]
        """
        return self._advanced_bit_locker_states
    
    @advanced_bit_locker_states.setter
    def advanced_bit_locker_states(self,value: Optional[advanced_bit_locker_state.AdvancedBitLockerState] = None) -> None:
        """
        Sets the advancedBitLockerStates property value. Advanced BitLocker State. Possible values are: success, noUserConsent, osVolumeUnprotected, osVolumeTpmRequired, osVolumeTpmOnlyRequired, osVolumeTpmPinRequired, osVolumeTpmStartupKeyRequired, osVolumeTpmPinStartupKeyRequired, osVolumeEncryptionMethodMismatch, recoveryKeyBackupFailed, fixedDriveNotEncrypted, fixedDriveEncryptionMethodMismatch, loggedOnUserNonAdmin, windowsRecoveryEnvironmentNotConfigured, tpmNotAvailable, tpmNotReady, networkError.
        Args:
            value: Value to set for the advanced_bit_locker_states property.
        """
        self._advanced_bit_locker_states = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceEncryptionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceEncryptionState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceEncryptionState()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    @property
    def device_type(self,) -> Optional[device_types.DeviceTypes]:
        """
        Gets the deviceType property value. Device type.
        Returns: Optional[device_types.DeviceTypes]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[device_types.DeviceTypes] = None) -> None:
        """
        Sets the deviceType property value. Device type.
        Args:
            value: Value to set for the device_type property.
        """
        self._device_type = value
    
    @property
    def encryption_policy_setting_state(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the encryptionPolicySettingState property value. The encryptionPolicySettingState property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._encryption_policy_setting_state
    
    @encryption_policy_setting_state.setter
    def encryption_policy_setting_state(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the encryptionPolicySettingState property value. The encryptionPolicySettingState property
        Args:
            value: Value to set for the encryption_policy_setting_state property.
        """
        self._encryption_policy_setting_state = value
    
    @property
    def encryption_readiness_state(self,) -> Optional[encryption_readiness_state.EncryptionReadinessState]:
        """
        Gets the encryptionReadinessState property value. Encryption readiness state
        Returns: Optional[encryption_readiness_state.EncryptionReadinessState]
        """
        return self._encryption_readiness_state
    
    @encryption_readiness_state.setter
    def encryption_readiness_state(self,value: Optional[encryption_readiness_state.EncryptionReadinessState] = None) -> None:
        """
        Sets the encryptionReadinessState property value. Encryption readiness state
        Args:
            value: Value to set for the encryption_readiness_state property.
        """
        self._encryption_readiness_state = value
    
    @property
    def encryption_state(self,) -> Optional[encryption_state.EncryptionState]:
        """
        Gets the encryptionState property value. Encryption state
        Returns: Optional[encryption_state.EncryptionState]
        """
        return self._encryption_state
    
    @encryption_state.setter
    def encryption_state(self,value: Optional[encryption_state.EncryptionState] = None) -> None:
        """
        Sets the encryptionState property value. Encryption state
        Args:
            value: Value to set for the encryption_state property.
        """
        self._encryption_state = value
    
    @property
    def file_vault_states(self,) -> Optional[file_vault_state.FileVaultState]:
        """
        Gets the fileVaultStates property value. FileVault State. Possible values are: success, driveEncryptedByUser, userDeferredEncryption, escrowNotEnabled.
        Returns: Optional[file_vault_state.FileVaultState]
        """
        return self._file_vault_states
    
    @file_vault_states.setter
    def file_vault_states(self,value: Optional[file_vault_state.FileVaultState] = None) -> None:
        """
        Sets the fileVaultStates property value. FileVault State. Possible values are: success, driveEncryptedByUser, userDeferredEncryption, escrowNotEnabled.
        Args:
            value: Value to set for the file_vault_states property.
        """
        self._file_vault_states = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import advanced_bit_locker_state, compliance_status, device_types, encryption_readiness_state, encryption_report_policy_details, encryption_state, entity, file_vault_state

        fields: Dict[str, Callable[[Any], None]] = {
            "advancedBitLockerStates": lambda n : setattr(self, 'advanced_bit_locker_states', n.get_enum_value(advanced_bit_locker_state.AdvancedBitLockerState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(device_types.DeviceTypes)),
            "encryptionPolicySettingState": lambda n : setattr(self, 'encryption_policy_setting_state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "encryptionReadinessState": lambda n : setattr(self, 'encryption_readiness_state', n.get_enum_value(encryption_readiness_state.EncryptionReadinessState)),
            "encryptionState": lambda n : setattr(self, 'encryption_state', n.get_enum_value(encryption_state.EncryptionState)),
            "fileVaultStates": lambda n : setattr(self, 'file_vault_states', n.get_enum_value(file_vault_state.FileVaultState)),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policyDetails": lambda n : setattr(self, 'policy_details', n.get_collection_of_object_values(encryption_report_policy_details.EncryptionReportPolicyDetails)),
            "tpmSpecificationVersion": lambda n : setattr(self, 'tpm_specification_version', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Operating system version of the device
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Operating system version of the device
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
    @property
    def policy_details(self,) -> Optional[List[encryption_report_policy_details.EncryptionReportPolicyDetails]]:
        """
        Gets the policyDetails property value. Policy Details
        Returns: Optional[List[encryption_report_policy_details.EncryptionReportPolicyDetails]]
        """
        return self._policy_details
    
    @policy_details.setter
    def policy_details(self,value: Optional[List[encryption_report_policy_details.EncryptionReportPolicyDetails]] = None) -> None:
        """
        Sets the policyDetails property value. Policy Details
        Args:
            value: Value to set for the policy_details property.
        """
        self._policy_details = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("advancedBitLockerStates", self.advanced_bit_locker_states)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_enum_value("encryptionPolicySettingState", self.encryption_policy_setting_state)
        writer.write_enum_value("encryptionReadinessState", self.encryption_readiness_state)
        writer.write_enum_value("encryptionState", self.encryption_state)
        writer.write_enum_value("fileVaultStates", self.file_vault_states)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_collection_of_object_values("policyDetails", self.policy_details)
        writer.write_str_value("tpmSpecificationVersion", self.tpm_specification_version)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def tpm_specification_version(self,) -> Optional[str]:
        """
        Gets the tpmSpecificationVersion property value. Device TPM Version
        Returns: Optional[str]
        """
        return self._tpm_specification_version
    
    @tpm_specification_version.setter
    def tpm_specification_version(self,value: Optional[str] = None) -> None:
        """
        Sets the tpmSpecificationVersion property value. Device TPM Version
        Args:
            value: Value to set for the tpm_specification_version property.
        """
        self._tpm_specification_version = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User name
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

