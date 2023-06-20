from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aad_user_conversation_member, anonymous_guest_conversation_member, azure_communication_services_user_conversation_member, entity, microsoft_account_user_conversation_member, skype_for_business_user_conversation_member, skype_user_conversation_member

from . import entity

@dataclass
class ConversationMember(entity.Entity):
    # The display name of the user.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The roles for that user. This property contains additional qualifiers only when relevant - for example, if the member has owner privileges, the roles property contains owner as one of the values. Similarly, if the member is an in-tenant guest, the roles property contains guest as one of the values. A basic member should not have any values specified in the roles property. An Out-of-tenant external member is assigned the owner role.
    roles: Optional[List[str]] = None
    # The timestamp denoting how far back a conversation's history is shared with the conversation member. This property is settable only for members of a chat.
    visible_history_start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConversationMember
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadUserConversationMember".casefold():
            from . import aad_user_conversation_member

            return aad_user_conversation_member.AadUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.anonymousGuestConversationMember".casefold():
            from . import anonymous_guest_conversation_member

            return anonymous_guest_conversation_member.AnonymousGuestConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserConversationMember".casefold():
            from . import azure_communication_services_user_conversation_member

            return azure_communication_services_user_conversation_member.AzureCommunicationServicesUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAccountUserConversationMember".casefold():
            from . import microsoft_account_user_conversation_member

            return microsoft_account_user_conversation_member.MicrosoftAccountUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeForBusinessUserConversationMember".casefold():
            from . import skype_for_business_user_conversation_member

            return skype_for_business_user_conversation_member.SkypeForBusinessUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeUserConversationMember".casefold():
            from . import skype_user_conversation_member

            return skype_user_conversation_member.SkypeUserConversationMember()
        return ConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aad_user_conversation_member, anonymous_guest_conversation_member, azure_communication_services_user_conversation_member, entity, microsoft_account_user_conversation_member, skype_for_business_user_conversation_member, skype_user_conversation_member

        from . import aad_user_conversation_member, anonymous_guest_conversation_member, azure_communication_services_user_conversation_member, entity, microsoft_account_user_conversation_member, skype_for_business_user_conversation_member, skype_user_conversation_member

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "visibleHistoryStartDateTime": lambda n : setattr(self, 'visible_history_start_date_time', n.get_datetime_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_datetime_value("visibleHistoryStartDateTime", self.visible_history_start_date_time)
    

