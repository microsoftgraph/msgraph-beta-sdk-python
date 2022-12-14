from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class SharedEmailDomainInvitation(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new sharedEmailDomainInvitation and sets the default values.
        """
        super().__init__()
        # The expiryTime property
        self._expiry_time: Optional[datetime] = None
        # The invitationDomain property
        self._invitation_domain: Optional[str] = None
        # The invitationStatus property
        self._invitation_status: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedEmailDomainInvitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedEmailDomainInvitation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedEmailDomainInvitation()
    
    @property
    def expiry_time(self,) -> Optional[datetime]:
        """
        Gets the expiryTime property value. The expiryTime property
        Returns: Optional[datetime]
        """
        return self._expiry_time
    
    @expiry_time.setter
    def expiry_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiryTime property value. The expiryTime property
        Args:
            value: Value to set for the expiryTime property.
        """
        self._expiry_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiry_time": lambda n : setattr(self, 'expiry_time', n.get_datetime_value()),
            "invitation_domain": lambda n : setattr(self, 'invitation_domain', n.get_str_value()),
            "invitation_status": lambda n : setattr(self, 'invitation_status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invitation_domain(self,) -> Optional[str]:
        """
        Gets the invitationDomain property value. The invitationDomain property
        Returns: Optional[str]
        """
        return self._invitation_domain
    
    @invitation_domain.setter
    def invitation_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the invitationDomain property value. The invitationDomain property
        Args:
            value: Value to set for the invitationDomain property.
        """
        self._invitation_domain = value
    
    @property
    def invitation_status(self,) -> Optional[str]:
        """
        Gets the invitationStatus property value. The invitationStatus property
        Returns: Optional[str]
        """
        return self._invitation_status
    
    @invitation_status.setter
    def invitation_status(self,value: Optional[str] = None) -> None:
        """
        Sets the invitationStatus property value. The invitationStatus property
        Args:
            value: Value to set for the invitationStatus property.
        """
        self._invitation_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("expiryTime", self.expiry_time)
        writer.write_str_value("invitationDomain", self.invitation_domain)
        writer.write_str_value("invitationStatus", self.invitation_status)
    

