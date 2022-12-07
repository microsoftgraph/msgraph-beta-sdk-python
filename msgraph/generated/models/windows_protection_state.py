from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
windows_defender_product_status = lazy_import('msgraph.generated.models.windows_defender_product_status')
windows_device_health_state = lazy_import('msgraph.generated.models.windows_device_health_state')
windows_device_malware_state = lazy_import('msgraph.generated.models.windows_device_malware_state')

class WindowsProtectionState(entity.Entity):
    @property
    def anti_malware_version(self,) -> Optional[str]:
        """
        Gets the antiMalwareVersion property value. Current anti malware version
        Returns: Optional[str]
        """
        return self._anti_malware_version
    
    @anti_malware_version.setter
    def anti_malware_version(self,value: Optional[str] = None) -> None:
        """
        Sets the antiMalwareVersion property value. Current anti malware version
        Args:
            value: Value to set for the antiMalwareVersion property.
        """
        self._anti_malware_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsProtectionState and sets the default values.
        """
        super().__init__()
        # Current anti malware version
        self._anti_malware_version: Optional[str] = None
        # Device malware list
        self._detected_malware_state: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]] = None
        # Computer's state (like clean or pending full scan or pending reboot etc). Possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical.
        self._device_state: Optional[windows_device_health_state.WindowsDeviceHealthState] = None
        # Current endpoint protection engine's version
        self._engine_version: Optional[str] = None
        # Full scan overdue or not?
        self._full_scan_overdue: Optional[bool] = None
        # Full scan required or not?
        self._full_scan_required: Optional[bool] = None
        # Indicates whether the device is a virtual machine.
        self._is_virtual_machine: Optional[bool] = None
        # Last quick scan datetime
        self._last_full_scan_date_time: Optional[datetime] = None
        # Last full scan signature version
        self._last_full_scan_signature_version: Optional[str] = None
        # Last quick scan datetime
        self._last_quick_scan_date_time: Optional[datetime] = None
        # Last quick scan signature version
        self._last_quick_scan_signature_version: Optional[str] = None
        # Last device health status reported time
        self._last_reported_date_time: Optional[datetime] = None
        # Anti malware is enabled or not
        self._malware_protection_enabled: Optional[bool] = None
        # Network inspection system enabled or not?
        self._network_inspection_system_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Product Status of Windows Defender Antivirus. Possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall.
        self._product_status: Optional[windows_defender_product_status.WindowsDefenderProductStatus] = None
        # Quick scan overdue or not?
        self._quick_scan_overdue: Optional[bool] = None
        # Real time protection is enabled or not?
        self._real_time_protection_enabled: Optional[bool] = None
        # Reboot required or not?
        self._reboot_required: Optional[bool] = None
        # Signature out of date or not?
        self._signature_update_overdue: Optional[bool] = None
        # Current malware definitions version
        self._signature_version: Optional[str] = None
        # Indicates whether the Windows Defender tamper protection feature is enabled.
        self._tamper_protection_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsProtectionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsProtectionState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsProtectionState()
    
    @property
    def detected_malware_state(self,) -> Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]]:
        """
        Gets the detectedMalwareState property value. Device malware list
        Returns: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]]
        """
        return self._detected_malware_state
    
    @detected_malware_state.setter
    def detected_malware_state(self,value: Optional[List[windows_device_malware_state.WindowsDeviceMalwareState]] = None) -> None:
        """
        Sets the detectedMalwareState property value. Device malware list
        Args:
            value: Value to set for the detectedMalwareState property.
        """
        self._detected_malware_state = value
    
    @property
    def device_state(self,) -> Optional[windows_device_health_state.WindowsDeviceHealthState]:
        """
        Gets the deviceState property value. Computer's state (like clean or pending full scan or pending reboot etc). Possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical.
        Returns: Optional[windows_device_health_state.WindowsDeviceHealthState]
        """
        return self._device_state
    
    @device_state.setter
    def device_state(self,value: Optional[windows_device_health_state.WindowsDeviceHealthState] = None) -> None:
        """
        Sets the deviceState property value. Computer's state (like clean or pending full scan or pending reboot etc). Possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical.
        Args:
            value: Value to set for the deviceState property.
        """
        self._device_state = value
    
    @property
    def engine_version(self,) -> Optional[str]:
        """
        Gets the engineVersion property value. Current endpoint protection engine's version
        Returns: Optional[str]
        """
        return self._engine_version
    
    @engine_version.setter
    def engine_version(self,value: Optional[str] = None) -> None:
        """
        Sets the engineVersion property value. Current endpoint protection engine's version
        Args:
            value: Value to set for the engineVersion property.
        """
        self._engine_version = value
    
    @property
    def full_scan_overdue(self,) -> Optional[bool]:
        """
        Gets the fullScanOverdue property value. Full scan overdue or not?
        Returns: Optional[bool]
        """
        return self._full_scan_overdue
    
    @full_scan_overdue.setter
    def full_scan_overdue(self,value: Optional[bool] = None) -> None:
        """
        Sets the fullScanOverdue property value. Full scan overdue or not?
        Args:
            value: Value to set for the fullScanOverdue property.
        """
        self._full_scan_overdue = value
    
    @property
    def full_scan_required(self,) -> Optional[bool]:
        """
        Gets the fullScanRequired property value. Full scan required or not?
        Returns: Optional[bool]
        """
        return self._full_scan_required
    
    @full_scan_required.setter
    def full_scan_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the fullScanRequired property value. Full scan required or not?
        Args:
            value: Value to set for the fullScanRequired property.
        """
        self._full_scan_required = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "anti_malware_version": lambda n : setattr(self, 'anti_malware_version', n.get_str_value()),
            "detected_malware_state": lambda n : setattr(self, 'detected_malware_state', n.get_collection_of_object_values(windows_device_malware_state.WindowsDeviceMalwareState)),
            "device_state": lambda n : setattr(self, 'device_state', n.get_enum_value(windows_device_health_state.WindowsDeviceHealthState)),
            "engine_version": lambda n : setattr(self, 'engine_version', n.get_str_value()),
            "full_scan_overdue": lambda n : setattr(self, 'full_scan_overdue', n.get_bool_value()),
            "full_scan_required": lambda n : setattr(self, 'full_scan_required', n.get_bool_value()),
            "is_virtual_machine": lambda n : setattr(self, 'is_virtual_machine', n.get_bool_value()),
            "last_full_scan_date_time": lambda n : setattr(self, 'last_full_scan_date_time', n.get_datetime_value()),
            "last_full_scan_signature_version": lambda n : setattr(self, 'last_full_scan_signature_version', n.get_str_value()),
            "last_quick_scan_date_time": lambda n : setattr(self, 'last_quick_scan_date_time', n.get_datetime_value()),
            "last_quick_scan_signature_version": lambda n : setattr(self, 'last_quick_scan_signature_version', n.get_str_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malware_protection_enabled": lambda n : setattr(self, 'malware_protection_enabled', n.get_bool_value()),
            "network_inspection_system_enabled": lambda n : setattr(self, 'network_inspection_system_enabled', n.get_bool_value()),
            "product_status": lambda n : setattr(self, 'product_status', n.get_enum_value(windows_defender_product_status.WindowsDefenderProductStatus)),
            "quick_scan_overdue": lambda n : setattr(self, 'quick_scan_overdue', n.get_bool_value()),
            "real_time_protection_enabled": lambda n : setattr(self, 'real_time_protection_enabled', n.get_bool_value()),
            "reboot_required": lambda n : setattr(self, 'reboot_required', n.get_bool_value()),
            "signature_update_overdue": lambda n : setattr(self, 'signature_update_overdue', n.get_bool_value()),
            "signature_version": lambda n : setattr(self, 'signature_version', n.get_str_value()),
            "tamper_protection_enabled": lambda n : setattr(self, 'tamper_protection_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_virtual_machine(self,) -> Optional[bool]:
        """
        Gets the isVirtualMachine property value. Indicates whether the device is a virtual machine.
        Returns: Optional[bool]
        """
        return self._is_virtual_machine
    
    @is_virtual_machine.setter
    def is_virtual_machine(self,value: Optional[bool] = None) -> None:
        """
        Sets the isVirtualMachine property value. Indicates whether the device is a virtual machine.
        Args:
            value: Value to set for the isVirtualMachine property.
        """
        self._is_virtual_machine = value
    
    @property
    def last_full_scan_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastFullScanDateTime property value. Last quick scan datetime
        Returns: Optional[datetime]
        """
        return self._last_full_scan_date_time
    
    @last_full_scan_date_time.setter
    def last_full_scan_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastFullScanDateTime property value. Last quick scan datetime
        Args:
            value: Value to set for the lastFullScanDateTime property.
        """
        self._last_full_scan_date_time = value
    
    @property
    def last_full_scan_signature_version(self,) -> Optional[str]:
        """
        Gets the lastFullScanSignatureVersion property value. Last full scan signature version
        Returns: Optional[str]
        """
        return self._last_full_scan_signature_version
    
    @last_full_scan_signature_version.setter
    def last_full_scan_signature_version(self,value: Optional[str] = None) -> None:
        """
        Sets the lastFullScanSignatureVersion property value. Last full scan signature version
        Args:
            value: Value to set for the lastFullScanSignatureVersion property.
        """
        self._last_full_scan_signature_version = value
    
    @property
    def last_quick_scan_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastQuickScanDateTime property value. Last quick scan datetime
        Returns: Optional[datetime]
        """
        return self._last_quick_scan_date_time
    
    @last_quick_scan_date_time.setter
    def last_quick_scan_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastQuickScanDateTime property value. Last quick scan datetime
        Args:
            value: Value to set for the lastQuickScanDateTime property.
        """
        self._last_quick_scan_date_time = value
    
    @property
    def last_quick_scan_signature_version(self,) -> Optional[str]:
        """
        Gets the lastQuickScanSignatureVersion property value. Last quick scan signature version
        Returns: Optional[str]
        """
        return self._last_quick_scan_signature_version
    
    @last_quick_scan_signature_version.setter
    def last_quick_scan_signature_version(self,value: Optional[str] = None) -> None:
        """
        Sets the lastQuickScanSignatureVersion property value. Last quick scan signature version
        Args:
            value: Value to set for the lastQuickScanSignatureVersion property.
        """
        self._last_quick_scan_signature_version = value
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. Last device health status reported time
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. Last device health status reported time
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    @property
    def malware_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the malwareProtectionEnabled property value. Anti malware is enabled or not
        Returns: Optional[bool]
        """
        return self._malware_protection_enabled
    
    @malware_protection_enabled.setter
    def malware_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the malwareProtectionEnabled property value. Anti malware is enabled or not
        Args:
            value: Value to set for the malwareProtectionEnabled property.
        """
        self._malware_protection_enabled = value
    
    @property
    def network_inspection_system_enabled(self,) -> Optional[bool]:
        """
        Gets the networkInspectionSystemEnabled property value. Network inspection system enabled or not?
        Returns: Optional[bool]
        """
        return self._network_inspection_system_enabled
    
    @network_inspection_system_enabled.setter
    def network_inspection_system_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the networkInspectionSystemEnabled property value. Network inspection system enabled or not?
        Args:
            value: Value to set for the networkInspectionSystemEnabled property.
        """
        self._network_inspection_system_enabled = value
    
    @property
    def product_status(self,) -> Optional[windows_defender_product_status.WindowsDefenderProductStatus]:
        """
        Gets the productStatus property value. Product Status of Windows Defender Antivirus. Possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall.
        Returns: Optional[windows_defender_product_status.WindowsDefenderProductStatus]
        """
        return self._product_status
    
    @product_status.setter
    def product_status(self,value: Optional[windows_defender_product_status.WindowsDefenderProductStatus] = None) -> None:
        """
        Sets the productStatus property value. Product Status of Windows Defender Antivirus. Possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall.
        Args:
            value: Value to set for the productStatus property.
        """
        self._product_status = value
    
    @property
    def quick_scan_overdue(self,) -> Optional[bool]:
        """
        Gets the quickScanOverdue property value. Quick scan overdue or not?
        Returns: Optional[bool]
        """
        return self._quick_scan_overdue
    
    @quick_scan_overdue.setter
    def quick_scan_overdue(self,value: Optional[bool] = None) -> None:
        """
        Sets the quickScanOverdue property value. Quick scan overdue or not?
        Args:
            value: Value to set for the quickScanOverdue property.
        """
        self._quick_scan_overdue = value
    
    @property
    def real_time_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the realTimeProtectionEnabled property value. Real time protection is enabled or not?
        Returns: Optional[bool]
        """
        return self._real_time_protection_enabled
    
    @real_time_protection_enabled.setter
    def real_time_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the realTimeProtectionEnabled property value. Real time protection is enabled or not?
        Args:
            value: Value to set for the realTimeProtectionEnabled property.
        """
        self._real_time_protection_enabled = value
    
    @property
    def reboot_required(self,) -> Optional[bool]:
        """
        Gets the rebootRequired property value. Reboot required or not?
        Returns: Optional[bool]
        """
        return self._reboot_required
    
    @reboot_required.setter
    def reboot_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the rebootRequired property value. Reboot required or not?
        Args:
            value: Value to set for the rebootRequired property.
        """
        self._reboot_required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("antiMalwareVersion", self.anti_malware_version)
        writer.write_collection_of_object_values("detectedMalwareState", self.detected_malware_state)
        writer.write_enum_value("deviceState", self.device_state)
        writer.write_str_value("engineVersion", self.engine_version)
        writer.write_bool_value("fullScanOverdue", self.full_scan_overdue)
        writer.write_bool_value("fullScanRequired", self.full_scan_required)
        writer.write_bool_value("isVirtualMachine", self.is_virtual_machine)
        writer.write_datetime_value("lastFullScanDateTime", self.last_full_scan_date_time)
        writer.write_str_value("lastFullScanSignatureVersion", self.last_full_scan_signature_version)
        writer.write_datetime_value("lastQuickScanDateTime", self.last_quick_scan_date_time)
        writer.write_str_value("lastQuickScanSignatureVersion", self.last_quick_scan_signature_version)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_bool_value("malwareProtectionEnabled", self.malware_protection_enabled)
        writer.write_bool_value("networkInspectionSystemEnabled", self.network_inspection_system_enabled)
        writer.write_enum_value("productStatus", self.product_status)
        writer.write_bool_value("quickScanOverdue", self.quick_scan_overdue)
        writer.write_bool_value("realTimeProtectionEnabled", self.real_time_protection_enabled)
        writer.write_bool_value("rebootRequired", self.reboot_required)
        writer.write_bool_value("signatureUpdateOverdue", self.signature_update_overdue)
        writer.write_str_value("signatureVersion", self.signature_version)
        writer.write_bool_value("tamperProtectionEnabled", self.tamper_protection_enabled)
    
    @property
    def signature_update_overdue(self,) -> Optional[bool]:
        """
        Gets the signatureUpdateOverdue property value. Signature out of date or not?
        Returns: Optional[bool]
        """
        return self._signature_update_overdue
    
    @signature_update_overdue.setter
    def signature_update_overdue(self,value: Optional[bool] = None) -> None:
        """
        Sets the signatureUpdateOverdue property value. Signature out of date or not?
        Args:
            value: Value to set for the signatureUpdateOverdue property.
        """
        self._signature_update_overdue = value
    
    @property
    def signature_version(self,) -> Optional[str]:
        """
        Gets the signatureVersion property value. Current malware definitions version
        Returns: Optional[str]
        """
        return self._signature_version
    
    @signature_version.setter
    def signature_version(self,value: Optional[str] = None) -> None:
        """
        Sets the signatureVersion property value. Current malware definitions version
        Args:
            value: Value to set for the signatureVersion property.
        """
        self._signature_version = value
    
    @property
    def tamper_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the tamperProtectionEnabled property value. Indicates whether the Windows Defender tamper protection feature is enabled.
        Returns: Optional[bool]
        """
        return self._tamper_protection_enabled
    
    @tamper_protection_enabled.setter
    def tamper_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the tamperProtectionEnabled property value. Indicates whether the Windows Defender tamper protection feature is enabled.
        Args:
            value: Value to set for the tamperProtectionEnabled property.
        """
        self._tamper_protection_enabled = value
    

