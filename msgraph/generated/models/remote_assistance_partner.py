from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, remote_assistance_onboarding_status

from . import entity

@dataclass
class RemoteAssistancePartner(entity.Entity):
    """
    RemoteAssistPartner resources represent the metadata and status of a given Remote Assistance partner service.
    """
    # Display name of the partner.
    display_name: Optional[str] = None
    # Timestamp of the last request sent to Intune by the TEM partner.
    last_connection_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When the OnboardingStatus is Onboarding, This is the date time when the onboarding request expires.
    onboarding_request_expiry_date_time: Optional[datetime] = None
    # The current TeamViewer connector status
    onboarding_status: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus] = None
    # URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
    onboarding_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteAssistancePartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteAssistancePartner
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RemoteAssistancePartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, remote_assistance_onboarding_status

        from . import entity, remote_assistance_onboarding_status

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "onboardingRequestExpiryDateTime": lambda n : setattr(self, 'onboarding_request_expiry_date_time', n.get_datetime_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus)),
            "onboardingUrl": lambda n : setattr(self, 'onboarding_url', n.get_str_value()),
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
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_datetime_value("onboardingRequestExpiryDateTime", self.onboarding_request_expiry_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_str_value("onboardingUrl", self.onboarding_url)
    

