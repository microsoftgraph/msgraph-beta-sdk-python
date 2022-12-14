from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

account = lazy_import('msgraph.generated.models.account')
entity = lazy_import('msgraph.generated.models.entity')

class GeneralLedgerEntry(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
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
    def account_id(self,) -> Optional[Guid]:
        """
        Gets the accountId property value. The accountId property
        Returns: Optional[Guid]
        """
        return self._account_id
    
    @account_id.setter
    def account_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the accountId property value. The accountId property
        Args:
            value: Value to set for the accountId property.
        """
        self._account_id = value
    
    @property
    def account_number(self,) -> Optional[str]:
        """
        Gets the accountNumber property value. The accountNumber property
        Returns: Optional[str]
        """
        return self._account_number
    
    @account_number.setter
    def account_number(self,value: Optional[str] = None) -> None:
        """
        Sets the accountNumber property value. The accountNumber property
        Args:
            value: Value to set for the accountNumber property.
        """
        self._account_number = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new generalLedgerEntry and sets the default values.
        """
        super().__init__()
        # The account property
        self._account: Optional[account.Account] = None
        # The accountId property
        self._account_id: Optional[Guid] = None
        # The accountNumber property
        self._account_number: Optional[str] = None
        # The creditAmount property
        self._credit_amount: Optional[float] = None
        # The debitAmount property
        self._debit_amount: Optional[float] = None
        # The description property
        self._description: Optional[str] = None
        # The documentNumber property
        self._document_number: Optional[str] = None
        # The documentType property
        self._document_type: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The postingDate property
        self._posting_date: Optional[Date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GeneralLedgerEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GeneralLedgerEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GeneralLedgerEntry()
    
    @property
    def credit_amount(self,) -> Optional[float]:
        """
        Gets the creditAmount property value. The creditAmount property
        Returns: Optional[float]
        """
        return self._credit_amount
    
    @credit_amount.setter
    def credit_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the creditAmount property value. The creditAmount property
        Args:
            value: Value to set for the creditAmount property.
        """
        self._credit_amount = value
    
    @property
    def debit_amount(self,) -> Optional[float]:
        """
        Gets the debitAmount property value. The debitAmount property
        Returns: Optional[float]
        """
        return self._debit_amount
    
    @debit_amount.setter
    def debit_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the debitAmount property value. The debitAmount property
        Args:
            value: Value to set for the debitAmount property.
        """
        self._debit_amount = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def document_number(self,) -> Optional[str]:
        """
        Gets the documentNumber property value. The documentNumber property
        Returns: Optional[str]
        """
        return self._document_number
    
    @document_number.setter
    def document_number(self,value: Optional[str] = None) -> None:
        """
        Sets the documentNumber property value. The documentNumber property
        Args:
            value: Value to set for the documentNumber property.
        """
        self._document_number = value
    
    @property
    def document_type(self,) -> Optional[str]:
        """
        Gets the documentType property value. The documentType property
        Returns: Optional[str]
        """
        return self._document_type
    
    @document_type.setter
    def document_type(self,value: Optional[str] = None) -> None:
        """
        Sets the documentType property value. The documentType property
        Args:
            value: Value to set for the documentType property.
        """
        self._document_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(account.Account)),
            "account_id": lambda n : setattr(self, 'account_id', n.get_object_value(Guid)),
            "account_number": lambda n : setattr(self, 'account_number', n.get_str_value()),
            "credit_amount": lambda n : setattr(self, 'credit_amount', n.get_float_value()),
            "debit_amount": lambda n : setattr(self, 'debit_amount', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "document_number": lambda n : setattr(self, 'document_number', n.get_str_value()),
            "document_type": lambda n : setattr(self, 'document_type', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "posting_date": lambda n : setattr(self, 'posting_date', n.get_object_value(Date)),
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
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def posting_date(self,) -> Optional[Date]:
        """
        Gets the postingDate property value. The postingDate property
        Returns: Optional[Date]
        """
        return self._posting_date
    
    @posting_date.setter
    def posting_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the postingDate property value. The postingDate property
        Args:
            value: Value to set for the postingDate property.
        """
        self._posting_date = value
    
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
        writer.write_object_value("accountId", self.account_id)
        writer.write_str_value("accountNumber", self.account_number)
        writer.write_float_value("creditAmount", self.credit_amount)
        writer.write_float_value("debitAmount", self.debit_amount)
        writer.write_str_value("description", self.description)
        writer.write_str_value("documentNumber", self.document_number)
        writer.write_str_value("documentType", self.document_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("postingDate", self.posting_date)
    

