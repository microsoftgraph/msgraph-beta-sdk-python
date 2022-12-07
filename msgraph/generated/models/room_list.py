from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

place = lazy_import('msgraph.generated.models.place')
room = lazy_import('msgraph.generated.models.room')
workspace = lazy_import('msgraph.generated.models.workspace')

class RoomList(place.Place):
    def __init__(self,) -> None:
        """
        Instantiates a new RoomList and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.roomList"
        # The email address of the room list.
        self._email_address: Optional[str] = None
        # The rooms property
        self._rooms: Optional[List[room.Room]] = None
        # The workspaces property
        self._workspaces: Optional[List[workspace.Workspace]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoomList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoomList
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoomList()
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The email address of the room list.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The email address of the room list.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "rooms": lambda n : setattr(self, 'rooms', n.get_collection_of_object_values(room.Room)),
            "workspaces": lambda n : setattr(self, 'workspaces', n.get_collection_of_object_values(workspace.Workspace)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def rooms(self,) -> Optional[List[room.Room]]:
        """
        Gets the rooms property value. The rooms property
        Returns: Optional[List[room.Room]]
        """
        return self._rooms
    
    @rooms.setter
    def rooms(self,value: Optional[List[room.Room]] = None) -> None:
        """
        Sets the rooms property value. The rooms property
        Args:
            value: Value to set for the rooms property.
        """
        self._rooms = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_collection_of_object_values("rooms", self.rooms)
        writer.write_collection_of_object_values("workspaces", self.workspaces)
    
    @property
    def workspaces(self,) -> Optional[List[workspace.Workspace]]:
        """
        Gets the workspaces property value. The workspaces property
        Returns: Optional[List[workspace.Workspace]]
        """
        return self._workspaces
    
    @workspaces.setter
    def workspaces(self,value: Optional[List[workspace.Workspace]] = None) -> None:
        """
        Sets the workspaces property value. The workspaces property
        Args:
            value: Value to set for the workspaces property.
        """
        self._workspaces = value
    

