from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import meeting_registrant_base

from . import meeting_registrant_base

class ExternalMeetingRegistrant(meeting_registrant_base.MeetingRegistrantBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ExternalMeetingRegistrant and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.externalMeetingRegistrant"
        # The tenant ID of this registrant if in Azure Active Directory.
        self._tenant_id: Optional[str] = None
        # The user ID of this registrant if in Azure Active Directory.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalMeetingRegistrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalMeetingRegistrant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalMeetingRegistrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import meeting_registrant_base

        fields: Dict[str, Callable[[Any], None]] = {
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenant ID of this registrant if in Azure Active Directory.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenant ID of this registrant if in Azure Active Directory.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user ID of this registrant if in Azure Active Directory.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user ID of this registrant if in Azure Active Directory.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

