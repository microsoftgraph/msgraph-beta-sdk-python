from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import advanced_bit_locker_state, compliance_status, device_types, encryption_readiness_state, encryption_report_policy_details, encryption_state, entity, file_vault_state

from . import entity

@dataclass
class ManagedDeviceEncryptionState(entity.Entity):
    """
    Encryption report per device
    """
    # Advanced BitLocker State. Possible values are: success, noUserConsent, osVolumeUnprotected, osVolumeTpmRequired, osVolumeTpmOnlyRequired, osVolumeTpmPinRequired, osVolumeTpmStartupKeyRequired, osVolumeTpmPinStartupKeyRequired, osVolumeEncryptionMethodMismatch, recoveryKeyBackupFailed, fixedDriveNotEncrypted, fixedDriveEncryptionMethodMismatch, loggedOnUserNonAdmin, windowsRecoveryEnvironmentNotConfigured, tpmNotAvailable, tpmNotReady, networkError.
    advanced_bit_locker_states: Optional[advanced_bit_locker_state.AdvancedBitLockerState] = None
    # Device name
    device_name: Optional[str] = None
    # Device type.
    device_type: Optional[device_types.DeviceTypes] = None
    # The encryptionPolicySettingState property
    encryption_policy_setting_state: Optional[compliance_status.ComplianceStatus] = None
    # Encryption readiness state
    encryption_readiness_state: Optional[encryption_readiness_state.EncryptionReadinessState] = None
    # Encryption state
    encryption_state: Optional[encryption_state.EncryptionState] = None
    # FileVault State. Possible values are: success, driveEncryptedByUser, userDeferredEncryption, escrowNotEnabled.
    file_vault_states: Optional[file_vault_state.FileVaultState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating system version of the device
    os_version: Optional[str] = None
    # Policy Details
    policy_details: Optional[List[encryption_report_policy_details.EncryptionReportPolicyDetails]] = None
    # Device TPM Version
    tpm_specification_version: Optional[str] = None
    # User name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceEncryptionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceEncryptionState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceEncryptionState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import advanced_bit_locker_state, compliance_status, device_types, encryption_readiness_state, encryption_report_policy_details, encryption_state, entity, file_vault_state

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
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
    

