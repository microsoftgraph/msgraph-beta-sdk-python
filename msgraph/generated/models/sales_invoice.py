from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import currency, customer, entity, payment_term, postal_address_type, sales_invoice_line, shipment_method

from . import entity

class SalesInvoice(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new salesInvoice and sets the default values.
        """
        super().__init__()
        # The billToCustomerId property
        self._bill_to_customer_id: Optional[UUID] = None
        # The billToCustomerNumber property
        self._bill_to_customer_number: Optional[str] = None
        # The billToName property
        self._bill_to_name: Optional[str] = None
        # The billingPostalAddress property
        self._billing_postal_address: Optional[postal_address_type.PostalAddressType] = None
        # The currency property
        self._currency: Optional[currency.Currency] = None
        # The currencyCode property
        self._currency_code: Optional[str] = None
        # The currencyId property
        self._currency_id: Optional[UUID] = None
        # The customer property
        self._customer: Optional[customer.Customer] = None
        # The customerId property
        self._customer_id: Optional[UUID] = None
        # The customerName property
        self._customer_name: Optional[str] = None
        # The customerNumber property
        self._customer_number: Optional[str] = None
        # The customerPurchaseOrderReference property
        self._customer_purchase_order_reference: Optional[str] = None
        # The discountAmount property
        self._discount_amount: Optional[float] = None
        # The discountAppliedBeforeTax property
        self._discount_applied_before_tax: Optional[bool] = None
        # The dueDate property
        self._due_date: Optional[date] = None
        # The email property
        self._email: Optional[str] = None
        # The externalDocumentNumber property
        self._external_document_number: Optional[str] = None
        # The invoiceDate property
        self._invoice_date: Optional[date] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The orderId property
        self._order_id: Optional[UUID] = None
        # The orderNumber property
        self._order_number: Optional[str] = None
        # The paymentTerm property
        self._payment_term: Optional[payment_term.PaymentTerm] = None
        # The paymentTermsId property
        self._payment_terms_id: Optional[UUID] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
        # The pricesIncludeTax property
        self._prices_include_tax: Optional[bool] = None
        # The salesInvoiceLines property
        self._sales_invoice_lines: Optional[List[sales_invoice_line.SalesInvoiceLine]] = None
        # The salesperson property
        self._salesperson: Optional[str] = None
        # The sellingPostalAddress property
        self._selling_postal_address: Optional[postal_address_type.PostalAddressType] = None
        # The shipToContact property
        self._ship_to_contact: Optional[str] = None
        # The shipToName property
        self._ship_to_name: Optional[str] = None
        # The shipmentMethod property
        self._shipment_method: Optional[shipment_method.ShipmentMethod] = None
        # The shipmentMethodId property
        self._shipment_method_id: Optional[UUID] = None
        # The shippingPostalAddress property
        self._shipping_postal_address: Optional[postal_address_type.PostalAddressType] = None
        # The status property
        self._status: Optional[str] = None
        # The totalAmountExcludingTax property
        self._total_amount_excluding_tax: Optional[float] = None
        # The totalAmountIncludingTax property
        self._total_amount_including_tax: Optional[float] = None
        # The totalTaxAmount property
        self._total_tax_amount: Optional[float] = None
    
    @property
    def bill_to_customer_id(self,) -> Optional[UUID]:
        """
        Gets the billToCustomerId property value. The billToCustomerId property
        Returns: Optional[UUID]
        """
        return self._bill_to_customer_id
    
    @bill_to_customer_id.setter
    def bill_to_customer_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the billToCustomerId property value. The billToCustomerId property
        Args:
            value: Value to set for the bill_to_customer_id property.
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
            value: Value to set for the bill_to_customer_number property.
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
            value: Value to set for the bill_to_name property.
        """
        self._bill_to_name = value
    
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
            value: Value to set for the billing_postal_address property.
        """
        self._billing_postal_address = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SalesInvoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SalesInvoice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SalesInvoice()
    
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
            value: Value to set for the currency_code property.
        """
        self._currency_code = value
    
    @property
    def currency_id(self,) -> Optional[UUID]:
        """
        Gets the currencyId property value. The currencyId property
        Returns: Optional[UUID]
        """
        return self._currency_id
    
    @currency_id.setter
    def currency_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the currencyId property value. The currencyId property
        Args:
            value: Value to set for the currency_id property.
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
    def customer_id(self,) -> Optional[UUID]:
        """
        Gets the customerId property value. The customerId property
        Returns: Optional[UUID]
        """
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the customerId property value. The customerId property
        Args:
            value: Value to set for the customer_id property.
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
            value: Value to set for the customer_name property.
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
            value: Value to set for the customer_number property.
        """
        self._customer_number = value
    
    @property
    def customer_purchase_order_reference(self,) -> Optional[str]:
        """
        Gets the customerPurchaseOrderReference property value. The customerPurchaseOrderReference property
        Returns: Optional[str]
        """
        return self._customer_purchase_order_reference
    
    @customer_purchase_order_reference.setter
    def customer_purchase_order_reference(self,value: Optional[str] = None) -> None:
        """
        Sets the customerPurchaseOrderReference property value. The customerPurchaseOrderReference property
        Args:
            value: Value to set for the customer_purchase_order_reference property.
        """
        self._customer_purchase_order_reference = value
    
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
            value: Value to set for the discount_amount property.
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
            value: Value to set for the discount_applied_before_tax property.
        """
        self._discount_applied_before_tax = value
    
    @property
    def due_date(self,) -> Optional[date]:
        """
        Gets the dueDate property value. The dueDate property
        Returns: Optional[date]
        """
        return self._due_date
    
    @due_date.setter
    def due_date(self,value: Optional[date] = None) -> None:
        """
        Sets the dueDate property value. The dueDate property
        Args:
            value: Value to set for the due_date property.
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
            value: Value to set for the external_document_number property.
        """
        self._external_document_number = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import currency, customer, entity, payment_term, postal_address_type, sales_invoice_line, shipment_method

        fields: Dict[str, Callable[[Any], None]] = {
            "billingPostalAddress": lambda n : setattr(self, 'billing_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "billToCustomerId": lambda n : setattr(self, 'bill_to_customer_id', n.get_uuid_value()),
            "billToCustomerNumber": lambda n : setattr(self, 'bill_to_customer_number', n.get_str_value()),
            "billToName": lambda n : setattr(self, 'bill_to_name', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(currency.Currency)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currencyId": lambda n : setattr(self, 'currency_id', n.get_uuid_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(customer.Customer)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "customerName": lambda n : setattr(self, 'customer_name', n.get_str_value()),
            "customerNumber": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "customerPurchaseOrderReference": lambda n : setattr(self, 'customer_purchase_order_reference', n.get_str_value()),
            "discountAmount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discountAppliedBeforeTax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_date_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalDocumentNumber": lambda n : setattr(self, 'external_document_number', n.get_str_value()),
            "invoiceDate": lambda n : setattr(self, 'invoice_date', n.get_date_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "orderId": lambda n : setattr(self, 'order_id', n.get_uuid_value()),
            "orderNumber": lambda n : setattr(self, 'order_number', n.get_str_value()),
            "paymentTerm": lambda n : setattr(self, 'payment_term', n.get_object_value(payment_term.PaymentTerm)),
            "paymentTermsId": lambda n : setattr(self, 'payment_terms_id', n.get_uuid_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "pricesIncludeTax": lambda n : setattr(self, 'prices_include_tax', n.get_bool_value()),
            "salesperson": lambda n : setattr(self, 'salesperson', n.get_str_value()),
            "salesInvoiceLines": lambda n : setattr(self, 'sales_invoice_lines', n.get_collection_of_object_values(sales_invoice_line.SalesInvoiceLine)),
            "sellingPostalAddress": lambda n : setattr(self, 'selling_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "shipmentMethod": lambda n : setattr(self, 'shipment_method', n.get_object_value(shipment_method.ShipmentMethod)),
            "shipmentMethodId": lambda n : setattr(self, 'shipment_method_id', n.get_uuid_value()),
            "shippingPostalAddress": lambda n : setattr(self, 'shipping_postal_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "shipToContact": lambda n : setattr(self, 'ship_to_contact', n.get_str_value()),
            "shipToName": lambda n : setattr(self, 'ship_to_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "totalAmountExcludingTax": lambda n : setattr(self, 'total_amount_excluding_tax', n.get_float_value()),
            "totalAmountIncludingTax": lambda n : setattr(self, 'total_amount_including_tax', n.get_float_value()),
            "totalTaxAmount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invoice_date(self,) -> Optional[date]:
        """
        Gets the invoiceDate property value. The invoiceDate property
        Returns: Optional[date]
        """
        return self._invoice_date
    
    @invoice_date.setter
    def invoice_date(self,value: Optional[date] = None) -> None:
        """
        Sets the invoiceDate property value. The invoiceDate property
        Args:
            value: Value to set for the invoice_date property.
        """
        self._invoice_date = value
    
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
    def order_id(self,) -> Optional[UUID]:
        """
        Gets the orderId property value. The orderId property
        Returns: Optional[UUID]
        """
        return self._order_id
    
    @order_id.setter
    def order_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the orderId property value. The orderId property
        Args:
            value: Value to set for the order_id property.
        """
        self._order_id = value
    
    @property
    def order_number(self,) -> Optional[str]:
        """
        Gets the orderNumber property value. The orderNumber property
        Returns: Optional[str]
        """
        return self._order_number
    
    @order_number.setter
    def order_number(self,value: Optional[str] = None) -> None:
        """
        Sets the orderNumber property value. The orderNumber property
        Args:
            value: Value to set for the order_number property.
        """
        self._order_number = value
    
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
            value: Value to set for the payment_term property.
        """
        self._payment_term = value
    
    @property
    def payment_terms_id(self,) -> Optional[UUID]:
        """
        Gets the paymentTermsId property value. The paymentTermsId property
        Returns: Optional[UUID]
        """
        return self._payment_terms_id
    
    @payment_terms_id.setter
    def payment_terms_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the paymentTermsId property value. The paymentTermsId property
        Args:
            value: Value to set for the payment_terms_id property.
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
            value: Value to set for the phone_number property.
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
            value: Value to set for the prices_include_tax property.
        """
        self._prices_include_tax = value
    
    @property
    def sales_invoice_lines(self,) -> Optional[List[sales_invoice_line.SalesInvoiceLine]]:
        """
        Gets the salesInvoiceLines property value. The salesInvoiceLines property
        Returns: Optional[List[sales_invoice_line.SalesInvoiceLine]]
        """
        return self._sales_invoice_lines
    
    @sales_invoice_lines.setter
    def sales_invoice_lines(self,value: Optional[List[sales_invoice_line.SalesInvoiceLine]] = None) -> None:
        """
        Sets the salesInvoiceLines property value. The salesInvoiceLines property
        Args:
            value: Value to set for the sales_invoice_lines property.
        """
        self._sales_invoice_lines = value
    
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
            value: Value to set for the selling_postal_address property.
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
        writer.write_uuid_value("billToCustomerId", self.bill_to_customer_id)
        writer.write_str_value("billToCustomerNumber", self.bill_to_customer_number)
        writer.write_str_value("billToName", self.bill_to_name)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_uuid_value("currencyId", self.currency_id)
        writer.write_object_value("customer", self.customer)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_str_value("customerName", self.customer_name)
        writer.write_str_value("customerNumber", self.customer_number)
        writer.write_str_value("customerPurchaseOrderReference", self.customer_purchase_order_reference)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_date_value("dueDate", self.due_date)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalDocumentNumber", self.external_document_number)
        writer.write_date_value("invoiceDate", self.invoice_date)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_uuid_value("orderId", self.order_id)
        writer.write_str_value("orderNumber", self.order_number)
        writer.write_object_value("paymentTerm", self.payment_term)
        writer.write_uuid_value("paymentTermsId", self.payment_terms_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_bool_value("pricesIncludeTax", self.prices_include_tax)
        writer.write_str_value("salesperson", self.salesperson)
        writer.write_collection_of_object_values("salesInvoiceLines", self.sales_invoice_lines)
        writer.write_object_value("sellingPostalAddress", self.selling_postal_address)
        writer.write_object_value("shipmentMethod", self.shipment_method)
        writer.write_uuid_value("shipmentMethodId", self.shipment_method_id)
        writer.write_object_value("shippingPostalAddress", self.shipping_postal_address)
        writer.write_str_value("shipToContact", self.ship_to_contact)
        writer.write_str_value("shipToName", self.ship_to_name)
        writer.write_str_value("status", self.status)
        writer.write_float_value("totalAmountExcludingTax", self.total_amount_excluding_tax)
        writer.write_float_value("totalAmountIncludingTax", self.total_amount_including_tax)
        writer.write_float_value("totalTaxAmount", self.total_tax_amount)
    
    @property
    def ship_to_contact(self,) -> Optional[str]:
        """
        Gets the shipToContact property value. The shipToContact property
        Returns: Optional[str]
        """
        return self._ship_to_contact
    
    @ship_to_contact.setter
    def ship_to_contact(self,value: Optional[str] = None) -> None:
        """
        Sets the shipToContact property value. The shipToContact property
        Args:
            value: Value to set for the ship_to_contact property.
        """
        self._ship_to_contact = value
    
    @property
    def ship_to_name(self,) -> Optional[str]:
        """
        Gets the shipToName property value. The shipToName property
        Returns: Optional[str]
        """
        return self._ship_to_name
    
    @ship_to_name.setter
    def ship_to_name(self,value: Optional[str] = None) -> None:
        """
        Sets the shipToName property value. The shipToName property
        Args:
            value: Value to set for the ship_to_name property.
        """
        self._ship_to_name = value
    
    @property
    def shipment_method(self,) -> Optional[shipment_method.ShipmentMethod]:
        """
        Gets the shipmentMethod property value. The shipmentMethod property
        Returns: Optional[shipment_method.ShipmentMethod]
        """
        return self._shipment_method
    
    @shipment_method.setter
    def shipment_method(self,value: Optional[shipment_method.ShipmentMethod] = None) -> None:
        """
        Sets the shipmentMethod property value. The shipmentMethod property
        Args:
            value: Value to set for the shipment_method property.
        """
        self._shipment_method = value
    
    @property
    def shipment_method_id(self,) -> Optional[UUID]:
        """
        Gets the shipmentMethodId property value. The shipmentMethodId property
        Returns: Optional[UUID]
        """
        return self._shipment_method_id
    
    @shipment_method_id.setter
    def shipment_method_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the shipmentMethodId property value. The shipmentMethodId property
        Args:
            value: Value to set for the shipment_method_id property.
        """
        self._shipment_method_id = value
    
    @property
    def shipping_postal_address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the shippingPostalAddress property value. The shippingPostalAddress property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._shipping_postal_address
    
    @shipping_postal_address.setter
    def shipping_postal_address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the shippingPostalAddress property value. The shippingPostalAddress property
        Args:
            value: Value to set for the shipping_postal_address property.
        """
        self._shipping_postal_address = value
    
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
            value: Value to set for the total_amount_excluding_tax property.
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
            value: Value to set for the total_amount_including_tax property.
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
            value: Value to set for the total_tax_amount property.
        """
        self._total_tax_amount = value
    

