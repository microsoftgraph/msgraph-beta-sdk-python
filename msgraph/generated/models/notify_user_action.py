from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dlp_action_info

from . import dlp_action_info

class NotifyUserAction(dlp_action_info.DlpActionInfo):
    def __init__(self,) -> None:
        """
        Instantiates a new NotifyUserAction and sets the default values.
        """
        super().__init__()
        # The actionLastModifiedDateTime property
        self._action_last_modified_date_time: Optional[datetime] = None
        # The emailText property
        self._email_text: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policyTip property
        self._policy_tip: Optional[str] = None
        # The recipients property
        self._recipients: Optional[List[str]] = None
    
    @property
    def action_last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the actionLastModifiedDateTime property value. The actionLastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._action_last_modified_date_time
    
    @action_last_modified_date_time.setter
    def action_last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the actionLastModifiedDateTime property value. The actionLastModifiedDateTime property
        Args:
            value: Value to set for the action_last_modified_date_time property.
        """
        self._action_last_modified_date_time = value
    
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
    
    @property
    def email_text(self,) -> Optional[str]:
        """
        Gets the emailText property value. The emailText property
        Returns: Optional[str]
        """
        return self._email_text
    
    @email_text.setter
    def email_text(self,value: Optional[str] = None) -> None:
        """
        Sets the emailText property value. The emailText property
        Args:
            value: Value to set for the email_text property.
        """
        self._email_text = value
    
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
    
    @property
    def policy_tip(self,) -> Optional[str]:
        """
        Gets the policyTip property value. The policyTip property
        Returns: Optional[str]
        """
        return self._policy_tip
    
    @policy_tip.setter
    def policy_tip(self,value: Optional[str] = None) -> None:
        """
        Sets the policyTip property value. The policyTip property
        Args:
            value: Value to set for the policy_tip property.
        """
        self._policy_tip = value
    
    @property
    def recipients(self,) -> Optional[List[str]]:
        """
        Gets the recipients property value. The recipients property
        Returns: Optional[List[str]]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the recipients property value. The recipients property
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
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
    

