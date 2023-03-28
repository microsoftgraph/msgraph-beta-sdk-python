from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import entity

from .. import entity

class ManagedTenantTicketingEndpoint(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new managedTenantTicketingEndpoint and sets the default values.
        """
        super().__init__()
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The emailAddress property
        self._email_address: Optional[str] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the created_by_user_id property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenantTicketingEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantTicketingEndpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedTenantTicketingEndpoint()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The emailAddress property
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The emailAddress property
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the last_action_by_user_id property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the last_action_date_time property.
        """
        self._last_action_date_time = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. The phoneNumber property
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. The phoneNumber property
        Args:
            value: Value to set for the phone_number property.
        """
        self._phone_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("phoneNumber", self.phone_number)
    

