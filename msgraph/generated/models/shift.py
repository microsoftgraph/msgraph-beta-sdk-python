from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
shift_item = lazy_import('msgraph.generated.models.shift_item')

class Shift(change_tracked_entity.ChangeTrackedEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new Shift and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.shift"
        # The draft version of this shift that is viewable by managers. Required.
        self._draft_shift: Optional[shift_item.ShiftItem] = None
        # The isStagedForDeletion property
        self._is_staged_for_deletion: Optional[bool] = None
        # The schedulingGroupId property
        self._scheduling_group_id: Optional[str] = None
        # The sharedShift property
        self._shared_shift: Optional[shift_item.ShiftItem] = None
        # The userId property
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Shift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Shift
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Shift()
    
    @property
    def draft_shift(self,) -> Optional[shift_item.ShiftItem]:
        """
        Gets the draftShift property value. The draft version of this shift that is viewable by managers. Required.
        Returns: Optional[shift_item.ShiftItem]
        """
        return self._draft_shift
    
    @draft_shift.setter
    def draft_shift(self,value: Optional[shift_item.ShiftItem] = None) -> None:
        """
        Sets the draftShift property value. The draft version of this shift that is viewable by managers. Required.
        Args:
            value: Value to set for the draftShift property.
        """
        self._draft_shift = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "draft_shift": lambda n : setattr(self, 'draft_shift', n.get_object_value(shift_item.ShiftItem)),
            "is_staged_for_deletion": lambda n : setattr(self, 'is_staged_for_deletion', n.get_bool_value()),
            "scheduling_group_id": lambda n : setattr(self, 'scheduling_group_id', n.get_str_value()),
            "shared_shift": lambda n : setattr(self, 'shared_shift', n.get_object_value(shift_item.ShiftItem)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_staged_for_deletion(self,) -> Optional[bool]:
        """
        Gets the isStagedForDeletion property value. The isStagedForDeletion property
        Returns: Optional[bool]
        """
        return self._is_staged_for_deletion
    
    @is_staged_for_deletion.setter
    def is_staged_for_deletion(self,value: Optional[bool] = None) -> None:
        """
        Sets the isStagedForDeletion property value. The isStagedForDeletion property
        Args:
            value: Value to set for the isStagedForDeletion property.
        """
        self._is_staged_for_deletion = value
    
    @property
    def scheduling_group_id(self,) -> Optional[str]:
        """
        Gets the schedulingGroupId property value. The schedulingGroupId property
        Returns: Optional[str]
        """
        return self._scheduling_group_id
    
    @scheduling_group_id.setter
    def scheduling_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the schedulingGroupId property value. The schedulingGroupId property
        Args:
            value: Value to set for the schedulingGroupId property.
        """
        self._scheduling_group_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("draftShift", self.draft_shift)
        writer.write_bool_value("isStagedForDeletion", self.is_staged_for_deletion)
        writer.write_str_value("schedulingGroupId", self.scheduling_group_id)
        writer.write_object_value("sharedShift", self.shared_shift)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def shared_shift(self,) -> Optional[shift_item.ShiftItem]:
        """
        Gets the sharedShift property value. The sharedShift property
        Returns: Optional[shift_item.ShiftItem]
        """
        return self._shared_shift
    
    @shared_shift.setter
    def shared_shift(self,value: Optional[shift_item.ShiftItem] = None) -> None:
        """
        Sets the sharedShift property value. The sharedShift property
        Args:
            value: Value to set for the sharedShift property.
        """
        self._shared_shift = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

