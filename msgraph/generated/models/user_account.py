from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account_status

@dataclass
class UserAccount(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The displayName property
    display_name: Optional[str] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The service property
    service: Optional[str] = None
    # The signinName property
    signin_name: Optional[str] = None
    # The status property
    status: Optional[account_status.AccountStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAccount
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserAccount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account_status

        from . import account_status

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "signinName": lambda n : setattr(self, 'signin_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(account_status.AccountStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_str_value("service", self.service)
        writer.write_str_value("signinName", self.signin_name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

