from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import currency, customer, entity, payment_term, postal_address_type, sales_credit_memo_line

from . import entity

@dataclass
class SalesCreditMemo(entity.Entity):
    # The billToCustomerId property
    bill_to_customer_id: Optional[UUID] = None
    # The billToCustomerNumber property
    bill_to_customer_number: Optional[str] = None
    # The billToName property
    bill_to_name: Optional[str] = None
    # The billingPostalAddress property
    billing_postal_address: Optional[postal_address_type.PostalAddressType] = None
    # The creditMemoDate property
    credit_memo_date: Optional[date] = None
    # The currency property
    currency: Optional[currency.Currency] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currencyId property
    currency_id: Optional[UUID] = None
    # The customer property
    customer: Optional[customer.Customer] = None
    # The customerId property
    customer_id: Optional[UUID] = None
    # The customerName property
    customer_name: Optional[str] = None
    # The customerNumber property
    customer_number: Optional[str] = None
    # The discountAmount property
    discount_amount: Optional[float] = None
    # The discountAppliedBeforeTax property
    discount_applied_before_tax: Optional[bool] = None
    # The dueDate property
    due_date: Optional[date] = None
    # The email property
    email: Optional[str] = None
    # The externalDocumentNumber property
    external_document_number: Optional[str] = None
    # The invoiceId property
    invoice_id: Optional[UUID] = None
    # The invoiceNumber property
    invoice_number: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The number property
    number: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The paymentTerm property
    payment_term: Optional[payment_term.PaymentTerm] = None
    # The paymentTermsId property
    payment_terms_id: Optional[UUID] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The pricesIncludeTax property
    prices_include_tax: Optional[bool] = None
    # The salesCreditMemoLines property
    sales_credit_memo_lines: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]] = None
    # The salesperson property
    salesperson: Optional[str] = None
    # The sellingPostalAddress property
    selling_postal_address: Optional[postal_address_type.PostalAddressType] = None
    # The status property
    status: Optional[str] = None
    # The totalAmountExcludingTax property
    total_amount_excluding_tax: Optional[float] = None
    # The totalAmountIncludingTax property
    total_amount_including_tax: Optional[float] = None
    # The totalTaxAmount property
    total_tax_amount: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SalesCreditMemo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SalesCreditMemo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SalesCreditMemo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import currency, customer, entity, payment_term, postal_address_type, sales_credit_memo_line

        fields: Dict[str, Callable[[Any], None]] = {
            "billingPostalAddress": lambda n : setattr(self, 'billing_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "billToCustomerId": lambda n : setattr(self, 'bill_to_customer_id', n.get_uuid_value()),
            "billToCustomerNumber": lambda n : setattr(self, 'bill_to_customer_number', n.get_str_value()),
            "billToName": lambda n : setattr(self, 'bill_to_name', n.get_str_value()),
            "creditMemoDate": lambda n : setattr(self, 'credit_memo_date', n.get_date_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(currency.Currency)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currencyId": lambda n : setattr(self, 'currency_id', n.get_uuid_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(customer.Customer)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "customerName": lambda n : setattr(self, 'customer_name', n.get_str_value()),
            "customerNumber": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "discountAmount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discountAppliedBeforeTax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_date_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalDocumentNumber": lambda n : setattr(self, 'external_document_number', n.get_str_value()),
            "invoiceId": lambda n : setattr(self, 'invoice_id', n.get_uuid_value()),
            "invoiceNumber": lambda n : setattr(self, 'invoice_number', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "paymentTerm": lambda n : setattr(self, 'payment_term', n.get_object_value(payment_term.PaymentTerm)),
            "paymentTermsId": lambda n : setattr(self, 'payment_terms_id', n.get_uuid_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "pricesIncludeTax": lambda n : setattr(self, 'prices_include_tax', n.get_bool_value()),
            "salesperson": lambda n : setattr(self, 'salesperson', n.get_str_value()),
            "salesCreditMemoLines": lambda n : setattr(self, 'sales_credit_memo_lines', n.get_collection_of_object_values(sales_credit_memo_line.SalesCreditMemoLine)),
            "sellingPostalAddress": lambda n : setattr(self, 'selling_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "totalAmountExcludingTax": lambda n : setattr(self, 'total_amount_excluding_tax', n.get_float_value()),
            "totalAmountIncludingTax": lambda n : setattr(self, 'total_amount_including_tax', n.get_float_value()),
            "totalTaxAmount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
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
        writer.write_object_value("billingPostalAddress", self.billing_postal_address)
        writer.write_uuid_value("billToCustomerId", self.bill_to_customer_id)
        writer.write_str_value("billToCustomerNumber", self.bill_to_customer_number)
        writer.write_str_value("billToName", self.bill_to_name)
        writer.write_date_value("creditMemoDate", self.credit_memo_date)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_uuid_value("currencyId", self.currency_id)
        writer.write_object_value("customer", self.customer)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_str_value("customerName", self.customer_name)
        writer.write_str_value("customerNumber", self.customer_number)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_date_value("dueDate", self.due_date)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalDocumentNumber", self.external_document_number)
        writer.write_uuid_value("invoiceId", self.invoice_id)
        writer.write_str_value("invoiceNumber", self.invoice_number)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_object_value("paymentTerm", self.payment_term)
        writer.write_uuid_value("paymentTermsId", self.payment_terms_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_bool_value("pricesIncludeTax", self.prices_include_tax)
        writer.write_str_value("salesperson", self.salesperson)
        writer.write_collection_of_object_values("salesCreditMemoLines", self.sales_credit_memo_lines)
        writer.write_object_value("sellingPostalAddress", self.selling_postal_address)
        writer.write_str_value("status", self.status)
        writer.write_float_value("totalAmountExcludingTax", self.total_amount_excluding_tax)
        writer.write_float_value("totalAmountIncludingTax", self.total_amount_including_tax)
        writer.write_float_value("totalTaxAmount", self.total_tax_amount)
    

