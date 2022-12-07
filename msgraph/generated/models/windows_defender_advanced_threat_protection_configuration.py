from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class WindowsDefenderAdvancedThreatProtectionConfiguration(device_configuration.DeviceConfiguration):
    @property
    def advanced_threat_protection_auto_populate_onboarding_blob(self,) -> Optional[bool]:
        """
        Gets the advancedThreatProtectionAutoPopulateOnboardingBlob property value. Auto populate onboarding blob programmatically from Advanced Threat protection service
        Returns: Optional[bool]
        """
        return self._advanced_threat_protection_auto_populate_onboarding_blob
    
    @advanced_threat_protection_auto_populate_onboarding_blob.setter
    def advanced_threat_protection_auto_populate_onboarding_blob(self,value: Optional[bool] = None) -> None:
        """
        Sets the advancedThreatProtectionAutoPopulateOnboardingBlob property value. Auto populate onboarding blob programmatically from Advanced Threat protection service
        Args:
            value: Value to set for the advancedThreatProtectionAutoPopulateOnboardingBlob property.
        """
        self._advanced_threat_protection_auto_populate_onboarding_blob = value
    
    @property
    def advanced_threat_protection_offboarding_blob(self,) -> Optional[str]:
        """
        Gets the advancedThreatProtectionOffboardingBlob property value. Windows Defender AdvancedThreatProtection Offboarding Blob.
        Returns: Optional[str]
        """
        return self._advanced_threat_protection_offboarding_blob
    
    @advanced_threat_protection_offboarding_blob.setter
    def advanced_threat_protection_offboarding_blob(self,value: Optional[str] = None) -> None:
        """
        Sets the advancedThreatProtectionOffboardingBlob property value. Windows Defender AdvancedThreatProtection Offboarding Blob.
        Args:
            value: Value to set for the advancedThreatProtectionOffboardingBlob property.
        """
        self._advanced_threat_protection_offboarding_blob = value
    
    @property
    def advanced_threat_protection_offboarding_filename(self,) -> Optional[str]:
        """
        Gets the advancedThreatProtectionOffboardingFilename property value. Name of the file from which AdvancedThreatProtectionOffboardingBlob was obtained.
        Returns: Optional[str]
        """
        return self._advanced_threat_protection_offboarding_filename
    
    @advanced_threat_protection_offboarding_filename.setter
    def advanced_threat_protection_offboarding_filename(self,value: Optional[str] = None) -> None:
        """
        Sets the advancedThreatProtectionOffboardingFilename property value. Name of the file from which AdvancedThreatProtectionOffboardingBlob was obtained.
        Args:
            value: Value to set for the advancedThreatProtectionOffboardingFilename property.
        """
        self._advanced_threat_protection_offboarding_filename = value
    
    @property
    def advanced_threat_protection_onboarding_blob(self,) -> Optional[str]:
        """
        Gets the advancedThreatProtectionOnboardingBlob property value. Windows Defender AdvancedThreatProtection Onboarding Blob.
        Returns: Optional[str]
        """
        return self._advanced_threat_protection_onboarding_blob
    
    @advanced_threat_protection_onboarding_blob.setter
    def advanced_threat_protection_onboarding_blob(self,value: Optional[str] = None) -> None:
        """
        Sets the advancedThreatProtectionOnboardingBlob property value. Windows Defender AdvancedThreatProtection Onboarding Blob.
        Args:
            value: Value to set for the advancedThreatProtectionOnboardingBlob property.
        """
        self._advanced_threat_protection_onboarding_blob = value
    
    @property
    def advanced_threat_protection_onboarding_filename(self,) -> Optional[str]:
        """
        Gets the advancedThreatProtectionOnboardingFilename property value. Name of the file from which AdvancedThreatProtectionOnboardingBlob was obtained.
        Returns: Optional[str]
        """
        return self._advanced_threat_protection_onboarding_filename
    
    @advanced_threat_protection_onboarding_filename.setter
    def advanced_threat_protection_onboarding_filename(self,value: Optional[str] = None) -> None:
        """
        Sets the advancedThreatProtectionOnboardingFilename property value. Name of the file from which AdvancedThreatProtectionOnboardingBlob was obtained.
        Args:
            value: Value to set for the advancedThreatProtectionOnboardingFilename property.
        """
        self._advanced_threat_protection_onboarding_filename = value
    
    @property
    def allow_sample_sharing(self,) -> Optional[bool]:
        """
        Gets the allowSampleSharing property value. Windows Defender AdvancedThreatProtection 'Allow Sample Sharing' Rule
        Returns: Optional[bool]
        """
        return self._allow_sample_sharing
    
    @allow_sample_sharing.setter
    def allow_sample_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowSampleSharing property value. Windows Defender AdvancedThreatProtection 'Allow Sample Sharing' Rule
        Args:
            value: Value to set for the allowSampleSharing property.
        """
        self._allow_sample_sharing = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsDefenderAdvancedThreatProtectionConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration"
        # Auto populate onboarding blob programmatically from Advanced Threat protection service
        self._advanced_threat_protection_auto_populate_onboarding_blob: Optional[bool] = None
        # Windows Defender AdvancedThreatProtection Offboarding Blob.
        self._advanced_threat_protection_offboarding_blob: Optional[str] = None
        # Name of the file from which AdvancedThreatProtectionOffboardingBlob was obtained.
        self._advanced_threat_protection_offboarding_filename: Optional[str] = None
        # Windows Defender AdvancedThreatProtection Onboarding Blob.
        self._advanced_threat_protection_onboarding_blob: Optional[str] = None
        # Name of the file from which AdvancedThreatProtectionOnboardingBlob was obtained.
        self._advanced_threat_protection_onboarding_filename: Optional[str] = None
        # Windows Defender AdvancedThreatProtection 'Allow Sample Sharing' Rule
        self._allow_sample_sharing: Optional[bool] = None
        # Expedite Windows Defender Advanced Threat Protection telemetry reporting frequency.
        self._enable_expedited_telemetry_reporting: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderAdvancedThreatProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderAdvancedThreatProtectionConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDefenderAdvancedThreatProtectionConfiguration()
    
    @property
    def enable_expedited_telemetry_reporting(self,) -> Optional[bool]:
        """
        Gets the enableExpeditedTelemetryReporting property value. Expedite Windows Defender Advanced Threat Protection telemetry reporting frequency.
        Returns: Optional[bool]
        """
        return self._enable_expedited_telemetry_reporting
    
    @enable_expedited_telemetry_reporting.setter
    def enable_expedited_telemetry_reporting(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableExpeditedTelemetryReporting property value. Expedite Windows Defender Advanced Threat Protection telemetry reporting frequency.
        Args:
            value: Value to set for the enableExpeditedTelemetryReporting property.
        """
        self._enable_expedited_telemetry_reporting = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "advanced_threat_protection_auto_populate_onboarding_blob": lambda n : setattr(self, 'advanced_threat_protection_auto_populate_onboarding_blob', n.get_bool_value()),
            "advanced_threat_protection_offboarding_blob": lambda n : setattr(self, 'advanced_threat_protection_offboarding_blob', n.get_str_value()),
            "advanced_threat_protection_offboarding_filename": lambda n : setattr(self, 'advanced_threat_protection_offboarding_filename', n.get_str_value()),
            "advanced_threat_protection_onboarding_blob": lambda n : setattr(self, 'advanced_threat_protection_onboarding_blob', n.get_str_value()),
            "advanced_threat_protection_onboarding_filename": lambda n : setattr(self, 'advanced_threat_protection_onboarding_filename', n.get_str_value()),
            "allow_sample_sharing": lambda n : setattr(self, 'allow_sample_sharing', n.get_bool_value()),
            "enable_expedited_telemetry_reporting": lambda n : setattr(self, 'enable_expedited_telemetry_reporting', n.get_bool_value()),
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
        writer.write_bool_value("advancedThreatProtectionAutoPopulateOnboardingBlob", self.advanced_threat_protection_auto_populate_onboarding_blob)
        writer.write_str_value("advancedThreatProtectionOffboardingBlob", self.advanced_threat_protection_offboarding_blob)
        writer.write_str_value("advancedThreatProtectionOffboardingFilename", self.advanced_threat_protection_offboarding_filename)
        writer.write_str_value("advancedThreatProtectionOnboardingBlob", self.advanced_threat_protection_onboarding_blob)
        writer.write_str_value("advancedThreatProtectionOnboardingFilename", self.advanced_threat_protection_onboarding_filename)
        writer.write_bool_value("allowSampleSharing", self.allow_sample_sharing)
        writer.write_bool_value("enableExpeditedTelemetryReporting", self.enable_expedited_telemetry_reporting)
    

