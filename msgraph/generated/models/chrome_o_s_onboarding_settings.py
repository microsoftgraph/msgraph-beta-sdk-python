from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
onboarding_status = lazy_import('msgraph.generated.models.onboarding_status')

class ChromeOSOnboardingSettings(entity.Entity):
    """
    Entity that represents a Chromebook tenant settings
    """
    def __init__(self,) -> None:
        """
        Instantiates a new chromeOSOnboardingSettings and sets the default values.
        """
        super().__init__()
        # The ChromebookTenant's LastDirectorySyncDateTime
        self._last_directory_sync_date_time: Optional[datetime] = None
        # The ChromebookTenant's LastModifiedDateTime
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The onboarding status of the tenant.
        self._onboarding_status: Optional[onboarding_status.OnboardingStatus] = None
        # The ChromebookTenant's OwnerUserPrincipalName
        self._owner_user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChromeOSOnboardingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChromeOSOnboardingSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChromeOSOnboardingSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_directory_sync_date_time": lambda n : setattr(self, 'last_directory_sync_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "onboarding_status": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(onboarding_status.OnboardingStatus)),
            "owner_user_principal_name": lambda n : setattr(self, 'owner_user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_directory_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastDirectorySyncDateTime property value. The ChromebookTenant's LastDirectorySyncDateTime
        Returns: Optional[datetime]
        """
        return self._last_directory_sync_date_time
    
    @last_directory_sync_date_time.setter
    def last_directory_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastDirectorySyncDateTime property value. The ChromebookTenant's LastDirectorySyncDateTime
        Args:
            value: Value to set for the lastDirectorySyncDateTime property.
        """
        self._last_directory_sync_date_time = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The ChromebookTenant's LastModifiedDateTime
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The ChromebookTenant's LastModifiedDateTime
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def onboarding_status(self,) -> Optional[onboarding_status.OnboardingStatus]:
        """
        Gets the onboardingStatus property value. The onboarding status of the tenant.
        Returns: Optional[onboarding_status.OnboardingStatus]
        """
        return self._onboarding_status
    
    @onboarding_status.setter
    def onboarding_status(self,value: Optional[onboarding_status.OnboardingStatus] = None) -> None:
        """
        Sets the onboardingStatus property value. The onboarding status of the tenant.
        Args:
            value: Value to set for the onboardingStatus property.
        """
        self._onboarding_status = value
    
    @property
    def owner_user_principal_name(self,) -> Optional[str]:
        """
        Gets the ownerUserPrincipalName property value. The ChromebookTenant's OwnerUserPrincipalName
        Returns: Optional[str]
        """
        return self._owner_user_principal_name
    
    @owner_user_principal_name.setter
    def owner_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerUserPrincipalName property value. The ChromebookTenant's OwnerUserPrincipalName
        Args:
            value: Value to set for the ownerUserPrincipalName property.
        """
        self._owner_user_principal_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastDirectorySyncDateTime", self.last_directory_sync_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_str_value("ownerUserPrincipalName", self.owner_user_principal_name)
    

