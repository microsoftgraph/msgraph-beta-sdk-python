from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class AgedAccountsPayable(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The agedAsOfDate property
    aged_as_of_date: Optional[datetime.date] = None
    # The balanceDue property
    balance_due: Optional[float] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currentAmount property
    current_amount: Optional[float] = None
    # The id property
    id: Optional[UUID] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The periodLengthFilter property
    period_length_filter: Optional[str] = None
    # The period1Amount property
    period1_amount: Optional[float] = None
    # The period2Amount property
    period2_amount: Optional[float] = None
    # The period3Amount property
    period3_amount: Optional[float] = None
    # The vendorId property
    vendor_id: Optional[str] = None
    # The vendorNumber property
    vendor_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgedAccountsPayable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgedAccountsPayable
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgedAccountsPayable()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "agedAsOfDate": lambda n : setattr(self, 'aged_as_of_date', n.get_date_value()),
            "balanceDue": lambda n : setattr(self, 'balance_due', n.get_float_value()),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currentAmount": lambda n : setattr(self, 'current_amount', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "periodLengthFilter": lambda n : setattr(self, 'period_length_filter', n.get_str_value()),
            "period1Amount": lambda n : setattr(self, 'period1_amount', n.get_float_value()),
            "period2Amount": lambda n : setattr(self, 'period2_amount', n.get_float_value()),
            "period3Amount": lambda n : setattr(self, 'period3_amount', n.get_float_value()),
            "vendorId": lambda n : setattr(self, 'vendor_id', n.get_str_value()),
            "vendorNumber": lambda n : setattr(self, 'vendor_number', n.get_str_value()),
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
        writer.write_date_value("agedAsOfDate", self.aged_as_of_date)
        writer.write_float_value("balanceDue", self.balance_due)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_float_value("currentAmount", self.current_amount)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("periodLengthFilter", self.period_length_filter)
        writer.write_float_value("period1Amount", self.period1_amount)
        writer.write_float_value("period2Amount", self.period2_amount)
        writer.write_float_value("period3Amount", self.period3_amount)
        writer.write_str_value("vendorId", self.vendor_id)
        writer.write_str_value("vendorNumber", self.vendor_number)
        writer.write_additional_data_value(self.additional_data)
    

