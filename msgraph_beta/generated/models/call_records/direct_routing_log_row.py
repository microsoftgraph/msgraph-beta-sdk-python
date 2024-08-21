from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_log_row import CallLogRow

from .call_log_row import CallLogRow

@dataclass
class DirectRoutingLogRow(CallLogRow):
    # In addition to the SIP codes, Microsoft has own subcodes that indicate the specific issue.
    call_end_sub_reason: Optional[int] = None
    # Call type and direction.
    call_type: Optional[str] = None
    # Number of the user or bot who received the call (E.164 format, but might include more data).
    callee_number: Optional[str] = None
    # Number of the user or bot who made the call (E.164 format, but might include more data).
    caller_number: Optional[str] = None
    # Identifier (GUID) for the call that you can use when calling Microsoft Support.
    correlation_id: Optional[str] = None
    # Duration of the call in seconds.
    duration: Optional[int] = None
    # Only exists for successful (fully established) calls. The time when the call ended.
    end_date_time: Optional[datetime.datetime] = None
    # Only exists for failed (not fully established) calls.
    failure_date_time: Optional[datetime.datetime] = None
    # The final response code with which the call ended (RFC 3261).
    final_sip_code: Optional[int] = None
    # Description of the SIP code and Microsoft subcode.
    final_sip_code_phrase: Optional[str] = None
    # The date and time when the initial invite was sent.
    invite_date_time: Optional[datetime.datetime] = None
    # Indicates if the trunk was enabled for media bypass or not.
    media_bypass_enabled: Optional[bool] = None
    # The data center used for media path in non-bypass call.
    media_path_location: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The data center used for signaling for both bypass and non-bypass calls.
    signaling_location: Optional[str] = None
    # Call start time.For failed and unanswered calls, this value can be equal to invite or failure time.
    start_date_time: Optional[datetime.datetime] = None
    # Success or attempt.
    successful_call: Optional[bool] = None
    # Correlation ID of the call to the transferor.
    transferor_correlation_id: Optional[str] = None
    # Fully qualified domain name of the session border controller.
    trunk_fully_qualified_domain_name: Optional[str] = None
    # Country/region code of the user. For details, see ISO 3166-1 alpha-2.
    user_country_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectRoutingLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectRoutingLogRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectRoutingLogRow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .call_log_row import CallLogRow

        from .call_log_row import CallLogRow

        fields: Dict[str, Callable[[Any], None]] = {
            "callEndSubReason": lambda n : setattr(self, 'call_end_sub_reason', n.get_int_value()),
            "callType": lambda n : setattr(self, 'call_type', n.get_str_value()),
            "calleeNumber": lambda n : setattr(self, 'callee_number', n.get_str_value()),
            "callerNumber": lambda n : setattr(self, 'caller_number', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "failureDateTime": lambda n : setattr(self, 'failure_date_time', n.get_datetime_value()),
            "finalSipCode": lambda n : setattr(self, 'final_sip_code', n.get_int_value()),
            "finalSipCodePhrase": lambda n : setattr(self, 'final_sip_code_phrase', n.get_str_value()),
            "inviteDateTime": lambda n : setattr(self, 'invite_date_time', n.get_datetime_value()),
            "mediaBypassEnabled": lambda n : setattr(self, 'media_bypass_enabled', n.get_bool_value()),
            "mediaPathLocation": lambda n : setattr(self, 'media_path_location', n.get_str_value()),
            "signalingLocation": lambda n : setattr(self, 'signaling_location', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "successfulCall": lambda n : setattr(self, 'successful_call', n.get_bool_value()),
            "transferorCorrelationId": lambda n : setattr(self, 'transferor_correlation_id', n.get_str_value()),
            "trunkFullyQualifiedDomainName": lambda n : setattr(self, 'trunk_fully_qualified_domain_name', n.get_str_value()),
            "userCountryCode": lambda n : setattr(self, 'user_country_code', n.get_str_value()),
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
        writer.write_int_value("callEndSubReason", self.call_end_sub_reason)
        writer.write_str_value("callType", self.call_type)
        writer.write_str_value("calleeNumber", self.callee_number)
        writer.write_str_value("callerNumber", self.caller_number)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_int_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("failureDateTime", self.failure_date_time)
        writer.write_int_value("finalSipCode", self.final_sip_code)
        writer.write_str_value("finalSipCodePhrase", self.final_sip_code_phrase)
        writer.write_datetime_value("inviteDateTime", self.invite_date_time)
        writer.write_bool_value("mediaBypassEnabled", self.media_bypass_enabled)
        writer.write_str_value("mediaPathLocation", self.media_path_location)
        writer.write_str_value("signalingLocation", self.signaling_location)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_bool_value("successfulCall", self.successful_call)
        writer.write_str_value("transferorCorrelationId", self.transferor_correlation_id)
        writer.write_str_value("trunkFullyQualifiedDomainName", self.trunk_fully_qualified_domain_name)
        writer.write_str_value("userCountryCode", self.user_country_code)
    

