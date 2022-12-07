from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
device_management_derived_credential_settings = lazy_import('msgraph.generated.models.device_management_derived_credential_settings')

class IosDerivedCredentialAuthenticationConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IosDerivedCredentialAuthenticationConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration"
        # Tenant level settings for the Derived Credentials to be used for authentication.
        self._derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDerivedCredentialAuthenticationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosDerivedCredentialAuthenticationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosDerivedCredentialAuthenticationConfiguration()
    
    @property
    def derived_credential_settings(self,) -> Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]:
        """
        Gets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Returns: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]
        """
        return self._derived_credential_settings
    
    @derived_credential_settings.setter
    def derived_credential_settings(self,value: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None) -> None:
        """
        Sets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Args:
            value: Value to set for the derivedCredentialSettings property.
        """
        self._derived_credential_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "derived_credential_settings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
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
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
    

