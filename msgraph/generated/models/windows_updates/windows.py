from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
updates = lazy_import('msgraph.generated.models.windows_updates.updates')

class Windows(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new windows and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Entity that acts as a container for the functionality of the Windows Update for Business deployment service. Read-only.
        self._updates: Optional[updates.Updates] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "updates": lambda n : setattr(self, 'updates', n.get_object_value(updates.Updates)),
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
    def updates(self,) -> Optional[updates.Updates]:
        """
        Gets the updates property value. Entity that acts as a container for the functionality of the Windows Update for Business deployment service. Read-only.
        Returns: Optional[updates.Updates]
        """
        return self._updates
    
    @updates.setter
    def updates(self,value: Optional[updates.Updates] = None) -> None:
        """
        Sets the updates property value. Entity that acts as a container for the functionality of the Windows Update for Business deployment service. Read-only.
        Args:
            value: Value to set for the updates property.
        """
        self._updates = value
    

