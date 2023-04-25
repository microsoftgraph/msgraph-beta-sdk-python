from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import admin_windows_updates, entity

from . import entity

class AdminWindows(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AdminWindows and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
        self._updates: Optional[admin_windows_updates.AdminWindowsUpdates] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminWindows:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdminWindows
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdminWindows()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import admin_windows_updates, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "updates": lambda n : setattr(self, 'updates', n.get_object_value(admin_windows_updates.AdminWindowsUpdates)),
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
        writer.write_object_value("updates", self.updates)
    
    @property
    def updates(self,) -> Optional[admin_windows_updates.AdminWindowsUpdates]:
        """
        Gets the updates property value. Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
        Returns: Optional[admin_windows_updates.AdminWindowsUpdates]
        """
        return self._updates
    
    @updates.setter
    def updates(self,value: Optional[admin_windows_updates.AdminWindowsUpdates] = None) -> None:
        """
        Sets the updates property value. Entity that acts as a container for all Windows Update for Business deployment service functionalities. Read-only.
        Args:
            value: Value to set for the updates property.
        """
        self._updates = value
    

