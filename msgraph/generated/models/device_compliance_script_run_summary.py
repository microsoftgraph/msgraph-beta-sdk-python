from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceComplianceScriptRunSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceScriptRunSummary and sets the default values.
        """
        super().__init__()
        # Number of devices on which the detection script execution encountered an error and did not complete. Valid values -2147483648 to 2147483647
        self._detection_script_error_device_count: Optional[int] = None
        # Number of devices which have not yet run the latest version of the device compliance script. Valid values -2147483648 to 2147483647
        self._detection_script_pending_device_count: Optional[int] = None
        # Number of devices for which the detection script found an issue. Valid values -2147483648 to 2147483647
        self._issue_detected_device_count: Optional[int] = None
        # Last run time for the script across all devices
        self._last_script_run_date_time: Optional[datetime] = None
        # Number of devices for which the detection script did not find an issue and the device is healthy. Valid values -2147483648 to 2147483647
        self._no_issue_detected_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScriptRunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptRunSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScriptRunSummary()
    
    @property
    def detection_script_error_device_count(self,) -> Optional[int]:
        """
        Gets the detectionScriptErrorDeviceCount property value. Number of devices on which the detection script execution encountered an error and did not complete. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._detection_script_error_device_count
    
    @detection_script_error_device_count.setter
    def detection_script_error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the detectionScriptErrorDeviceCount property value. Number of devices on which the detection script execution encountered an error and did not complete. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the detectionScriptErrorDeviceCount property.
        """
        self._detection_script_error_device_count = value
    
    @property
    def detection_script_pending_device_count(self,) -> Optional[int]:
        """
        Gets the detectionScriptPendingDeviceCount property value. Number of devices which have not yet run the latest version of the device compliance script. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._detection_script_pending_device_count
    
    @detection_script_pending_device_count.setter
    def detection_script_pending_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the detectionScriptPendingDeviceCount property value. Number of devices which have not yet run the latest version of the device compliance script. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the detectionScriptPendingDeviceCount property.
        """
        self._detection_script_pending_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detection_script_error_device_count": lambda n : setattr(self, 'detection_script_error_device_count', n.get_int_value()),
            "detection_script_pending_device_count": lambda n : setattr(self, 'detection_script_pending_device_count', n.get_int_value()),
            "issue_detected_device_count": lambda n : setattr(self, 'issue_detected_device_count', n.get_int_value()),
            "last_script_run_date_time": lambda n : setattr(self, 'last_script_run_date_time', n.get_datetime_value()),
            "no_issue_detected_device_count": lambda n : setattr(self, 'no_issue_detected_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issue_detected_device_count(self,) -> Optional[int]:
        """
        Gets the issueDetectedDeviceCount property value. Number of devices for which the detection script found an issue. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._issue_detected_device_count
    
    @issue_detected_device_count.setter
    def issue_detected_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the issueDetectedDeviceCount property value. Number of devices for which the detection script found an issue. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the issueDetectedDeviceCount property.
        """
        self._issue_detected_device_count = value
    
    @property
    def last_script_run_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastScriptRunDateTime property value. Last run time for the script across all devices
        Returns: Optional[datetime]
        """
        return self._last_script_run_date_time
    
    @last_script_run_date_time.setter
    def last_script_run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastScriptRunDateTime property value. Last run time for the script across all devices
        Args:
            value: Value to set for the lastScriptRunDateTime property.
        """
        self._last_script_run_date_time = value
    
    @property
    def no_issue_detected_device_count(self,) -> Optional[int]:
        """
        Gets the noIssueDetectedDeviceCount property value. Number of devices for which the detection script did not find an issue and the device is healthy. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._no_issue_detected_device_count
    
    @no_issue_detected_device_count.setter
    def no_issue_detected_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the noIssueDetectedDeviceCount property value. Number of devices for which the detection script did not find an issue and the device is healthy. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the noIssueDetectedDeviceCount property.
        """
        self._no_issue_detected_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("detectionScriptErrorDeviceCount", self.detection_script_error_device_count)
        writer.write_int_value("detectionScriptPendingDeviceCount", self.detection_script_pending_device_count)
        writer.write_int_value("issueDetectedDeviceCount", self.issue_detected_device_count)
        writer.write_datetime_value("lastScriptRunDateTime", self.last_script_run_date_time)
        writer.write_int_value("noIssueDetectedDeviceCount", self.no_issue_detected_device_count)
    

