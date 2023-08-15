from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class SensitivityLabel(Entity):
    # The color that the UI should display for the label, if configured.
    color: Optional[str] = None
    # Returns the supported content formats for the label.
    content_formats: Optional[List[str]] = None
    # The admin-defined description for the label.
    description: Optional[str] = None
    # Indicates whether the label has protection actions configured.
    has_protection: Optional[bool] = None
    # Indicates whether the label is active or not. Active labels should be hidden or disabled in the UI.
    is_active: Optional[bool] = None
    # Indicates whether the label can be applied to content. False if the label is a parent with child labels.
    is_appliable: Optional[bool] = None
    # The plaintext name of the label.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parent label associated with a child label. Null if the label has no parent.
    parent: Optional[SensitivityLabel] = None
    # The sensitivity value of the label, where lower is less sensitive.
    sensitivity: Optional[int] = None
    # The tooltip that should be displayed for the label in a UI.
    tooltip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitivityLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityLabel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SensitivityLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "contentFormats": lambda n : setattr(self, 'content_formats', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "hasProtection": lambda n : setattr(self, 'has_protection', n.get_bool_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "isAppliable": lambda n : setattr(self, 'is_appliable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(SensitivityLabel)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_int_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_collection_of_primitive_values("contentFormats", self.content_formats)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("hasProtection", self.has_protection)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_bool_value("isAppliable", self.is_appliable)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parent", self.parent)
        writer.write_int_value("sensitivity", self.sensitivity)
        writer.write_str_value("tooltip", self.tooltip)
    

