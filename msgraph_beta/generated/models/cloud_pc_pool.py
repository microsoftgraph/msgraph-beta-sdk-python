from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_agent_pool import CloudPcAgentPool
    from .cloud_pc_configuration import CloudPcConfiguration
    from .cloud_pc_network_configuration import CloudPcNetworkConfiguration
    from .cloud_pc_pool_assignment import CloudPcPoolAssignment
    from .cloud_pc_pool_capability_configuration import CloudPcPoolCapabilityConfiguration
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcPool(Entity, Parsable):
    # The assignments property
    assignments: Optional[list[CloudPcPoolAssignment]] = None
    # The capabilities property
    capabilities: Optional[CloudPcPoolCapabilityConfiguration] = None
    # The cloudPcConfiguration property
    cloud_pc_configuration: Optional[CloudPcConfiguration] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The networkConfiguration property
    network_configuration: Optional[CloudPcNetworkConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcPool:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcPool
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcAgentPool".casefold():
            from .cloud_pc_agent_pool import CloudPcAgentPool

            return CloudPcAgentPool()
        return CloudPcPool()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_agent_pool import CloudPcAgentPool
        from .cloud_pc_configuration import CloudPcConfiguration
        from .cloud_pc_network_configuration import CloudPcNetworkConfiguration
        from .cloud_pc_pool_assignment import CloudPcPoolAssignment
        from .cloud_pc_pool_capability_configuration import CloudPcPoolCapabilityConfiguration
        from .entity import Entity

        from .cloud_pc_agent_pool import CloudPcAgentPool
        from .cloud_pc_configuration import CloudPcConfiguration
        from .cloud_pc_network_configuration import CloudPcNetworkConfiguration
        from .cloud_pc_pool_assignment import CloudPcPoolAssignment
        from .cloud_pc_pool_capability_configuration import CloudPcPoolCapabilityConfiguration
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(CloudPcPoolAssignment)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(CloudPcPoolCapabilityConfiguration)),
            "cloudPcConfiguration": lambda n : setattr(self, 'cloud_pc_configuration', n.get_object_value(CloudPcConfiguration)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "networkConfiguration": lambda n : setattr(self, 'network_configuration', n.get_object_value(CloudPcNetworkConfiguration)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_object_value("capabilities", self.capabilities)
        writer.write_object_value("cloudPcConfiguration", self.cloud_pc_configuration)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("networkConfiguration", self.network_configuration)
    

