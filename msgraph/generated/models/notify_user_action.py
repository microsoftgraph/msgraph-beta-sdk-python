from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dlp_action_info

from . import dlp_action_info

@dataclass
class NotifyUserAction(dlp_action_info.DlpActionInfo):
    # The actionLastModifiedDateTime property
    action_last_modified_date_time: Optional[datetime] = None
    # The emailText property
    email_text: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyTip property
    policy_tip: Optional[str] = None
    # The recipients property
    recipients: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NotifyUserAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NotifyUserAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NotifyUserAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import dlp_action_info

        fields: Dict[str, Callable[[Any], None]] = {
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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("actionLastModifiedDateTime", self.action_last_modified_date_time)
        writer.write_str_value("emailText", self.email_text)
        writer.write_str_value("policyTip", self.policy_tip)
        writer.write_collection_of_primitive_values("recipients", self.recipients)
    

