from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .device_type import DeviceType
    from .managed_device_owner_type import ManagedDeviceOwnerType
    from .management_agent_type import ManagementAgentType

@dataclass
class RetireScheduledManagedDevice(AdditionalDataHolder, BackedModel, Parsable):
    """
    ManagedDevices that are scheduled for retire
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The complianceState property
    compliance_state: Optional[ComplianceStatus] = None
    # Device Compliance PolicyId
    device_compliance_policy_id: Optional[str] = None
    # Device Compliance Policy Name
    device_compliance_policy_name: Optional[str] = None
    # Device type.
    device_type: Optional[DeviceType] = None
    # Key of the entity.
    id: Optional[str] = None
    # Managed DeviceId
    managed_device_id: Optional[str] = None
    # Managed Device Name
    managed_device_name: Optional[str] = None
    # Management agent type.
    management_agent: Optional[ManagementAgentType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[ManagedDeviceOwnerType] = None
    # Managed Device Retire After DateTime
    retire_after_date_time: Optional[datetime.datetime] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetireScheduledManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetireScheduledManagedDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetireScheduledManagedDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .device_type import DeviceType
        from .managed_device_owner_type import ManagedDeviceOwnerType
        from .management_agent_type import ManagementAgentType

        from .compliance_status import ComplianceStatus
        from .device_type import DeviceType
        from .managed_device_owner_type import ManagedDeviceOwnerType
        from .management_agent_type import ManagementAgentType

        fields: Dict[str, Callable[[Any], None]] = {
            "complianceState": lambda n : setattr(self, 'compliance_state', n.get_enum_value(ComplianceStatus)),
            "deviceCompliancePolicyId": lambda n : setattr(self, 'device_compliance_policy_id', n.get_str_value()),
            "deviceCompliancePolicyName": lambda n : setattr(self, 'device_compliance_policy_name', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(DeviceType)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "managementAgent": lambda n : setattr(self, 'management_agent', n.get_enum_value(ManagementAgentType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(ManagedDeviceOwnerType)),
            "retireAfterDateTime": lambda n : setattr(self, 'retire_after_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

