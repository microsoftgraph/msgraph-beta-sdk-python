from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_management_service import CloudPcManagementService
    from .cloud_pc_region_group import CloudPcRegionGroup
    from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcSupportedRegion(Entity):
    # The name for the supported region. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The regionGroup property
    region_group: Optional[CloudPcRegionGroup] = None
    # The status of the supported region. Possible values are: available, restricted, unavailable, unknownFutureValue. Read-only.
    region_status: Optional[CloudPcSupportedRegionStatus] = None
    # The supportedSolution property
    supported_solution: Optional[CloudPcManagementService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcSupportedRegion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSupportedRegion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcSupportedRegion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_region_group import CloudPcRegionGroup
        from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
        from .entity import Entity

        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_region_group import CloudPcRegionGroup
        from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "regionGroup": lambda n : setattr(self, 'region_group', n.get_enum_value(CloudPcRegionGroup)),
            "regionStatus": lambda n : setattr(self, 'region_status', n.get_enum_value(CloudPcSupportedRegionStatus)),
            "supportedSolution": lambda n : setattr(self, 'supported_solution', n.get_collection_of_enum_values(CloudPcManagementService)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("regionGroup", self.region_group)
        writer.write_enum_value("regionStatus", self.region_status)
        writer.write_enum_value("supportedSolution", self.supported_solution)
    

