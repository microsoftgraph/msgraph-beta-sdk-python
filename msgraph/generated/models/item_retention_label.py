from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, retention_label_settings

from . import entity

@dataclass
class ItemRetentionLabel(entity.Entity):
    # The isLabelAppliedExplicitly property
    is_label_applied_explicitly: Optional[bool] = None
    # The labelAppliedBy property
    label_applied_by: Optional[identity_set.IdentitySet] = None
    # The labelAppliedDateTime property
    label_applied_date_time: Optional[datetime] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The retentionSettings property
    retention_settings: Optional[retention_label_settings.RetentionLabelSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemRetentionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemRetentionLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemRetentionLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, retention_label_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "isLabelAppliedExplicitly": lambda n : setattr(self, 'is_label_applied_explicitly', n.get_bool_value()),
            "labelAppliedBy": lambda n : setattr(self, 'label_applied_by', n.get_object_value(identity_set.IdentitySet)),
            "labelAppliedDateTime": lambda n : setattr(self, 'label_applied_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "retentionSettings": lambda n : setattr(self, 'retention_settings', n.get_object_value(retention_label_settings.RetentionLabelSettings)),
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
        writer.write_bool_value("isLabelAppliedExplicitly", self.is_label_applied_explicitly)
        writer.write_object_value("labelAppliedBy", self.label_applied_by)
        writer.write_datetime_value("labelAppliedDateTime", self.label_applied_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("retentionSettings", self.retention_settings)
    

