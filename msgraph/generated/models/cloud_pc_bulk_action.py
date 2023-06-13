from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_bulk_action_summary, cloud_pc_bulk_power_off, cloud_pc_bulk_power_on, entity

from . import entity

@dataclass
class CloudPcBulkAction(entity.Entity):
    # The actionSummary property
    action_summary: Optional[cloud_pc_bulk_action_summary.CloudPcBulkActionSummary] = None
    # The cloudPcIds property
    cloud_pc_ids: Optional[List[str]] = None
    # The createdDateTime property
    created_date_time: Optional[datetime] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcBulkAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.cloudPcBulkPowerOff":
                from . import cloud_pc_bulk_power_off

                return cloud_pc_bulk_power_off.CloudPcBulkPowerOff()
            if mapping_value == "#microsoft.graph.cloudPcBulkPowerOn":
                from . import cloud_pc_bulk_power_on

                return cloud_pc_bulk_power_on.CloudPcBulkPowerOn()
        return CloudPcBulkAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_bulk_action_summary, cloud_pc_bulk_power_off, cloud_pc_bulk_power_on, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSummary": lambda n : setattr(self, 'action_summary', n.get_object_value(cloud_pc_bulk_action_summary.CloudPcBulkActionSummary)),
            "cloudPcIds": lambda n : setattr(self, 'cloud_pc_ids', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_object_value("actionSummary", self.action_summary)
        writer.write_collection_of_primitive_values("cloudPcIds", self.cloud_pc_ids)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
    

