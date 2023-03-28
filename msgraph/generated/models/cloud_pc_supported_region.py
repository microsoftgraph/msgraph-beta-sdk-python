from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_management_service, cloud_pc_region_group, cloud_pc_supported_region_status, entity

from . import entity

class CloudPcSupportedRegion(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcSupportedRegion and sets the default values.
        """
        super().__init__()
        # The name for the supported region. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The regionGroup property
        self._region_group: Optional[cloud_pc_region_group.CloudPcRegionGroup] = None
        # The status of the supported region. Possible values are: available, restricted, unavailable, unknownFutureValue. Read-only.
        self._region_status: Optional[cloud_pc_supported_region_status.CloudPcSupportedRegionStatus] = None
        # The supportedSolution property
        self._supported_solution: Optional[cloud_pc_management_service.CloudPcManagementService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcSupportedRegion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSupportedRegion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcSupportedRegion()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name for the supported region. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name for the supported region. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_management_service, cloud_pc_region_group, cloud_pc_supported_region_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "regionGroup": lambda n : setattr(self, 'region_group', n.get_enum_value(cloud_pc_region_group.CloudPcRegionGroup)),
            "regionStatus": lambda n : setattr(self, 'region_status', n.get_enum_value(cloud_pc_supported_region_status.CloudPcSupportedRegionStatus)),
            "supportedSolution": lambda n : setattr(self, 'supported_solution', n.get_enum_value(cloud_pc_management_service.CloudPcManagementService)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def region_group(self,) -> Optional[cloud_pc_region_group.CloudPcRegionGroup]:
        """
        Gets the regionGroup property value. The regionGroup property
        Returns: Optional[cloud_pc_region_group.CloudPcRegionGroup]
        """
        return self._region_group
    
    @region_group.setter
    def region_group(self,value: Optional[cloud_pc_region_group.CloudPcRegionGroup] = None) -> None:
        """
        Sets the regionGroup property value. The regionGroup property
        Args:
            value: Value to set for the region_group property.
        """
        self._region_group = value
    
    @property
    def region_status(self,) -> Optional[cloud_pc_supported_region_status.CloudPcSupportedRegionStatus]:
        """
        Gets the regionStatus property value. The status of the supported region. Possible values are: available, restricted, unavailable, unknownFutureValue. Read-only.
        Returns: Optional[cloud_pc_supported_region_status.CloudPcSupportedRegionStatus]
        """
        return self._region_status
    
    @region_status.setter
    def region_status(self,value: Optional[cloud_pc_supported_region_status.CloudPcSupportedRegionStatus] = None) -> None:
        """
        Sets the regionStatus property value. The status of the supported region. Possible values are: available, restricted, unavailable, unknownFutureValue. Read-only.
        Args:
            value: Value to set for the region_status property.
        """
        self._region_status = value
    
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
        writer.write_enum_value("regionGroup", self.region_group)
        writer.write_enum_value("regionStatus", self.region_status)
        writer.write_enum_value("supportedSolution", self.supported_solution)
    
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
    

