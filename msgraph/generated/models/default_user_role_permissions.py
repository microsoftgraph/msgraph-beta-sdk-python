from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DefaultUserRolePermissions(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new defaultUserRolePermissions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the default user role can create applications.
        self._allowed_to_create_apps: Optional[bool] = None
        # Indicates whether the default user role can create security groups.
        self._allowed_to_create_security_groups: Optional[bool] = None
        # Indicates whether the registered owners of a device can read their own BitLocker recovery keys with default user role.
        self._allowed_to_read_bitlocker_keys_for_owned_device: Optional[bool] = None
        # Indicates whether the default user role can read other users.
        self._allowed_to_read_other_users: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allowed_to_create_apps(self,) -> Optional[bool]:
        """
        Gets the allowedToCreateApps property value. Indicates whether the default user role can create applications.
        Returns: Optional[bool]
        """
        return self._allowed_to_create_apps
    
    @allowed_to_create_apps.setter
    def allowed_to_create_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToCreateApps property value. Indicates whether the default user role can create applications.
        Args:
            value: Value to set for the allowed_to_create_apps property.
        """
        self._allowed_to_create_apps = value
    
    @property
    def allowed_to_create_security_groups(self,) -> Optional[bool]:
        """
        Gets the allowedToCreateSecurityGroups property value. Indicates whether the default user role can create security groups.
        Returns: Optional[bool]
        """
        return self._allowed_to_create_security_groups
    
    @allowed_to_create_security_groups.setter
    def allowed_to_create_security_groups(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToCreateSecurityGroups property value. Indicates whether the default user role can create security groups.
        Args:
            value: Value to set for the allowed_to_create_security_groups property.
        """
        self._allowed_to_create_security_groups = value
    
    @property
    def allowed_to_read_bitlocker_keys_for_owned_device(self,) -> Optional[bool]:
        """
        Gets the allowedToReadBitlockerKeysForOwnedDevice property value. Indicates whether the registered owners of a device can read their own BitLocker recovery keys with default user role.
        Returns: Optional[bool]
        """
        return self._allowed_to_read_bitlocker_keys_for_owned_device
    
    @allowed_to_read_bitlocker_keys_for_owned_device.setter
    def allowed_to_read_bitlocker_keys_for_owned_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToReadBitlockerKeysForOwnedDevice property value. Indicates whether the registered owners of a device can read their own BitLocker recovery keys with default user role.
        Args:
            value: Value to set for the allowed_to_read_bitlocker_keys_for_owned_device property.
        """
        self._allowed_to_read_bitlocker_keys_for_owned_device = value
    
    @property
    def allowed_to_read_other_users(self,) -> Optional[bool]:
        """
        Gets the allowedToReadOtherUsers property value. Indicates whether the default user role can read other users.
        Returns: Optional[bool]
        """
        return self._allowed_to_read_other_users
    
    @allowed_to_read_other_users.setter
    def allowed_to_read_other_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToReadOtherUsers property value. Indicates whether the default user role can read other users.
        Args:
            value: Value to set for the allowed_to_read_other_users property.
        """
        self._allowed_to_read_other_users = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DefaultUserRolePermissions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DefaultUserRolePermissions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DefaultUserRolePermissions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowedToCreateApps": lambda n : setattr(self, 'allowed_to_create_apps', n.get_bool_value()),
            "allowedToCreateSecurityGroups": lambda n : setattr(self, 'allowed_to_create_security_groups', n.get_bool_value()),
            "allowedToReadBitlockerKeysForOwnedDevice": lambda n : setattr(self, 'allowed_to_read_bitlocker_keys_for_owned_device', n.get_bool_value()),
            "allowedToReadOtherUsers": lambda n : setattr(self, 'allowed_to_read_other_users', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowedToCreateApps", self.allowed_to_create_apps)
        writer.write_bool_value("allowedToCreateSecurityGroups", self.allowed_to_create_security_groups)
        writer.write_bool_value("allowedToReadBitlockerKeysForOwnedDevice", self.allowed_to_read_bitlocker_keys_for_owned_device)
        writer.write_bool_value("allowedToReadOtherUsers", self.allowed_to_read_other_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

