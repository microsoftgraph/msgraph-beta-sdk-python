from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_properties

from . import content_properties

class FileContentProperties(content_properties.ContentProperties):
    def __init__(self,) -> None:
        """
        Instantiates a new FileContentProperties and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.fileContentProperties"
        # The isVisibleOnlyToOneDriveOwner property
        self._is_visible_only_to_one_drive_owner: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileContentProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileContentProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileContentProperties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_properties

        fields: Dict[str, Callable[[Any], None]] = {
            "isVisibleOnlyToOneDriveOwner": lambda n : setattr(self, 'is_visible_only_to_one_drive_owner', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_visible_only_to_one_drive_owner(self,) -> Optional[bool]:
        """
        Gets the isVisibleOnlyToOneDriveOwner property value. The isVisibleOnlyToOneDriveOwner property
        Returns: Optional[bool]
        """
        return self._is_visible_only_to_one_drive_owner
    
    @is_visible_only_to_one_drive_owner.setter
    def is_visible_only_to_one_drive_owner(self,value: Optional[bool] = None) -> None:
        """
        Sets the isVisibleOnlyToOneDriveOwner property value. The isVisibleOnlyToOneDriveOwner property
        Args:
            value: Value to set for the is_visible_only_to_one_drive_owner property.
        """
        self._is_visible_only_to_one_drive_owner = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isVisibleOnlyToOneDriveOwner", self.is_visible_only_to_one_drive_owner)
    

