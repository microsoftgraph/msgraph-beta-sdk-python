from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_status import AccountStatus

@dataclass
class UserAccount(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The displayName property
    display_name: Optional[str] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The service property
    service: Optional[str] = None
    # The signinName property
    signin_name: Optional[str] = None
    # The status property
    status: Optional[AccountStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserAccount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserAccount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account_status import AccountStatus

        from .account_status import AccountStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "signinName": lambda n : setattr(self, 'signin_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AccountStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_str_value("service", self.service)
        writer.write_str_value("signinName", self.signin_name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

