from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_derived_credential_issuer = lazy_import('msgraph.generated.models.device_management_derived_credential_issuer')
device_management_derived_credential_notification_type = lazy_import('msgraph.generated.models.device_management_derived_credential_notification_type')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementDerivedCredentialSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementDerivedCredentialSettings and sets the default values.
        """
        super().__init__()
        # The display name for the profile.
        self._display_name: Optional[str] = None
        # The URL that will be accessible to end users as they retrieve a derived credential using the Company Portal.
        self._help_url: Optional[str] = None
        # Supported values for the derived credential issuer.
        self._issuer: Optional[device_management_derived_credential_issuer.DeviceManagementDerivedCredentialIssuer] = None
        # Supported values for the notification type to use.
        self._notification_type: Optional[device_management_derived_credential_notification_type.DeviceManagementDerivedCredentialNotificationType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The nominal percentage of time before certificate renewal is initiated by the client.
        self._renewal_threshold_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementDerivedCredentialSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementDerivedCredentialSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementDerivedCredentialSettings()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the profile.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the profile.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "help_url": lambda n : setattr(self, 'help_url', n.get_str_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_enum_value(device_management_derived_credential_issuer.DeviceManagementDerivedCredentialIssuer)),
            "notification_type": lambda n : setattr(self, 'notification_type', n.get_enum_value(device_management_derived_credential_notification_type.DeviceManagementDerivedCredentialNotificationType)),
            "renewal_threshold_percentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def help_url(self,) -> Optional[str]:
        """
        Gets the helpUrl property value. The URL that will be accessible to end users as they retrieve a derived credential using the Company Portal.
        Returns: Optional[str]
        """
        return self._help_url
    
    @help_url.setter
    def help_url(self,value: Optional[str] = None) -> None:
        """
        Sets the helpUrl property value. The URL that will be accessible to end users as they retrieve a derived credential using the Company Portal.
        Args:
            value: Value to set for the helpUrl property.
        """
        self._help_url = value
    
    @property
    def issuer(self,) -> Optional[device_management_derived_credential_issuer.DeviceManagementDerivedCredentialIssuer]:
        """
        Gets the issuer property value. Supported values for the derived credential issuer.
        Returns: Optional[device_management_derived_credential_issuer.DeviceManagementDerivedCredentialIssuer]
        """
        return self._issuer
    
    @issuer.setter
    def issuer(self,value: Optional[device_management_derived_credential_issuer.DeviceManagementDerivedCredentialIssuer] = None) -> None:
        """
        Sets the issuer property value. Supported values for the derived credential issuer.
        Args:
            value: Value to set for the issuer property.
        """
        self._issuer = value
    
    @property
    def notification_type(self,) -> Optional[device_management_derived_credential_notification_type.DeviceManagementDerivedCredentialNotificationType]:
        """
        Gets the notificationType property value. Supported values for the notification type to use.
        Returns: Optional[device_management_derived_credential_notification_type.DeviceManagementDerivedCredentialNotificationType]
        """
        return self._notification_type
    
    @notification_type.setter
    def notification_type(self,value: Optional[device_management_derived_credential_notification_type.DeviceManagementDerivedCredentialNotificationType] = None) -> None:
        """
        Sets the notificationType property value. Supported values for the notification type to use.
        Args:
            value: Value to set for the notificationType property.
        """
        self._notification_type = value
    
    @property
    def renewal_threshold_percentage(self,) -> Optional[int]:
        """
        Gets the renewalThresholdPercentage property value. The nominal percentage of time before certificate renewal is initiated by the client.
        Returns: Optional[int]
        """
        return self._renewal_threshold_percentage
    
    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the renewalThresholdPercentage property value. The nominal percentage of time before certificate renewal is initiated by the client.
        Args:
            value: Value to set for the renewalThresholdPercentage property.
        """
        self._renewal_threshold_percentage = value
    
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
        writer.write_str_value("helpUrl", self.help_url)
        writer.write_enum_value("issuer", self.issuer)
        writer.write_enum_value("notificationType", self.notification_type)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
    

