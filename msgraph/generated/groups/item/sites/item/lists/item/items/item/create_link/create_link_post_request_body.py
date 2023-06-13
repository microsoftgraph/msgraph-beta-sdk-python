from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models import drive_recipient

@dataclass
class CreateLinkPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The expirationDateTime property
    expiration_date_time: Optional[datetime] = None
    # The password property
    password: Optional[str] = None
    # The recipients property
    recipients: Optional[List[drive_recipient.DriveRecipient]] = None
    # The retainInheritedPermissions property
    retain_inherited_permissions: Optional[bool] = None
    # The scope property
    scope: Optional[str] = None
    # The sendNotification property
    send_notification: Optional[bool] = None
    # The type property
    type: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..........models import drive_recipient

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
    

