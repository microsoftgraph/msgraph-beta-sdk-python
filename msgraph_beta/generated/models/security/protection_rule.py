from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .detection_rule import DetectionRule

from ..entity import Entity

@dataclass
class ProtectionRule(Entity):
    # Name of the user or application that created the rule.
    created_by: Optional[str] = None
    # Timestamp of rule creation.
    created_date_time: Optional[datetime.datetime] = None
    # Name of the rule.
    display_name: Optional[str] = None
    # Whether rule is turned on for the tenant.
    is_enabled: Optional[bool] = None
    # Name of the user or application who last updated the rule.
    last_modified_by: Optional[str] = None
    # Timestamp of when the rule was last updated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.detectionRule".casefold():
            from .detection_rule import DetectionRule

            return DetectionRule()
        return ProtectionRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .detection_rule import DetectionRule

        from ..entity import Entity
        from .detection_rule import DetectionRule

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

