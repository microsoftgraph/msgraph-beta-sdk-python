from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, outlook_geo_coordinates, physical_address, room, room_list, workspace

from . import entity

@dataclass
class Place(entity.Entity):
    # The street address of the place.
    address: Optional[physical_address.PhysicalAddress] = None
    # The name associated with the place.
    display_name: Optional[str] = None
    # Specifies the place location in latitude, longitude and (optionally) altitude coordinates.
    geo_coordinates: Optional[outlook_geo_coordinates.OutlookGeoCoordinates] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phone number of the place.
    phone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Place:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Place
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.room".casefold():
            from . import room

            return room.Room()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roomList".casefold():
            from . import room_list

            return room_list.RoomList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workspace".casefold():
            from . import workspace

            return workspace.Workspace()
        return Place()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, outlook_geo_coordinates, physical_address, room, room_list, workspace

        from . import entity, outlook_geo_coordinates, physical_address, room, room_list, workspace

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(outlook_geo_coordinates.OutlookGeoCoordinates)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("phone", self.phone)
    

