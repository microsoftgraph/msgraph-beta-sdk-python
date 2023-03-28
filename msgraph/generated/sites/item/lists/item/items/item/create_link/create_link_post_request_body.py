from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import drive_recipient

class CreateLinkPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new createLinkPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expirationDateTime property
        self._expiration_date_time: Optional[datetime] = None
        # The password property
        self._password: Optional[str] = None
        # The recipients property
        self._recipients: Optional[List[drive_recipient.DriveRecipient]] = None
        # The retainInheritedPermissions property
        self._retain_inherited_permissions: Optional[bool] = None
        # The scope property
        self._scope: Optional[str] = None
        # The sendNotification property
        self._send_notification: Optional[bool] = None
        # The type property
        self._type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateLinkPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreateLinkPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreateLinkPostRequestBody()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expirationDateTime property
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expirationDateTime property
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import drive_recipient

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(drive_recipient.DriveRecipient)),
            "retainInheritedPermissions": lambda n : setattr(self, 'retain_inherited_permissions', n.get_bool_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "sendNotification": lambda n : setattr(self, 'send_notification', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The password property
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The password property
        Args:
            value: Value to set for the password property.
        """
        self._password = value
    
    @property
    def recipients(self,) -> Optional[List[drive_recipient.DriveRecipient]]:
        """
        Gets the recipients property value. The recipients property
        Returns: Optional[List[drive_recipient.DriveRecipient]]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[List[drive_recipient.DriveRecipient]] = None) -> None:
        """
        Sets the recipients property value. The recipients property
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
    @property
    def retain_inherited_permissions(self,) -> Optional[bool]:
        """
        Gets the retainInheritedPermissions property value. The retainInheritedPermissions property
        Returns: Optional[bool]
        """
        return self._retain_inherited_permissions
    
    @retain_inherited_permissions.setter
    def retain_inherited_permissions(self,value: Optional[bool] = None) -> None:
        """
        Sets the retainInheritedPermissions property value. The retainInheritedPermissions property
        Args:
            value: Value to set for the retain_inherited_permissions property.
        """
        self._retain_inherited_permissions = value
    
    @property
    def scope(self,) -> Optional[str]:
        """
        Gets the scope property value. The scope property
        Returns: Optional[str]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[str] = None) -> None:
        """
        Sets the scope property value. The scope property
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    @property
    def send_notification(self,) -> Optional[bool]:
        """
        Gets the sendNotification property value. The sendNotification property
        Returns: Optional[bool]
        """
        return self._send_notification
    
    @send_notification.setter
    def send_notification(self,value: Optional[bool] = None) -> None:
        """
        Sets the sendNotification property value. The sendNotification property
        Args:
            value: Value to set for the send_notification property.
        """
        self._send_notification = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("password", self.password)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_bool_value("retainInheritedPermissions", self.retain_inherited_permissions)
        writer.write_str_value("scope", self.scope)
        writer.write_bool_value("sendNotification", self.send_notification)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

