from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, ios_vpp_app_assigned_device_license, ios_vpp_app_assigned_user_license

from . import entity

class IosVppAppAssignedLicense(entity.Entity):
    """
    iOS Volume Purchase Program license assignment. This class does not support Create, Delete, or Update.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new iosVppAppAssignedLicense and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user email address.
        self._user_email_address: Optional[str] = None
        # The user ID.
        self._user_id: Optional[str] = None
        # The user name.
        self._user_name: Optional[str] = None
        # The user principal name.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppAppAssignedLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignedLicense
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosVppAppAssignedDeviceLicense":
                from . import ios_vpp_app_assigned_device_license

                return ios_vpp_app_assigned_device_license.IosVppAppAssignedDeviceLicense()
            if mapping_value == "#microsoft.graph.iosVppAppAssignedUserLicense":
                from . import ios_vpp_app_assigned_user_license

                return ios_vpp_app_assigned_user_license.IosVppAppAssignedUserLicense()
        return IosVppAppAssignedLicense()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, ios_vpp_app_assigned_device_license, ios_vpp_app_assigned_user_license

        fields: Dict[str, Callable[[Any], None]] = {
            "userEmailAddress": lambda n : setattr(self, 'user_email_address', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("userEmailAddress", self.user_email_address)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_email_address(self,) -> Optional[str]:
        """
        Gets the userEmailAddress property value. The user email address.
        Returns: Optional[str]
        """
        return self._user_email_address
    
    @user_email_address.setter
    def user_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the userEmailAddress property value. The user email address.
        Args:
            value: Value to set for the user_email_address property.
        """
        self._user_email_address = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user ID.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user ID.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The user name.
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The user name.
        Args:
            value: Value to set for the user_name property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

