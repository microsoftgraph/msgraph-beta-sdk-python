from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .pronouns_settings import PronounsSettings

from .entity import Entity

@dataclass
class PeopleAdminSettings(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents administrator settings that manage the support of pronouns in an organization.
    pronouns: Optional[PronounsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PeopleAdminSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PeopleAdminSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PeopleAdminSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .pronouns_settings import PronounsSettings

        from .entity import Entity
        from .pronouns_settings import PronounsSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "pronouns": lambda n : setattr(self, 'pronouns', n.get_object_value(PronounsSettings)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("pronouns", self.pronouns)
    

