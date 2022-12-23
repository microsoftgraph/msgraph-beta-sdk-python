from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

drive_item = lazy_import('msgraph.generated.models.drive_item')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
item_action_set = lazy_import('msgraph.generated.models.item_action_set')
item_activity_time_set = lazy_import('msgraph.generated.models.item_activity_time_set')
list_item = lazy_import('msgraph.generated.models.list_item')

class ItemActivityOLD(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def action(self,) -> Optional[item_action_set.ItemActionSet]:
        """
        Gets the action property value. The action property
        Returns: Optional[item_action_set.ItemActionSet]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[item_action_set.ItemActionSet] = None) -> None:
        """
        Sets the action property value. The action property
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def actor(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the actor property value. The actor property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._actor
    
    @actor.setter
    def actor(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the actor property value. The actor property
        Args:
            value: Value to set for the actor property.
        """
        self._actor = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemActivityOLD and sets the default values.
        """
        super().__init__()
        # The action property
        self._action: Optional[item_action_set.ItemActionSet] = None
        # The actor property
        self._actor: Optional[identity_set.IdentitySet] = None
        # The driveItem property
        self._drive_item: Optional[drive_item.DriveItem] = None
        # The listItem property
        self._list_item: Optional[list_item.ListItem] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The times property
        self._times: Optional[item_activity_time_set.ItemActivityTimeSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActivityOLD:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityOLD
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemActivityOLD()
    
    @property
    def drive_item(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the driveItem property value. The driveItem property
        Returns: Optional[drive_item.DriveItem]
        """
        return self._drive_item
    
    @drive_item.setter
    def drive_item(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the driveItem property value. The driveItem property
        Args:
            value: Value to set for the driveItem property.
        """
        self._drive_item = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(item_action_set.ItemActionSet)),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(identity_set.IdentitySet)),
            "drive_item": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
            "list_item": lambda n : setattr(self, 'list_item', n.get_object_value(list_item.ListItem)),
            "times": lambda n : setattr(self, 'times', n.get_object_value(item_activity_time_set.ItemActivityTimeSet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def list_item(self,) -> Optional[list_item.ListItem]:
        """
        Gets the listItem property value. The listItem property
        Returns: Optional[list_item.ListItem]
        """
        return self._list_item
    
    @list_item.setter
    def list_item(self,value: Optional[list_item.ListItem] = None) -> None:
        """
        Sets the listItem property value. The listItem property
        Args:
            value: Value to set for the listItem property.
        """
        self._list_item = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("action", self.action)
        writer.write_object_value("actor", self.actor)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("times", self.times)
    
    @property
    def times(self,) -> Optional[item_activity_time_set.ItemActivityTimeSet]:
        """
        Gets the times property value. The times property
        Returns: Optional[item_activity_time_set.ItemActivityTimeSet]
        """
        return self._times
    
    @times.setter
    def times(self,value: Optional[item_activity_time_set.ItemActivityTimeSet] = None) -> None:
        """
        Sets the times property value. The times property
        Args:
            value: Value to set for the times property.
        """
        self._times = value
    

