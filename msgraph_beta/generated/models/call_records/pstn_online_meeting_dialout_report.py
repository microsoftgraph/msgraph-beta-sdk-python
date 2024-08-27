from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PstnOnlineMeetingDialoutReport(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Currency used to calculate the cost of the call. For details, see ISO 4217.
    currency: Optional[str] = None
    # Indicates whether the call was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
    destination_context: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total costs of all the calls within the selected time range, including call charges and connection fees.
    total_call_charge: Optional[float] = None
    # Total duration of all the calls within the selected time range, in seconds.
    total_call_seconds: Optional[int] = None
    # Total number of dial-out calls within the selected time range.
    total_calls: Optional[int] = None
    # Country code of the user. For details, see ISO 3166-1 alpha-2.
    usage_location: Optional[str] = None
    # Display name of the user.
    user_display_name: Optional[str] = None
    # The unique identifier (GUID) of the user in Microsoft Entra ID.
    user_id: Optional[str] = None
    # The user principal name (sign-in name) in Microsoft Entra ID. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PstnOnlineMeetingDialoutReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PstnOnlineMeetingDialoutReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PstnOnlineMeetingDialoutReport()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "destinationContext": lambda n : setattr(self, 'destination_context', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalCallCharge": lambda n : setattr(self, 'total_call_charge', n.get_float_value()),
            "totalCallSeconds": lambda n : setattr(self, 'total_call_seconds', n.get_int_value()),
            "totalCalls": lambda n : setattr(self, 'total_calls', n.get_int_value()),
            "usageLocation": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("totalCallCharge", self.total_call_charge)
        writer.write_int_value("totalCallSeconds", self.total_call_seconds)
        writer.write_int_value("totalCalls", self.total_calls)
        writer.write_str_value("usageLocation", self.usage_location)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

