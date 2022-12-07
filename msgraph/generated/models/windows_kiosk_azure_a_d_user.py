from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_user = lazy_import('msgraph.generated.models.windows_kiosk_user')

class WindowsKioskAzureADUser(windows_kiosk_user.WindowsKioskUser):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskAzureADUser and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskAzureADUser"
        # The ID of the AzureAD user that will be locked to this kiosk configuration
        self._user_id: Optional[str] = None
        # The user accounts that will be locked to this kiosk configuration
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskAzureADUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAzureADUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskAzureADUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The ID of the AzureAD user that will be locked to this kiosk configuration
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The ID of the AzureAD user that will be locked to this kiosk configuration
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user accounts that will be locked to this kiosk configuration
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user accounts that will be locked to this kiosk configuration
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

