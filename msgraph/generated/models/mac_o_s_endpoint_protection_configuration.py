from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')
mac_o_s_file_vault_recovery_key_types = lazy_import('msgraph.generated.models.mac_o_s_file_vault_recovery_key_types')
mac_o_s_firewall_application = lazy_import('msgraph.generated.models.mac_o_s_firewall_application')
mac_o_s_gatekeeper_app_sources = lazy_import('msgraph.generated.models.mac_o_s_gatekeeper_app_sources')

class MacOSEndpointProtectionConfiguration(device_configuration.DeviceConfiguration):
    @property
    def advanced_threat_protection_automatic_sample_submission(self,) -> Optional[enablement.Enablement]:
        """
        Gets the advancedThreatProtectionAutomaticSampleSubmission property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._advanced_threat_protection_automatic_sample_submission
    
    @advanced_threat_protection_automatic_sample_submission.setter
    def advanced_threat_protection_automatic_sample_submission(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the advancedThreatProtectionAutomaticSampleSubmission property value. Possible values of a property
        Args:
            value: Value to set for the advancedThreatProtectionAutomaticSampleSubmission property.
        """
        self._advanced_threat_protection_automatic_sample_submission = value
    
    @property
    def advanced_threat_protection_cloud_delivered(self,) -> Optional[enablement.Enablement]:
        """
        Gets the advancedThreatProtectionCloudDelivered property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._advanced_threat_protection_cloud_delivered
    
    @advanced_threat_protection_cloud_delivered.setter
    def advanced_threat_protection_cloud_delivered(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the advancedThreatProtectionCloudDelivered property value. Possible values of a property
        Args:
            value: Value to set for the advancedThreatProtectionCloudDelivered property.
        """
        self._advanced_threat_protection_cloud_delivered = value
    
    @property
    def advanced_threat_protection_diagnostic_data_collection(self,) -> Optional[enablement.Enablement]:
        """
        Gets the advancedThreatProtectionDiagnosticDataCollection property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._advanced_threat_protection_diagnostic_data_collection
    
    @advanced_threat_protection_diagnostic_data_collection.setter
    def advanced_threat_protection_diagnostic_data_collection(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the advancedThreatProtectionDiagnosticDataCollection property value. Possible values of a property
        Args:
            value: Value to set for the advancedThreatProtectionDiagnosticDataCollection property.
        """
        self._advanced_threat_protection_diagnostic_data_collection = value
    
    @property
    def advanced_threat_protection_excluded_extensions(self,) -> Optional[List[str]]:
        """
        Gets the advancedThreatProtectionExcludedExtensions property value. A list of file extensions to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Returns: Optional[List[str]]
        """
        return self._advanced_threat_protection_excluded_extensions
    
    @advanced_threat_protection_excluded_extensions.setter
    def advanced_threat_protection_excluded_extensions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the advancedThreatProtectionExcludedExtensions property value. A list of file extensions to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Args:
            value: Value to set for the advancedThreatProtectionExcludedExtensions property.
        """
        self._advanced_threat_protection_excluded_extensions = value
    
    @property
    def advanced_threat_protection_excluded_files(self,) -> Optional[List[str]]:
        """
        Gets the advancedThreatProtectionExcludedFiles property value. A list of paths to files to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Returns: Optional[List[str]]
        """
        return self._advanced_threat_protection_excluded_files
    
    @advanced_threat_protection_excluded_files.setter
    def advanced_threat_protection_excluded_files(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the advancedThreatProtectionExcludedFiles property value. A list of paths to files to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Args:
            value: Value to set for the advancedThreatProtectionExcludedFiles property.
        """
        self._advanced_threat_protection_excluded_files = value
    
    @property
    def advanced_threat_protection_excluded_folders(self,) -> Optional[List[str]]:
        """
        Gets the advancedThreatProtectionExcludedFolders property value. A list of paths to folders to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Returns: Optional[List[str]]
        """
        return self._advanced_threat_protection_excluded_folders
    
    @advanced_threat_protection_excluded_folders.setter
    def advanced_threat_protection_excluded_folders(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the advancedThreatProtectionExcludedFolders property value. A list of paths to folders to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Args:
            value: Value to set for the advancedThreatProtectionExcludedFolders property.
        """
        self._advanced_threat_protection_excluded_folders = value
    
    @property
    def advanced_threat_protection_excluded_processes(self,) -> Optional[List[str]]:
        """
        Gets the advancedThreatProtectionExcludedProcesses property value. A list of process names to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Returns: Optional[List[str]]
        """
        return self._advanced_threat_protection_excluded_processes
    
    @advanced_threat_protection_excluded_processes.setter
    def advanced_threat_protection_excluded_processes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the advancedThreatProtectionExcludedProcesses property value. A list of process names to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        Args:
            value: Value to set for the advancedThreatProtectionExcludedProcesses property.
        """
        self._advanced_threat_protection_excluded_processes = value
    
    @property
    def advanced_threat_protection_real_time(self,) -> Optional[enablement.Enablement]:
        """
        Gets the advancedThreatProtectionRealTime property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._advanced_threat_protection_real_time
    
    @advanced_threat_protection_real_time.setter
    def advanced_threat_protection_real_time(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the advancedThreatProtectionRealTime property value. Possible values of a property
        Args:
            value: Value to set for the advancedThreatProtectionRealTime property.
        """
        self._advanced_threat_protection_real_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSEndpointProtectionConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSEndpointProtectionConfiguration"
        # Possible values of a property
        self._advanced_threat_protection_automatic_sample_submission: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._advanced_threat_protection_cloud_delivered: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._advanced_threat_protection_diagnostic_data_collection: Optional[enablement.Enablement] = None
        # A list of file extensions to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        self._advanced_threat_protection_excluded_extensions: Optional[List[str]] = None
        # A list of paths to files to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        self._advanced_threat_protection_excluded_files: Optional[List[str]] = None
        # A list of paths to folders to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        self._advanced_threat_protection_excluded_folders: Optional[List[str]] = None
        # A list of process names to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
        self._advanced_threat_protection_excluded_processes: Optional[List[str]] = None
        # Possible values of a property
        self._advanced_threat_protection_real_time: Optional[enablement.Enablement] = None
        # Optional. If set to true, the user can defer the enabling of FileVault until they sign out.
        self._file_vault_allow_deferral_until_sign_out: Optional[bool] = None
        # Optional. When using the Defer option, if set to true, the user is not prompted to enable FileVault at sign-out.
        self._file_vault_disable_prompt_at_sign_out: Optional[bool] = None
        # Whether FileVault should be enabled or not.
        self._file_vault_enabled: Optional[bool] = None
        # Optional. A hidden personal recovery key does not appear on the user's screen during FileVault encryption, reducing the risk of it ending up in the wrong hands.
        self._file_vault_hide_personal_recovery_key: Optional[bool] = None
        # Required if selected recovery key type(s) include InstitutionalRecoveryKey. The DER Encoded certificate file used to set an institutional recovery key.
        self._file_vault_institutional_recovery_key_certificate: Optional[bytes] = None
        # File name of the institutional recovery key certificate to display in UI. (.der).
        self._file_vault_institutional_recovery_key_certificate_file_name: Optional[str] = None
        # Optional. When using the Defer option, this is the maximum number of times the user can ignore prompts to enable FileVault before FileVault will be required for the user to sign in. If set to -1, it will always prompt to enable FileVault until FileVault is enabled, though it will allow the user to bypass enabling FileVault. Setting this to 0 will disable the feature.
        self._file_vault_number_of_times_user_can_ignore: Optional[int] = None
        # Required if selected recovery key type(s) include PersonalRecoveryKey. A short message displayed to the user that explains how they can retrieve their personal recovery key.
        self._file_vault_personal_recovery_key_help_message: Optional[str] = None
        # Optional. If selected recovery key type(s) include PersonalRecoveryKey, the frequency to rotate that key, in months.
        self._file_vault_personal_recovery_key_rotation_in_months: Optional[int] = None
        # Recovery key types for macOS FileVault
        self._file_vault_selected_recovery_key_types: Optional[mac_o_s_file_vault_recovery_key_types.MacOSFileVaultRecoveryKeyTypes] = None
        # List of applications with firewall settings. Firewall settings for applications not on this list are determined by the user. This collection can contain a maximum of 500 elements.
        self._firewall_applications: Optional[List[mac_o_s_firewall_application.MacOSFirewallApplication]] = None
        # Corresponds to the 'Block all incoming connections' option.
        self._firewall_block_all_incoming: Optional[bool] = None
        # Whether the firewall should be enabled or not.
        self._firewall_enabled: Optional[bool] = None
        # Corresponds to 'Enable stealth mode.'
        self._firewall_enable_stealth_mode: Optional[bool] = None
        # App source options for macOS Gatekeeper.
        self._gatekeeper_allowed_app_source: Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources] = None
        # If set to true, the user override for Gatekeeper will be disabled.
        self._gatekeeper_block_override: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSEndpointProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSEndpointProtectionConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSEndpointProtectionConfiguration()
    
    @property
    def file_vault_allow_deferral_until_sign_out(self,) -> Optional[bool]:
        """
        Gets the fileVaultAllowDeferralUntilSignOut property value. Optional. If set to true, the user can defer the enabling of FileVault until they sign out.
        Returns: Optional[bool]
        """
        return self._file_vault_allow_deferral_until_sign_out
    
    @file_vault_allow_deferral_until_sign_out.setter
    def file_vault_allow_deferral_until_sign_out(self,value: Optional[bool] = None) -> None:
        """
        Sets the fileVaultAllowDeferralUntilSignOut property value. Optional. If set to true, the user can defer the enabling of FileVault until they sign out.
        Args:
            value: Value to set for the fileVaultAllowDeferralUntilSignOut property.
        """
        self._file_vault_allow_deferral_until_sign_out = value
    
    @property
    def file_vault_disable_prompt_at_sign_out(self,) -> Optional[bool]:
        """
        Gets the fileVaultDisablePromptAtSignOut property value. Optional. When using the Defer option, if set to true, the user is not prompted to enable FileVault at sign-out.
        Returns: Optional[bool]
        """
        return self._file_vault_disable_prompt_at_sign_out
    
    @file_vault_disable_prompt_at_sign_out.setter
    def file_vault_disable_prompt_at_sign_out(self,value: Optional[bool] = None) -> None:
        """
        Sets the fileVaultDisablePromptAtSignOut property value. Optional. When using the Defer option, if set to true, the user is not prompted to enable FileVault at sign-out.
        Args:
            value: Value to set for the fileVaultDisablePromptAtSignOut property.
        """
        self._file_vault_disable_prompt_at_sign_out = value
    
    @property
    def file_vault_enabled(self,) -> Optional[bool]:
        """
        Gets the fileVaultEnabled property value. Whether FileVault should be enabled or not.
        Returns: Optional[bool]
        """
        return self._file_vault_enabled
    
    @file_vault_enabled.setter
    def file_vault_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the fileVaultEnabled property value. Whether FileVault should be enabled or not.
        Args:
            value: Value to set for the fileVaultEnabled property.
        """
        self._file_vault_enabled = value
    
    @property
    def file_vault_hide_personal_recovery_key(self,) -> Optional[bool]:
        """
        Gets the fileVaultHidePersonalRecoveryKey property value. Optional. A hidden personal recovery key does not appear on the user's screen during FileVault encryption, reducing the risk of it ending up in the wrong hands.
        Returns: Optional[bool]
        """
        return self._file_vault_hide_personal_recovery_key
    
    @file_vault_hide_personal_recovery_key.setter
    def file_vault_hide_personal_recovery_key(self,value: Optional[bool] = None) -> None:
        """
        Sets the fileVaultHidePersonalRecoveryKey property value. Optional. A hidden personal recovery key does not appear on the user's screen during FileVault encryption, reducing the risk of it ending up in the wrong hands.
        Args:
            value: Value to set for the fileVaultHidePersonalRecoveryKey property.
        """
        self._file_vault_hide_personal_recovery_key = value
    
    @property
    def file_vault_institutional_recovery_key_certificate(self,) -> Optional[bytes]:
        """
        Gets the fileVaultInstitutionalRecoveryKeyCertificate property value. Required if selected recovery key type(s) include InstitutionalRecoveryKey. The DER Encoded certificate file used to set an institutional recovery key.
        Returns: Optional[bytes]
        """
        return self._file_vault_institutional_recovery_key_certificate
    
    @file_vault_institutional_recovery_key_certificate.setter
    def file_vault_institutional_recovery_key_certificate(self,value: Optional[bytes] = None) -> None:
        """
        Sets the fileVaultInstitutionalRecoveryKeyCertificate property value. Required if selected recovery key type(s) include InstitutionalRecoveryKey. The DER Encoded certificate file used to set an institutional recovery key.
        Args:
            value: Value to set for the fileVaultInstitutionalRecoveryKeyCertificate property.
        """
        self._file_vault_institutional_recovery_key_certificate = value
    
    @property
    def file_vault_institutional_recovery_key_certificate_file_name(self,) -> Optional[str]:
        """
        Gets the fileVaultInstitutionalRecoveryKeyCertificateFileName property value. File name of the institutional recovery key certificate to display in UI. (.der).
        Returns: Optional[str]
        """
        return self._file_vault_institutional_recovery_key_certificate_file_name
    
    @file_vault_institutional_recovery_key_certificate_file_name.setter
    def file_vault_institutional_recovery_key_certificate_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileVaultInstitutionalRecoveryKeyCertificateFileName property value. File name of the institutional recovery key certificate to display in UI. (.der).
        Args:
            value: Value to set for the fileVaultInstitutionalRecoveryKeyCertificateFileName property.
        """
        self._file_vault_institutional_recovery_key_certificate_file_name = value
    
    @property
    def file_vault_number_of_times_user_can_ignore(self,) -> Optional[int]:
        """
        Gets the fileVaultNumberOfTimesUserCanIgnore property value. Optional. When using the Defer option, this is the maximum number of times the user can ignore prompts to enable FileVault before FileVault will be required for the user to sign in. If set to -1, it will always prompt to enable FileVault until FileVault is enabled, though it will allow the user to bypass enabling FileVault. Setting this to 0 will disable the feature.
        Returns: Optional[int]
        """
        return self._file_vault_number_of_times_user_can_ignore
    
    @file_vault_number_of_times_user_can_ignore.setter
    def file_vault_number_of_times_user_can_ignore(self,value: Optional[int] = None) -> None:
        """
        Sets the fileVaultNumberOfTimesUserCanIgnore property value. Optional. When using the Defer option, this is the maximum number of times the user can ignore prompts to enable FileVault before FileVault will be required for the user to sign in. If set to -1, it will always prompt to enable FileVault until FileVault is enabled, though it will allow the user to bypass enabling FileVault. Setting this to 0 will disable the feature.
        Args:
            value: Value to set for the fileVaultNumberOfTimesUserCanIgnore property.
        """
        self._file_vault_number_of_times_user_can_ignore = value
    
    @property
    def file_vault_personal_recovery_key_help_message(self,) -> Optional[str]:
        """
        Gets the fileVaultPersonalRecoveryKeyHelpMessage property value. Required if selected recovery key type(s) include PersonalRecoveryKey. A short message displayed to the user that explains how they can retrieve their personal recovery key.
        Returns: Optional[str]
        """
        return self._file_vault_personal_recovery_key_help_message
    
    @file_vault_personal_recovery_key_help_message.setter
    def file_vault_personal_recovery_key_help_message(self,value: Optional[str] = None) -> None:
        """
        Sets the fileVaultPersonalRecoveryKeyHelpMessage property value. Required if selected recovery key type(s) include PersonalRecoveryKey. A short message displayed to the user that explains how they can retrieve their personal recovery key.
        Args:
            value: Value to set for the fileVaultPersonalRecoveryKeyHelpMessage property.
        """
        self._file_vault_personal_recovery_key_help_message = value
    
    @property
    def file_vault_personal_recovery_key_rotation_in_months(self,) -> Optional[int]:
        """
        Gets the fileVaultPersonalRecoveryKeyRotationInMonths property value. Optional. If selected recovery key type(s) include PersonalRecoveryKey, the frequency to rotate that key, in months.
        Returns: Optional[int]
        """
        return self._file_vault_personal_recovery_key_rotation_in_months
    
    @file_vault_personal_recovery_key_rotation_in_months.setter
    def file_vault_personal_recovery_key_rotation_in_months(self,value: Optional[int] = None) -> None:
        """
        Sets the fileVaultPersonalRecoveryKeyRotationInMonths property value. Optional. If selected recovery key type(s) include PersonalRecoveryKey, the frequency to rotate that key, in months.
        Args:
            value: Value to set for the fileVaultPersonalRecoveryKeyRotationInMonths property.
        """
        self._file_vault_personal_recovery_key_rotation_in_months = value
    
    @property
    def file_vault_selected_recovery_key_types(self,) -> Optional[mac_o_s_file_vault_recovery_key_types.MacOSFileVaultRecoveryKeyTypes]:
        """
        Gets the fileVaultSelectedRecoveryKeyTypes property value. Recovery key types for macOS FileVault
        Returns: Optional[mac_o_s_file_vault_recovery_key_types.MacOSFileVaultRecoveryKeyTypes]
        """
        return self._file_vault_selected_recovery_key_types
    
    @file_vault_selected_recovery_key_types.setter
    def file_vault_selected_recovery_key_types(self,value: Optional[mac_o_s_file_vault_recovery_key_types.MacOSFileVaultRecoveryKeyTypes] = None) -> None:
        """
        Sets the fileVaultSelectedRecoveryKeyTypes property value. Recovery key types for macOS FileVault
        Args:
            value: Value to set for the fileVaultSelectedRecoveryKeyTypes property.
        """
        self._file_vault_selected_recovery_key_types = value
    
    @property
    def firewall_applications(self,) -> Optional[List[mac_o_s_firewall_application.MacOSFirewallApplication]]:
        """
        Gets the firewallApplications property value. List of applications with firewall settings. Firewall settings for applications not on this list are determined by the user. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_firewall_application.MacOSFirewallApplication]]
        """
        return self._firewall_applications
    
    @firewall_applications.setter
    def firewall_applications(self,value: Optional[List[mac_o_s_firewall_application.MacOSFirewallApplication]] = None) -> None:
        """
        Sets the firewallApplications property value. List of applications with firewall settings. Firewall settings for applications not on this list are determined by the user. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the firewallApplications property.
        """
        self._firewall_applications = value
    
    @property
    def firewall_block_all_incoming(self,) -> Optional[bool]:
        """
        Gets the firewallBlockAllIncoming property value. Corresponds to the 'Block all incoming connections' option.
        Returns: Optional[bool]
        """
        return self._firewall_block_all_incoming
    
    @firewall_block_all_incoming.setter
    def firewall_block_all_incoming(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallBlockAllIncoming property value. Corresponds to the 'Block all incoming connections' option.
        Args:
            value: Value to set for the firewallBlockAllIncoming property.
        """
        self._firewall_block_all_incoming = value
    
    @property
    def firewall_enabled(self,) -> Optional[bool]:
        """
        Gets the firewallEnabled property value. Whether the firewall should be enabled or not.
        Returns: Optional[bool]
        """
        return self._firewall_enabled
    
    @firewall_enabled.setter
    def firewall_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallEnabled property value. Whether the firewall should be enabled or not.
        Args:
            value: Value to set for the firewallEnabled property.
        """
        self._firewall_enabled = value
    
    @property
    def firewall_enable_stealth_mode(self,) -> Optional[bool]:
        """
        Gets the firewallEnableStealthMode property value. Corresponds to 'Enable stealth mode.'
        Returns: Optional[bool]
        """
        return self._firewall_enable_stealth_mode
    
    @firewall_enable_stealth_mode.setter
    def firewall_enable_stealth_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallEnableStealthMode property value. Corresponds to 'Enable stealth mode.'
        Args:
            value: Value to set for the firewallEnableStealthMode property.
        """
        self._firewall_enable_stealth_mode = value
    
    @property
    def gatekeeper_allowed_app_source(self,) -> Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources]:
        """
        Gets the gatekeeperAllowedAppSource property value. App source options for macOS Gatekeeper.
        Returns: Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources]
        """
        return self._gatekeeper_allowed_app_source
    
    @gatekeeper_allowed_app_source.setter
    def gatekeeper_allowed_app_source(self,value: Optional[mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources] = None) -> None:
        """
        Sets the gatekeeperAllowedAppSource property value. App source options for macOS Gatekeeper.
        Args:
            value: Value to set for the gatekeeperAllowedAppSource property.
        """
        self._gatekeeper_allowed_app_source = value
    
    @property
    def gatekeeper_block_override(self,) -> Optional[bool]:
        """
        Gets the gatekeeperBlockOverride property value. If set to true, the user override for Gatekeeper will be disabled.
        Returns: Optional[bool]
        """
        return self._gatekeeper_block_override
    
    @gatekeeper_block_override.setter
    def gatekeeper_block_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the gatekeeperBlockOverride property value. If set to true, the user override for Gatekeeper will be disabled.
        Args:
            value: Value to set for the gatekeeperBlockOverride property.
        """
        self._gatekeeper_block_override = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "advanced_threat_protection_automatic_sample_submission": lambda n : setattr(self, 'advanced_threat_protection_automatic_sample_submission', n.get_enum_value(enablement.Enablement)),
            "advanced_threat_protection_cloud_delivered": lambda n : setattr(self, 'advanced_threat_protection_cloud_delivered', n.get_enum_value(enablement.Enablement)),
            "advanced_threat_protection_diagnostic_data_collection": lambda n : setattr(self, 'advanced_threat_protection_diagnostic_data_collection', n.get_enum_value(enablement.Enablement)),
            "advanced_threat_protection_excluded_extensions": lambda n : setattr(self, 'advanced_threat_protection_excluded_extensions', n.get_collection_of_primitive_values(str)),
            "advanced_threat_protection_excluded_files": lambda n : setattr(self, 'advanced_threat_protection_excluded_files', n.get_collection_of_primitive_values(str)),
            "advanced_threat_protection_excluded_folders": lambda n : setattr(self, 'advanced_threat_protection_excluded_folders', n.get_collection_of_primitive_values(str)),
            "advanced_threat_protection_excluded_processes": lambda n : setattr(self, 'advanced_threat_protection_excluded_processes', n.get_collection_of_primitive_values(str)),
            "advanced_threat_protection_real_time": lambda n : setattr(self, 'advanced_threat_protection_real_time', n.get_enum_value(enablement.Enablement)),
            "file_vault_allow_deferral_until_sign_out": lambda n : setattr(self, 'file_vault_allow_deferral_until_sign_out', n.get_bool_value()),
            "file_vault_disable_prompt_at_sign_out": lambda n : setattr(self, 'file_vault_disable_prompt_at_sign_out', n.get_bool_value()),
            "file_vault_enabled": lambda n : setattr(self, 'file_vault_enabled', n.get_bool_value()),
            "file_vault_hide_personal_recovery_key": lambda n : setattr(self, 'file_vault_hide_personal_recovery_key', n.get_bool_value()),
            "file_vault_institutional_recovery_key_certificate": lambda n : setattr(self, 'file_vault_institutional_recovery_key_certificate', n.get_bytes_value()),
            "file_vault_institutional_recovery_key_certificate_file_name": lambda n : setattr(self, 'file_vault_institutional_recovery_key_certificate_file_name', n.get_str_value()),
            "file_vault_number_of_times_user_can_ignore": lambda n : setattr(self, 'file_vault_number_of_times_user_can_ignore', n.get_int_value()),
            "file_vault_personal_recovery_key_help_message": lambda n : setattr(self, 'file_vault_personal_recovery_key_help_message', n.get_str_value()),
            "file_vault_personal_recovery_key_rotation_in_months": lambda n : setattr(self, 'file_vault_personal_recovery_key_rotation_in_months', n.get_int_value()),
            "file_vault_selected_recovery_key_types": lambda n : setattr(self, 'file_vault_selected_recovery_key_types', n.get_enum_value(mac_o_s_file_vault_recovery_key_types.MacOSFileVaultRecoveryKeyTypes)),
            "firewall_applications": lambda n : setattr(self, 'firewall_applications', n.get_collection_of_object_values(mac_o_s_firewall_application.MacOSFirewallApplication)),
            "firewall_block_all_incoming": lambda n : setattr(self, 'firewall_block_all_incoming', n.get_bool_value()),
            "firewall_enabled": lambda n : setattr(self, 'firewall_enabled', n.get_bool_value()),
            "firewall_enable_stealth_mode": lambda n : setattr(self, 'firewall_enable_stealth_mode', n.get_bool_value()),
            "gatekeeper_allowed_app_source": lambda n : setattr(self, 'gatekeeper_allowed_app_source', n.get_enum_value(mac_o_s_gatekeeper_app_sources.MacOSGatekeeperAppSources)),
            "gatekeeper_block_override": lambda n : setattr(self, 'gatekeeper_block_override', n.get_bool_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("advancedThreatProtectionAutomaticSampleSubmission", self.advanced_threat_protection_automatic_sample_submission)
        writer.write_enum_value("advancedThreatProtectionCloudDelivered", self.advanced_threat_protection_cloud_delivered)
        writer.write_enum_value("advancedThreatProtectionDiagnosticDataCollection", self.advanced_threat_protection_diagnostic_data_collection)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedExtensions", self.advanced_threat_protection_excluded_extensions)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedFiles", self.advanced_threat_protection_excluded_files)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedFolders", self.advanced_threat_protection_excluded_folders)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedProcesses", self.advanced_threat_protection_excluded_processes)
        writer.write_enum_value("advancedThreatProtectionRealTime", self.advanced_threat_protection_real_time)
        writer.write_bool_value("fileVaultAllowDeferralUntilSignOut", self.file_vault_allow_deferral_until_sign_out)
        writer.write_bool_value("fileVaultDisablePromptAtSignOut", self.file_vault_disable_prompt_at_sign_out)
        writer.write_bool_value("fileVaultEnabled", self.file_vault_enabled)
        writer.write_bool_value("fileVaultHidePersonalRecoveryKey", self.file_vault_hide_personal_recovery_key)
        writer.write_object_value("fileVaultInstitutionalRecoveryKeyCertificate", self.file_vault_institutional_recovery_key_certificate)
        writer.write_str_value("fileVaultInstitutionalRecoveryKeyCertificateFileName", self.file_vault_institutional_recovery_key_certificate_file_name)
        writer.write_int_value("fileVaultNumberOfTimesUserCanIgnore", self.file_vault_number_of_times_user_can_ignore)
        writer.write_str_value("fileVaultPersonalRecoveryKeyHelpMessage", self.file_vault_personal_recovery_key_help_message)
        writer.write_int_value("fileVaultPersonalRecoveryKeyRotationInMonths", self.file_vault_personal_recovery_key_rotation_in_months)
        writer.write_enum_value("fileVaultSelectedRecoveryKeyTypes", self.file_vault_selected_recovery_key_types)
        writer.write_collection_of_object_values("firewallApplications", self.firewall_applications)
        writer.write_bool_value("firewallBlockAllIncoming", self.firewall_block_all_incoming)
        writer.write_bool_value("firewallEnabled", self.firewall_enabled)
        writer.write_bool_value("firewallEnableStealthMode", self.firewall_enable_stealth_mode)
        writer.write_enum_value("gatekeeperAllowedAppSource", self.gatekeeper_allowed_app_source)
        writer.write_bool_value("gatekeeperBlockOverride", self.gatekeeper_block_override)
    

