from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label_action_base import LabelActionBase
    from .lobby_bypass_settings import LobbyBypassSettings
    from .online_meeting_forwarders import OnlineMeetingForwarders
    from .online_meeting_presenters import OnlineMeetingPresenters

from .label_action_base import LabelActionBase

@dataclass
class ProtectOnlineMeetingAction(LabelActionBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.protectOnlineMeetingAction"
    # The allowedForwarders property
    allowed_forwarders: Optional[OnlineMeetingForwarders] = None
    # The allowedPresenters property
    allowed_presenters: Optional[OnlineMeetingPresenters] = None
    # The isCopyToClipboardEnabled property
    is_copy_to_clipboard_enabled: Optional[bool] = None
    # The isLobbyEnabled property
    is_lobby_enabled: Optional[bool] = None
    # The lobbyBypassSettings property
    lobby_bypass_settings: Optional[LobbyBypassSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectOnlineMeetingAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectOnlineMeetingAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProtectOnlineMeetingAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .label_action_base import LabelActionBase
        from .lobby_bypass_settings import LobbyBypassSettings
        from .online_meeting_forwarders import OnlineMeetingForwarders
        from .online_meeting_presenters import OnlineMeetingPresenters

        from .label_action_base import LabelActionBase
        from .lobby_bypass_settings import LobbyBypassSettings
        from .online_meeting_forwarders import OnlineMeetingForwarders
        from .online_meeting_presenters import OnlineMeetingPresenters

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedForwarders": lambda n : setattr(self, 'allowed_forwarders', n.get_enum_value(OnlineMeetingForwarders)),
            "allowedPresenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(OnlineMeetingPresenters)),
            "isCopyToClipboardEnabled": lambda n : setattr(self, 'is_copy_to_clipboard_enabled', n.get_bool_value()),
            "isLobbyEnabled": lambda n : setattr(self, 'is_lobby_enabled', n.get_bool_value()),
            "lobbyBypassSettings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(LobbyBypassSettings)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("allowedForwarders", self.allowed_forwarders)
        writer.write_enum_value("allowedPresenters", self.allowed_presenters)
        writer.write_bool_value("isCopyToClipboardEnabled", self.is_copy_to_clipboard_enabled)
        writer.write_bool_value("isLobbyEnabled", self.is_lobby_enabled)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
    

