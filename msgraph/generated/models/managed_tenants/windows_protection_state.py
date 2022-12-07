from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsProtectionState(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def anti_malware_version(self,) -> Optional[str]:
        """
        Gets the antiMalwareVersion property value. The anti-malware version for the managed device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._anti_malware_version
    
    @anti_malware_version.setter
    def anti_malware_version(self,value: Optional[str] = None) -> None:
        """
        Sets the antiMalwareVersion property value. The anti-malware version for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the antiMalwareVersion property.
        """
        self._anti_malware_version = value
    
    @property
    def attention_required(self,) -> Optional[bool]:
        """
        Gets the attentionRequired property value. A flag indicating whether attention is required for the managed device. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._attention_required
    
    @attention_required.setter
    def attention_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the attentionRequired property value. A flag indicating whether attention is required for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the attentionRequired property.
        """
        self._attention_required = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsProtectionState and sets the default values.
        """
        super().__init__()
        # The anti-malware version for the managed device. Optional. Read-only.
        self._anti_malware_version: Optional[str] = None
        # A flag indicating whether attention is required for the managed device. Optional. Read-only.
        self._attention_required: Optional[bool] = None
        # A flag indicating whether the managed device has been deleted. Optional. Read-only.
        self._device_deleted: Optional[bool] = None
        # The date and time the device property has been refreshed. Optional. Read-only.
        self._device_property_refresh_date_time: Optional[datetime] = None
        # The anti-virus engine version for the managed device. Optional. Read-only.
        self._engine_version: Optional[str] = None
        # A flag indicating whether quick scan is overdue for the managed device. Optional. Read-only.
        self._full_scan_overdue: Optional[bool] = None
        # A flag indicating whether full scan is overdue for the managed device. Optional. Read-only.
        self._full_scan_required: Optional[bool] = None
        # The date and time a full scan was completed. Optional. Read-only.
        self._last_full_scan_date_time: Optional[datetime] = None
        # The version anti-malware version used to perform the last full scan. Optional. Read-only.
        self._last_full_scan_signature_version: Optional[str] = None
        # The date and time a quick scan was completed. Optional. Read-only.
        self._last_quick_scan_date_time: Optional[datetime] = None
        # The version anti-malware version used to perform the last full scan. Optional. Read-only.
        self._last_quick_scan_signature_version: Optional[str] = None
        # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The date and time the protection state was last reported for the managed device. Optional. Read-only.
        self._last_reported_date_time: Optional[datetime] = None
        # A flag indicating whether malware protection is enabled for the managed device. Optional. Read-only.
        self._malware_protection_enabled: Optional[bool] = None
        # The health state for the managed device. Optional. Read-only.
        self._managed_device_health_state: Optional[str] = None
        # The unique identifier for the managed device. Optional. Read-only.
        self._managed_device_id: Optional[str] = None
        # The display name for the managed device. Optional. Read-only.
        self._managed_device_name: Optional[str] = None
        # A flag indicating whether the network inspection system is enabled. Optional. Read-only.
        self._network_inspection_system_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A flag indicating weather a quick scan is overdue. Optional. Read-only.
        self._quick_scan_overdue: Optional[bool] = None
        # A flag indicating whether real time protection is enabled. Optional. Read-only.
        self._real_time_protection_enabled: Optional[bool] = None
        # A flag indicating whether a reboot is required. Optional. Read-only.
        self._reboot_required: Optional[bool] = None
        # A flag indicating whether an signature update is overdue. Optional. Read-only.
        self._signature_update_overdue: Optional[bool] = None
        # The signature version for the managed device. Optional. Read-only.
        self._signature_version: Optional[str] = None
        # The display name for the managed tenant. Optional. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        self._tenant_id: Optional[str] = None
    
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
    def device_deleted(self,) -> Optional[bool]:
        """
        Gets the deviceDeleted property value. A flag indicating whether the managed device has been deleted. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._device_deleted
    
    @device_deleted.setter
    def device_deleted(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceDeleted property value. A flag indicating whether the managed device has been deleted. Optional. Read-only.
        Args:
            value: Value to set for the deviceDeleted property.
        """
        self._device_deleted = value
    
    @property
    def device_property_refresh_date_time(self,) -> Optional[datetime]:
        """
        Gets the devicePropertyRefreshDateTime property value. The date and time the device property has been refreshed. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._device_property_refresh_date_time
    
    @device_property_refresh_date_time.setter
    def device_property_refresh_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the devicePropertyRefreshDateTime property value. The date and time the device property has been refreshed. Optional. Read-only.
        Args:
            value: Value to set for the devicePropertyRefreshDateTime property.
        """
        self._device_property_refresh_date_time = value
    
    @property
    def engine_version(self,) -> Optional[str]:
        """
        Gets the engineVersion property value. The anti-virus engine version for the managed device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._engine_version
    
    @engine_version.setter
    def engine_version(self,value: Optional[str] = None) -> None:
        """
        Sets the engineVersion property value. The anti-virus engine version for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the engineVersion property.
        """
        self._engine_version = value
    
    @property
    def full_scan_overdue(self,) -> Optional[bool]:
        """
        Gets the fullScanOverdue property value. A flag indicating whether quick scan is overdue for the managed device. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._full_scan_overdue
    
    @full_scan_overdue.setter
    def full_scan_overdue(self,value: Optional[bool] = None) -> None:
        """
        Sets the fullScanOverdue property value. A flag indicating whether quick scan is overdue for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the fullScanOverdue property.
        """
        self._full_scan_overdue = value
    
    @property
    def full_scan_required(self,) -> Optional[bool]:
        """
        Gets the fullScanRequired property value. A flag indicating whether full scan is overdue for the managed device. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._full_scan_required
    
    @full_scan_required.setter
    def full_scan_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the fullScanRequired property value. A flag indicating whether full scan is overdue for the managed device. Optional. Read-only.
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
            "attention_required": lambda n : setattr(self, 'attention_required', n.get_bool_value()),
            "device_deleted": lambda n : setattr(self, 'device_deleted', n.get_bool_value()),
            "device_property_refresh_date_time": lambda n : setattr(self, 'device_property_refresh_date_time', n.get_datetime_value()),
            "engine_version": lambda n : setattr(self, 'engine_version', n.get_str_value()),
            "full_scan_overdue": lambda n : setattr(self, 'full_scan_overdue', n.get_bool_value()),
            "full_scan_required": lambda n : setattr(self, 'full_scan_required', n.get_bool_value()),
            "last_full_scan_date_time": lambda n : setattr(self, 'last_full_scan_date_time', n.get_datetime_value()),
            "last_full_scan_signature_version": lambda n : setattr(self, 'last_full_scan_signature_version', n.get_str_value()),
            "last_quick_scan_date_time": lambda n : setattr(self, 'last_quick_scan_date_time', n.get_datetime_value()),
            "last_quick_scan_signature_version": lambda n : setattr(self, 'last_quick_scan_signature_version', n.get_str_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malware_protection_enabled": lambda n : setattr(self, 'malware_protection_enabled', n.get_bool_value()),
            "managed_device_health_state": lambda n : setattr(self, 'managed_device_health_state', n.get_str_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managed_device_name": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "network_inspection_system_enabled": lambda n : setattr(self, 'network_inspection_system_enabled', n.get_bool_value()),
            "quick_scan_overdue": lambda n : setattr(self, 'quick_scan_overdue', n.get_bool_value()),
            "real_time_protection_enabled": lambda n : setattr(self, 'real_time_protection_enabled', n.get_bool_value()),
            "reboot_required": lambda n : setattr(self, 'reboot_required', n.get_bool_value()),
            "signature_update_overdue": lambda n : setattr(self, 'signature_update_overdue', n.get_bool_value()),
            "signature_version": lambda n : setattr(self, 'signature_version', n.get_str_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_full_scan_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastFullScanDateTime property value. The date and time a full scan was completed. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_full_scan_date_time
    
    @last_full_scan_date_time.setter
    def last_full_scan_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastFullScanDateTime property value. The date and time a full scan was completed. Optional. Read-only.
        Args:
            value: Value to set for the lastFullScanDateTime property.
        """
        self._last_full_scan_date_time = value
    
    @property
    def last_full_scan_signature_version(self,) -> Optional[str]:
        """
        Gets the lastFullScanSignatureVersion property value. The version anti-malware version used to perform the last full scan. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._last_full_scan_signature_version
    
    @last_full_scan_signature_version.setter
    def last_full_scan_signature_version(self,value: Optional[str] = None) -> None:
        """
        Sets the lastFullScanSignatureVersion property value. The version anti-malware version used to perform the last full scan. Optional. Read-only.
        Args:
            value: Value to set for the lastFullScanSignatureVersion property.
        """
        self._last_full_scan_signature_version = value
    
    @property
    def last_quick_scan_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastQuickScanDateTime property value. The date and time a quick scan was completed. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_quick_scan_date_time
    
    @last_quick_scan_date_time.setter
    def last_quick_scan_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastQuickScanDateTime property value. The date and time a quick scan was completed. Optional. Read-only.
        Args:
            value: Value to set for the lastQuickScanDateTime property.
        """
        self._last_quick_scan_date_time = value
    
    @property
    def last_quick_scan_signature_version(self,) -> Optional[str]:
        """
        Gets the lastQuickScanSignatureVersion property value. The version anti-malware version used to perform the last full scan. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._last_quick_scan_signature_version
    
    @last_quick_scan_signature_version.setter
    def last_quick_scan_signature_version(self,value: Optional[str] = None) -> None:
        """
        Sets the lastQuickScanSignatureVersion property value. The version anti-malware version used to perform the last full scan. Optional. Read-only.
        Args:
            value: Value to set for the lastQuickScanSignatureVersion property.
        """
        self._last_quick_scan_signature_version = value
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        Args:
            value: Value to set for the lastRefreshedDateTime property.
        """
        self._last_refreshed_date_time = value
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. The date and time the protection state was last reported for the managed device. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. The date and time the protection state was last reported for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    @property
    def malware_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the malwareProtectionEnabled property value. A flag indicating whether malware protection is enabled for the managed device. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._malware_protection_enabled
    
    @malware_protection_enabled.setter
    def malware_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the malwareProtectionEnabled property value. A flag indicating whether malware protection is enabled for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the malwareProtectionEnabled property.
        """
        self._malware_protection_enabled = value
    
    @property
    def managed_device_health_state(self,) -> Optional[str]:
        """
        Gets the managedDeviceHealthState property value. The health state for the managed device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._managed_device_health_state
    
    @managed_device_health_state.setter
    def managed_device_health_state(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceHealthState property value. The health state for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the managedDeviceHealthState property.
        """
        self._managed_device_health_state = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The unique identifier for the managed device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The unique identifier for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. The display name for the managed device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. The display name for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the managedDeviceName property.
        """
        self._managed_device_name = value
    
    @property
    def network_inspection_system_enabled(self,) -> Optional[bool]:
        """
        Gets the networkInspectionSystemEnabled property value. A flag indicating whether the network inspection system is enabled. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._network_inspection_system_enabled
    
    @network_inspection_system_enabled.setter
    def network_inspection_system_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the networkInspectionSystemEnabled property value. A flag indicating whether the network inspection system is enabled. Optional. Read-only.
        Args:
            value: Value to set for the networkInspectionSystemEnabled property.
        """
        self._network_inspection_system_enabled = value
    
    @property
    def quick_scan_overdue(self,) -> Optional[bool]:
        """
        Gets the quickScanOverdue property value. A flag indicating weather a quick scan is overdue. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._quick_scan_overdue
    
    @quick_scan_overdue.setter
    def quick_scan_overdue(self,value: Optional[bool] = None) -> None:
        """
        Sets the quickScanOverdue property value. A flag indicating weather a quick scan is overdue. Optional. Read-only.
        Args:
            value: Value to set for the quickScanOverdue property.
        """
        self._quick_scan_overdue = value
    
    @property
    def real_time_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the realTimeProtectionEnabled property value. A flag indicating whether real time protection is enabled. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._real_time_protection_enabled
    
    @real_time_protection_enabled.setter
    def real_time_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the realTimeProtectionEnabled property value. A flag indicating whether real time protection is enabled. Optional. Read-only.
        Args:
            value: Value to set for the realTimeProtectionEnabled property.
        """
        self._real_time_protection_enabled = value
    
    @property
    def reboot_required(self,) -> Optional[bool]:
        """
        Gets the rebootRequired property value. A flag indicating whether a reboot is required. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._reboot_required
    
    @reboot_required.setter
    def reboot_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the rebootRequired property value. A flag indicating whether a reboot is required. Optional. Read-only.
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
        writer.write_bool_value("attentionRequired", self.attention_required)
        writer.write_bool_value("deviceDeleted", self.device_deleted)
        writer.write_datetime_value("devicePropertyRefreshDateTime", self.device_property_refresh_date_time)
        writer.write_str_value("engineVersion", self.engine_version)
        writer.write_bool_value("fullScanOverdue", self.full_scan_overdue)
        writer.write_bool_value("fullScanRequired", self.full_scan_required)
        writer.write_datetime_value("lastFullScanDateTime", self.last_full_scan_date_time)
        writer.write_str_value("lastFullScanSignatureVersion", self.last_full_scan_signature_version)
        writer.write_datetime_value("lastQuickScanDateTime", self.last_quick_scan_date_time)
        writer.write_str_value("lastQuickScanSignatureVersion", self.last_quick_scan_signature_version)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_bool_value("malwareProtectionEnabled", self.malware_protection_enabled)
        writer.write_str_value("managedDeviceHealthState", self.managed_device_health_state)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_bool_value("networkInspectionSystemEnabled", self.network_inspection_system_enabled)
        writer.write_bool_value("quickScanOverdue", self.quick_scan_overdue)
        writer.write_bool_value("realTimeProtectionEnabled", self.real_time_protection_enabled)
        writer.write_bool_value("rebootRequired", self.reboot_required)
        writer.write_bool_value("signatureUpdateOverdue", self.signature_update_overdue)
        writer.write_str_value("signatureVersion", self.signature_version)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def signature_update_overdue(self,) -> Optional[bool]:
        """
        Gets the signatureUpdateOverdue property value. A flag indicating whether an signature update is overdue. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._signature_update_overdue
    
    @signature_update_overdue.setter
    def signature_update_overdue(self,value: Optional[bool] = None) -> None:
        """
        Sets the signatureUpdateOverdue property value. A flag indicating whether an signature update is overdue. Optional. Read-only.
        Args:
            value: Value to set for the signatureUpdateOverdue property.
        """
        self._signature_update_overdue = value
    
    @property
    def signature_version(self,) -> Optional[str]:
        """
        Gets the signatureVersion property value. The signature version for the managed device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._signature_version
    
    @signature_version.setter
    def signature_version(self,value: Optional[str] = None) -> None:
        """
        Sets the signatureVersion property value. The signature version for the managed device. Optional. Read-only.
        Args:
            value: Value to set for the signatureVersion property.
        """
        self._signature_version = value
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The display name for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The display name for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenantDisplayName property.
        """
        self._tenant_display_name = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

