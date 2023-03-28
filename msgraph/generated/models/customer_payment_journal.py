from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import account, customer_payment, entity

from . import entity

class CustomerPaymentJournal(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new customerPaymentJournal and sets the default values.
        """
        super().__init__()
        # The account property
        self._account: Optional[account.Account] = None
        # The balancingAccountId property
        self._balancing_account_id: Optional[UUID] = None
        # The balancingAccountNumber property
        self._balancing_account_number: Optional[str] = None
        # The code property
        self._code: Optional[str] = None
        # The customerPayments property
        self._customer_payments: Optional[List[customer_payment.CustomerPayment]] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def account(self,) -> Optional[account.Account]:
        """
        Gets the account property value. The account property
        Returns: Optional[account.Account]
        """
        return self._account
    
    @account.setter
    def account(self,value: Optional[account.Account] = None) -> None:
        """
        Sets the account property value. The account property
        Args:
            value: Value to set for the account property.
        """
        self._account = value
    
    @property
    def balancing_account_id(self,) -> Optional[UUID]:
        """
        Gets the balancingAccountId property value. The balancingAccountId property
        Returns: Optional[UUID]
        """
        return self._balancing_account_id
    
    @balancing_account_id.setter
    def balancing_account_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the balancingAccountId property value. The balancingAccountId property
        Args:
            value: Value to set for the balancing_account_id property.
        """
        self._balancing_account_id = value
    
    @property
    def balancing_account_number(self,) -> Optional[str]:
        """
        Gets the balancingAccountNumber property value. The balancingAccountNumber property
        Returns: Optional[str]
        """
        return self._balancing_account_number
    
    @balancing_account_number.setter
    def balancing_account_number(self,value: Optional[str] = None) -> None:
        """
        Sets the balancingAccountNumber property value. The balancingAccountNumber property
        Args:
            value: Value to set for the balancing_account_number property.
        """
        self._balancing_account_number = value
    
    @property
    def code(self,) -> Optional[str]:
        """
        Gets the code property value. The code property
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. The code property
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
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
    
    @property
    def customer_payments(self,) -> Optional[List[customer_payment.CustomerPayment]]:
        """
        Gets the customerPayments property value. The customerPayments property
        Returns: Optional[List[customer_payment.CustomerPayment]]
        """
        return self._customer_payments
    
    @customer_payments.setter
    def customer_payments(self,value: Optional[List[customer_payment.CustomerPayment]] = None) -> None:
        """
        Sets the customerPayments property value. The customerPayments property
        Args:
            value: Value to set for the customer_payments property.
        """
        self._customer_payments = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
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
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
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
    

