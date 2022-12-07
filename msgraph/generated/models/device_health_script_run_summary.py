from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceHealthScriptRunSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScriptRunSummary and sets the default values.
        """
        super().__init__()
        # Number of devices on which the detection script execution encountered an error and did not complete
        self._detection_script_error_device_count: Optional[int] = None
        # Number of devices for which the detection script was not applicable
        self._detection_script_not_applicable_device_count: Optional[int] = None
        # Number of devices which have not yet run the latest version of the device health script
        self._detection_script_pending_device_count: Optional[int] = None
        # Number of devices for which the detection script found an issue
        self._issue_detected_device_count: Optional[int] = None
        # Number of devices that were remediated over the last 30 days
        self._issue_remediated_cumulative_device_count: Optional[int] = None
        # Number of devices for which the remediation script was able to resolve the detected issue
        self._issue_remediated_device_count: Optional[int] = None
        # Number of devices for which the remediation script executed successfully but failed to resolve the detected issue
        self._issue_reoccurred_device_count: Optional[int] = None
        # Last run time for the script across all devices
        self._last_script_run_date_time: Optional[datetime] = None
        # Number of devices for which the detection script did not find an issue and the device is healthy
        self._no_issue_detected_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of devices for which the remediation script execution encountered an error and did not complete
        self._remediation_script_error_device_count: Optional[int] = None
        # Number of devices for which remediation was skipped
        self._remediation_skipped_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptRunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRunSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptRunSummary()
    
    @property
    def detection_script_error_device_count(self,) -> Optional[int]:
        """
        Gets the detectionScriptErrorDeviceCount property value. Number of devices on which the detection script execution encountered an error and did not complete
        Returns: Optional[int]
        """
        return self._detection_script_error_device_count
    
    @detection_script_error_device_count.setter
    def detection_script_error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the detectionScriptErrorDeviceCount property value. Number of devices on which the detection script execution encountered an error and did not complete
        Args:
            value: Value to set for the detectionScriptErrorDeviceCount property.
        """
        self._detection_script_error_device_count = value
    
    @property
    def detection_script_not_applicable_device_count(self,) -> Optional[int]:
        """
        Gets the detectionScriptNotApplicableDeviceCount property value. Number of devices for which the detection script was not applicable
        Returns: Optional[int]
        """
        return self._detection_script_not_applicable_device_count
    
    @detection_script_not_applicable_device_count.setter
    def detection_script_not_applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the detectionScriptNotApplicableDeviceCount property value. Number of devices for which the detection script was not applicable
        Args:
            value: Value to set for the detectionScriptNotApplicableDeviceCount property.
        """
        self._detection_script_not_applicable_device_count = value
    
    @property
    def detection_script_pending_device_count(self,) -> Optional[int]:
        """
        Gets the detectionScriptPendingDeviceCount property value. Number of devices which have not yet run the latest version of the device health script
        Returns: Optional[int]
        """
        return self._detection_script_pending_device_count
    
    @detection_script_pending_device_count.setter
    def detection_script_pending_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the detectionScriptPendingDeviceCount property value. Number of devices which have not yet run the latest version of the device health script
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
            "detection_script_not_applicable_device_count": lambda n : setattr(self, 'detection_script_not_applicable_device_count', n.get_int_value()),
            "detection_script_pending_device_count": lambda n : setattr(self, 'detection_script_pending_device_count', n.get_int_value()),
            "issue_detected_device_count": lambda n : setattr(self, 'issue_detected_device_count', n.get_int_value()),
            "issue_remediated_cumulative_device_count": lambda n : setattr(self, 'issue_remediated_cumulative_device_count', n.get_int_value()),
            "issue_remediated_device_count": lambda n : setattr(self, 'issue_remediated_device_count', n.get_int_value()),
            "issue_reoccurred_device_count": lambda n : setattr(self, 'issue_reoccurred_device_count', n.get_int_value()),
            "last_script_run_date_time": lambda n : setattr(self, 'last_script_run_date_time', n.get_datetime_value()),
            "no_issue_detected_device_count": lambda n : setattr(self, 'no_issue_detected_device_count', n.get_int_value()),
            "remediation_script_error_device_count": lambda n : setattr(self, 'remediation_script_error_device_count', n.get_int_value()),
            "remediation_skipped_device_count": lambda n : setattr(self, 'remediation_skipped_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issue_detected_device_count(self,) -> Optional[int]:
        """
        Gets the issueDetectedDeviceCount property value. Number of devices for which the detection script found an issue
        Returns: Optional[int]
        """
        return self._issue_detected_device_count
    
    @issue_detected_device_count.setter
    def issue_detected_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the issueDetectedDeviceCount property value. Number of devices for which the detection script found an issue
        Args:
            value: Value to set for the issueDetectedDeviceCount property.
        """
        self._issue_detected_device_count = value
    
    @property
    def issue_remediated_cumulative_device_count(self,) -> Optional[int]:
        """
        Gets the issueRemediatedCumulativeDeviceCount property value. Number of devices that were remediated over the last 30 days
        Returns: Optional[int]
        """
        return self._issue_remediated_cumulative_device_count
    
    @issue_remediated_cumulative_device_count.setter
    def issue_remediated_cumulative_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the issueRemediatedCumulativeDeviceCount property value. Number of devices that were remediated over the last 30 days
        Args:
            value: Value to set for the issueRemediatedCumulativeDeviceCount property.
        """
        self._issue_remediated_cumulative_device_count = value
    
    @property
    def issue_remediated_device_count(self,) -> Optional[int]:
        """
        Gets the issueRemediatedDeviceCount property value. Number of devices for which the remediation script was able to resolve the detected issue
        Returns: Optional[int]
        """
        return self._issue_remediated_device_count
    
    @issue_remediated_device_count.setter
    def issue_remediated_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the issueRemediatedDeviceCount property value. Number of devices for which the remediation script was able to resolve the detected issue
        Args:
            value: Value to set for the issueRemediatedDeviceCount property.
        """
        self._issue_remediated_device_count = value
    
    @property
    def issue_reoccurred_device_count(self,) -> Optional[int]:
        """
        Gets the issueReoccurredDeviceCount property value. Number of devices for which the remediation script executed successfully but failed to resolve the detected issue
        Returns: Optional[int]
        """
        return self._issue_reoccurred_device_count
    
    @issue_reoccurred_device_count.setter
    def issue_reoccurred_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the issueReoccurredDeviceCount property value. Number of devices for which the remediation script executed successfully but failed to resolve the detected issue
        Args:
            value: Value to set for the issueReoccurredDeviceCount property.
        """
        self._issue_reoccurred_device_count = value
    
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
        Gets the noIssueDetectedDeviceCount property value. Number of devices for which the detection script did not find an issue and the device is healthy
        Returns: Optional[int]
        """
        return self._no_issue_detected_device_count
    
    @no_issue_detected_device_count.setter
    def no_issue_detected_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the noIssueDetectedDeviceCount property value. Number of devices for which the detection script did not find an issue and the device is healthy
        Args:
            value: Value to set for the noIssueDetectedDeviceCount property.
        """
        self._no_issue_detected_device_count = value
    
    @property
    def remediation_script_error_device_count(self,) -> Optional[int]:
        """
        Gets the remediationScriptErrorDeviceCount property value. Number of devices for which the remediation script execution encountered an error and did not complete
        Returns: Optional[int]
        """
        return self._remediation_script_error_device_count
    
    @remediation_script_error_device_count.setter
    def remediation_script_error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediationScriptErrorDeviceCount property value. Number of devices for which the remediation script execution encountered an error and did not complete
        Args:
            value: Value to set for the remediationScriptErrorDeviceCount property.
        """
        self._remediation_script_error_device_count = value
    
    @property
    def remediation_skipped_device_count(self,) -> Optional[int]:
        """
        Gets the remediationSkippedDeviceCount property value. Number of devices for which remediation was skipped
        Returns: Optional[int]
        """
        return self._remediation_skipped_device_count
    
    @remediation_skipped_device_count.setter
    def remediation_skipped_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediationSkippedDeviceCount property value. Number of devices for which remediation was skipped
        Args:
            value: Value to set for the remediationSkippedDeviceCount property.
        """
        self._remediation_skipped_device_count = value
    
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
        writer.write_int_value("detectionScriptNotApplicableDeviceCount", self.detection_script_not_applicable_device_count)
        writer.write_int_value("detectionScriptPendingDeviceCount", self.detection_script_pending_device_count)
        writer.write_int_value("issueDetectedDeviceCount", self.issue_detected_device_count)
        writer.write_int_value("issueRemediatedCumulativeDeviceCount", self.issue_remediated_cumulative_device_count)
        writer.write_int_value("issueRemediatedDeviceCount", self.issue_remediated_device_count)
        writer.write_int_value("issueReoccurredDeviceCount", self.issue_reoccurred_device_count)
        writer.write_datetime_value("lastScriptRunDateTime", self.last_script_run_date_time)
        writer.write_int_value("noIssueDetectedDeviceCount", self.no_issue_detected_device_count)
        writer.write_int_value("remediationScriptErrorDeviceCount", self.remediation_script_error_device_count)
        writer.write_int_value("remediationSkippedDeviceCount", self.remediation_skipped_device_count)
    

