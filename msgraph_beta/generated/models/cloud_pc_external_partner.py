from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcExternalPartner(Entity, Parsable):
    # The connectionStatus property
    connection_status: Optional[CloudPcExternalPartnerStatus] = None
    # The enableConnection property
    enable_connection: Optional[bool] = None
    # The lastSyncDateTime property
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The partnerId property
    partner_id: Optional[str] = None
    # The statusDetails property
    status_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcExternalPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcExternalPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcExternalPartner()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
        from .entity import Entity

        from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "connectionStatus": lambda n : setattr(self, 'connection_status', n.get_enum_value(CloudPcExternalPartnerStatus)),
            "enableConnection": lambda n : setattr(self, 'enable_connection', n.get_bool_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "partnerId": lambda n : setattr(self, 'partner_id', n.get_str_value()),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_str_value()),
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
        writer.write_enum_value("connectionStatus", self.connection_status)
        writer.write_bool_value("enableConnection", self.enable_connection)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("partnerId", self.partner_id)
        writer.write_str_value("statusDetails", self.status_details)
    

