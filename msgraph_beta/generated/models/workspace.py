from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place

from .place import Place

@dataclass
class Workspace(Place):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.workspace"
    # Specifies the building name or building number that the workspace is in.
    building: Optional[str] = None
    # Specifies the capacity of the workspace.
    capacity: Optional[int] = None
    # Email address of the workspace.
    email_address: Optional[str] = None
    # Specifies a descriptive label for the floor, for example, P.
    floor_label: Optional[str] = None
    # Specifies the floor number that the workspace is on.
    floor_number: Optional[int] = None
    # Specifies whether the workspace is wheelchair accessible.
    is_wheel_chair_accessible: Optional[bool] = None
    # Specifies a descriptive label for the workspace, for example, a number or name.
    label: Optional[str] = None
    # Specifies a nickname for the workspace, for example, 'quiet workspace'.
    nickname: Optional[str] = None
    # Specifies other features of the workspace; for example, the type of view or furniture type.
    tags: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Workspace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Workspace
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Workspace()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place

        from .place import Place

        fields: Dict[str, Callable[[Any], None]] = {
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "floorLabel": lambda n : setattr(self, 'floor_label', n.get_str_value()),
            "floorNumber": lambda n : setattr(self, 'floor_number', n.get_int_value()),
            "isWheelChairAccessible": lambda n : setattr(self, 'is_wheel_chair_accessible', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("building", self.building)
        writer.write_int_value("capacity", self.capacity)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("floorLabel", self.floor_label)
        writer.write_int_value("floorNumber", self.floor_number)
        writer.write_bool_value("isWheelChairAccessible", self.is_wheel_chair_accessible)
        writer.write_str_value("label", self.label)
        writer.write_str_value("nickname", self.nickname)
        writer.write_collection_of_primitive_values("tags", self.tags)
    

