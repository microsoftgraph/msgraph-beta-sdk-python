from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceProtectionOverview(AdditionalDataHolder, Parsable):
    """
    Hardware information of a given device.
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
    def clean_device_count(self,) -> Optional[int]:
        """
        Gets the cleanDeviceCount property value. Clean device count.
        Returns: Optional[int]
        """
        return self._clean_device_count
    
    @clean_device_count.setter
    def clean_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the cleanDeviceCount property value. Clean device count.
        Args:
            value: Value to set for the cleanDeviceCount property.
        """
        self._clean_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceProtectionOverview and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Clean device count.
        self._clean_device_count: Optional[int] = None
        # Critical failures device count.
        self._critical_failures_device_count: Optional[int] = None
        # Device with inactive threat agent count
        self._inactive_threat_agent_device_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Pending full scan device count.
        self._pending_full_scan_device_count: Optional[int] = None
        # Pending manual steps device count.
        self._pending_manual_steps_device_count: Optional[int] = None
        # Pending offline scan device count.
        self._pending_offline_scan_device_count: Optional[int] = None
        # Pending quick scan device count. Valid values -2147483648 to 2147483647
        self._pending_quick_scan_device_count: Optional[int] = None
        # Pending restart device count.
        self._pending_restart_device_count: Optional[int] = None
        # Device with old signature count.
        self._pending_signature_update_device_count: Optional[int] = None
        # Total device count.
        self._total_reported_device_count: Optional[int] = None
        # Device with threat agent state as unknown count.
        self._unknown_state_threat_agent_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceProtectionOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceProtectionOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceProtectionOverview()
    
    @property
    def critical_failures_device_count(self,) -> Optional[int]:
        """
        Gets the criticalFailuresDeviceCount property value. Critical failures device count.
        Returns: Optional[int]
        """
        return self._critical_failures_device_count
    
    @critical_failures_device_count.setter
    def critical_failures_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the criticalFailuresDeviceCount property value. Critical failures device count.
        Args:
            value: Value to set for the criticalFailuresDeviceCount property.
        """
        self._critical_failures_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "clean_device_count": lambda n : setattr(self, 'clean_device_count', n.get_int_value()),
            "critical_failures_device_count": lambda n : setattr(self, 'critical_failures_device_count', n.get_int_value()),
            "inactive_threat_agent_device_count": lambda n : setattr(self, 'inactive_threat_agent_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pending_full_scan_device_count": lambda n : setattr(self, 'pending_full_scan_device_count', n.get_int_value()),
            "pending_manual_steps_device_count": lambda n : setattr(self, 'pending_manual_steps_device_count', n.get_int_value()),
            "pending_offline_scan_device_count": lambda n : setattr(self, 'pending_offline_scan_device_count', n.get_int_value()),
            "pending_quick_scan_device_count": lambda n : setattr(self, 'pending_quick_scan_device_count', n.get_int_value()),
            "pending_restart_device_count": lambda n : setattr(self, 'pending_restart_device_count', n.get_int_value()),
            "pending_signature_update_device_count": lambda n : setattr(self, 'pending_signature_update_device_count', n.get_int_value()),
            "total_reported_device_count": lambda n : setattr(self, 'total_reported_device_count', n.get_int_value()),
            "unknown_state_threat_agent_device_count": lambda n : setattr(self, 'unknown_state_threat_agent_device_count', n.get_int_value()),
        }
        return fields
    
    @property
    def inactive_threat_agent_device_count(self,) -> Optional[int]:
        """
        Gets the inactiveThreatAgentDeviceCount property value. Device with inactive threat agent count
        Returns: Optional[int]
        """
        return self._inactive_threat_agent_device_count
    
    @inactive_threat_agent_device_count.setter
    def inactive_threat_agent_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the inactiveThreatAgentDeviceCount property value. Device with inactive threat agent count
        Args:
            value: Value to set for the inactiveThreatAgentDeviceCount property.
        """
        self._inactive_threat_agent_device_count = value
    
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
    def pending_full_scan_device_count(self,) -> Optional[int]:
        """
        Gets the pendingFullScanDeviceCount property value. Pending full scan device count.
        Returns: Optional[int]
        """
        return self._pending_full_scan_device_count
    
    @pending_full_scan_device_count.setter
    def pending_full_scan_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingFullScanDeviceCount property value. Pending full scan device count.
        Args:
            value: Value to set for the pendingFullScanDeviceCount property.
        """
        self._pending_full_scan_device_count = value
    
    @property
    def pending_manual_steps_device_count(self,) -> Optional[int]:
        """
        Gets the pendingManualStepsDeviceCount property value. Pending manual steps device count.
        Returns: Optional[int]
        """
        return self._pending_manual_steps_device_count
    
    @pending_manual_steps_device_count.setter
    def pending_manual_steps_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingManualStepsDeviceCount property value. Pending manual steps device count.
        Args:
            value: Value to set for the pendingManualStepsDeviceCount property.
        """
        self._pending_manual_steps_device_count = value
    
    @property
    def pending_offline_scan_device_count(self,) -> Optional[int]:
        """
        Gets the pendingOfflineScanDeviceCount property value. Pending offline scan device count.
        Returns: Optional[int]
        """
        return self._pending_offline_scan_device_count
    
    @pending_offline_scan_device_count.setter
    def pending_offline_scan_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingOfflineScanDeviceCount property value. Pending offline scan device count.
        Args:
            value: Value to set for the pendingOfflineScanDeviceCount property.
        """
        self._pending_offline_scan_device_count = value
    
    @property
    def pending_quick_scan_device_count(self,) -> Optional[int]:
        """
        Gets the pendingQuickScanDeviceCount property value. Pending quick scan device count. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._pending_quick_scan_device_count
    
    @pending_quick_scan_device_count.setter
    def pending_quick_scan_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingQuickScanDeviceCount property value. Pending quick scan device count. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the pendingQuickScanDeviceCount property.
        """
        self._pending_quick_scan_device_count = value
    
    @property
    def pending_restart_device_count(self,) -> Optional[int]:
        """
        Gets the pendingRestartDeviceCount property value. Pending restart device count.
        Returns: Optional[int]
        """
        return self._pending_restart_device_count
    
    @pending_restart_device_count.setter
    def pending_restart_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingRestartDeviceCount property value. Pending restart device count.
        Args:
            value: Value to set for the pendingRestartDeviceCount property.
        """
        self._pending_restart_device_count = value
    
    @property
    def pending_signature_update_device_count(self,) -> Optional[int]:
        """
        Gets the pendingSignatureUpdateDeviceCount property value. Device with old signature count.
        Returns: Optional[int]
        """
        return self._pending_signature_update_device_count
    
    @pending_signature_update_device_count.setter
    def pending_signature_update_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingSignatureUpdateDeviceCount property value. Device with old signature count.
        Args:
            value: Value to set for the pendingSignatureUpdateDeviceCount property.
        """
        self._pending_signature_update_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("cleanDeviceCount", self.clean_device_count)
        writer.write_int_value("criticalFailuresDeviceCount", self.critical_failures_device_count)
        writer.write_int_value("inactiveThreatAgentDeviceCount", self.inactive_threat_agent_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingFullScanDeviceCount", self.pending_full_scan_device_count)
        writer.write_int_value("pendingManualStepsDeviceCount", self.pending_manual_steps_device_count)
        writer.write_int_value("pendingOfflineScanDeviceCount", self.pending_offline_scan_device_count)
        writer.write_int_value("pendingQuickScanDeviceCount", self.pending_quick_scan_device_count)
        writer.write_int_value("pendingRestartDeviceCount", self.pending_restart_device_count)
        writer.write_int_value("pendingSignatureUpdateDeviceCount", self.pending_signature_update_device_count)
        writer.write_int_value("totalReportedDeviceCount", self.total_reported_device_count)
        writer.write_int_value("unknownStateThreatAgentDeviceCount", self.unknown_state_threat_agent_device_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_reported_device_count(self,) -> Optional[int]:
        """
        Gets the totalReportedDeviceCount property value. Total device count.
        Returns: Optional[int]
        """
        return self._total_reported_device_count
    
    @total_reported_device_count.setter
    def total_reported_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalReportedDeviceCount property value. Total device count.
        Args:
            value: Value to set for the totalReportedDeviceCount property.
        """
        self._total_reported_device_count = value
    
    @property
    def unknown_state_threat_agent_device_count(self,) -> Optional[int]:
        """
        Gets the unknownStateThreatAgentDeviceCount property value. Device with threat agent state as unknown count.
        Returns: Optional[int]
        """
        return self._unknown_state_threat_agent_device_count
    
    @unknown_state_threat_agent_device_count.setter
    def unknown_state_threat_agent_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownStateThreatAgentDeviceCount property value. Device with threat agent state as unknown count.
        Args:
            value: Value to set for the unknownStateThreatAgentDeviceCount property.
        """
        self._unknown_state_threat_agent_device_count = value
    

