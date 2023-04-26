from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, remote_assistance_onboarding_status

from . import entity

class RemoteAssistancePartner(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RemoteAssistancePartner and sets the default values.
        """
        super().__init__()
        # Display name of the partner.
        self._display_name: Optional[str] = None
        # Timestamp of the last request sent to Intune by the TEM partner.
        self._last_connection_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # When the OnboardingStatus is Onboarding, This is the date time when the onboarding request expires.
        self._onboarding_request_expiry_date_time: Optional[datetime] = None
        # The current TeamViewer connector status
        self._onboarding_status: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus] = None
        # URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
        self._onboarding_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteAssistancePartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteAssistancePartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoteAssistancePartner()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the partner.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the partner.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def last_connection_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastConnectionDateTime property value. Timestamp of the last request sent to Intune by the TEM partner.
        Returns: Optional[datetime]
        """
        return self._last_connection_date_time
    
    @last_connection_date_time.setter
    def last_connection_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastConnectionDateTime property value. Timestamp of the last request sent to Intune by the TEM partner.
        Args:
            value: Value to set for the last_connection_date_time property.
        """
        self._last_connection_date_time = value
    
    @property
    def onboarding_request_expiry_date_time(self,) -> Optional[datetime]:
        """
        Gets the onboardingRequestExpiryDateTime property value. When the OnboardingStatus is Onboarding, This is the date time when the onboarding request expires.
        Returns: Optional[datetime]
        """
        return self._onboarding_request_expiry_date_time
    
    @onboarding_request_expiry_date_time.setter
    def onboarding_request_expiry_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onboardingRequestExpiryDateTime property value. When the OnboardingStatus is Onboarding, This is the date time when the onboarding request expires.
        Args:
            value: Value to set for the onboarding_request_expiry_date_time property.
        """
        self._onboarding_request_expiry_date_time = value
    
    @property
    def onboarding_status(self,) -> Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus]:
        """
        Gets the onboardingStatus property value. The current TeamViewer connector status
        Returns: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus]
        """
        return self._onboarding_status
    
    @onboarding_status.setter
    def onboarding_status(self,value: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus] = None) -> None:
        """
        Sets the onboardingStatus property value. The current TeamViewer connector status
        Args:
            value: Value to set for the onboarding_status property.
        """
        self._onboarding_status = value
    
    @property
    def onboarding_url(self,) -> Optional[str]:
        """
        Gets the onboardingUrl property value. URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
        Returns: Optional[str]
        """
        return self._onboarding_url
    
    @onboarding_url.setter
    def onboarding_url(self,value: Optional[str] = None) -> None:
        """
        Sets the onboardingUrl property value. URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
        Args:
            value: Value to set for the onboarding_url property.
        """
        self._onboarding_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_datetime_value("onboardingRequestExpiryDateTime", self.onboarding_request_expiry_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_str_value("onboardingUrl", self.onboarding_url)
    

