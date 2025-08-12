from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place
    from .place_mode import PlaceMode

from .place import Place

@dataclass
class Workspace(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.workspace"
    # The name or identifier of the building where the workspace is located.
    building: Optional[str] = None
    # The maximum number of individual desks within a workspace.
    capacity: Optional[int] = None
    # The name of the display device (for example, monitor or projector) that is available in the workspace.
    display_device_name: Optional[str] = None
    # The email address that is associated with the workspace. This email address is used for booking.
    email_address: Optional[str] = None
    # A human-readable label for the floor; for example, Ground Floor.
    floor_label: Optional[str] = None
    # The numeric floor level within the building. For example, 1 for first floor, 2 for second floor, and so on.
    floor_number: Optional[int] = None
    # The mode for a workspace. The supported modes are:reservablePlaceMode - Workspaces that can be booked in advance using desk pool reservation tools.dropInPlaceMode - First come, first served desks. When you plug into a peripheral on one of these desks in the workspace, the desk is booked for you, assuming that the peripheral has been associated with the desk in the Microsoft Teams Rooms Pro management portal.offlinePlaceMode - Workspaces that are taken down for maintenance or marked as not reservable.
    mode: Optional[PlaceMode] = None
    # A short, friendly name for the workspace, often used for easier identification or display in the UI.
    nickname: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place
        from .place_mode import PlaceMode

        from .place import Place
        from .place_mode import PlaceMode

        fields: dict[str, Callable[[Any], None]] = {
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "displayDeviceName": lambda n : setattr(self, 'display_device_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "floorLabel": lambda n : setattr(self, 'floor_label', n.get_str_value()),
            "floorNumber": lambda n : setattr(self, 'floor_number', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_object_value(PlaceMode)),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
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
        writer.write_str_value("displayDeviceName", self.display_device_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("floorLabel", self.floor_label)
        writer.write_int_value("floorNumber", self.floor_number)
        writer.write_object_value("mode", self.mode)
        writer.write_str_value("nickname", self.nickname)
    

