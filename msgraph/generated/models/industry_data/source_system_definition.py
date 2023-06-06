from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import user_matching_setting
    from .. import entity

from .. import entity

@dataclass
class SourceSystemDefinition(entity.Entity):
    # The name of the source system. Maximum supported length is 100 characters.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of user matching settings by roleGroup.
    user_matching_settings: Optional[List[user_matching_setting.UserMatchingSetting]] = None
    # The name of the vendor who supplies the source system. Maximum supported length is 100 characters.
    vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SourceSystemDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SourceSystemDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SourceSystemDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import user_matching_setting
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "userMatchingSettings": lambda n : setattr(self, 'user_matching_settings', n.get_collection_of_object_values(user_matching_setting.UserMatchingSetting)),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
        writer.write_collection_of_object_values("userMatchingSettings", self.user_matching_settings)
        writer.write_str_value("vendor", self.vendor)
    

