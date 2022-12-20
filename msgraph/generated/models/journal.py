from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

account = lazy_import('msgraph.generated.models.account')
entity = lazy_import('msgraph.generated.models.entity')
journal_line = lazy_import('msgraph.generated.models.journal_line')

class Journal(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
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
    def balancing_account_id(self,) -> Optional[Guid]:
        """
        Gets the balancingAccountId property value. The balancingAccountId property
        Returns: Optional[Guid]
        """
        return self._balancing_account_id
    
    @balancing_account_id.setter
    def balancing_account_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the balancingAccountId property value. The balancingAccountId property
        Args:
            value: Value to set for the balancingAccountId property.
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
            value: Value to set for the balancingAccountNumber property.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new journal and sets the default values.
        """
        super().__init__()
        # The account property
        self._account: Optional[account.Account] = None
        # The balancingAccountId property
        self._balancing_account_id: Optional[Guid] = None
        # The balancingAccountNumber property
        self._balancing_account_number: Optional[str] = None
        # The code property
        self._code: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The journalLines property
        self._journal_lines: Optional[List[journal_line.JournalLine]] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Journal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Journal
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Journal()
    
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
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(account.Account)),
            "balancing_account_id": lambda n : setattr(self, 'balancing_account_id', n.get_object_value(Guid)),
            "balancing_account_number": lambda n : setattr(self, 'balancing_account_number', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "journal_lines": lambda n : setattr(self, 'journal_lines', n.get_collection_of_object_values(journal_line.JournalLine)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def journal_lines(self,) -> Optional[List[journal_line.JournalLine]]:
        """
        Gets the journalLines property value. The journalLines property
        Returns: Optional[List[journal_line.JournalLine]]
        """
        return self._journal_lines
    
    @journal_lines.setter
    def journal_lines(self,value: Optional[List[journal_line.JournalLine]] = None) -> None:
        """
        Sets the journalLines property value. The journalLines property
        Args:
            value: Value to set for the journalLines property.
        """
        self._journal_lines = value
    
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
        writer.write_object_value("balancingAccountId", self.balancing_account_id)
        writer.write_str_value("balancingAccountNumber", self.balancing_account_number)
        writer.write_str_value("code", self.code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("journalLines", self.journal_lines)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

