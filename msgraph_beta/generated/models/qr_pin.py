from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class QrPin(Entity, Parsable):
    # PIN of the user. It is between 8-20 digits as configured in the QR code authentication method policy. The code is temporary when issued by admin but permanent after the user changes it at the first login attempt. This PIN can be reset by the admin but not the user.
    code: Optional[str] = None
    # The date and time when the PIN was created.
    created_date_time: Optional[datetime.datetime] = None
    # Defaults to true for a temporary PIN.
    force_change_pin_next_sign_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the PIN was updated.
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrPin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrPin
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrPin()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "forceChangePinNextSignIn": lambda n : setattr(self, 'force_change_pin_next_sign_in', n.get_bool_value()),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("code", self.code)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("forceChangePinNextSignIn", self.force_change_pin_next_sign_in)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
    

