from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_privacy = lazy_import('msgraph.generated.models.group_privacy')
label_action_base = lazy_import('msgraph.generated.models.label_action_base')

class ProtectGroup(label_action_base.LabelActionBase):
    @property
    def allow_email_from_guest_users(self,) -> Optional[bool]:
        """
        Gets the allowEmailFromGuestUsers property value. The allowEmailFromGuestUsers property
        Returns: Optional[bool]
        """
        return self._allow_email_from_guest_users
    
    @allow_email_from_guest_users.setter
    def allow_email_from_guest_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowEmailFromGuestUsers property value. The allowEmailFromGuestUsers property
        Args:
            value: Value to set for the allowEmailFromGuestUsers property.
        """
        self._allow_email_from_guest_users = value
    
    @property
    def allow_guest_users(self,) -> Optional[bool]:
        """
        Gets the allowGuestUsers property value. The allowGuestUsers property
        Returns: Optional[bool]
        """
        return self._allow_guest_users
    
    @allow_guest_users.setter
    def allow_guest_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowGuestUsers property value. The allowGuestUsers property
        Args:
            value: Value to set for the allowGuestUsers property.
        """
        self._allow_guest_users = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ProtectGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.protectGroup"
        # The allowEmailFromGuestUsers property
        self._allow_email_from_guest_users: Optional[bool] = None
        # The allowGuestUsers property
        self._allow_guest_users: Optional[bool] = None
        # The privacy property
        self._privacy: Optional[group_privacy.GroupPrivacy] = None
    
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
        fields = {
            "allow_email_from_guest_users": lambda n : setattr(self, 'allow_email_from_guest_users', n.get_bool_value()),
            "allow_guest_users": lambda n : setattr(self, 'allow_guest_users', n.get_bool_value()),
            "privacy": lambda n : setattr(self, 'privacy', n.get_enum_value(group_privacy.GroupPrivacy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def privacy(self,) -> Optional[group_privacy.GroupPrivacy]:
        """
        Gets the privacy property value. The privacy property
        Returns: Optional[group_privacy.GroupPrivacy]
        """
        return self._privacy
    
    @privacy.setter
    def privacy(self,value: Optional[group_privacy.GroupPrivacy] = None) -> None:
        """
        Sets the privacy property value. The privacy property
        Args:
            value: Value to set for the privacy property.
        """
        self._privacy = value
    
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
    

