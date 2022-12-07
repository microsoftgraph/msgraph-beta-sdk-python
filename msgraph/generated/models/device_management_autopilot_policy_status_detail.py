from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_autopilot_policy_compliance_status = lazy_import('msgraph.generated.models.device_management_autopilot_policy_compliance_status')
device_management_autopilot_policy_type = lazy_import('msgraph.generated.models.device_management_autopilot_policy_type')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementAutopilotPolicyStatusDetail(entity.Entity):
    """
    Policy status detail item contained by an autopilot event.
    """
    @property
    def compliance_status(self,) -> Optional[device_management_autopilot_policy_compliance_status.DeviceManagementAutopilotPolicyComplianceStatus]:
        """
        Gets the complianceStatus property value. The complianceStatus property
        Returns: Optional[device_management_autopilot_policy_compliance_status.DeviceManagementAutopilotPolicyComplianceStatus]
        """
        return self._compliance_status
    
    @compliance_status.setter
    def compliance_status(self,value: Optional[device_management_autopilot_policy_compliance_status.DeviceManagementAutopilotPolicyComplianceStatus] = None) -> None:
        """
        Sets the complianceStatus property value. The complianceStatus property
        Args:
            value: Value to set for the complianceStatus property.
        """
        self._compliance_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementAutopilotPolicyStatusDetail and sets the default values.
        """
        super().__init__()
        # The complianceStatus property
        self._compliance_status: Optional[device_management_autopilot_policy_compliance_status.DeviceManagementAutopilotPolicyComplianceStatus] = None
        # The friendly name of the policy.
        self._display_name: Optional[str] = None
        # The errorode associated with the compliance or enforcement status of the policy. Error code for enforcement status takes precedence if it exists.
        self._error_code: Optional[int] = None
        # Timestamp of the reported policy status
        self._last_reported_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policyType property
        self._policy_type: Optional[device_management_autopilot_policy_type.DeviceManagementAutopilotPolicyType] = None
        # Indicates if this prolicy was tracked as part of the autopilot bootstrap enrollment sync session
        self._tracked_on_enrollment_status: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementAutopilotPolicyStatusDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAutopilotPolicyStatusDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementAutopilotPolicyStatusDetail()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The friendly name of the policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The friendly name of the policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. The errorode associated with the compliance or enforcement status of the policy. Error code for enforcement status takes precedence if it exists.
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. The errorode associated with the compliance or enforcement status of the policy. Error code for enforcement status takes precedence if it exists.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_status": lambda n : setattr(self, 'compliance_status', n.get_enum_value(device_management_autopilot_policy_compliance_status.DeviceManagementAutopilotPolicyComplianceStatus)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "policy_type": lambda n : setattr(self, 'policy_type', n.get_enum_value(device_management_autopilot_policy_type.DeviceManagementAutopilotPolicyType)),
            "tracked_on_enrollment_status": lambda n : setattr(self, 'tracked_on_enrollment_status', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. Timestamp of the reported policy status
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. Timestamp of the reported policy status
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    @property
    def policy_type(self,) -> Optional[device_management_autopilot_policy_type.DeviceManagementAutopilotPolicyType]:
        """
        Gets the policyType property value. The policyType property
        Returns: Optional[device_management_autopilot_policy_type.DeviceManagementAutopilotPolicyType]
        """
        return self._policy_type
    
    @policy_type.setter
    def policy_type(self,value: Optional[device_management_autopilot_policy_type.DeviceManagementAutopilotPolicyType] = None) -> None:
        """
        Sets the policyType property value. The policyType property
        Args:
            value: Value to set for the policyType property.
        """
        self._policy_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("complianceStatus", self.compliance_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_bool_value("trackedOnEnrollmentStatus", self.tracked_on_enrollment_status)
    
    @property
    def tracked_on_enrollment_status(self,) -> Optional[bool]:
        """
        Gets the trackedOnEnrollmentStatus property value. Indicates if this prolicy was tracked as part of the autopilot bootstrap enrollment sync session
        Returns: Optional[bool]
        """
        return self._tracked_on_enrollment_status
    
    @tracked_on_enrollment_status.setter
    def tracked_on_enrollment_status(self,value: Optional[bool] = None) -> None:
        """
        Sets the trackedOnEnrollmentStatus property value. Indicates if this prolicy was tracked as part of the autopilot bootstrap enrollment sync session
        Args:
            value: Value to set for the trackedOnEnrollmentStatus property.
        """
        self._tracked_on_enrollment_status = value
    

