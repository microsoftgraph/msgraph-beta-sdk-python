from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import open_shift_item, schedule_entity, shift_activity

from . import schedule_entity

class ShiftItem(schedule_entity.ScheduleEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new ShiftItem and sets the default values.
        """
        super().__init__()
        # An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.
        self._activities: Optional[List[shift_activity.ShiftActivity]] = None
        # The shift label of the shiftItem.
        self._display_name: Optional[str] = None
        # The shift notes for the shiftItem.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def activities(self,) -> Optional[List[shift_activity.ShiftActivity]]:
        """
        Gets the activities property value. An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.
        Returns: Optional[List[shift_activity.ShiftActivity]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[shift_activity.ShiftActivity]] = None) -> None:
        """
        Sets the activities property value. An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ShiftItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ShiftItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.openShiftItem":
                from . import open_shift_item

                return open_shift_item.OpenShiftItem()
        return ShiftItem()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The shift label of the shiftItem.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The shift label of the shiftItem.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import open_shift_item, schedule_entity, shift_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(shift_activity.ShiftActivity)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. The shift notes for the shiftItem.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. The shift notes for the shiftItem.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("notes", self.notes)
    

