from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import place

from . import place

class Workspace(place.Place):
    def __init__(self,) -> None:
        """
        Instantiates a new workspace and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.workspace"
        # Specifies the building name or building number that the workspace is in.
        self._building: Optional[str] = None
        # Specifies the capacity of the workspace.
        self._capacity: Optional[int] = None
        # Email address of the workspace.
        self._email_address: Optional[str] = None
        # Specifies a descriptive label for the floor, for example, P.
        self._floor_label: Optional[str] = None
        # Specifies the floor number that the workspace is on.
        self._floor_number: Optional[int] = None
        # Specifies whether the workspace is wheelchair accessible.
        self._is_wheel_chair_accessible: Optional[bool] = None
        # Specifies a descriptive label for the workspace, for example, a number or name.
        self._label: Optional[str] = None
        # Specifies a nickname for the workspace, for example, 'quiet workspace'.
        self._nickname: Optional[str] = None
        # Specifies additional features of the workspace, for example, details like the type of view or furniture type.
        self._tags: Optional[List[str]] = None
    
    @property
    def building(self,) -> Optional[str]:
        """
        Gets the building property value. Specifies the building name or building number that the workspace is in.
        Returns: Optional[str]
        """
        return self._building
    
    @building.setter
    def building(self,value: Optional[str] = None) -> None:
        """
        Sets the building property value. Specifies the building name or building number that the workspace is in.
        Args:
            value: Value to set for the building property.
        """
        self._building = value
    
    @property
    def capacity(self,) -> Optional[int]:
        """
        Gets the capacity property value. Specifies the capacity of the workspace.
        Returns: Optional[int]
        """
        return self._capacity
    
    @capacity.setter
    def capacity(self,value: Optional[int] = None) -> None:
        """
        Sets the capacity property value. Specifies the capacity of the workspace.
        Args:
            value: Value to set for the capacity property.
        """
        self._capacity = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Workspace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Workspace
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Workspace()
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. Email address of the workspace.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. Email address of the workspace.
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    @property
    def floor_label(self,) -> Optional[str]:
        """
        Gets the floorLabel property value. Specifies a descriptive label for the floor, for example, P.
        Returns: Optional[str]
        """
        return self._floor_label
    
    @floor_label.setter
    def floor_label(self,value: Optional[str] = None) -> None:
        """
        Sets the floorLabel property value. Specifies a descriptive label for the floor, for example, P.
        Args:
            value: Value to set for the floor_label property.
        """
        self._floor_label = value
    
    @property
    def floor_number(self,) -> Optional[int]:
        """
        Gets the floorNumber property value. Specifies the floor number that the workspace is on.
        Returns: Optional[int]
        """
        return self._floor_number
    
    @floor_number.setter
    def floor_number(self,value: Optional[int] = None) -> None:
        """
        Sets the floorNumber property value. Specifies the floor number that the workspace is on.
        Args:
            value: Value to set for the floor_number property.
        """
        self._floor_number = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import place

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
    
    @property
    def is_wheel_chair_accessible(self,) -> Optional[bool]:
        """
        Gets the isWheelChairAccessible property value. Specifies whether the workspace is wheelchair accessible.
        Returns: Optional[bool]
        """
        return self._is_wheel_chair_accessible
    
    @is_wheel_chair_accessible.setter
    def is_wheel_chair_accessible(self,value: Optional[bool] = None) -> None:
        """
        Sets the isWheelChairAccessible property value. Specifies whether the workspace is wheelchair accessible.
        Args:
            value: Value to set for the is_wheel_chair_accessible property.
        """
        self._is_wheel_chair_accessible = value
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. Specifies a descriptive label for the workspace, for example, a number or name.
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. Specifies a descriptive label for the workspace, for example, a number or name.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def nickname(self,) -> Optional[str]:
        """
        Gets the nickname property value. Specifies a nickname for the workspace, for example, 'quiet workspace'.
        Returns: Optional[str]
        """
        return self._nickname
    
    @nickname.setter
    def nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the nickname property value. Specifies a nickname for the workspace, for example, 'quiet workspace'.
        Args:
            value: Value to set for the nickname property.
        """
        self._nickname = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. Specifies additional features of the workspace, for example, details like the type of view or furniture type.
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. Specifies additional features of the workspace, for example, details like the type of view or furniture type.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    

