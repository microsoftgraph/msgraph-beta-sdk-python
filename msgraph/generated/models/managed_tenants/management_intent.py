from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .management_template_detailed_info import ManagementTemplateDetailedInfo

from ..entity import Entity

@dataclass
class ManagementIntent(Entity):
    # The display name for the management intent. Optional. Read-only.
    display_name: Optional[str] = None
    # A flag indicating whether the management intent is global. Required. Read-only.
    is_global: Optional[bool] = None
    # The collection of management templates associated with the management intent. Optional. Read-only.
    management_templates: Optional[List[ManagementTemplateDetailedInfo]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementIntent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementIntent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagementIntent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .management_template_detailed_info import ManagementTemplateDetailedInfo

        from ..entity import Entity
        from .management_template_detailed_info import ManagementTemplateDetailedInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isGlobal": lambda n : setattr(self, 'is_global', n.get_bool_value()),
            "managementTemplates": lambda n : setattr(self, 'management_templates', n.get_collection_of_object_values(ManagementTemplateDetailedInfo)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isGlobal", self.is_global)
        writer.write_collection_of_object_values("managementTemplates", self.management_templates)
    

