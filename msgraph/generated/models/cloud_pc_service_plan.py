from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_service_plan_type = lazy_import('msgraph.generated.models.cloud_pc_service_plan_type')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcServicePlan(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcServicePlan and sets the default values.
        """
        super().__init__()
        # The name for the service plan. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The size of the RAM in GB. Read-only.
        self._ram_in_g_b: Optional[int] = None
        # The size of the OS Disk in GB. Read-only.
        self._storage_in_g_b: Optional[int] = None
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
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ram_in_g_b": lambda n : setattr(self, 'ram_in_g_b', n.get_int_value()),
            "storage_in_g_b": lambda n : setattr(self, 'storage_in_g_b', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(cloud_pc_service_plan_type.CloudPcServicePlanType)),
            "user_profile_in_g_b": lambda n : setattr(self, 'user_profile_in_g_b', n.get_int_value()),
            "v_cpu_count": lambda n : setattr(self, 'v_cpu_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
            value: Value to set for the ramInGB property.
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
        writer.write_int_value("ramInGB", self.ram_in_g_b)
        writer.write_int_value("storageInGB", self.storage_in_g_b)
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
            value: Value to set for the storageInGB property.
        """
        self._storage_in_g_b = value
    
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
            value: Value to set for the userProfileInGB property.
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
            value: Value to set for the vCpuCount property.
        """
        self._v_cpu_count = value
    

