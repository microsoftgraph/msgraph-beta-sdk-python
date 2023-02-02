from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

admin_windows_updates = lazy_import('msgraph.generated.models.admin_windows_updates')
entity = lazy_import('msgraph.generated.models.entity')

class AdminWindows(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new adminWindows and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The updates property
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
        fields = {
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
        Gets the updates property value. The updates property
        Returns: Optional[admin_windows_updates.AdminWindowsUpdates]
        """
        return self._updates
    
    @updates.setter
    def updates(self,value: Optional[admin_windows_updates.AdminWindowsUpdates] = None) -> None:
        """
        Sets the updates property value. The updates property
        Args:
            value: Value to set for the updates property.
        """
        self._updates = value
    

