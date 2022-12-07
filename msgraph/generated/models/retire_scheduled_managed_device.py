from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_status = lazy_import('msgraph.generated.models.compliance_status')
device_type = lazy_import('msgraph.generated.models.device_type')
managed_device_owner_type = lazy_import('msgraph.generated.models.managed_device_owner_type')
management_agent_type = lazy_import('msgraph.generated.models.management_agent_type')

class RetireScheduledManagedDevice(AdditionalDataHolder, Parsable):
    """
    ManagedDevices that are scheduled for retire
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
    def compliance_state(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the complianceState property value. The complianceState property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._compliance_state
    
    @compliance_state.setter
    def compliance_state(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the complianceState property value. The complianceState property
        Args:
            value: Value to set for the complianceState property.
        """
        self._compliance_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new retireScheduledManagedDevice and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The complianceState property
        self._compliance_state: Optional[compliance_status.ComplianceStatus] = None
        # Device Compliance PolicyId
        self._device_compliance_policy_id: Optional[str] = None
        # Device Compliance Policy Name
        self._device_compliance_policy_name: Optional[str] = None
        # Device type.
        self._device_type: Optional[device_type.DeviceType] = None
        # Key of the entity.
        self._id: Optional[str] = None
        # Managed DeviceId
        self._managed_device_id: Optional[str] = None
        # Managed Device Name
        self._managed_device_name: Optional[str] = None
        # Management agent type.
        self._management_agent: Optional[management_agent_type.ManagementAgentType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Owner type of device.
        self._owner_type: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None
        # Managed Device Retire After DateTime
        self._retire_after_date_time: Optional[datetime] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
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
    
    @property
    def device_compliance_policy_id(self,) -> Optional[str]:
        """
        Gets the deviceCompliancePolicyId property value. Device Compliance PolicyId
        Returns: Optional[str]
        """
        return self._device_compliance_policy_id
    
    @device_compliance_policy_id.setter
    def device_compliance_policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceCompliancePolicyId property value. Device Compliance PolicyId
        Args:
            value: Value to set for the deviceCompliancePolicyId property.
        """
        self._device_compliance_policy_id = value
    
    @property
    def device_compliance_policy_name(self,) -> Optional[str]:
        """
        Gets the deviceCompliancePolicyName property value. Device Compliance Policy Name
        Returns: Optional[str]
        """
        return self._device_compliance_policy_name
    
    @device_compliance_policy_name.setter
    def device_compliance_policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceCompliancePolicyName property value. Device Compliance Policy Name
        Args:
            value: Value to set for the deviceCompliancePolicyName property.
        """
        self._device_compliance_policy_name = value
    
    @property
    def device_type(self,) -> Optional[device_type.DeviceType]:
        """
        Gets the deviceType property value. Device type.
        Returns: Optional[device_type.DeviceType]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[device_type.DeviceType] = None) -> None:
        """
        Sets the deviceType property value. Device type.
        Args:
            value: Value to set for the deviceType property.
        """
        self._device_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_state": lambda n : setattr(self, 'compliance_state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "device_compliance_policy_id": lambda n : setattr(self, 'device_compliance_policy_id', n.get_str_value()),
            "device_compliance_policy_name": lambda n : setattr(self, 'device_compliance_policy_name', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_enum_value(device_type.DeviceType)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managed_device_name": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "management_agent": lambda n : setattr(self, 'management_agent', n.get_enum_value(management_agent_type.ManagementAgentType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owner_type": lambda n : setattr(self, 'owner_type', n.get_enum_value(managed_device_owner_type.ManagedDeviceOwnerType)),
            "retire_after_date_time": lambda n : setattr(self, 'retire_after_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Key of the entity.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Key of the entity.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Managed DeviceId
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Managed DeviceId
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. Managed Device Name
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. Managed Device Name
        Args:
            value: Value to set for the managedDeviceName property.
        """
        self._managed_device_name = value
    
    @property
    def management_agent(self,) -> Optional[management_agent_type.ManagementAgentType]:
        """
        Gets the managementAgent property value. Management agent type.
        Returns: Optional[management_agent_type.ManagementAgentType]
        """
        return self._management_agent
    
    @management_agent.setter
    def management_agent(self,value: Optional[management_agent_type.ManagementAgentType] = None) -> None:
        """
        Sets the managementAgent property value. Management agent type.
        Args:
            value: Value to set for the managementAgent property.
        """
        self._management_agent = value
    
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
    def owner_type(self,) -> Optional[managed_device_owner_type.ManagedDeviceOwnerType]:
        """
        Gets the ownerType property value. Owner type of device.
        Returns: Optional[managed_device_owner_type.ManagedDeviceOwnerType]
        """
        return self._owner_type
    
    @owner_type.setter
    def owner_type(self,value: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None) -> None:
        """
        Sets the ownerType property value. Owner type of device.
        Args:
            value: Value to set for the ownerType property.
        """
        self._owner_type = value
    
    @property
    def retire_after_date_time(self,) -> Optional[datetime]:
        """
        Gets the retireAfterDateTime property value. Managed Device Retire After DateTime
        Returns: Optional[datetime]
        """
        return self._retire_after_date_time
    
    @retire_after_date_time.setter
    def retire_after_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the retireAfterDateTime property value. Managed Device Retire After DateTime
        Args:
            value: Value to set for the retireAfterDateTime property.
        """
        self._retire_after_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
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
    

