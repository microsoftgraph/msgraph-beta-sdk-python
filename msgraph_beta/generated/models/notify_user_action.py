from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dlp_action_info import DlpActionInfo

from .dlp_action_info import DlpActionInfo

@dataclass
class NotifyUserAction(DlpActionInfo, Parsable):
    # Timestamp when the notification action configuration was last modified.
    action_last_modified_date_time: Optional[datetime.datetime] = None
    # The body text of the email notification sent to users.
    email_text: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The text of the policy tip displayed to the user within the application (For example, Outlook, Word).
    policy_tip: Optional[str] = None
    # List of email addresses or user identifiers designated to receive the notification email. Can include sender, owner, manager, etc.
    recipients: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotifyUserAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotifyUserAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotifyUserAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dlp_action_info import DlpActionInfo

        from .dlp_action_info import DlpActionInfo

        fields: dict[str, Callable[[Any], None]] = {
            "actionLastModifiedDateTime": lambda n : setattr(self, 'action_last_modified_date_time', n.get_datetime_value()),
            "emailText": lambda n : setattr(self, 'email_text', n.get_str_value()),
            "policyTip": lambda n : setattr(self, 'policy_tip', n.get_str_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_primitive_values(str)),
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
        writer.write_datetime_value("actionLastModifiedDateTime", self.action_last_modified_date_time)
        writer.write_str_value("emailText", self.email_text)
        writer.write_str_value("policyTip", self.policy_tip)
        writer.write_collection_of_primitive_values("recipients", self.recipients)
    

