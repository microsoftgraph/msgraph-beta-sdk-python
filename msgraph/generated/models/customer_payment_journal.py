from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .account import Account
    from .customer_payment import CustomerPayment

@dataclass
class CustomerPaymentJournal(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The account property
    account: Optional[Account] = None
    # The balancingAccountId property
    balancing_account_id: Optional[UUID] = None
    # The balancingAccountNumber property
    balancing_account_number: Optional[str] = None
    # The code property
    code: Optional[str] = None
    # The customerPayments property
    customer_payments: Optional[List[CustomerPayment]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomerPaymentJournal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerPaymentJournal
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomerPaymentJournal()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account import Account
        from .customer_payment import CustomerPayment

        from .account import Account
        from .customer_payment import CustomerPayment

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(Account)),
            "balancingAccountId": lambda n : setattr(self, 'balancing_account_id', n.get_uuid_value()),
            "balancingAccountNumber": lambda n : setattr(self, 'balancing_account_number', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "customerPayments": lambda n : setattr(self, 'customer_payments', n.get_collection_of_object_values(CustomerPayment)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("account", self.account)
        writer.write_uuid_value("balancingAccountId", self.balancing_account_id)
        writer.write_str_value("balancingAccountNumber", self.balancing_account_number)
        writer.write_str_value("code", self.code)
        writer.write_collection_of_object_values("customerPayments", self.customer_payments)
        writer.write_str_value("displayName", self.display_name)
        writer.write_uuid_value("id", self.id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

