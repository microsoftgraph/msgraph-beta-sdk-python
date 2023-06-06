from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import management_category, workload_action
    from .. import entity

from .. import entity

@dataclass
class ManagementAction(entity.Entity):
    # The category property
    category: Optional[management_category.ManagementCategory] = None
    # The description for the management action. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the management action. Optional. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reference for the management template used to generate the management action. Required. Read-only.
    reference_template_id: Optional[str] = None
    # The referenceTemplateVersion property
    reference_template_version: Optional[int] = None
    # The collection of workload actions associated with the management action. Required. Read-only.
    workload_actions: Optional[List[workload_action.WorkloadAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import management_category, workload_action
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(management_category.ManagementCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "referenceTemplateId": lambda n : setattr(self, 'reference_template_id', n.get_str_value()),
            "referenceTemplateVersion": lambda n : setattr(self, 'reference_template_version', n.get_int_value()),
            "workloadActions": lambda n : setattr(self, 'workload_actions', n.get_collection_of_object_values(workload_action.WorkloadAction)),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("referenceTemplateId", self.reference_template_id)
        writer.write_int_value("referenceTemplateVersion", self.reference_template_version)
        writer.write_collection_of_object_values("workloadActions", self.workload_actions)
    

