from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
    from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
    from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
    from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
    from .cloud_pc_bulk_resize import CloudPcBulkResize
    from .cloud_pc_bulk_restart import CloudPcBulkRestart
    from .cloud_pc_bulk_restore import CloudPcBulkRestore
    from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcBulkAction(Entity):
    # The actionSummary property
    action_summary: Optional[CloudPcBulkActionSummary] = None
    # The cloudPcIds property
    cloud_pc_ids: Optional[List[str]] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcBulkAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkPowerOff".casefold():
            from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff

            return CloudPcBulkPowerOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkPowerOn".casefold():
            from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn

            return CloudPcBulkPowerOn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkReprovision".casefold():
            from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision

            return CloudPcBulkReprovision()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkResize".casefold():
            from .cloud_pc_bulk_resize import CloudPcBulkResize

            return CloudPcBulkResize()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkRestart".casefold():
            from .cloud_pc_bulk_restart import CloudPcBulkRestart

            return CloudPcBulkRestart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkRestore".casefold():
            from .cloud_pc_bulk_restore import CloudPcBulkRestore

            return CloudPcBulkRestore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkTroubleshoot".casefold():
            from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot

            return CloudPcBulkTroubleshoot()
        return CloudPcBulkAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
        from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
        from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
        from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
        from .cloud_pc_bulk_resize import CloudPcBulkResize
        from .cloud_pc_bulk_restart import CloudPcBulkRestart
        from .cloud_pc_bulk_restore import CloudPcBulkRestore
        from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
        from .entity import Entity

        from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
        from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
        from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
        from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
        from .cloud_pc_bulk_resize import CloudPcBulkResize
        from .cloud_pc_bulk_restart import CloudPcBulkRestart
        from .cloud_pc_bulk_restore import CloudPcBulkRestore
        from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSummary": lambda n : setattr(self, 'action_summary', n.get_object_value(CloudPcBulkActionSummary)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("actionSummary", self.action_summary)
        writer.write_collection_of_primitive_values("cloudPcIds", self.cloud_pc_ids)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
    

