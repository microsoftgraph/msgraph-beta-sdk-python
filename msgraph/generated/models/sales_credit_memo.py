from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

currency = lazy_import('msgraph.generated.models.currency')
customer = lazy_import('msgraph.generated.models.customer')
entity = lazy_import('msgraph.generated.models.entity')
payment_term = lazy_import('msgraph.generated.models.payment_term')
postal_address_type = lazy_import('msgraph.generated.models.postal_address_type')
sales_credit_memo_line = lazy_import('msgraph.generated.models.sales_credit_memo_line')

class SalesCreditMemo(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def billing_postal_address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the billingPostalAddress property value. The billingPostalAddress property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._billing_postal_address
    
    @billing_postal_address.setter
    def billing_postal_address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the billingPostalAddress property value. The billingPostalAddress property
        Args:
            value: Value to set for the billingPostalAddress property.
        """
        self._billing_postal_address = value
    
    @property
    def bill_to_customer_id(self,) -> Optional[Guid]:
        """
        Gets the billToCustomerId property value. The billToCustomerId property
        Returns: Optional[Guid]
        """
        return self._bill_to_customer_id
    
    @bill_to_customer_id.setter
    def bill_to_customer_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the billToCustomerId property value. The billToCustomerId property
        Args:
            value: Value to set for the billToCustomerId property.
        """
        self._bill_to_customer_id = value
    
    @property
    def bill_to_customer_number(self,) -> Optional[str]:
        """
        Gets the billToCustomerNumber property value. The billToCustomerNumber property
        Returns: Optional[str]
        """
        return self._bill_to_customer_number
    
    @bill_to_customer_number.setter
    def bill_to_customer_number(self,value: Optional[str] = None) -> None:
        """
        Sets the billToCustomerNumber property value. The billToCustomerNumber property
        Args:
            value: Value to set for the billToCustomerNumber property.
        """
        self._bill_to_customer_number = value
    
    @property
    def bill_to_name(self,) -> Optional[str]:
        """
        Gets the billToName property value. The billToName property
        Returns: Optional[str]
        """
        return self._bill_to_name
    
    @bill_to_name.setter
    def bill_to_name(self,value: Optional[str] = None) -> None:
        """
        Sets the billToName property value. The billToName property
        Args:
            value: Value to set for the billToName property.
        """
        self._bill_to_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new salesCreditMemo and sets the default values.
        """
        super().__init__()
        # The billingPostalAddress property
        self._billing_postal_address: Optional[postal_address_type.PostalAddressType] = None
        # The billToCustomerId property
        self._bill_to_customer_id: Optional[Guid] = None
        # The billToCustomerNumber property
        self._bill_to_customer_number: Optional[str] = None
        # The billToName property
        self._bill_to_name: Optional[str] = None
        # The creditMemoDate property
        self._credit_memo_date: Optional[Date] = None
        # The currency property
        self._currency: Optional[currency.Currency] = None
        # The currencyCode property
        self._currency_code: Optional[str] = None
        # The currencyId property
        self._currency_id: Optional[Guid] = None
        # The customer property
        self._customer: Optional[customer.Customer] = None
        # The customerId property
        self._customer_id: Optional[Guid] = None
        # The customerName property
        self._customer_name: Optional[str] = None
        # The customerNumber property
        self._customer_number: Optional[str] = None
        # The discountAmount property
        self._discount_amount: Optional[float] = None
        # The discountAppliedBeforeTax property
        self._discount_applied_before_tax: Optional[bool] = None
        # The dueDate property
        self._due_date: Optional[Date] = None
        # The email property
        self._email: Optional[str] = None
        # The externalDocumentNumber property
        self._external_document_number: Optional[str] = None
        # The invoiceId property
        self._invoice_id: Optional[Guid] = None
        # The invoiceNumber property
        self._invoice_number: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The paymentTerm property
        self._payment_term: Optional[payment_term.PaymentTerm] = None
        # The paymentTermsId property
        self._payment_terms_id: Optional[Guid] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
        # The pricesIncludeTax property
        self._prices_include_tax: Optional[bool] = None
        # The salesCreditMemoLines property
        self._sales_credit_memo_lines: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]] = None
        # The salesperson property
        self._salesperson: Optional[str] = None
        # The sellingPostalAddress property
        self._selling_postal_address: Optional[postal_address_type.PostalAddressType] = None
        # The status property
        self._status: Optional[str] = None
        # The totalAmountExcludingTax property
        self._total_amount_excluding_tax: Optional[float] = None
        # The totalAmountIncludingTax property
        self._total_amount_including_tax: Optional[float] = None
        # The totalTaxAmount property
        self._total_tax_amount: Optional[float] = None
    
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
    
    @property
    def credit_memo_date(self,) -> Optional[Date]:
        """
        Gets the creditMemoDate property value. The creditMemoDate property
        Returns: Optional[Date]
        """
        return self._credit_memo_date
    
    @credit_memo_date.setter
    def credit_memo_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the creditMemoDate property value. The creditMemoDate property
        Args:
            value: Value to set for the creditMemoDate property.
        """
        self._credit_memo_date = value
    
    @property
    def currency(self,) -> Optional[currency.Currency]:
        """
        Gets the currency property value. The currency property
        Returns: Optional[currency.Currency]
        """
        return self._currency
    
    @currency.setter
    def currency(self,value: Optional[currency.Currency] = None) -> None:
        """
        Sets the currency property value. The currency property
        Args:
            value: Value to set for the currency property.
        """
        self._currency = value
    
    @property
    def currency_code(self,) -> Optional[str]:
        """
        Gets the currencyCode property value. The currencyCode property
        Returns: Optional[str]
        """
        return self._currency_code
    
    @currency_code.setter
    def currency_code(self,value: Optional[str] = None) -> None:
        """
        Sets the currencyCode property value. The currencyCode property
        Args:
            value: Value to set for the currencyCode property.
        """
        self._currency_code = value
    
    @property
    def currency_id(self,) -> Optional[Guid]:
        """
        Gets the currencyId property value. The currencyId property
        Returns: Optional[Guid]
        """
        return self._currency_id
    
    @currency_id.setter
    def currency_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the currencyId property value. The currencyId property
        Args:
            value: Value to set for the currencyId property.
        """
        self._currency_id = value
    
    @property
    def customer(self,) -> Optional[customer.Customer]:
        """
        Gets the customer property value. The customer property
        Returns: Optional[customer.Customer]
        """
        return self._customer
    
    @customer.setter
    def customer(self,value: Optional[customer.Customer] = None) -> None:
        """
        Sets the customer property value. The customer property
        Args:
            value: Value to set for the customer property.
        """
        self._customer = value
    
    @property
    def customer_id(self,) -> Optional[Guid]:
        """
        Gets the customerId property value. The customerId property
        Returns: Optional[Guid]
        """
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the customerId property value. The customerId property
        Args:
            value: Value to set for the customerId property.
        """
        self._customer_id = value
    
    @property
    def customer_name(self,) -> Optional[str]:
        """
        Gets the customerName property value. The customerName property
        Returns: Optional[str]
        """
        return self._customer_name
    
    @customer_name.setter
    def customer_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customerName property value. The customerName property
        Args:
            value: Value to set for the customerName property.
        """
        self._customer_name = value
    
    @property
    def customer_number(self,) -> Optional[str]:
        """
        Gets the customerNumber property value. The customerNumber property
        Returns: Optional[str]
        """
        return self._customer_number
    
    @customer_number.setter
    def customer_number(self,value: Optional[str] = None) -> None:
        """
        Sets the customerNumber property value. The customerNumber property
        Args:
            value: Value to set for the customerNumber property.
        """
        self._customer_number = value
    
    @property
    def discount_amount(self,) -> Optional[float]:
        """
        Gets the discountAmount property value. The discountAmount property
        Returns: Optional[float]
        """
        return self._discount_amount
    
    @discount_amount.setter
    def discount_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the discountAmount property value. The discountAmount property
        Args:
            value: Value to set for the discountAmount property.
        """
        self._discount_amount = value
    
    @property
    def discount_applied_before_tax(self,) -> Optional[bool]:
        """
        Gets the discountAppliedBeforeTax property value. The discountAppliedBeforeTax property
        Returns: Optional[bool]
        """
        return self._discount_applied_before_tax
    
    @discount_applied_before_tax.setter
    def discount_applied_before_tax(self,value: Optional[bool] = None) -> None:
        """
        Sets the discountAppliedBeforeTax property value. The discountAppliedBeforeTax property
        Args:
            value: Value to set for the discountAppliedBeforeTax property.
        """
        self._discount_applied_before_tax = value
    
    @property
    def due_date(self,) -> Optional[Date]:
        """
        Gets the dueDate property value. The dueDate property
        Returns: Optional[Date]
        """
        return self._due_date
    
    @due_date.setter
    def due_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the dueDate property value. The dueDate property
        Args:
            value: Value to set for the dueDate property.
        """
        self._due_date = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email property
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email property
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    @property
    def external_document_number(self,) -> Optional[str]:
        """
        Gets the externalDocumentNumber property value. The externalDocumentNumber property
        Returns: Optional[str]
        """
        return self._external_document_number
    
    @external_document_number.setter
    def external_document_number(self,value: Optional[str] = None) -> None:
        """
        Sets the externalDocumentNumber property value. The externalDocumentNumber property
        Args:
            value: Value to set for the externalDocumentNumber property.
        """
        self._external_document_number = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "billing_postal_address": lambda n : setattr(self, 'billing_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "bill_to_customer_id": lambda n : setattr(self, 'bill_to_customer_id', n.get_object_value(Guid)),
            "bill_to_customer_number": lambda n : setattr(self, 'bill_to_customer_number', n.get_str_value()),
            "bill_to_name": lambda n : setattr(self, 'bill_to_name', n.get_str_value()),
            "credit_memo_date": lambda n : setattr(self, 'credit_memo_date', n.get_object_value(Date)),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(currency.Currency)),
            "currency_code": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currency_id": lambda n : setattr(self, 'currency_id', n.get_object_value(Guid)),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(customer.Customer)),
            "customer_id": lambda n : setattr(self, 'customer_id', n.get_object_value(Guid)),
            "customer_name": lambda n : setattr(self, 'customer_name', n.get_str_value()),
            "customer_number": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "discount_amount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discount_applied_before_tax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "due_date": lambda n : setattr(self, 'due_date', n.get_object_value(Date)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "external_document_number": lambda n : setattr(self, 'external_document_number', n.get_str_value()),
            "invoice_id": lambda n : setattr(self, 'invoice_id', n.get_object_value(Guid)),
            "invoice_number": lambda n : setattr(self, 'invoice_number', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "payment_term": lambda n : setattr(self, 'payment_term', n.get_object_value(payment_term.PaymentTerm)),
            "payment_terms_id": lambda n : setattr(self, 'payment_terms_id', n.get_object_value(Guid)),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "prices_include_tax": lambda n : setattr(self, 'prices_include_tax', n.get_bool_value()),
            "sales_credit_memo_lines": lambda n : setattr(self, 'sales_credit_memo_lines', n.get_collection_of_object_values(sales_credit_memo_line.SalesCreditMemoLine)),
            "salesperson": lambda n : setattr(self, 'salesperson', n.get_str_value()),
            "selling_postal_address": lambda n : setattr(self, 'selling_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "total_amount_excluding_tax": lambda n : setattr(self, 'total_amount_excluding_tax', n.get_float_value()),
            "total_amount_including_tax": lambda n : setattr(self, 'total_amount_including_tax', n.get_float_value()),
            "total_tax_amount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invoice_id(self,) -> Optional[Guid]:
        """
        Gets the invoiceId property value. The invoiceId property
        Returns: Optional[Guid]
        """
        return self._invoice_id
    
    @invoice_id.setter
    def invoice_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the invoiceId property value. The invoiceId property
        Args:
            value: Value to set for the invoiceId property.
        """
        self._invoice_id = value
    
    @property
    def invoice_number(self,) -> Optional[str]:
        """
        Gets the invoiceNumber property value. The invoiceNumber property
        Returns: Optional[str]
        """
        return self._invoice_number
    
    @invoice_number.setter
    def invoice_number(self,value: Optional[str] = None) -> None:
        """
        Sets the invoiceNumber property value. The invoiceNumber property
        Args:
            value: Value to set for the invoiceNumber property.
        """
        self._invoice_number = value
    
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
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. The number property
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    @property
    def payment_term(self,) -> Optional[payment_term.PaymentTerm]:
        """
        Gets the paymentTerm property value. The paymentTerm property
        Returns: Optional[payment_term.PaymentTerm]
        """
        return self._payment_term
    
    @payment_term.setter
    def payment_term(self,value: Optional[payment_term.PaymentTerm] = None) -> None:
        """
        Sets the paymentTerm property value. The paymentTerm property
        Args:
            value: Value to set for the paymentTerm property.
        """
        self._payment_term = value
    
    @property
    def payment_terms_id(self,) -> Optional[Guid]:
        """
        Gets the paymentTermsId property value. The paymentTermsId property
        Returns: Optional[Guid]
        """
        return self._payment_terms_id
    
    @payment_terms_id.setter
    def payment_terms_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the paymentTermsId property value. The paymentTermsId property
        Args:
            value: Value to set for the paymentTermsId property.
        """
        self._payment_terms_id = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. The phoneNumber property
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. The phoneNumber property
        Args:
            value: Value to set for the phoneNumber property.
        """
        self._phone_number = value
    
    @property
    def prices_include_tax(self,) -> Optional[bool]:
        """
        Gets the pricesIncludeTax property value. The pricesIncludeTax property
        Returns: Optional[bool]
        """
        return self._prices_include_tax
    
    @prices_include_tax.setter
    def prices_include_tax(self,value: Optional[bool] = None) -> None:
        """
        Sets the pricesIncludeTax property value. The pricesIncludeTax property
        Args:
            value: Value to set for the pricesIncludeTax property.
        """
        self._prices_include_tax = value
    
    @property
    def sales_credit_memo_lines(self,) -> Optional[List[sales_credit_memo_line.SalesCreditMemoLine]]:
        """
        Gets the salesCreditMemoLines property value. The salesCreditMemoLines property
        Returns: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]]
        """
        return self._sales_credit_memo_lines
    
    @sales_credit_memo_lines.setter
    def sales_credit_memo_lines(self,value: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]] = None) -> None:
        """
        Sets the salesCreditMemoLines property value. The salesCreditMemoLines property
        Args:
            value: Value to set for the salesCreditMemoLines property.
        """
        self._sales_credit_memo_lines = value
    
    @property
    def salesperson(self,) -> Optional[str]:
        """
        Gets the salesperson property value. The salesperson property
        Returns: Optional[str]
        """
        return self._salesperson
    
    @salesperson.setter
    def salesperson(self,value: Optional[str] = None) -> None:
        """
        Sets the salesperson property value. The salesperson property
        Args:
            value: Value to set for the salesperson property.
        """
        self._salesperson = value
    
    @property
    def selling_postal_address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the sellingPostalAddress property value. The sellingPostalAddress property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._selling_postal_address
    
    @selling_postal_address.setter
    def selling_postal_address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the sellingPostalAddress property value. The sellingPostalAddress property
        Args:
            value: Value to set for the sellingPostalAddress property.
        """
        self._selling_postal_address = value
    
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
        writer.write_object_value("billToCustomerId", self.bill_to_customer_id)
        writer.write_str_value("billToCustomerNumber", self.bill_to_customer_number)
        writer.write_str_value("billToName", self.bill_to_name)
        writer.write_object_value("creditMemoDate", self.credit_memo_date)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_object_value("currencyId", self.currency_id)
        writer.write_object_value("customer", self.customer)
        writer.write_object_value("customerId", self.customer_id)
        writer.write_str_value("customerName", self.customer_name)
        writer.write_str_value("customerNumber", self.customer_number)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_object_value("dueDate", self.due_date)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalDocumentNumber", self.external_document_number)
        writer.write_object_value("invoiceId", self.invoice_id)
        writer.write_str_value("invoiceNumber", self.invoice_number)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_object_value("paymentTerm", self.payment_term)
        writer.write_object_value("paymentTermsId", self.payment_terms_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_bool_value("pricesIncludeTax", self.prices_include_tax)
        writer.write_collection_of_object_values("salesCreditMemoLines", self.sales_credit_memo_lines)
        writer.write_str_value("salesperson", self.salesperson)
        writer.write_object_value("sellingPostalAddress", self.selling_postal_address)
        writer.write_str_value("status", self.status)
        writer.write_float_value("totalAmountExcludingTax", self.total_amount_excluding_tax)
        writer.write_float_value("totalAmountIncludingTax", self.total_amount_including_tax)
        writer.write_float_value("totalTaxAmount", self.total_tax_amount)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def total_amount_excluding_tax(self,) -> Optional[float]:
        """
        Gets the totalAmountExcludingTax property value. The totalAmountExcludingTax property
        Returns: Optional[float]
        """
        return self._total_amount_excluding_tax
    
    @total_amount_excluding_tax.setter
    def total_amount_excluding_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the totalAmountExcludingTax property value. The totalAmountExcludingTax property
        Args:
            value: Value to set for the totalAmountExcludingTax property.
        """
        self._total_amount_excluding_tax = value
    
    @property
    def total_amount_including_tax(self,) -> Optional[float]:
        """
        Gets the totalAmountIncludingTax property value. The totalAmountIncludingTax property
        Returns: Optional[float]
        """
        return self._total_amount_including_tax
    
    @total_amount_including_tax.setter
    def total_amount_including_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the totalAmountIncludingTax property value. The totalAmountIncludingTax property
        Args:
            value: Value to set for the totalAmountIncludingTax property.
        """
        self._total_amount_including_tax = value
    
    @property
    def total_tax_amount(self,) -> Optional[float]:
        """
        Gets the totalTaxAmount property value. The totalTaxAmount property
        Returns: Optional[float]
        """
        return self._total_tax_amount
    
    @total_tax_amount.setter
    def total_tax_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the totalTaxAmount property value. The totalTaxAmount property
        Args:
            value: Value to set for the totalTaxAmount property.
        """
        self._total_tax_amount = value
    

