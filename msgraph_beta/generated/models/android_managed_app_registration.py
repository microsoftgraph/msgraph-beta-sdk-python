from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_app_registration import ManagedAppRegistration

from .managed_app_registration import ManagedAppRegistration

@dataclass
class AndroidManagedAppRegistration(ManagedAppRegistration, Parsable):
    """
    Represents the synchronization details of an android app, with management capabilities, for a specific user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidManagedAppRegistration"
    # The patch version for the current android app registration
    patch_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedAppRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedAppRegistration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedAppRegistration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_registration import ManagedAppRegistration

        from .managed_app_registration import ManagedAppRegistration

        fields: dict[str, Callable[[Any], None]] = {
            "patchVersion": lambda n : setattr(self, 'patch_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("patchVersion", self.patch_version)
    

