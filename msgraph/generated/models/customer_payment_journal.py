from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import account, customer_payment, entity

from . import entity

@dataclass
class CustomerPaymentJournal(entity.Entity):
    # The account property
    account: Optional[account.Account] = None
    # The balancingAccountId property
    balancing_account_id: Optional[UUID] = None
    # The balancingAccountNumber property
    balancing_account_number: Optional[str] = None
    # The code property
    code: Optional[str] = None
    # The customerPayments property
    customer_payments: Optional[List[customer_payment.CustomerPayment]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomerPaymentJournal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomerPaymentJournal
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomerPaymentJournal()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account, customer_payment, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(account.Account)),
            "balancingAccountId": lambda n : setattr(self, 'balancing_account_id', n.get_uuid_value()),
            "balancingAccountNumber": lambda n : setattr(self, 'balancing_account_number', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "customerPayments": lambda n : setattr(self, 'customer_payments', n.get_collection_of_object_values(customer_payment.CustomerPayment)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("account", self.account)
        writer.write_uuid_value("balancingAccountId", self.balancing_account_id)
        writer.write_str_value("balancingAccountNumber", self.balancing_account_number)
        writer.write_str_value("code", self.code)
        writer.write_collection_of_object_values("customerPayments", self.customer_payments)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

