from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

@dataclass
class AndroidForWorkGmailEasConfiguration(AndroidForWorkEasEmailProfileBase):
    """
    By providing configurations in this profile you can instruct the Gmail email client on Android For Work devices to communicate with an Exchange server and get email, contacts, calendar, tasks, and notes. Furthermore, you can also specify how much email to sync and how often the device should sync.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkGmailEasConfiguration"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkGmailEasConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkGmailEasConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkGmailEasConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

        fields: Dict[str, Callable[[Any], None]] = {
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
    

