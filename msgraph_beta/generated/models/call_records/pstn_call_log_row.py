from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_log_row import CallLogRow
    from .pstn_call_duration_source import PstnCallDurationSource

from .call_log_row import CallLogRow

@dataclass
class PstnCallLogRow(CallLogRow):
    # The source of the call duration data. If the call uses a third-party telecommunications operator via the Operator Connect Program, the operator may provide their own call duration data. In this case, the property value is operator. Otherwise, the value is microsoft.
    call_duration_source: Optional[PstnCallDurationSource] = None
    # Call identifier. Not guaranteed to be unique.
    call_id: Optional[str] = None
    # Indicates whether the call was a PSTN outbound or inbound call and the type of call such as a call placed by a user or an audio conference.
    call_type: Optional[str] = None
    # Number of the user or bot who received the call (E.164).
    callee_number: Optional[str] = None
    # Number of the user or bot who made the call (E.164).
    caller_number: Optional[str] = None
    # Amount of money or cost of the call that is charged to your account.
    charge: Optional[float] = None
    # Local IPv4 of the client that is retrieved from the operating system of the client.
    client_local_ip_v4_address: Optional[str] = None
    # Local IPv6 of the client that is retrieved from the operating system of the client.
    client_local_ip_v6_address: Optional[str] = None
    # Public IPv4 of the client that can be used to determine the location of the client.
    client_public_ip_v4_address: Optional[str] = None
    # Public IPv6 of the client that can be used to determine the location of the client.
    client_public_ip_v6_address: Optional[str] = None
    # ID of the audio conference.
    conference_id: Optional[str] = None
    # Connection fee price.
    connection_charge: Optional[float] = None
    # Type of currency used to calculate the cost of the call (ISO 4217).
    currency: Optional[str] = None
    # Indicates whether the call was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
    destination_context: Optional[str] = None
    # Country or region dialed.
    destination_name: Optional[str] = None
    # How long the call was connected, in seconds.
    duration: Optional[int] = None
    # Call end time.
    end_date_time: Optional[datetime.datetime] = None
    # User's phone number type, such as a service of toll-free number.
    inventory_type: Optional[str] = None
    # The license used for the call.
    license_capability: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The telecommunications operator that provided PSTN services for this call. It may be Microsoft, or it may be a third-party operator via the Operator Connect Program.
    operator: Optional[str] = None
    # Call start time.
    start_date_time: Optional[datetime.datetime] = None
    # Country code of the tenant. For details, see ISO 3166-1 alpha-2.
    tenant_country_code: Optional[str] = None
    # Country code of the user. For details, see ISO 3166-1 alpha-2.
    usage_country_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PstnCallLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PstnCallLogRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PstnCallLogRow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .call_log_row import CallLogRow
        from .pstn_call_duration_source import PstnCallDurationSource

        from .call_log_row import CallLogRow
        from .pstn_call_duration_source import PstnCallDurationSource

        fields: Dict[str, Callable[[Any], None]] = {
            "callDurationSource": lambda n : setattr(self, 'call_duration_source', n.get_enum_value(PstnCallDurationSource)),
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callType": lambda n : setattr(self, 'call_type', n.get_str_value()),
            "calleeNumber": lambda n : setattr(self, 'callee_number', n.get_str_value()),
            "callerNumber": lambda n : setattr(self, 'caller_number', n.get_str_value()),
            "charge": lambda n : setattr(self, 'charge', n.get_float_value()),
            "clientLocalIpV4Address": lambda n : setattr(self, 'client_local_ip_v4_address', n.get_str_value()),
            "clientLocalIpV6Address": lambda n : setattr(self, 'client_local_ip_v6_address', n.get_str_value()),
            "clientPublicIpV4Address": lambda n : setattr(self, 'client_public_ip_v4_address', n.get_str_value()),
            "clientPublicIpV6Address": lambda n : setattr(self, 'client_public_ip_v6_address', n.get_str_value()),
            "conferenceId": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "connectionCharge": lambda n : setattr(self, 'connection_charge', n.get_float_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "destinationContext": lambda n : setattr(self, 'destination_context', n.get_str_value()),
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "inventoryType": lambda n : setattr(self, 'inventory_type', n.get_str_value()),
            "licenseCapability": lambda n : setattr(self, 'license_capability', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "tenantCountryCode": lambda n : setattr(self, 'tenant_country_code', n.get_str_value()),
            "usageCountryCode": lambda n : setattr(self, 'usage_country_code', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("callDurationSource", self.call_duration_source)
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callType", self.call_type)
        writer.write_str_value("calleeNumber", self.callee_number)
        writer.write_str_value("callerNumber", self.caller_number)
        writer.write_float_value("charge", self.charge)
        writer.write_str_value("clientLocalIpV4Address", self.client_local_ip_v4_address)
        writer.write_str_value("clientLocalIpV6Address", self.client_local_ip_v6_address)
        writer.write_str_value("clientPublicIpV4Address", self.client_public_ip_v4_address)
        writer.write_str_value("clientPublicIpV6Address", self.client_public_ip_v6_address)
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_float_value("connectionCharge", self.connection_charge)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_int_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("inventoryType", self.inventory_type)
        writer.write_str_value("licenseCapability", self.license_capability)
        writer.write_str_value("operator", self.operator)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("tenantCountryCode", self.tenant_country_code)
        writer.write_str_value("usageCountryCode", self.usage_country_code)
    

