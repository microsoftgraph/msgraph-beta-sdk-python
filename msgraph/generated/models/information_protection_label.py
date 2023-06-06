from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, parent_label_details

from . import entity

@dataclass
class InformationProtectionLabel(entity.Entity):
    # The color that the UI should display for the label, if configured.
    color: Optional[str] = None
    # The admin-defined description for the label.
    description: Optional[str] = None
    # Indicates whether the label is active or not. Active labels should be hidden or disabled in UI.
    is_active: Optional[bool] = None
    # The plaintext name of the label.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parent label associated with a child label. Null if label has no parent.
    parent: Optional[parent_label_details.ParentLabelDetails] = None
    # The sensitivity value of the label, where lower is less sensitive.
    sensitivity: Optional[int] = None
    # The tooltip that should be displayed for the label in a UI.
    tooltip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtectionLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, parent_label_details

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(parent_label_details.ParentLabelDetails)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_int_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parent", self.parent)
        writer.write_int_value("sensitivity", self.sensitivity)
        writer.write_str_value("tooltip", self.tooltip)
    

