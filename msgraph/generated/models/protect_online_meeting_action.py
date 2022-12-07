from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

label_action_base = lazy_import('msgraph.generated.models.label_action_base')
lobby_bypass_settings = lazy_import('msgraph.generated.models.lobby_bypass_settings')
online_meeting_forwarders = lazy_import('msgraph.generated.models.online_meeting_forwarders')
online_meeting_presenters = lazy_import('msgraph.generated.models.online_meeting_presenters')

class ProtectOnlineMeetingAction(label_action_base.LabelActionBase):
    @property
    def allowed_forwarders(self,) -> Optional[online_meeting_forwarders.OnlineMeetingForwarders]:
        """
        Gets the allowedForwarders property value. The allowedForwarders property
        Returns: Optional[online_meeting_forwarders.OnlineMeetingForwarders]
        """
        return self._allowed_forwarders
    
    @allowed_forwarders.setter
    def allowed_forwarders(self,value: Optional[online_meeting_forwarders.OnlineMeetingForwarders] = None) -> None:
        """
        Sets the allowedForwarders property value. The allowedForwarders property
        Args:
            value: Value to set for the allowedForwarders property.
        """
        self._allowed_forwarders = value
    
    @property
    def allowed_presenters(self,) -> Optional[online_meeting_presenters.OnlineMeetingPresenters]:
        """
        Gets the allowedPresenters property value. The allowedPresenters property
        Returns: Optional[online_meeting_presenters.OnlineMeetingPresenters]
        """
        return self._allowed_presenters
    
    @allowed_presenters.setter
    def allowed_presenters(self,value: Optional[online_meeting_presenters.OnlineMeetingPresenters] = None) -> None:
        """
        Sets the allowedPresenters property value. The allowedPresenters property
        Args:
            value: Value to set for the allowedPresenters property.
        """
        self._allowed_presenters = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ProtectOnlineMeetingAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.protectOnlineMeetingAction"
        # The allowedForwarders property
        self._allowed_forwarders: Optional[online_meeting_forwarders.OnlineMeetingForwarders] = None
        # The allowedPresenters property
        self._allowed_presenters: Optional[online_meeting_presenters.OnlineMeetingPresenters] = None
        # The isCopyToClipboardEnabled property
        self._is_copy_to_clipboard_enabled: Optional[bool] = None
        # The isLobbyEnabled property
        self._is_lobby_enabled: Optional[bool] = None
        # The lobbyBypassSettings property
        self._lobby_bypass_settings: Optional[lobby_bypass_settings.LobbyBypassSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectOnlineMeetingAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProtectOnlineMeetingAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProtectOnlineMeetingAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_forwarders": lambda n : setattr(self, 'allowed_forwarders', n.get_enum_value(online_meeting_forwarders.OnlineMeetingForwarders)),
            "allowed_presenters": lambda n : setattr(self, 'allowed_presenters', n.get_enum_value(online_meeting_presenters.OnlineMeetingPresenters)),
            "is_copy_to_clipboard_enabled": lambda n : setattr(self, 'is_copy_to_clipboard_enabled', n.get_bool_value()),
            "is_lobby_enabled": lambda n : setattr(self, 'is_lobby_enabled', n.get_bool_value()),
            "lobby_bypass_settings": lambda n : setattr(self, 'lobby_bypass_settings', n.get_object_value(lobby_bypass_settings.LobbyBypassSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_copy_to_clipboard_enabled(self,) -> Optional[bool]:
        """
        Gets the isCopyToClipboardEnabled property value. The isCopyToClipboardEnabled property
        Returns: Optional[bool]
        """
        return self._is_copy_to_clipboard_enabled
    
    @is_copy_to_clipboard_enabled.setter
    def is_copy_to_clipboard_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCopyToClipboardEnabled property value. The isCopyToClipboardEnabled property
        Args:
            value: Value to set for the isCopyToClipboardEnabled property.
        """
        self._is_copy_to_clipboard_enabled = value
    
    @property
    def is_lobby_enabled(self,) -> Optional[bool]:
        """
        Gets the isLobbyEnabled property value. The isLobbyEnabled property
        Returns: Optional[bool]
        """
        return self._is_lobby_enabled
    
    @is_lobby_enabled.setter
    def is_lobby_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLobbyEnabled property value. The isLobbyEnabled property
        Args:
            value: Value to set for the isLobbyEnabled property.
        """
        self._is_lobby_enabled = value
    
    @property
    def lobby_bypass_settings(self,) -> Optional[lobby_bypass_settings.LobbyBypassSettings]:
        """
        Gets the lobbyBypassSettings property value. The lobbyBypassSettings property
        Returns: Optional[lobby_bypass_settings.LobbyBypassSettings]
        """
        return self._lobby_bypass_settings
    
    @lobby_bypass_settings.setter
    def lobby_bypass_settings(self,value: Optional[lobby_bypass_settings.LobbyBypassSettings] = None) -> None:
        """
        Sets the lobbyBypassSettings property value. The lobbyBypassSettings property
        Args:
            value: Value to set for the lobbyBypassSettings property.
        """
        self._lobby_bypass_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowedForwarders", self.allowed_forwarders)
        writer.write_enum_value("allowedPresenters", self.allowed_presenters)
        writer.write_bool_value("isCopyToClipboardEnabled", self.is_copy_to_clipboard_enabled)
        writer.write_bool_value("isLobbyEnabled", self.is_lobby_enabled)
        writer.write_object_value("lobbyBypassSettings", self.lobby_bypass_settings)
    

