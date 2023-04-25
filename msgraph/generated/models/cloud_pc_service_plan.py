from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_management_service, cloud_pc_provisioning_type, cloud_pc_service_plan_type, entity

from . import entity

class CloudPcServicePlan(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcServicePlan and sets the default values.
        """
        super().__init__()
        # The name for the service plan. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the type of license used when provisioning Cloud PCs. By default, the license type is dedicated. Possible values are: dedicated, shared, unknownFutureValue.
        self._provisioning_type: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None
        # The size of the RAM in GB. Read-only.
        self._ram_in_g_b: Optional[int] = None
        # The size of the OS Disk in GB. Read-only.
        self._storage_in_g_b: Optional[int] = None
        # The supportedSolution property
        self._supported_solution: Optional[cloud_pc_management_service.CloudPcManagementService] = None
        # The type of the service plan. Possible values are: enterprise, business, unknownFutureValue. Read-only.
        self._type: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType] = None
        # The size of the user profile disk in GB. Read-only.
        self._user_profile_in_g_b: Optional[int] = None
        # The number of vCPUs. Read-only.
        self._v_cpu_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcServicePlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcServicePlan
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcServicePlan()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name for the service plan. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name for the service plan. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_management_service, cloud_pc_provisioning_type, cloud_pc_service_plan_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(cloud_pc_provisioning_type.CloudPcProvisioningType)),
            "ramInGB": lambda n : setattr(self, 'ram_in_g_b', n.get_int_value()),
            "storageInGB": lambda n : setattr(self, 'storage_in_g_b', n.get_int_value()),
            "supportedSolution": lambda n : setattr(self, 'supported_solution', n.get_enum_value(cloud_pc_management_service.CloudPcManagementService)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(cloud_pc_service_plan_type.CloudPcServicePlanType)),
            "userProfileInGB": lambda n : setattr(self, 'user_profile_in_g_b', n.get_int_value()),
            "vCpuCount": lambda n : setattr(self, 'v_cpu_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def provisioning_type(self,) -> Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]:
        """
        Gets the provisioningType property value. Specifies the type of license used when provisioning Cloud PCs. By default, the license type is dedicated. Possible values are: dedicated, shared, unknownFutureValue.
        Returns: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]
        """
        return self._provisioning_type
    
    @provisioning_type.setter
    def provisioning_type(self,value: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None) -> None:
        """
        Sets the provisioningType property value. Specifies the type of license used when provisioning Cloud PCs. By default, the license type is dedicated. Possible values are: dedicated, shared, unknownFutureValue.
        Args:
            value: Value to set for the provisioning_type property.
        """
        self._provisioning_type = value
    
    @property
    def ram_in_g_b(self,) -> Optional[int]:
        """
        Gets the ramInGB property value. The size of the RAM in GB. Read-only.
        Returns: Optional[int]
        """
        return self._ram_in_g_b
    
    @ram_in_g_b.setter
    def ram_in_g_b(self,value: Optional[int] = None) -> None:
        """
        Sets the ramInGB property value. The size of the RAM in GB. Read-only.
        Args:
            value: Value to set for the ram_in_g_b property.
        """
        self._ram_in_g_b = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_int_value("ramInGB", self.ram_in_g_b)
        writer.write_int_value("storageInGB", self.storage_in_g_b)
        writer.write_enum_value("supportedSolution", self.supported_solution)
        writer.write_enum_value("type", self.type)
        writer.write_int_value("userProfileInGB", self.user_profile_in_g_b)
        writer.write_int_value("vCpuCount", self.v_cpu_count)
    
    @property
    def storage_in_g_b(self,) -> Optional[int]:
        """
        Gets the storageInGB property value. The size of the OS Disk in GB. Read-only.
        Returns: Optional[int]
        """
        return self._storage_in_g_b
    
    @storage_in_g_b.setter
    def storage_in_g_b(self,value: Optional[int] = None) -> None:
        """
        Sets the storageInGB property value. The size of the OS Disk in GB. Read-only.
        Args:
            value: Value to set for the storage_in_g_b property.
        """
        self._storage_in_g_b = value
    
    @property
    def supported_solution(self,) -> Optional[cloud_pc_management_service.CloudPcManagementService]:
        """
        Gets the supportedSolution property value. The supportedSolution property
        Returns: Optional[cloud_pc_management_service.CloudPcManagementService]
        """
        return self._supported_solution
    
    @supported_solution.setter
    def supported_solution(self,value: Optional[cloud_pc_management_service.CloudPcManagementService] = None) -> None:
        """
        Sets the supportedSolution property value. The supportedSolution property
        Args:
            value: Value to set for the supported_solution property.
        """
        self._supported_solution = value
    
    @property
    def type(self,) -> Optional[cloud_pc_service_plan_type.CloudPcServicePlanType]:
        """
        Gets the type property value. The type of the service plan. Possible values are: enterprise, business, unknownFutureValue. Read-only.
        Returns: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType] = None) -> None:
        """
        Sets the type property value. The type of the service plan. Possible values are: enterprise, business, unknownFutureValue. Read-only.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_profile_in_g_b(self,) -> Optional[int]:
        """
        Gets the userProfileInGB property value. The size of the user profile disk in GB. Read-only.
        Returns: Optional[int]
        """
        return self._user_profile_in_g_b
    
    @user_profile_in_g_b.setter
    def user_profile_in_g_b(self,value: Optional[int] = None) -> None:
        """
        Sets the userProfileInGB property value. The size of the user profile disk in GB. Read-only.
        Args:
            value: Value to set for the user_profile_in_g_b property.
        """
        self._user_profile_in_g_b = value
    
    @property
    def v_cpu_count(self,) -> Optional[int]:
        """
        Gets the vCpuCount property value. The number of vCPUs. Read-only.
        Returns: Optional[int]
        """
        return self._v_cpu_count
    
    @v_cpu_count.setter
    def v_cpu_count(self,value: Optional[int] = None) -> None:
        """
        Sets the vCpuCount property value. The number of vCPUs. Read-only.
        Args:
            value: Value to set for the v_cpu_count property.
        """
        self._v_cpu_count = value
    

