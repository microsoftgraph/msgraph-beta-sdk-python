from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_address = lazy_import('msgraph.generated.models.email_address')
entity = lazy_import('msgraph.generated.models.entity')

class Mention(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def application(self,) -> Optional[str]:
        """
        Gets the application property value. The name of the application where the mention is created. Optional. Not used and defaulted as null for message.
        Returns: Optional[str]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[str] = None) -> None:
        """
        Sets the application property value. The name of the application where the mention is created. Optional. Not used and defaulted as null for message.
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    @property
    def client_reference(self,) -> Optional[str]:
        """
        Gets the clientReference property value. A unique identifier that represents a parent of the resource instance. Optional. Not used and defaulted as null for message.
        Returns: Optional[str]
        """
        return self._client_reference
    
    @client_reference.setter
    def client_reference(self,value: Optional[str] = None) -> None:
        """
        Sets the clientReference property value. A unique identifier that represents a parent of the resource instance. Optional. Not used and defaulted as null for message.
        Args:
            value: Value to set for the clientReference property.
        """
        self._client_reference = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mention and sets the default values.
        """
        super().__init__()
        # The name of the application where the mention is created. Optional. Not used and defaulted as null for message.
        self._application: Optional[str] = None
        # A unique identifier that represents a parent of the resource instance. Optional. Not used and defaulted as null for message.
        self._client_reference: Optional[str] = None
        # The email information of the user who made the mention.
        self._created_by: Optional[email_address.EmailAddress] = None
        # The date and time that the mention is created on the client.
        self._created_date_time: Optional[datetime] = None
        # A deep web link to the context of the mention in the resource instance. Optional. Not used and defaulted as null for message.
        self._deep_link: Optional[str] = None
        # The mentioned property
        self._mentioned: Optional[email_address.EmailAddress] = None
        # Optional. Not used and defaulted as null for message. To get the mentions in a message, see the bodyPreview property of the message instead.
        self._mention_text: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date and time that the mention is created on the server. Optional. Not used and defaulted as null for message.
        self._server_created_date_time: Optional[datetime] = None
    
    @property
    def created_by(self,) -> Optional[email_address.EmailAddress]:
        """
        Gets the createdBy property value. The email information of the user who made the mention.
        Returns: Optional[email_address.EmailAddress]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[email_address.EmailAddress] = None) -> None:
        """
        Sets the createdBy property value. The email information of the user who made the mention.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time that the mention is created on the client.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time that the mention is created on the client.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Mention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Mention
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Mention()
    
    @property
    def deep_link(self,) -> Optional[str]:
        """
        Gets the deepLink property value. A deep web link to the context of the mention in the resource instance. Optional. Not used and defaulted as null for message.
        Returns: Optional[str]
        """
        return self._deep_link
    
    @deep_link.setter
    def deep_link(self,value: Optional[str] = None) -> None:
        """
        Sets the deepLink property value. A deep web link to the context of the mention in the resource instance. Optional. Not used and defaulted as null for message.
        Args:
            value: Value to set for the deepLink property.
        """
        self._deep_link = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application": lambda n : setattr(self, 'application', n.get_str_value()),
            "client_reference": lambda n : setattr(self, 'client_reference', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(email_address.EmailAddress)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deep_link": lambda n : setattr(self, 'deep_link', n.get_str_value()),
            "mentioned": lambda n : setattr(self, 'mentioned', n.get_object_value(email_address.EmailAddress)),
            "mention_text": lambda n : setattr(self, 'mention_text', n.get_str_value()),
            "server_created_date_time": lambda n : setattr(self, 'server_created_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mentioned(self,) -> Optional[email_address.EmailAddress]:
        """
        Gets the mentioned property value. The mentioned property
        Returns: Optional[email_address.EmailAddress]
        """
        return self._mentioned
    
    @mentioned.setter
    def mentioned(self,value: Optional[email_address.EmailAddress] = None) -> None:
        """
        Sets the mentioned property value. The mentioned property
        Args:
            value: Value to set for the mentioned property.
        """
        self._mentioned = value
    
    @property
    def mention_text(self,) -> Optional[str]:
        """
        Gets the mentionText property value. Optional. Not used and defaulted as null for message. To get the mentions in a message, see the bodyPreview property of the message instead.
        Returns: Optional[str]
        """
        return self._mention_text
    
    @mention_text.setter
    def mention_text(self,value: Optional[str] = None) -> None:
        """
        Sets the mentionText property value. Optional. Not used and defaulted as null for message. To get the mentions in a message, see the bodyPreview property of the message instead.
        Args:
            value: Value to set for the mentionText property.
        """
        self._mention_text = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("application", self.application)
        writer.write_str_value("clientReference", self.client_reference)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deepLink", self.deep_link)
        writer.write_object_value("mentioned", self.mentioned)
        writer.write_str_value("mentionText", self.mention_text)
        writer.write_datetime_value("serverCreatedDateTime", self.server_created_date_time)
    
    @property
    def server_created_date_time(self,) -> Optional[datetime]:
        """
        Gets the serverCreatedDateTime property value. The date and time that the mention is created on the server. Optional. Not used and defaulted as null for message.
        Returns: Optional[datetime]
        """
        return self._server_created_date_time
    
    @server_created_date_time.setter
    def server_created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the serverCreatedDateTime property value. The date and time that the mention is created on the server. Optional. Not used and defaulted as null for message.
        Args:
            value: Value to set for the serverCreatedDateTime property.
        """
        self._server_created_date_time = value
    

