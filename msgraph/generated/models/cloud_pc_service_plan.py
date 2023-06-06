from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_management_service, cloud_pc_provisioning_type, cloud_pc_service_plan_type, entity

from . import entity

@dataclass
class CloudPcServicePlan(entity.Entity):
    # The name for the service plan. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the type of license used when provisioning Cloud PCs. By default, the license type is dedicated. Possible values are: dedicated, shared, unknownFutureValue.
    provisioning_type: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None
    # The size of the RAM in GB. Read-only.
    ram_in_g_b: Optional[int] = None
    # The size of the OS Disk in GB. Read-only.
    storage_in_g_b: Optional[int] = None
    # The supportedSolution property
    supported_solution: Optional[cloud_pc_management_service.CloudPcManagementService] = None
    # The type of the service plan. Possible values are: enterprise, business, unknownFutureValue. Read-only.
    type: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType] = None
    # The size of the user profile disk in GB. Read-only.
    user_profile_in_g_b: Optional[int] = None
    # The number of vCPUs. Read-only.
    v_cpu_count: Optional[int] = None
    
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
    

