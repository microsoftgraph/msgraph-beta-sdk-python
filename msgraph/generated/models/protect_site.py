from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import label_action_base, site_access_type

from . import label_action_base

@dataclass
class ProtectSite(label_action_base.LabelActionBase):
    odata_type = "#microsoft.graph.protectSite"
    # The accessType property
    access_type: Optional[site_access_type.SiteAccessType] = None
    # The conditionalAccessProtectionLevelId property
    conditional_access_protection_level_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProtectSite
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProtectSite()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import label_action_base, site_access_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(site_access_type.SiteAccessType)),
            "conditionalAccessProtectionLevelId": lambda n : setattr(self, 'conditional_access_protection_level_id', n.get_str_value()),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("conditionalAccessProtectionLevelId", self.conditional_access_protection_level_id)
    

