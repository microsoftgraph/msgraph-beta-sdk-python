from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_status, device_type, managed_device_owner_type, management_agent_type

@dataclass
class RetireScheduledManagedDevice(AdditionalDataHolder, Parsable):
    """
    ManagedDevices that are scheduled for retire
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The complianceState property
    compliance_state: Optional[compliance_status.ComplianceStatus] = None
    # Device Compliance PolicyId
    device_compliance_policy_id: Optional[str] = None
    # Device Compliance Policy Name
    device_compliance_policy_name: Optional[str] = None
    # Device type.
    device_type: Optional[device_type.DeviceType] = None
    # Key of the entity.
    id: Optional[str] = None
    # Managed DeviceId
    managed_device_id: Optional[str] = None
    # Managed Device Name
    managed_device_name: Optional[str] = None
    # Management agent type.
    management_agent: Optional[management_agent_type.ManagementAgentType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None
    # Managed Device Retire After DateTime
    retire_after_date_time: Optional[datetime] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetireScheduledManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetireScheduledManagedDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetireScheduledManagedDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_status, device_type, managed_device_owner_type, management_agent_type

        fields: Dict[str, Callable[[Any], None]] = {
            "complianceState": lambda n : setattr(self, 'compliance_state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "deviceCompliancePolicyId": lambda n : setattr(self, 'device_compliance_policy_id', n.get_str_value()),
            "deviceCompliancePolicyName": lambda n : setattr(self, 'device_compliance_policy_name', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(device_type.DeviceType)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "managementAgent": lambda n : setattr(self, 'management_agent', n.get_enum_value(management_agent_type.ManagementAgentType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(managed_device_owner_type.ManagedDeviceOwnerType)),
            "retireAfterDateTime": lambda n : setattr(self, 'retire_after_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("complianceState", self.compliance_state)
        writer.write_str_value("deviceCompliancePolicyId", self.device_compliance_policy_id)
        writer.write_str_value("deviceCompliancePolicyName", self.device_compliance_policy_name)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_str_value("id", self.id)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_enum_value("managementAgent", self.management_agent)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_datetime_value("retireAfterDateTime", self.retire_after_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_additional_data_value(self.additional_data)
    

