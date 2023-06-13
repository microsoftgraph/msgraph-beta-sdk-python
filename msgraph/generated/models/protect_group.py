from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group_privacy, label_action_base

from . import label_action_base

@dataclass
class ProtectGroup(label_action_base.LabelActionBase):
    odata_type = "#microsoft.graph.protectGroup"
    # The allowEmailFromGuestUsers property
    allow_email_from_guest_users: Optional[bool] = None
    # The allowGuestUsers property
    allow_guest_users: Optional[bool] = None
    # The privacy property
    privacy: Optional[group_privacy.GroupPrivacy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProtectGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProtectGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group_privacy, label_action_base

        fields: Dict[str, Callable[[Any], None]] = {
            "allowEmailFromGuestUsers": lambda n : setattr(self, 'allow_email_from_guest_users', n.get_bool_value()),
            "allowGuestUsers": lambda n : setattr(self, 'allow_guest_users', n.get_bool_value()),
            "privacy": lambda n : setattr(self, 'privacy', n.get_enum_value(group_privacy.GroupPrivacy)),
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
        writer.write_bool_value("allowEmailFromGuestUsers", self.allow_email_from_guest_users)
        writer.write_bool_value("allowGuestUsers", self.allow_guest_users)
        writer.write_enum_value("privacy", self.privacy)
    

