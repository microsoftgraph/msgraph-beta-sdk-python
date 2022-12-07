from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method = lazy_import('msgraph.generated.models.authentication_method')
device = lazy_import('msgraph.generated.models.device')

class PasswordlessMicrosoftAuthenticatorAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new PasswordlessMicrosoftAuthenticatorAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.passwordlessMicrosoftAuthenticatorAuthenticationMethod"
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The timestamp when this method was registered to the user.
        self._creation_date_time: Optional[datetime] = None
        # The device property
        self._device: Optional[device.Device] = None
        # The display name of the mobile device as given by the user.
        self._display_name: Optional[str] = None
    
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
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PasswordlessMicrosoftAuthenticatorAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PasswordlessMicrosoftAuthenticatorAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PasswordlessMicrosoftAuthenticatorAuthenticationMethod()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The timestamp when this method was registered to the user.
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The timestamp when this method was registered to the user.
        Args:
            value: Value to set for the creationDateTime property.
        """
        self._creation_date_time = value
    
    @property
    def device(self,) -> Optional[device.Device]:
        """
        Gets the device property value. The device property
        Returns: Optional[device.Device]
        """
        return self._device
    
    @device.setter
    def device(self,value: Optional[device.Device] = None) -> None:
        """
        Sets the device property value. The device property
        Args:
            value: Value to set for the device property.
        """
        self._device = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the mobile device as given by the user.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the mobile device as given by the user.
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
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(device.Device)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("device", self.device)
        writer.write_str_value("displayName", self.display_name)
    

